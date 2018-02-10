

import requests
from datetime import date, timedelta

#GET URL
get_url= "https://candidate.hubteam.com/candidateTest/v2/partners?userKey=951ac06344f4622159e444ff5acf"
#POST URL
post_url = "https://candidate.hubteam.com/candidateTest/v2/results?userKey=951ac06344f4622159e444ff5acf"

# Class Country - to store country name and attending dates and frequency of people available on those dates
class Country:
    def __init__(self, country_name):
        self.country_name = country_name
        #dict with date as key, and number of attendees for consecutive dates, as value
        self.dates_dict = {}

    def get_country_name(self):
        return(self.country_name)

    def get_dates(self):
        return(self.dates_dict)

    def add_dates_to_dict(self, date_list):
        #Iterate over the date_list
        for i in range(0,len(date_list)-1):
            #Converting two dates in the list to Date objects, so as to check if they are consecutive
            first_date_array = [int(x) for x in date_list[i].split('-')]
            first_date_object = date(first_date_array[0], first_date_array[1], first_date_array[2])
            next_date_array = [int(x) for x in date_list[i + 1].split('-')]
            next_date_object = date(next_date_array[0], next_date_array[1], next_date_array[2])

            #if the difference between first and next date is 1, then the attending days are consecutive
            date_diff = next_date_object - first_date_object
            #Convert timedelta object date_diff into list. Date diff is in the form "x day, hh:mm:ss"
            date_diff_array = str(date_diff).split(' ')
            #First element in date_diff_array will contain the number of days between first_date and next_date
            #if the first element is 1, then it means that dates are consecutive
            if(int(date_diff_array[0]) == 1):
                #Dates are consecutive, add the first_date_object to date_dict hash
                # Check if the date_obj exist is dates_dict
                if (first_date_object in self.dates_dict.keys()):
                    self.dates_dict[first_date_object] += 1
                else:
                    self.dates_dict[first_date_object] = 1



# Method to send HTTP get and return data from server after it has been serialized
def get_info(url):
    try:
        response = requests.get(url,verify=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)
    #Check if response was ok
    if(response.ok):
        return(response.json())
    else:
        return None


# Method to sent HTTP POST with data to server
def post_info(url, post_hash):
    try:
        response = requests.post(url, json=post_hash)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(5)
    if(response.ok):
        print(response.json())
        return True
    else:
        return False



#Main

#Get info from server
input_data = get_info(get_url)
#If no data, then nothing to do and exit
if not(input_data):
    exit(1)

# print(type(input_data))
# print(input_data)

# Add the availability dates for each country into a dictionary
#Dictionary for Country objects
country_dict = {}

for partner in input_data['partners']:
    country_name = partner['country']
    #check if the country being attended by the partner already has a Country Object
    if(country_name in country_dict.keys()):
        #Country object exists for this country, just add available consecutive dates
        country_dict[country_name].add_dates_to_dict(partner['availableDates'])
    else:
        #Country object does not exist. Create new object and then add available consecutive dates
        country_dict[country_name] = Country(country_name)
        country_dict[country_name].add_dates_to_dict(partner['availableDates'])

#Start - Debug
for elem in country_dict.keys():
    print(country_dict[elem].get_country_name())
    print(country_dict[elem].get_dates())
#End - Debug


#Results list of hashes
results_list =[]

#Now that we have a list of the consecutive dates, find the partners that are available on those dates

for elem in country_dict.keys():
    #result hash for each country, holding country name, emails, and start date
    result_country_hash={}
    country_name = elem
    consec_dates_hash = country_dict[elem].get_dates()
    #Check if there are any consecutive dates that partners can attend, for this country
    if not(consec_dates_hash):
        #no consecutive dates of any partners
        result_country_hash["name"] = country_name
        result_country_hash["startDate"] = None
        result_country_hash["attendeeCount"] = 0
        result_country_hash["attendees"] = []
        results_list.append(result_country_hash)
    else:
        #There are some consecutive dates
        #First sort the consec_dates_hash values so that we can find date where most partners can attend
        #Frist element of frequency_array will have the max number of partners attending, over the list of dates
        frequency_array = sorted(list(consec_dates_hash.values()), reverse=True)
        #Checking for dates which have the number of partners
        dates_list = []
        for k,v in consec_dates_hash.items():
            if(v == frequency_array[0]):
                #print(k)
                dates_list.append(k)
        #If there are more that one dates where same number of partners can attend, find the earliest date
        dates_list.sort()
        #print(dates_list)
        #The first element of dates_list will have the earliest date for the max possible attending partners
        #Build the output hash for this particular country
        result_country_hash["name"] = country_name
        result_country_hash["startDate"] = str(dates_list[0])
        result_country_hash["attendeeCount"] = 0
        result_country_hash["attendees"] = []
        results_list.append(result_country_hash)
        # Find partners who will be able to attend
        for partner in input_data['partners']:
            event_dates = []
            event_dates.append(str(dates_list[0]))
            event_dates.append(str(dates_list[0] + timedelta(1)))
            #Check if these event dates are in the list of available dates in the partners list
            if((set(event_dates).issubset(partner['availableDates']) and (country_name == partner["country"]))):
                result_country_hash["attendeeCount"] += 1
                result_country_hash["attendees"].append(partner["email"])



#Start - Debug
print("Results.......")
print(results_list)
#End - Debug

results_hash = {'countries': results_list}
print(post_info(post_url, results_hash))

#Create an API from scratch that takes user names, emails, one country they could attend and what dates
# they could attend that country. Find which dates for each country that the most people could attend in
# two consecutive days and return the dates as strings that they would be attending them. POST the countries
# with the dates as JSON properties to their server until you get a status of 200.
# The resulting JSON they're looking for does not match the example result provided.

# This is the coding challenge from Hubspot. Ideally, we would getting the input data from a REST based server but
# since we have none, we will create an array of hashes( as would be returned through a GET request to the server)

from datetime import date, timedelta


input_array = [
    {
        "uname":"rohit",
        "country":"United States",
        "start_date": "2017-10-23",
        "end_date": "2017-10-28"
    },
    {
        "uname":"yunwen",
        "country":"United States",
        "start_date": "2017-10-21",
        "end_date": "2017-10-25"
    },
    {
        "uname":"joseph",
        "country":"United States",
        "start_date": "2017-10-25",
        "end_date": "2017-10-26"
    },
    {
        "uname":"matias",
        "country":"Germany",
        "start_date": "2017-10-23",
        "end_date": "2017-10-25"
    },
    {
        "uname":"Altie",
        "country":"Germany",
        "start_date": "2017-10-23",
        "end_date": "2017-10-25"
    },
    {
        "uname":"blackie",
        "country":"Canada",
        "start_date": "2017-10-23",
        "end_date": "2017-10-25"
    }
]

class Country:
    def __init__(self, country_name):
        self.country =  country_name
        self.dates_dict = {}
        self.people_count = 0

    def get_country_name(self):
        return(self.country)

    def add_dates_to_dates_dict(self,start_date, end_date):
        # Splitting the dates into year, month, day
        start_date_array = [int(x) for x in start_date.split('-')]
        end_date_array = [int(x) for x in end_date.split('-')]
        #Check whether we got exactly a 3 element array
        #Might have to check if its a year, month, day, etc. But thats for later
        self.start_date = date(start_date_array[0], start_date_array[1], start_date_array[2])
        self.end_date = date(end_date_array[0], end_date_array[1], end_date_array[2])

        #Now date the dates are created, add them to the dates_dict to count the frequency
        s_date = self.start_date
        while(s_date <= self.end_date):
            #print("Adding date" + str(s_date))
            if(s_date in self.dates_dict.keys()):
                self.dates_dict[s_date] += 1
            else:
                self.dates_dict[s_date] = 1
            s_date = s_date + timedelta(1)


    def get_max_consecutive_dates(self):
        pass

#Get the consecutive days for each country in the country_hash
def get_consecutive_days_for_country(country_hash):

    result_hash = {}

    for country in country_hash.keys():
        print(country_hash[country].country)
        #Since keys are stored in arbitrary order, sort them
        sorted_dates_array = sorted(country_hash[country].dates_dict.keys())
        print(sorted_dates_array)

        # Now that we have the sorted keys, determine the 2 consecutive dates that most people can attend
        # this is done by determining which 2 consecutive dates has the max sum
        max_people = 0
        start_date = None
        country_dates_dict = country_hash[country].dates_dict
        for i in range(0,(len(sorted_dates_array)-1)):
            if((country_dates_dict[sorted_dates_array[i]] + country_dates_dict[sorted_dates_array[i + 1]]) > max_people):
                max_people = (country_dates_dict[sorted_dates_array[i]] + country_dates_dict[sorted_dates_array[i + 1]])
                start_date = sorted_dates_array[i]

        print("Start date for " + country_hash[country].country + "::"+ str(start_date) + " with " + str(max_people)+ " people.")

        result_hash[country] = start_date.strftime('%m/%d/%Y')

    return result_hash


country_hash = {}

for elem in input_array:
    country_name = elem['country'];
    if(country_name in country_hash.keys()):
        #print(country_hash[country_name].get_country_name())
        country_hash[country_name].add_dates_to_dates_dict(elem["start_date"], elem["end_date"])

    else:
        country_hash[country_name] = Country(elem['country'])
        country_hash[country_name].add_dates_to_dates_dict(elem["start_date"], elem["end_date"])


for key in country_hash.keys():
    print(country_hash[key].country)
    print(country_hash[key].dates_dict)

# Find the consecutive dates that most people can attend for each county
print("Sorting.......................")
ret_hash = get_consecutive_days_for_country(country_hash)
print("Results.......................")
print(ret_hash)
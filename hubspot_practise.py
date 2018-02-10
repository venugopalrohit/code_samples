#Create an API from scratch that takes user names, emails, one country they could attend and what dates
# they could attend that country. Find which dates for each country that the most people could attend in
# two consecutive days and return the dates as strings that they would be attending them. POST the countries
# with the dates as JSON properties to their server until you get a status of 200.
# The resulting JSON they're looking for does not match the example result provided.

import requests

# Our REST test URL
url = "http://jsonplaceholder.typicode.com/posts/"
# Fake data for testing POST
#Create hash with data to be posted
new_entry = {
	"title": "foo",
	"body": "bar",
	"userId": 1
}

# Class Country - to store country name and attending dates and frequency of people available on those dates
class Country:
    def __init__(self, country_name):
        self.country_name = country_name
        self.dates_dict = {}

    def get_country_name(self):
        return(self.country_name)

    def add_dates_to_dict(self, date_list):
        pass




# Method to send HTTP get and return data from server after it has been serialized
def get_info(url):
    try:
        response = requests.get(url,verify=False)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(5)
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
        exit(6)
    if(response.ok):
        print(response.json())
        return True
    else:
        return False



#Get info from server
input_data = get_info(url)
#If no data, then nothing to do and exit
if not(input_data):
    exit(1)

print(input_data)
print(len(input_data))

#Input data is in the form of list of hashes
#Process them, one hash at a time, extracting country and dates, creating "Country" objects when required

#Dict of country objects, with coutry name as key and Country object as value
country_dict={}

for elem in input_data:
    country_name = elem['country']
    #check if this country_name has already an object created for it
    if country_name in country_dict.keys():
        #Just add dates to Country Object
        country_dict[country_name].add_dates_to_dict(elem['dates'])
    else:
        #create a new Country object and then add dates to this object
        country_dict[country_name] = Country(country_name)
        country_dict[country_name].add_dates_to_dict(elem['dates'])




#We have hash ready to POST back to server
print("Posting.....")
print(post_info(url, new_entry))
import requests
import json
from pprint import pprint


# Replace with the correct URL
url = "http://jsonplaceholder.typicode.com/posts/"

# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
# myResponse = requests.get(url, verify=False)
# # prints to understand what the GET results in
# print (myResponse.status_code)
# print(type(myResponse.content))
# print(myResponse.encoding)
#
# # For successful API call, response code will be 200 (OK), and response.ok will be True
# if(myResponse.ok):
#     alt_data = myResponse.json()
#     print(type(alt_data))
#     #print(alt_data)
#     id_list = []
#     user_id_list = []
#
#     #Parsing through GET response
#     for element in alt_data:
#         user_id_list.append(element['userId'])
#         id_list.append(element['id'])
#
#     print(len(user_id_list))
#     pprint(user_id_list)
#     print(len(id_list))
#     pprint(id_list)
#
# else:
#   # If response code is not ok (200), print the resulting http error code with description
#     myResponse.raise_for_status()
#

# POST data to server
# URL is the same

#Create hash with data to be posted
new_entry = {
	"title": "foo",
	"body": "bar",
	"userId": 1
}

post_response = requests.post(url,json=new_entry)
if(post_response.ok):
    print(type(post_response))
    print(post_response.json())
else:
    post_response.raise_for_status()

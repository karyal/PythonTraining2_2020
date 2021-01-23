# http://dummy.restapiexample.com/
# https://github.com/public-apis/public-apis

# Using the YouTube API
# pip install requests
import requests
import json
# Get the feed
r = requests.get("http://dummy.restapiexample.com/api/v1/employees")
#print(r.text)
# Convert it to a Python dictionary
data = json.loads(r.text)
#print(data)

'''    
    print("id", item['id'])
    print("name", item['employee_name'])
    print("employee_salary", item['employee_salary'])
    print("employee_age", item['employee_age'])
    print("profile_image", item['profile_image'])
'''
import requests
newurl = "http://localhost:5000/names"

newperson = {
    "name" : "maria",
    "last_name" : "faratz"

}

newrequest = requests.post(newurl, json=newperson)
print (newrequest)


new_get_request = requests.get(newurl)
for item in new_get_request.json():
    print (item["first name"])
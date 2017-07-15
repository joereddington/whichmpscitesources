#Okay, what has to happen here?

#first download the file.
#Then go thought and print out each of the names and their twitter handles.
#http://everypolitician.org/uk/commons/download.html


#From https://stackoverflow.com/a/12965254/170243

import urllib, json
url = "https://cdn.rawgit.com/everypolitician/everypolitician-data/2fcff6382b2abf8e490893fcff0e6e34f26b9f93/data/UK/Commons/ep-popolo-v1.0.json"
response = urllib.urlopen(url)
data = json.loads(response.read())
for mp in data['persons']:
#    print mp['name']
    if 'contact_details' in mp.keys():
        contacts=mp['contact_details']
        for contact in contacts:
            #print contact['type']
            #print contact['value']
            if contact['type'] == "twitter":
                print "Name: {}, Twitter: {}".format(mp['name'],contact['value'])

import urllib
import json
import requests

send_url = 'http://freegeoip.net/json'
serviceurl='http://maps.googleapis.com/maps/api/geocode/json?'

read = requests.get(send_url)
j = json.loads(read.text)

your_lat = j['latitude']
your_lon = j['longitude']

print("Press 1 if you want to get your Address")
print("Press 2 if you want to find location nearby")
print("Press 3 if you want to retrive information between 2 places")
choice=int(raw_input())
if(choice==1):
    url=serviceurl+'latlng='+str(your_lat)+","+str(your_lon)
    print url
    uh=urllib.urlopen(url)
    data=uh.read()
    js=json.loads(str(data))
    print "Your Current Location is: ",js["results"][0]["formatted_address"]
if(choice==2):
    print("What are you looking for?")
    searchfor=raw_input()
    service_url2="https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    url=service_url2+"location="+str(your_lat)+","+str(your_lon)+"&radius="+"50000"+"&type="+searchfor+"&keyword="+"cruise&key=AIzaSyDXMGysARarA3iS-u5soaUjtJPHDwssJ8Q"
#     url=service_url2+"location="+"-33.8670522,151.1957362"+"&radius="+"50000"+"&type="+searchfor+"&keyword="+"cruise&key=AIzaSyDXMGysARarA3iS-u5soaUjtJPHDwssJ8Q"
    print url
    uh=urllib.urlopen(url)
    data=uh.read()
    js=json.loads(str(data))
#     print data
    if(js["status"] !="OK"):
        print "Sorry There is no place within 50 Km range."
    else:
        print "You have ",len(js["results"]),"places nearby,matching your search result ! \n"
        for x in range(len(js["results"])):
            print(str((x+1))+'): '+js["results"][x]["name"])
            
            try: print(js["results"][x]["rating"] + " Star Rating Provided by People")
            except: print "Rating is not available"
                
            try: 
                if(js["results"][x]["opening_hours"]["open_now"]==False):
                    print "It is currently closed"
                else:
                    print "It is open right now"
            except: print "Its Opening Data Not present"
            
            print "Address: "+js["results"][x]["vicinity"]+"\n"
if(choice==3):
    startpoint=raw_input("Starting Location: ")
    endpoint=raw_input("End location: ")
    service_url3="https://maps.googleapis.com/maps/api/directions/json?"
#     origin=Disneyland&destination=Universal+Studios+Hollywood4&key=YOUR_API_KEY
    url=service_url3+urllib.urlencode({'origin':startpoint,'destination':endpoint})+"&key=AIzaSyBz92av8XPzOkuW9SRKYxH581MV7dijXxo"
    uh=urllib.urlopen(url)
    data=uh.read()
    js=json.loads(str(data))
    print "Distance between : ", js["routes"][0]["legs"][0]["start_address"],"\tand\t",js["routes"][0]["legs"][0]["end_address"],"\tis:\t",js["routes"][0]["legs"][0]["distance"]["text"]

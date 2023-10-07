import requests
import googlemaps
import json
import ast
from IPython.display import Image

location = ""
location = input("Do you want the location of nearby DONATION CENTERS (D) or THRIFT STORES (T)?")
if location == "D" or location =="d":
    location_type = "donation%20center"
elif location =="T" or location == "t":
    location_type = "thrift%20store"

response = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json?fields=formatted_address%2Cname%2Cgeometry&input=" + location_type + "&inputtype=textquery&key=AIzaSyD_sSmpo87OoqW0jQKfpOe0mPOMC_MwYQQ")
location_data = ast.literal_eval(response.text)
#print(location_data)
address = location_data["candidates"][0]["formatted_address"]
formatted_addy = address.replace(",", "")
formatted_addy = formatted_addy.replace(" ", "+")
#lat_long = str(location_data["candidates"][0]["geometry"]["lat"]) + "," + str(location_data["candidates"][0]["geometry"]["location"]["lng"])
print("Name: ", location_data["candidates"][0]["name"])
print("Address: ", location_data["candidates"][0]["formatted_address"])

#static_map = requests.get("https://maps.googleapis.com/maps/api/staticmap?marker=color:red|" + address + "&zoom=14&size=400x400&key=AIzaSyD_sSmpo87OoqW0jQKfpOe0mPOMC_MwYQQ")
url_with_marker = "https://maps.googleapis.com/maps/api/staticmap?center=" + formatted_addy + "&markers=color:red|" + formatted_addy + "&zoom=14&size=400x400&key=AIzaSyD_sSmpo87OoqW0jQKfpOe0mPOMC_MwYQQ"
Image(url=url_with_marker, embed=True, format='png')

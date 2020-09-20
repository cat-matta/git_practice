import googlemaps
import pprint
import time
from geopy.geocoders import Nominatim

# Ask for authorization for info with API key
API_KEY = 'AIzaSyDYMwRSfChNGRiFY90ygxLzhiigkfBuhIo'
gmaps = googlemaps.Client(key = API_KEY)

geolocator = Nominatim(user_agent="googleapi")

def get_location(foodie):
	foodie=geolocator.geocode(foodie)
	lat=str(foodie.latitude)
	lon=str(foodie.longitude)
	address=lat+','+lon
	return address

def top_five(location, place,size=5): #should pass location and food, default passes 5

    # Make a request for nearby places near user's location
    places_result = gmaps.places_nearby(location = location, keyword = place, open_now = True, rank_by = 'distance', type = 'restaurant, cafe')   

    # List to store top five results
    five_list = []

    if len(places_result['results']) > size:
        for i in range(size):

            # Define place id
            my_place_id = places_result['results'][i]['place_id']

            # Define necessary fields
            my_fields = ['name', 'formatted_address', 'formatted_phone_number', 'price_level', 'rating']

            # Make a request for the place details
            place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

            five_list.append(place_details)

    elif (len(places_result['results']) <= size and len(places_result['results'])>0):
        for place in places_result['results']:

            my_place_id = place['place_id']    
            my_fields = ['name', 'formatted_address', 'formatted_phone_number', 'price_level', 'rating']
            place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
            five_list.append(place_details)
    elif (len(places_result['results'])==0):
        return "Place is closed"
    
    results = ""
    for item in five_list:
        results += "{name}\n {address}\n Number: {phone_number}\n Rating: {rating}\n\n".format(name = item['result']['name'],address=item['result']['formatted_address'],phone_number = item['result']['formatted_phone_number'], rating = item['result']['rating']) 

    return results



user_input=input("Input the location(can be a zip code or a place like central park): ")
food_choice,size=input("Input resturant or type of food and number of choices to appear separated by a space: ").split()
location=get_location(user_input)
choice=top_five(location,food_choice,int(size))
print("\nHere are {size} {food_choice} places near: {user_input}".format(size=size,food_choice=food_choice,user_input=user_input))
print(choice)  
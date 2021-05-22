
#This file is not run; it just demonstrates how the location and date values are taken and how the data from the websites gets stored
#This is just a part of the code that is later merged with the telegram bot code.


from bs4 import BeautifulSoup
from scrapingant_client import ScrapingAntClient
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import date

#latitudes and longitudes of all the states
state_coordinates = {"ap" : (15.9129, 79.7400),
"agra" : (27.1767, 78.0081),
"aligarh" : (27.8974, 78.0880),
"assam" : (26.2006, 92.9376),
"bihar" : (25.0961, 85.3131),
"chattisgarh" : (21.2787, 81.8661),
"delhi" : (28.7041, 77.1025),
"gujarat" : (22.2587, 71.1924),
"gurgaon" : (28.4595, 77.0266),
"haryana" : (29.0588, 76.0856),
"jk" : (33.2778, 75.3412),
"karnataka" : (12.9716, 77.5946),
"kerala" : (10.8505, 76.2711),
"lucknow" : (26.8467, 80.9462),
"maharashtra" : (19.7515, 75.7139),
"mp": (22.9734, 78.6569),
"odisha" : (20.9517, 85.0985),
"punjab" : (31.1471, 75.3412),
"rajasthan" : (27.0238, 74.2179),
"up" : (26.8467, 80.9462),
"uttarakhand" :  (30.0668, 79.0193),
"westbengal" : (22.9868, 87.8550)}


today = date.today()
current_lat = 21.971649 #just some initial values are given, but the actual values are taken from the user
current_lon = 83.912827
current_location = (current_lat, current_lon)
date_string = str(today.strftime("%d-%m-%Y"))
print("date =", date_string)
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse(str(current_lat) + "," + str(current_lon)).raw
address = location['address']
print(address)

if 'state' in address.keys():
    new_location = geolocator.geocode(address['state']).raw
    current_lat = new_location['lat']
    current_lon = new_location['lon']
    current_location = (current_lat, current_lon)
    location = geolocator.reverse(str(current_lat) + "," + str(current_lon)).raw
    address = location['address']
    print(address)
    if 'postcode' in address.keys():
      pincode = str(address['postcode'])
      print("Postcode is not present for the region, so postcode of state is taken")

if 'state_district' in address.keys():
    new_location = geolocator.geocode(address['state_district']).raw
    current_lat = new_location['lat']
    current_lon = new_location['lon']
    current_location = (current_lat, current_lon)
    location = geolocator.reverse(str(current_lat) + "," + str(current_lon)).raw
    address = location['address']
    print(address)
    if 'postcode' in address.keys():
      pincode = str(address['postcode'])
      print("Postcode is not present for the region, so postcode of district is taken")


if 'county' in address.keys():
    new_location = geolocator.geocode(address['county']).raw
    current_lat = new_location['lat']
    current_lon = new_location['lon']
    current_location = (current_lat, current_lon)
    location = geolocator.reverse(str(current_lat) + "," + str(current_lon)).raw
    address = location['address']
    print(address)
    if 'postcode' in address.keys():
      pincode = str(address['postcode'])
      print("Postcode is not present for the region, so postcode of county is taken")

if 'postcode' in address.keys():
  pincode = str(address['postcode'])
  print("Postcode is present for the region")
print("pincode = " + pincode)


dist_list = []
for entry in state_coordinates.items():
  state = entry[0]
  coordinates = entry[1]
  dist = geodesic(current_location, coordinates).km
  dist_list.append(dist)
  print("distance between current location and : " + state + " is " + str(dist) + " km")

minpos = dist_list.index(min(dist_list))
state_name = list(state_coordinates)[minpos]
print(state_name)

# Define URL with a dynamic web content
url = "https://covidresources.netlify.app/state/" + state_name

# Create a ScrapingAntClient instance
client = ScrapingAntClient(token='63ff99569178494cab0ddd76fb4e1f25')

# Get the HTML page rendered content
page_content = client.general_request(url).content

# Parse content with BeautifulSoup
soup = BeautifulSoup(page_content)

data = soup.find_all('div', class_ = "my-4 bgimp hoverclass card bg-light text-dark border-success")

result = {}
dict_keys = []
dict_values = []
k=0
for i in data:
  a = BeautifulSoup(str(i))
  inner_map = {"Distributor Name" : "", "City" : "", "Extra-Info" : "", "Helpline" : "", "Links" : ""}
  heading = a.find_all("div", class_ = "green card-header", text = True)
  title = BeautifulSoup(str(heading))
  dict_keys.append(title.text.replace("[", "").replace("]", "").replace(" ", ""))
  card_body = a.find_all("div", class_ = "card-body")
  card_body = BeautifulSoup(str(card_body))
  distributor_tag = card_body.find_all("div", class_ = "card-title h5")
  other_tags = card_body.find_all("p", class_ = "pb-3 cardfont card-text")
  names = str(distributor_tag[0].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
  city = str(other_tags[0].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
  extra_info = str(other_tags[1].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
  helpline = str(other_tags[2].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
  if(len(other_tags) > 3):
    links = str(other_tags[3].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
  else:
    links = "Links : "
  names = str(names.split(":")[1])
  city = str(city.split(":")[1])
  extra_info = str(extra_info.split(":")[1])
  helpline = str(helpline.split(":")[1])
  links = str(links.split(":")[1])
  
  inner_map["Distributor Name"] = names
  inner_map["City"] = city
  inner_map["Extra-Info"] = extra_info
  inner_map["Helpline"] = helpline
  inner_map["Links"] = links
  
  # print(inner_map)
  dict_values.append(inner_map)
  # print(names)
  #print(city)
  # print(helpline)
  # print(extra_info)
  # print(links)

for key in dict_keys:
  result[key] = []
for p in dict_keys:
   s = result[p]
   s.append(dict_values[k])
   k=k+1
for k, v in result.items():
    print(k, v)

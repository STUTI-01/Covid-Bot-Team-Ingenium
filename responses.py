#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from scrapingant_client import ScrapingAntClient
import unidecode
from bs4 import BeautifulSoup


import requests, json
def sample_responses(input_text):
	user_message = str(input_text).lower()
	print(user_message)
	new_data = user_message.split(':')
	pin = new_data[0]
	date = new_data[1]
	try:
		pin = int(pin)
	except Exception as e:
		pass
	if(int(pin)<10000 and int(pin)>0):
		
		url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={pin}&date={date}'
		browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
		print(url)
		response = requests.get(url, headers=browser_header)
		print(response)
		json_data = response.json()
		final_text = ''
		if len(json_data['sessions'])==0:
			print("\nSlots Not Available\n")
		else:
			for slots in json_data['sessions']:
				final_text = final_text + "\nName: "+str(slots['name']) +'\n'+ "Available Capacity: "+str(slots['available_capacity']) +'\n' + "Min Age Limit: "+str(slots['min_age_limit']) +'\n' + "Vaccine: "+str(slots['vaccine'])+ '\n'
				final_text = final_text + '----------------------------------------'

		return final_text
	else:
		return "Invalid input"
def get_json():
	url = "https://covidresources.netlify.app/state/karnataka"


	client = ScrapingAntClient(token='63ff99569178494cab0ddd76fb4e1f25')


	page_content = client.general_request(url).content


	soup = BeautifulSoup(page_content,"html.parser")

	data = soup.find_all('div', class_ = "my-4 bgimp hoverclass card bg-light text-dark border-success")
	result = {}
	dict_keys = []
	dict_values = []
	k=0
	for i in data:
		a = BeautifulSoup(str(i),"html.parser")
		inner_map = {"Distributor Name" : "", "City" : "", "Extra-Info" : "", "Helpline" : "", "Links" : ""}
		heading = a.find_all("div", class_ = "green card-header", text = True)
		title = BeautifulSoup(str(heading),"html.parser")
		dict_keys.append(title.text.replace("[", "").replace("]", "").replace(" ", ""))
		card_body = a.find_all("div", class_ = "card-body")
		card_body = BeautifulSoup(str(card_body),"html.parser")
		distributor_tag = card_body.find_all("div", class_ = "card-title h5")
		other_tags = card_body.find_all("p", class_ = "pb-3 cardfont card-text")
		names = str(distributor_tag[0].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
		city = str(other_tags[0].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
		extra_info = str(other_tags[1].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
		helpline = str(other_tags[2].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
		if(len(other_tags) > 3):
    			links = str(other_tags[3].text.split("\n")).replace("[", "").replace("]", "").replace("'", "")
		else:
			links = "Links :"
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
		dict_values.append(inner_map)
	for key in dict_keys:
		result[key] = []
	for p in dict_keys:
		s = result[p]
		s.append(dict_values[k])
		k=k+1
	for k, v in result.items():
		print(k, v)
	return json.dumps(result)
		


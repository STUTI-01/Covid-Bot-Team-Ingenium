#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Constants as keys
from telegram.ext import *
import responses as R 
import requests, json


print('Bot is starting')

def start_command(update, context):
	update.message.reply_text('1->Vaccine slots'+'\n' + '2->Plasma'+'\n' +'3->RemdesivirandOxygen'+'\n' +'4->OxygenSuppliers'+'\n' +'5->OxygenCylinder'+'\n' +'6->OxygenConcentrators'+'\n' +'7->Oximeters'+'\n' +'8->Hospitals'+'\n' +'9->HomeICU'+'\n' +'10->CremationServices'+'\n' +'11->CovidWarRoom'+'\n' +'12->CovidTesting')
def next_command(update, context):
	url = f'https://cdn-api.co-vin.in/api/v2/admin/location/districts/16'
	browser_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
	response = requests.get(url, headers=browser_header)
	print(response)
	json_data = response.json()
	final_text = ''

	if len(json_data['districts'])==0:
		print("\nSlots Not Available\n")
	else:
		for slots in json_data['districts']:
			final_text = final_text + "\nName: "+str(slots['district_name']) +'\n'+ "District_id: "+str(slots['district_id']) +'\n' 
			final_text = final_text + '----------------------------------------'+'\n'
			
	update.message.reply_text('enter districtid:dd-mm-yyyy')
	
	
	
	
	
	

def vaccine_command(update, context):
	pin = '170'
	date = '11-5-2021'
	url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={pin}&date={date}'
	browser_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
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
	update.message.reply_text(final_text)
def plasma_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'Plasma'+'\n'

	if len(json_data1['Plasma'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['Plasma']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def remdesivir_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'RemdesivirandOxygen'

	if len(json_data1['RemdesivirandOxygen'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['RemdesivirandOxygen']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def oxygensuppliers_command(update,context):
	i=0
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'OxygenSuppliers'+'\n'

	if len(json_data1['OxygenSuppliers'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['OxygenSuppliers']:
			i=i+1
			if(i<10):
				final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
				final_text = final_text + '----------------------------------------'
			else:
				break	
	update.message.reply_text(final_text)
def oxygencylinders_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'OxygenCylinder'+'\n'

	if len(json_data1['OxygenCylinder'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['OxygenCylinder']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def oxygenconcentrators_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'OxygenConcentrators'+'\n'

	if len(json_data1['OxygenConcentrators'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['OxygenConcentrators']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def oximeters_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'Oximeters'+'\n'

	if len(json_data1['Oximeters'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['Oximeters']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def hospital_command(update,context):
	i=0
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'Hospital'+'\n'

	if len(json_data1['Hospital'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['Hospital']:
			i=i+1
			if(i<10):
				final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
				final_text = final_text + '----------------------------------------'
			else:
				break
	update.message.reply_text(final_text)
def homeicu_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'HomeICU'+'\n'

	if len(json_data1['HomeICU'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['HomeICU']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def cremationservices_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'CremationServices'+'\n'

	if len(json_data1['CremationServices'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['CremationServices']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def covidwarroom_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'CovidWarRoom'+'\n'

	if len(json_data1['CovidWarRoom'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['CovidWarRoom']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)
def covidtesting_command(update,context):
	json_value = R.get_json()
	json_data1 = json.loads(json_value)
	final_text = 'CovidTesting'+'\n'

	if len(json_data1['CovidTesting'])==0:
		print("\nNot Available\n")
	else:
		for slots in json_data1['CovidTesting']:
			final_text = final_text + "\nDistributor Name: "+str(slots['Distributor Name']) +'\n'+ "City: "+str(slots['City']) +'\n' + "Extra-Info "+str(slots['Extra-Info']) +'\n' + "Helpline: "+ str(slots['Helpline'])  +'\n' + "Links: "+ str(slots['Links']) + '\n'
			final_text = final_text + '----------------------------------------'
	update.message.reply_text(final_text)




def handle_message(update, context):
	text = str(update.message.text).lower()
	user = update.effective_user
	print(f'{user["username"]}: {text}')
	response = R.sample_responses(text)
	print(f'Bot: {response}')
	update.message.reply_text(response)





def error(update, context):
	print(f"Update {update} caused error {context.error}")


def main():
	updater = Updater(keys.API_KEY, use_context=True)
	dp = updater.dispatcher

	
	
	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("1", next_command))
	
	dp.add_handler(CommandHandler("2", plasma_command))
	dp.add_handler(CommandHandler("3", remdesivir_command))
	dp.add_handler(CommandHandler("4", oxygensuppliers_command))
	dp.add_handler(CommandHandler("5", oxygencylinders_command))
	dp.add_handler(CommandHandler("6", oxygenconcentrators_command))
	dp.add_handler(CommandHandler("7", oximeters_command))
	dp.add_handler(CommandHandler("8", hospital_command))
	dp.add_handler(CommandHandler("9", homeicu_command))
	dp.add_handler(CommandHandler("10", cremationservices_command))
	dp.add_handler(CommandHandler("11", covidwarroom_command))
	dp.add_handler(CommandHandler("12", covidtesting_command))
	dp.add_handler(MessageHandler(Filters.text, handle_message))
	dp.add_error_handler(error)


	updater.start_polling()
	updater.idle()

main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





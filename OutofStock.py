from bs4 import BeautifulSoup
import requests
from twilio.rest import Client
import time

#Twilio Account information
account_sid = 'TWILIO SID'
auth_token = 'TWILIO AUTH TOKEN'
client = Client(account_sid, auth_token)

#Disguise header so the script doesn't get blocked
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = requests.get('WEBSITE URL', headers=headers)

#Keywork I'm searching for on web page
status = 'Out of Stock'

#Parse the website
soup = BeautifulSoup(url.content, 'html.parser')

#Look for the headers, change soup.h1 to other HTML code, depending on where the website puts the status variable in HTML
stock = soup.h1

while True:
	if status not in stock:
			message = client.messages \
    			.create(
         			body='The item you wish to purchase is now in stock!',
         			from_='+TWILIOPHONE',
         			to='+YOURPHONE'
     			)
     			break
else: 
    time.sleep(600)

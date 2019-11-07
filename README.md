# OutofStock
Simple python script that scrapes a website every 10 minutes for an item that you want to order but is out of stock. Sends an SMS when it is back in stock and ready to order.

You will need to have the requests, time, twilio, and BeautifulSoup modules installed to run this script. The variables you will need to change are:

TWILIO SID - SID given by Twilio after account creation
TWILIO AUTH TOKEN - token given by Twilio after account creation
WEBSITE - The website address you want to scrape for the out of stock item
status - Change the variable from 'Out of Stock' if the website doesn't use it (i.e. Stock: 0, 0 Items left)
TWILIOPHONE: Phone number given by Twilio when you sign up
YOURPHONE: The phone number you wish to send the SMS message to

# Program to find carrier and region 
# of a phone number 
import phonenumbers 
from phonenumbers import geocoder, carrier 

phoneNumber1 = phonenumbers.parse("+919346766265")
phoneNumber2 = phonenumbers.parse("+919701466230")

# Getting carrier of a phone number 
Carrier1 = carrier.name_for_number(phoneNumber1, 'en')
Carrier2 = carrier.name_for_number(phoneNumber2, 'en')

# Getting region information 
Region1 = geocoder.description_for_number(phoneNumber1, 'en')
Region2 = geocoder.description_for_number(phoneNumber2, 'en')

# Printing the carrier and region of a phone number 
print(Carrier1,' *from* ',Region1) 
 
print(Carrier2,' *from* ',Region2)


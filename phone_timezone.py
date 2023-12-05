import phonenumbers 
from phonenumbers import timezone 
# Parsing String to Phone number 
phoneNumber = phonenumbers.parse("+918340870565") 
# Pass the parsed phone number in below function 
timeZone = timezone.time_zones_for_number(phoneNumber) 
# It print the timezone of a phonenumber 
print(timeZone) 

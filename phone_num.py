import phonenumbers as ph
from phonenumbers import geocoder

phone1=ph.parse("+918340870565")
phone2=ph.parse("+919346766265")

print("The phone numbers are :\n\n")

print(geocoder.description_for_number(phone1,"en"))
print(geocoder.description_for_number(phone2,"en"))

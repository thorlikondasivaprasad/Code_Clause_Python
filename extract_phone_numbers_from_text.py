import phonenumbers 
  
text = "Contact us at +919876543210 or +919691234567 and +918340870565" 
# Pass the text and country code to the below function 
numbers = phonenumbers.PhoneNumberMatcher(text, "IN") 

# and also the indexes of the phone numbers in the string input 
for number in numbers: 
    print(number) 

#Enchant is a module in python which is used to
#check the spelling of a word, gives suggestions
#to correct words. Also, gives antonym and synonym of words.
#It checks whether a word exists in dictionary or not.

import enchant  
# Using 'en_US' dictionary 
d = enchant.Dict("en_US") 
# Taking input from user 
word = input("Enter word: ") 
  
d.check(word)  
# Will suggest similar words 
# form given dictionary 
print(d.suggest(word)) 

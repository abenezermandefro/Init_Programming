from num2words import num2words
from translate import Translator

number = int(input("Enter a number: "))
converted = num2words(number)
translater = Translator(to_lang="am")
out = translater.translate(converted)
print("The number you entered is:- " + out) 

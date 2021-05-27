import requests

#input english word
print('Word? ',end="")
word = input()

response  = requests.get('https://api.dictionaryapi.dev/api/v2/entries/en_US/' + word)
json = response.json()

#checking for valif word or not
#it will return list for valid word and dict for invalid word
if type(json) == dict:
	print('Invalid Word!')

else:
	partOfSpeech = json[0]['meanings'][0]['partOfSpeech']
	definition = json[0]['meanings'][0]['definitions'][0]['definition']

	print(word.capitalize() + '.',  partOfSpeech.capitalize() + '.', definition.capitalize())
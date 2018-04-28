from urllib import request
import json


## parameters:
##word: the phrase to be converted to pics
##n: number of pics
def word_to_pics(word, n):
   array= []
   rawData = request.urlopen('https://www.googleapis.com/customsearch/v1?key=AIzaSyAvlXs6UPjILP-KW2kU9DTRfRWn1VIbqso&cx=005548162878739948931:tn-uu7o72gg&searchType=image&safe=high&q='+word).read()
   jsonData = json.loads(rawData)
   for i in range(0,n):
      array.append(jsonData['items'][i]['link'])

   return array

def all_words_to_pics(words_lst, n):
	pics = []
	for sentence_words in words_lst:
		sentence_arr = []
		for word in sentence_words:
			word_arr = word_to_pics(word, n)
			sentence_arr.append(word_arr)
		pics.append(sentence_arr)

	return pics

# word = "headache"
# print wordToPics(word,3)
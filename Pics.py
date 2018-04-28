import urllib
import json


## parameters:
##word: the phrase to be converted to pics
##n: number of pics
def wordToPics(word, n):
   array= []
   rawData = urllib.urlopen('https://www.googleapis.com/customsearch/v1?key=AIzaSyAvlXs6UPjILP-KW2kU9DTRfRWn1VIbqso&cx=005548162878739948931:tn-uu7o72gg&searchType=image&safe=high&q='+word).read()
   jsonData = json.loads(rawData)
   for i in range(0,n):
      array.append(jsonData['items'][i]['link'])

   return array


word = "headache"
print wordToPics(word,3)

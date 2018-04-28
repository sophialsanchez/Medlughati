PicDict= {"headache" : ["http://cdn1.medicalnewstoday.com/content/images/headlines/317/317511/lady-with-headache.jpg",
                           "https://d2ebzu6go672f3.cloudfront.net/media/content/images/headache-man-senior%20(002).jpg"],

                "no smoking" : ["https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/No_smoking_symbol.svg/2000px-No_smoking_symbol.svg.png",
                                "https://s3.envato.com/files/242872522/preview.jpg"],
             
                "after eating" :["http://worldartsme.com/random-eating-clipart.html#gal_post_77199_random-eating-clipart-1.jpg",
                                 "https://photos.gograph.com/thumbs/CSP/CSP606/done-eating-vector-clipart_k18972219.jpg"],
   
                "when I wake up" : ["https://2.bp.blogspot.com/_ckPB1Ppopzg/TRQJ2X860LI/AAAAAAAAAQA/q1YsNmLsp_4/s1600/kring.jpg",
                                    "https://i.pinimg.com/originals/d1/2b/d3/d12bd319ff0fb387383939fac6ec1ca4.jpg"],
                
                "chest burn" : ["https://familydoctor.org/wp-content/uploads/1996/11/62502365_l-705x445.jpg",
                                "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/articles/2015/12/heartburn2-1508867553.jpg"],
                
               }
def word_to_pics(word):
   try:
      urls = PicDict[word]
      array= [word]
      array.append(urls[0])
      array.append(urls[1])
      return array
   except:
      return "NULL"

def all_words_to_pics(words_lst):
	pics = []
	for sentence_words in words_lst:
		sentence_arr = []
		for word in sentence_words:
			#word_arr = word_to_pics(word, n)
			word_arr = "https://i.ytimg.com/vi/m5d1FlSeF-M/maxresdefault.jpg"
			#word_arr = word_to_pics(word)
			sentence_arr.append(word_arr)
		pics.append(sentence_arr)

	return pics

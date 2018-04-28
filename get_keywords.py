from rake_nltk import Rake
import nltk

"""
A function to determine which keywords 
in a given sentence should be displayed.
"""
# pip install rake-nltk

example_sentences = [
	"I woke up this morning and my head really hurt.",
	"I had major surgery on my throat yesterday.",
	"My child has been feeling sick for a week, and I'm not sure what's wrong with her."
]

example_paragraph = """
I woke up this morning and my head really hurt. 
I had major surgery on my throat yesterday. 
My child has been feeling sick for a week, and I'm not sure what's wrong with her.
"""


def get_keywords(text, print_bool):
	#sentence_lst = r.split_sentences(text)
	#print(sentence_lst)
	sentences = nltk.tokenize.sent_tokenize(example_paragraph)
	keywords = []
	for sentence in sentences:
		r = Rake(stopwords = get_stopwords())
		r.extract_keywords_from_text(sentence)
		phrases = r.get_ranked_phrases()
		keywords.append(phrases)
		if print_bool:
			print(sentence)
			print(phrases)
			print('')
	
	return keywords


def get_stopwords():
	stopwords = nltk.corpus.stopwords.words('english')
	newStopWords = ['really']
	stopwords.extend(newStopWords)
	return stopwords


get_keywords(example_paragraph, True)

from rake_nltk import Rake

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

example_paragraph = 
	"""
	I woke up this morning and my head really hurt. 
	I had major surgery on my throat yesterday. 
	My child has been feeling sick for a week, and I'm not sure what's wrong with her.
	"""


def get_keywords(text):
	r = Rake()
	sentence_lst = r.split_sentences(text)
	print(sentence_lst)
	r.extract_keywords_from_text(sentence)
	return r.get_ranked_phrases_with_scores()

print(get_keywords(example_paragraph))

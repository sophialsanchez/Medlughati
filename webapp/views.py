
# Create your views here.

import json
from django.views import View
from django.http import HttpResponse
from webapp import get_keywords, translate, Pics


# Martin added this piece of code to avoid using SSL certificates because they weren't working
# in his computer

import ssl
_create_unverified_https_context = ssl._create_unverified_context
ssl._create_default_https_context = _create_unverified_https_context

class MainEndport(View):

	def post(self, request):

		print("parameters:", request.POST)

		response_data = {}
		text = translate.translate(request.POST['input_text'], request.POST['input_language'], request.POST['output_language'])
		#text = "I have a really really big headache yo."
		keywords = get_keywords.get_keywords(text, False)
		images = Pics.all_words_to_pics(keywords["not_ranked"])
		response_data['translation'] = {"text": str(text), "keywords": keywords, "images": images}

		print("output:", response_data)

		return HttpResponse(json.dumps(response_data), content_type="application/json")

#curl -d "input_text=I woke up and my head hurt.&input_language=arabic&output_language=english" -X POST http://localhost:8000/api/

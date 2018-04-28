
# Create your views here.

import json
from django.views import View
from django.http import HttpResponse
from webapp import get_keywords, translate, Pics

class MainEndport(View):

	def post(self, request):

		#print(request.POST['input_text'])
		response_data = {}
		text = translate.translate(request.POST['input_text'], request.POST['input_language'], request.POST['output_language'])
		#text = "I have a really really big headache yo."
		keywords = get_keywords.get_keywords(text, False)
		images = Pics.all_words_to_pics(keywords["not_ranked"], 3)
		response_data['translation'] = {"text": str(text), "keywords": keywords, "images": images}

		return HttpResponse(json.dumps(response_data), content_type="application/json")

#curl -d "input_text=I woke up and my head hurt.&input_language=arabic&output_language=english" -X POST http://localhost:8000/api/
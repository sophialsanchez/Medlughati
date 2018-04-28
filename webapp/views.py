
# Create your views here.

import json
from django.views import View
from django.http import HttpResponse

class MainEndport(View):

	def post(self, request):

		print(request.POST) # it's a dictionary

		response_data = {}
		response_data['example_key'] = "Example content"

		return HttpResponse(json.dumps(response_data), content_type="application/json")
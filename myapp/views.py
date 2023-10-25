from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .openai_service import gpt_search

@csrf_exempt
def handle_get(request):
    return JsonResponse({"message": "Test Success"})

@csrf_exempt
def handle_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        query = data.get('query')
        output = gpt_search(query)
        return JsonResponse({"response": output}, status=200)
    else:
        return JsonResponse({"error": "Something went wrong"}, status=400)

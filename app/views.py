from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def hello_world(request):
    if request.method == 'GET':
        return JsonResponse({
            'message': 'Hello from Makhachkala API!',
            'version': '1.0.0',
            'status': 'operational'
        })
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name', 'Guest')
            return JsonResponse({
                'message': f'Hello, {name}! Welcome to Makhachkala!',
                'your_data': data
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
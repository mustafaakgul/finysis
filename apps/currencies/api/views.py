from django.http import JsonResponse


def defaulf_view(request):
    return JsonResponse({'message': 'Hello World!'})
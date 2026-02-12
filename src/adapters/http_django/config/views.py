from django.http import JsonResponse
from django.views.decorators.http import require_GET
from core.app.greet import make_greeting

@require_GET
def hello(request):
    name = request.GET.get("name")
    greeting = make_greeting(name)
    return JsonResponse({"message": greeting.message})
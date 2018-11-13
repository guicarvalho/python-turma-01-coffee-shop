from django.http import HttpResponse


def home_view(request):
    return HttpResponse('<h1>Olá mundo!!! Rodando com Docker Compose!!!</h1>')


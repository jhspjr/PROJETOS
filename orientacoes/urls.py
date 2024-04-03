from django.urls import path
from django.http import HttpResponse
from orientacoes.views import home, defesas, papers

#dominio/orientacoes
urlpatterns = [
    path('', home),
    path("defesas/", defesas),
    path("papers/", papers)
]
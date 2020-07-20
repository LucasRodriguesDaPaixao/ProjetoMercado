from django.shortcuts import render

# Create your views here.
def Produto(request):
    return render(request, "mercado/index.html")
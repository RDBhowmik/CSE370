from django.shortcuts import render
# from django.http.response import HttpResponse
# Create your views here.
def cake(request):
    return render(request, 'product/product.html')

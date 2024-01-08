from django.shortcuts import render

# Create your views here.
def bk(request):
    names ={'friends' :["aronno",'ahnaf','jhilik','anwesha','achol','borsha','monjur']}
    return render(request, 'payments/bkash.html', names)
def rk(request):
    return render(request, 'payments/rocket.html')


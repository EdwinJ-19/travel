from django.shortcuts import render,HttpResponse

# Create your views here.
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'index.html')
def home(request):
    return render(request,'main.html')
def hotel(request):
    return render(request,'hotelacc.html')
def team(request):
    return render(request,'about.html')
def trip(request):
    return render(request,'trip.html')
def payment(request):
    return render(request,'payment.html')
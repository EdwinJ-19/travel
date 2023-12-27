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
from django.shortcuts import render

# Create your views here.
def hello(requst):
    return render(requst,'hello.html')
from django.shortcuts import render

# Create your views here.
def Polls(request):
    return render(request, 'polls.html')
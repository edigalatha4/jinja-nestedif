from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':40,'b':200,'c':80}
    return render(request,'operations.html',d)

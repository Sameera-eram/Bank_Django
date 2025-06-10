from django.shortcuts import render,redirect
from .forms import dataForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = dataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('succes')
    else:
        form =dataForm()
    return render(request,'index.html',{'form':form})
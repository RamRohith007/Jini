from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='login')
def uploadpics(request):
    form = PicStockForm()
    if request.method == 'POST':
        form = PicStockForm(request.POST, request.FILES)
        if form.is_valid():
            picstock_instance = form.save(commit=False)
            picstock_instance.owner = request.user
            picstock_instance.save()
            messages.success(request,"Uploaded Successfull!")
            return redirect('picstockcollections')
    formvalue = {'imgupload':form}
    return render(request,'picstock/uploadpics.html',context=formvalue)

def collections(request):
    posts = PicStock.objects.all()
    formvalue = {'posts':posts}
    return render(request,'picstock/collections.html',context=formvalue)
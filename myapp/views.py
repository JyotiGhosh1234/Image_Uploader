from django.shortcuts import render
from django.http import HttpResponseRedirect
from myapp.models import *
from myapp.forms import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def upload(request):
    if request.method == 'POST':
          form = ImageForm(request.POST, request.FILES)
          form.is_valid()
          form.save()
          messages.success(request, "Image upload successfully..!")
    form = ImageForm()

    img = Image.objects.all().order_by('id')
    paginator = Paginator(img, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
          
    return render(request, "myapp/upload.html", {'form' : form, 'page_obj' : page_obj})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Image.objects.get(pk=id)
        pi.delete()
        messages.success(request, "Image Deleted successfully...!")
        return HttpResponseRedirect('/')
    
def update_data(request, id):
    if request.method == "POST":
        pi = Image.objects.get(pk=id)
        form = ImageForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.success(request, "Image updated successfully...!")
    else:
        pi = Image.objects.get(pk=id)
        form = ImageForm(instance=pi)
        return render(request, "myapp/update.html", {'form' : form})
    return HttpResponseRedirect('/')



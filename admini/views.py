from django.shortcuts import render,redirect, get_object_or_404
from .models import Admin_comment
from .forms import Admin_form

# Create your views here.
# def home(request):
#   return HttpResponse('welcome')

def home_page(request):
  admin_comment=Admin_comment.objects.all()
  return render(request,'admin.html',{'admin_comment':admin_comment})

def add_comment(request):
  if request.method=='POST':
    add=Admin_form(request.POST)
    if add.is_valid():
      add.save()
      return redirect('home_page')
    
  else :
    add = Admin_form()
  return render(request,'add_comment.html',{'add':add})

def added_details(request):
  added=get_object_or_404(Admin_comment)
  return render(request, 'added.html',{'added':added})
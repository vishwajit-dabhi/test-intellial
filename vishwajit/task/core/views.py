from django.shortcuts import render
from django.http import JsonResponse
from core import models as core_models
# Create your views here.
def index(request):

    if request.method =='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        

        core_models.user.objects.create(
            email =email,
            password =password,
            firstname = firstname,
            lastname = lastname
        )

    return render(request, 'index.html')





def list(request):
    if request.method =='GET':
        data = [obj.user_details() for obj in core_models.user.objects.all()]
       
        context ={
            "data":data,
        }
    return render(request , 'list.html',context)
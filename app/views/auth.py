from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from globals.request_manager import Action
from django.contrib import messages


def login (request): 
    
    if request.method == "POST" :
        data = request.POST
        action = Action(
            url=MAIN_URL + "/api/auth/login/",
            data=data
        )
        action.post()

        if action.is_valid() : 
            res =  redirect('home')
            res.set_cookie('user',action.json_data()['access'])
            return res
        
        messages.error(request,'البيانات التي ادخلتها غير صحيحة')
        return redirect('login')

    return render(request,'auth/login.html')

def register (request): 
    if request.method == "POST" :
        data = request.POST
        action = Action(
            url=MAIN_URL + "/api/auth/register/",
            data=data
        )

        if 'picture' in request.FILES:
            action.files = {
                "picture":request.FILES['picture']
            }

        action.post()

        if action.is_valid() : 
            res =  redirect('login')
            return res
        
        messages.error(request,'البيانات التي ادخلتها غير صحيحة')
        return redirect('register')
    
    return render(request,'auth/register.html')
    


def logout (request): 
    response = redirect('login')
    response.delete_cookie('user')
    return response


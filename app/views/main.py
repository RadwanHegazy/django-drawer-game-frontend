from django.shortcuts import render, redirect
from frontend.settings import MAIN_URL
from globals.request_manager import Action
from globals.decorators import login_required
from django.http import HttpResponse

@login_required
def profile (request) :
    context = {}
    return render(request,'home.html',context)


@login_required
def create_battle(request):
    action = Action(
        url=MAIN_URL + "/api/battle/create/",
        headers={'Authorization':f"Bearer {request.COOKIES.get('user')}"}
    )

    action.post()
    battle_id = action.json_data()['id']

    return redirect('view_battle',battle_id)



@login_required
def view_battle (request, user,battle_id):
    action = Action(
        url=MAIN_URL + f"/api/battle/get/{battle_id}/",
        headers={'Authorization':f"Bearer {request.COOKIES.get('user')}"}
    )

    action.get()
    if not action.is_valid() :
        return redirect('home')
    
    data = action.json_data()

    
    user_id = user['id']
    battle_owner_id = data['owner']
    
    if user_id == battle_owner_id : 
        return render(request,'gameplay/owner-gameplay.html',context={'battle_id':battle_id})
    else:
        return render(request,'gameplay/guest-gameplay.html',context={'battle_id':battle_id})

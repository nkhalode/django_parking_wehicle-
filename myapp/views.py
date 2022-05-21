from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth.models import User
import sweetify
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import UserDataModel

def login(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']
        
        user = authenticate(username=username1, password=password1)
        print(user)
        if user is not None:
            user_id =  str(user)
            return redirect('user-dashboard/' + user_id)
            
        else:
            messages.warning(request, 'Your Username and password are Incorrect.')
            return render(request,'myapp/login.html',{})
    else:
        return render(request,'myapp/login.html',{})
        
def UserDashBoard(request, user_id):
    if request.method == 'POST':
        
        if request.POST.get('edit_user_record_id') == '1':
            edit_record_id = request.POST['edit_record_id']
            edit_roll_number = request.POST['edit_roll_number']
            edit_name = request.POST['edit_name']
            edit_marks = request.POST['edit_marks']
            
            available_marks = UserDataModel.objects.get(id=edit_record_id).marks
            
            total_marks = int(edit_marks) + int(available_marks)
            
            UserDataModel.objects.filter(id=edit_record_id).update(roll_no = edit_roll_number, name = edit_name, marks = total_marks)
            
        else:
            roll_number = request.POST['roll_number']
            name = request.POST['name']
            marks = request.POST['marks']
            
            UserDataModel.objects.create(user_id = user_id, roll_no = roll_number, name = name, marks = marks)
        
    user_data = UserDataModel.objects.filter(user_id = user_id).order_by('-id')
    context = {
        'user' : user_id,
        'data': user_data,
    }
    return render(request,'myapp/userdasboard.html',context)

def DeleteUserRecords(request, id):
    result = UserDataModel.objects.filter(id = id).delete()
    
    if result:
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"error": False})

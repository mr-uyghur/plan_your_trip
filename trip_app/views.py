from django.shortcuts import render
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    
    return render(request, "index.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    password = request.POST['password']
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    register_incidence = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed

    )
    request.session['user_id'] = register_incidence.id
        
    return redirect('/dashboard')

def login(request):
    errors = User.objects.login_validator(request.POST)
        # check if the errors dictionary has anything in it
    if errors:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    user_list = User.objects.filter(email = request.POST['email'])
    #the if statement below chekcs if the uer exists
    if user_list:
        our_user = user_list[0]
        if bcrypt.checkpw(request.POST['password'].encode(),our_user.password.encode()):
            request.session['user_id'] = our_user.id 
            return redirect('/dashboard')
    else:
        messages.error(request, 'user or password incorrect')

    return redirect('/')

def shows_new(request):
    loggedin_user = User.objects.get(id = request.session['user_id'])
    context = {
            'user' : loggedin_user
        }
    return render(request, 'trip_new.html',context)

def create(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/trip/new')
    else:
        new = request.POST
        show_instance = Show.objects.create(
        title=new['title'],
        # network = new['network'],
        release_date = new['date_time'],
        end_date = new['end_time'],
        description = new["description"],
        
    
        )

 
        return redirect('/dashboard')


def dashboard(request):
    loggedin_user = User.objects.get(id = request.session['user_id'])
    context = {
        "show_list": Show.objects.all(),
        'user':loggedin_user,
        
    }
    return render(request, 'dashboard.html',context)

def edit(request,id):
    loggedin_user = User.objects.get(id = request.session['user_id'])
    context = {
        "show_list": Show.objects.get(id = id),
        'user' : loggedin_user,
        
        
    }
    return render(request, "edit.html",context)

def update(request,id):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/trip/{id}/edit')
    new = request.POST
    update = Show.objects.get(id = id)
    update.title = new['title']
    update.release_date = new['date_time']
    update.end_date = new['end_time']
    update.description = new['description']
    update.save()
    return redirect('/dashboard')

def delete(request,id):
    
    to_delete = Show.objects.get(id = id).delete()
    
        
    
    return redirect('/dashboard')

def logout(request):
    request.session.flush()
    return redirect('/')

def display_show(request,id):
    loggedin_user = User.objects.get(id = request.session['user_id'])
    context = {
        "show_list": Show.objects.get(id = id),
        'user' : loggedin_user,
        
        
    }
    return render(request, "trips.html",context)

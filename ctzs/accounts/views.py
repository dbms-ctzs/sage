from __future__ import unicode_literals


from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .decorators import unauthenticated_user,allowed_users





from .models import Profile, Comment
from datetime import datetime
from django.urls import reverse
from django.db.models import Q
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.template.loader import render_to_string
from django.forms import modelformset_factory


# Create your views here.

# Registration Page
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user) 
            return redirect('login')
    
    context={'form':form}
    return render(request,'accounts/register.html',context)


# Login Page
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
       
        user = authenticate(request,username=username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect ')     
            
    context={}
    return render(request,'accounts/login.html',context)


# Logout page
def logoutUser(request):
    logout(request)
    return redirect('login')



def sage(request):
    #post = get_object( id=id)
    comments = Comment.objects.filter( reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(user=request.user, content=content)
            comment.save()
             #return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form= CommentForm()

    context = {
        'comments': comments,
        'comment_form': comment_form,
    }
    if request.is_ajax():
        html = render_to_string('accounts/comments.html', context, request=request)
        return JsonResponse({'form': html})

    return render(request, 'accounts/home.html', context)



# @allowed_users(allowed_roles=['admin'])
@login_required(login_url='login', redirect_field_name=None)
def home(request):
    return redirect('sage')


# Profile View for the users profile
@login_required(login_url='login', redirect_field_name=None)
def profile(request):
    profiledata = {
        "name": request.user.username,
        "email": request.user.email,
        "rank": 1,
        "badge": "Great Sage",
    }
    return render(request, "accounts/profile.html", {
        "data": profiledata,
    })

# Display news using AJAX
#@login_required(login_url='login', redirect_field_name=None)
def news(request):
    return render(request, "accounts/news.html")

def grabnews(request):
    data = "New Grabber is Working"
    html = "<p>%s.</p>" % data
    return HttpResponse(html)

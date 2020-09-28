from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

#------------------------------------------------HTML Page---------------------------------------------------
#----------------------------------------------------home------------------------------------------
def home(request):
    allpost=Post.objects.all()
    context={'allpost':allpost}
    return render(request,'home/home.html',context)
#-----------------------------------------------contact-----------------------------------------------
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        content = request.POST.get('content', '')
        cont =Contact(name=name,email=email,phone=phone,content=content)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please Fill the form Correctly.')
        else:
            cont.save()
            messages.success(request, 'Your Massage has been success.')

    return render(request,'home/contact.html')


def about(request):
    messages.success(request,'This is about')
    return render(request,'home/about.html')

#---------------------------------------------search------------------------------------
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none()
    else:
        allposts_title = Post.objects.filter(title__contains=query)
        allposts_content = Post.objects.filter(content__contains=query)
        allposts = allposts_title.union(allposts_content)

    if allposts.count() == 0:
        messages.warning(request, 'No Search Result found. Please refine your Query')
    params = {'allposts': allposts ,'query':query}
    return render(request, 'home/search.html', params)

#----------------------------------------------------- Authentications APIs-----------------------------------------------
#----------------------------------Signup function----------------------------------------------------------
def handleSignup(request):
    if request.method=='POST':
        username =request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        Pass1 = request.POST['Pass1']
        Pass2 = request.POST['Pass2']
    #check for errorneous input
        #username should be 10 charchactres
        if len(username)>10:
            messages.error(request, 'Username Must be under 10 characters')
            return redirect('home')

        #passwords should match
        if Pass1 != Pass2:
            messages.error(request,'Password do not match')
            return redirect('home')

        #create user only alphabet and numeric
        if not username.isalnum() :
            messages.error(request,'Username should only contain lettter number')
            return redirect('home')

    #create the user
        myuser=User.objects.create_user(username, email, Pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your iCoder Account has been successfully created')
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found ')

#-------------------------------------------------login function------------------------------------------
def handleLogin(request):
    if request.method=='POST':
        #get the post parameters
        loginusername = request.POST['loginusername']
        loginPass = request.POST['loginPass']
        user = authenticate(username=loginusername , password=loginPass)
        if user is not None:
           login(request , user)
           messages.success(request,'Successfully Logged In')
           return redirect('home')
        else:
            messages.error(request,"Invaild Credentials , please try again ")
            return redirect('home')

    return HttpResponse('404 - Not Found ')

#-------------------------------------------------logout function-----------------------------------------
def handleLogout(request):
        logout(request)
        messages.success(request, 'Successfully Logged Out')
        return redirect('home')


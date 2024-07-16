from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from play.models import *
import os 
# Create your views here.
def index(request):
    return render(request,'index.html')
def register1(request):
    return render(request,'register1.html')
def register2(request):
    return render(request,'register2.html')
def rgs1(request):
    a = request.GET['a1']
    obj = user.objects.all()
    for i in obj:
        if i.name == a:
            error_message = "The username already exists. Please choose a different name."
            return render(request, 'register1.html', {'error_message': error_message})
    u = user()
    u.name = request.GET['a1']
    u.pwd = request.GET['a2']
    u.save()
    return render(request, 'register_success.html')

def rgs2(request):
    a = request.GET['a1']
    b = request.GET['a2']
    obj = admin.objects.all()
    for i in obj:
        if i.name == a:
            error_message = "The username already exists. Please choose a different name."
            return render(request, 'register2.html', {'error_message': error_message})
    if not admin.objects.exists():
        new_admin = admin.objects.create(name=a, pwd=b)
        return render(request,'register_success.html')
    else:
        v = verify()
        v.name = request.GET['a1']
        v.pwd = request.GET['a2']
        v.save()
        return render(request,'verifypage.html')
def login(request):
    return render(request,'login.html')
def login2(request):
    return render(request,'login2.html')
def register_success(request):
    return render(request,'register_success.html')
def welcome(request):
    return render(request,'welcome.html')
def log(request):
    a = request.GET.get('a1')
    b = request.GET.get('a2')
    obj = user.objects.all()
    if not a or not b:
        error_message = "Please provide both username and password."
        return render(request, 'login.html', {'error_message': error_message})
    for i in obj:
        if i.name == a and i.pwd == b:
            return render(request, 'index.html')
    error_message = "Incorrect username or password. Please try again."
    return render(request, 'login.html', {'error_message': error_message})
def log2(request):
    a = request.GET.get('a1')
    b = request.GET.get('a2')
    obj = admin.objects.all()
    if not a or not b:
        error_message = "Please provide both username and password."
        return render(request, 'login2.html', {'error_message': error_message})
    for i in obj:
        if i.name == a and i.pwd == b:
            return render(request, 'adminpage.html')
    error_message = "Incorrect username or password. Please try again."
    return render(request, 'login2.html', {'error_message': error_message})

def show(request):
    u = user.objects.all()
    return render(request,'show.html',{'u':u})
def dele(request,id):
    u = user.objects.get(id=id)
    u.delete()
    return redirect("../show")
def edit(request,id):
    u = user.objects.get(id=id)
    return render(request,'edit.html',{'u':u})
def edcode(request,id):
    u = user.objects.get(id=id)
    u.name = request.GET['a1']
    u.pwd  = request.GET['a2']
    u.save()
    return redirect("../show")

def search_user(request):
    if request.method=="POST":
        query=request.POST['query']
        users=user.objects.filter(name__contains=query)
        return render(request,'search_user.html',{'query':query,'users':users}) 
    
    else:
        return HttpResponse('user_not_found') #newly added

    
def search_admin(request):
    if request.method=="POST":
        adminquery=request.POST['adminquery']
        admins=admin.objects.filter(name__contains=adminquery)
        return render(request,'search_admin.html',{'adminquery':adminquery,'admins':admins}) 
    
    else:
        return HttpResponse('user_not_found')                                          #newly added

def show2(request):
    a = admin.objects.all()
    return render(request,'show2.html',{'a':a})
def dele2(request,id):
    a = admin.objects.get(id=id)
    a.delete()
    return redirect("../show2")
def edit2(request,id):
    a = admin.objects.get(id=id)
    return render(request, 'edit2.html',{'a':a})
def edcode2(request,id):
    a = admin.objects.get(id=id)
    a.name = request.GET['a1']
    a.pwd = request.GET['a2']
    a.save()
    return redirect("../show2")
def adminpage(request):
    return render(request,'adminpage.html')
def verifypage(request):
    return render(request, 'verifypage.html')
def show3(request):
    v = verify.objects.all()
    return render(request,'show3.html',{'v':v})
def dele3(request,id):
    v = verify.objects.get(id=id)
    v.delete()
    return redirect("../show3")
def accept_admin(request, id):
    # Ensure that the request method is GET
    if request.method == 'GET':
        # Get the admin from the verification table
        v = verify.objects.get(id=id)
        # Create a new admin entry in the admin table
        a = admin.objects.create(name=v.name, pwd=v.pwd)
        # Delete the admin entry from the verification table
        v.delete()
        return redirect('../show3')  # Redirect back to the verification table page
    else:
        return redirect('../show3')  # Redirect back to the verification table page if not a GET request
def rockballad(request):
    return render(request, 'rockballad.html')

#for track upload
def upld(request):
    return render(request, 'upload.html')

def handle_uploaded_file(file, filename):
    if not os.path.exists('play/static/media/'):
        os.makedirs('play/static/media/')  # Create directory if not exists

    with open('play/static/media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def upd(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        # You can add validation here if needed (e.g., file type, size)

        handle_uploaded_file(audio_file, str(audio_file))
        url = "upload/" + str(audio_file)
        
        # Save the file information to the database
        audio = AudioFile()
        audio.filename = str(audio_file)
        audio.fileurl = url
        audio.save()

        return HttpResponse("Successful")
    
    return HttpResponse("Failed")

def show_audio(request):
    audio_files = AudioFile.objects.all()
    return render(request, 'audioshow.html', {'audio_files': audio_files})

#for rupam islam song upload
def rockupload(request):
    return render(request, 'rockupload.html')

def handle_uploaded_file2(file, filename):
    if not os.path.exists('play/static/media/'):
        os.makedirs('play/static/media/')  # Create directory if not exists

    with open('play/static/media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def rockupd(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        # You can add validation here if needed (e.g., file type, size)

        handle_uploaded_file2(audio_file, str(audio_file))
        url = "upload/" + str(audio_file)
        
        # Save the file information to the database
        audio = rockfile()
        audio.filename = str(audio_file)
        audio.fileurl = url
        audio.save()

        return HttpResponse("Successful")
    
    return HttpResponse("Failed")

def rockshow(request):
    audio_files = rockfile.objects.all()
    return render(request, 'rockshow.html', {'audio_files': audio_files})

#for kk songs upload
def kkupload(request):
    return render(request, 'kkupload.html')

def handle_uploaded_file3(file, filename):
    if not os.path.exists('play/static/media/'):
        os.makedirs('play/static/media/')  # Create directory if not exists

    with open('play/static/media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def kkupd(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        # You can add validation here if needed (e.g., file type, size)

        handle_uploaded_file3(audio_file, str(audio_file))
        url = "upload/" + str(audio_file)
        
        # Save the file information to the database
        audio = kksongs()
        audio.filename = str(audio_file)
        audio.fileurl = url
        audio.save()

        return HttpResponse("Successful")
    
    return HttpResponse("Failed")

def kkshow(request):
    audio_files = kksongs.objects.all()
    return render(request, 'kkshow.html', {'audio_files': audio_files})

#user playlist upload

def userplaylistupload(request):
    return render(request, 'userplaylistupload.html')

def handle_uploaded_file4(file, filename):
    if not os.path.exists('play/static/media/'):
        os.makedirs('play/static/media/')  # Create directory if not exists

    with open('play/static/media/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def userplaylistupd(request):
    if request.method == 'POST':
        audio_file = request.FILES['audio_file']
        # You can add validation here if needed (e.g., file type, size)

        handle_uploaded_file4(audio_file, str(audio_file))
        url = "upload/" + str(audio_file)
        
        # Save the file information to the database
        audio = usersongs()
        audio.filename = str(audio_file)
        audio.fileurl = url
        audio.save()

        return HttpResponse("Successful")
    
    return HttpResponse("Failed")

def userplaylistshow(request):
    audio_files = usersongs.objects.all()
    return render(request, 'userplaylistshow.html', {'audio_files': audio_files})


#for playlist creation
def customplaylist(request):
    return render(request, 'customplaylist.html')


def song_list(request):
    song_directory = 'play/static/songs'  
    songs = os.listdir(song_directory)
    return JsonResponse({'songs': songs})
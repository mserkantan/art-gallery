
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, user_logged_in
from django.contrib.auth import login as lg

from django.http import HttpResponse
from datetime import date
import calendar
from calendar import HTMLCalendar
from django.contrib.auth.models import User as us

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required



import pandas as pd

from artist.models import Artist, Artist_Image
from museum.models import Museum, MuseumImage
from art_object.models import Artifact, ArtifactImage
from user.models import User, Contact
from place.models import Place
from art_movement.models import Art_Movement


def place(request):
    return render(request, 'user/place.html')

@login_required(login_url='login')
def artifact(request):
    artifact_objects = Artifact.objects.all()
    image_objects = ArtifactImage.objects.all()
    artifact_names = [a.artifact_title for a in artifact_objects]
    images= [i.artifact_image for i in image_objects]
    artifact = [{'name': t[0], 'image':t[1]} for t in zip(artifact_names, images)]

    context= {
        "artifact": artifact
    }

    return render(request, 'user/artifact.html', context=context)
@login_required(login_url='login')
def museum(request):
    museum_objects = Museum.objects.all()
    #image_objects = [get_object_or_404(Museum, of_artist=i) for i in artist_objects]

    image_objects = MuseumImage.objects.all()
    museum_names = [a.museum_name for a in museum_objects]

    images= [i.museum_image for i in image_objects]
    museum = [{'name': t[0], 'image':t[1]} for t in zip(museum_names, images)]

    context= {
        "museum": museum
    }

    return render(request, 'user/museum.html', context=context)
@login_required(login_url='login')
def index(request, year=date.today().year, month=date.today().month):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return HttpResponse("Not Authenticated")

    user = User.objects.get(user_name=username)
    year = int(year)
    month = int(month)
    if year < 1900 or year > 2099: 
        year = date.today().year
    month_name = calendar.month_name[month]
    title = "MyClub Event Calendar - %s %s" % (month_name, year)
    cal = HTMLCalendar().formatmonth(year, month)
    page_title = 'Art Gallery Website'
    # return HttpResponse("<h1>%s</h1><p>%s</p>" % (title, cal))
    return render(request, 'user/index.html', {'title': title, 'cal': cal, 'page_title': page_title, 'name':user.user_real_name})  

@login_required(login_url='login')
def artist(request):
    artist_objects = Artist.objects.all()
    image_objects = [get_object_or_404(Artist_Image, of_artist=i) for i in artist_objects]
    artist_names = [a.artist_name for a in artist_objects]

    images= [i.image for i in image_objects]
    artist_surnames = [a.artist_surname for a in artist_objects]
    artist = zip(artist_names, artist_surnames, images)
    artist = [{'name': t[0], 'surname': t[1], 'image':t[2]} for t in zip(artist_names, artist_surnames, images)]

    context= {
        "artist_names": artist_names,
        "artist_surnames": artist_surnames,
        "images": images,
        "artist": artist
    }

    return render(request, 'user/artist.html',  context=context)  
    
def sign_up(request):
    return render(request, 'user/signup.html')

def login(request):
    if len(request.POST) != 0:
        email=request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        print(email, username, password)
        try:
            current_user = Contact.objects.get(user_email=email)
        except Contact.DoesNotExist:
            current_user = None
        if current_user == None:
            user =  User.objects.create(user_name=username, user_password=password)
            contact = Contact.objects.create(user_id=user, user_email=email)
            django_user = us.objects.create_user(username, email, password)

        else: return HttpResponse("The email is in use!")

    return render(request, 'user/login.html')

def auth(request):
    if len(request.POST) != 0:
        username=request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username=username, password=password)
    
    if user is None:
        return HttpResponse("email or password is incorrent but I won't tell which is :)")
    else:
        lg(request, user)
        return render(request, 'user/index.html')



@login_required(login_url='login')
def works(request, name):
    artist_id = get_object_or_404(Artist, artist_name=name)
    artifacts = get_list_or_404(Artifact, artist_id=artist_id)
    artifact_images = [get_object_or_404(ArtifactImage, artifact_id=a) for a in artifacts]
    
    works = [{'artifacts': t[0], 'artifact_images': t[1]} for t in zip(artifacts, artifact_images)]

    context = {
        "artist_name": name,
        "works": works
    }
    return render(request, 'user/works.html', context=context)

def museum_artifacts(request, name):
    museum_id = get_object_or_404(Museum, museum_name=name)
    artifacts = get_list_or_404(Artifact, museum_id=museum_id)
    artifact_images = [get_object_or_404(ArtifactImage, artifact_id=a) for a in artifacts]
    works = [{'artifacts': t[0], 'artifact_images': t[1]} for t in zip(artifacts, artifact_images)]
    context = {
            "artist_name": name,
            "works": works
        }
    return render(request, "user/works.html", context=context)

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return render(request, "user/login.html")


def details(request, title):
    artifact_object = get_object_or_404(Artifact, artifact_title=title)
    artifact_id = artifact_object.id
    artifact_image = get_object_or_404(ArtifactImage, artifact_id=artifact_id)
    context ={
        "image": artifact_image.artifact_image,
        "artifact_title": artifact_object.artifact_title,
        "content": artifact_object.artifact_description,

    }

    #return HttpResponse(context.items())
    return render(request, "user/details.html", context=context)

def user_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    else:
        return HttpResponse("Not Authenticated")

    if len(request.POST) != 0:
        print(request.POST["image"])
        user_contact = Contact.objects.get(user_email=request.POST.get("email"))
        user = user_contact.user_id
        User.objects.filter(pk=user.user_id).update(user_real_name=request.POST.get("first_name"),
                                        user_surname=request.POST.get("last_name"),
                                        user_password=request.POST.get("password"),
                                        user_picture=request.POST.get("image"),
                                        )
    
        Contact.objects.filter(user_id=user).update(user_email=request.POST.get("email"),
                                        user_phone_number=request.POST.get("phone"),
                                        )
    
            
    print(username)
    user = User.objects.get(user_name=username)
    user_contact = Contact.objects.get(user_id=user)
    context ={
        "username": username,
        "name":user.user_real_name,
        "surname": user.user_surname,
        "email": user_contact.user_email,
        "phone": user_contact.user_phone_number,
        "picture": user.user_picture,
        "birthdate": user.user_birthdate,
        "image": user.user_picture,


    }
    return render(request, 'user/user.html', context=context)
    

def user_edit(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        print(username)
        user = User.objects.get(user_name=username)
        user_contact = Contact.objects.get(user_id=user)
        context ={
            "username": username,
            "name":user.user_real_name,
            "surname": user.user_surname,
            "email": user_contact.user_email,
            "phone": user_contact.user_phone_number,
            "password": user.user_password,
            "image": user.user_picture,
        }
        return render(request, 'user/user_edit.html', context=context)
    else:
        return HttpResponse("Not Authenticated")


def art_movement(request):
    artmovement_objects = Art_Movement.objects.all()   
    movement_names = [a.movement_name for a in artmovement_objects]
    movement_descriptions = [a.movement_description for a in artmovement_objects]
    movement_era = [a.movement_era for a in artmovement_objects]
    images= [a.movement_picture for a in artmovement_objects]

    artmovements = [{'name': t[0], 'description': t[1], 'era':t[2], 'image':t[3]} for t in zip(movement_names, movement_descriptions, movement_era, images)]

    context= {

        "artmovements": artmovements
    }

    return render(request, 'user/art_movement.html',  context=context)  
''' We start to handle admin operations . . .'''
def admin_panel(request):
    places = [i.place_city for i in Place.objects.all()]
    artists =[i.artist_name for i in Artist.objects.all()]
    museums = [i.museum_name for i in Museum.objects.all()]
    context = {
        "places": places,
        "artists": artists,
        "museums": museums,
        "artist_objects": Artist.objects.all(),
        "artifact_objects": Artifact.objects.all(),
        "museum_objects": Museum.objects.all(),
        "place_objects": Place.objects.all(),
        "user_objects": User.objects.all(),
    }
    print(places)
    print(artists)
    print(museums)
    return render(request, "user/admin_panel.html", context=context)

def create(request, model):
    query = request.POST
    print(query)
    if model == "artist":
        new_artist = Artist.objects.create(artist_name=query["name"],
                              artist_surname=query["surname"],
                              artist_birthdate=query["birthdate"],
                              artist_deathdate=query["deathdate"],
                              place_born=Place.objects.get(place_city=query["born"]),  
                              place_death=Place.objects.get(place_city=query["death"])  
                            )
        print(new_artist)
        Artist_Image.objects.create(of_artist=new_artist, image=query["artist_image"])

    elif model == "artifact":
        new_artifact = Artifact.objects.create(artist_id=Artist.objects.get(artist_name=query["artist"]),  
                                museum_id=Museum.objects.get(museum_name=query["museum"]),  
                                artifact_title=query["title"],
                                artifact_original_title=query["ori_title"],
                                artifact_description=query["description"],
                                artifact_creation=query["creation"],
                            )
        print(new_artifact)
        ArtifactImage.objects.create(artifact_id=new_artifact, artifact_image=query["artifact_image"])


    elif model == "museum":
        new_museum = Museum.objects.create(place_id=Place.objects.get(place_city=query["place"]),  
                                museum_name=query["name"],
                                museum_description=query["description"],
                                foundation_date=query["foundation"],
                            )
        print(new_museum)
        MuseumImage.objects.create(museum_id=new_museum, museum_image=query["museum_image"])
    elif model == "place":
        new_place = Place.objects.create(place_country=query["country"],  
                                place_city=query["city"],
                                place_zip=query["zip"],
                                place_description=query["description"],
                            )
        print(new_place)
    elif model == "artmovement":
        new_artmovement = Art_Movement.objects.create(movement_name=query["name"],  
                                movement_description=query["description"],
                                movement_era=query["era"],
                                movement_picture=query["image"],
                            )
        print(new_artmovement)

    return render(request, "user/admin_panel.html")

def update(request, model):
    update = None
    if len(request.POST) != 0:
        update = request.POST
    else: 
        return HttpResponse("No post!")
        
    if model == "artist":
        Artist.objects.filter(pk=update["id"]).update(artist_name=request.POST.get("first_name"),
                                        artist_surname=request.POST.get("last_name"),
                                        artist_birthdate=request.POST.get("password"),
                                        artist_deathdate=request.POST.get("password"),
                                        place_born=request.POST.get("password"),
                                        place_death=request.POST.get("password"),
                                        )
    
        Contact.objects.filter(user_id=user).update(user_email=request.POST.get("email"),
                                        user_phone_number=request.POST.get("phone"),
                                        )    
    elif model == "artifact":
        pass
    elif model == "museum":
        model_objects = Museum.objects.all()
    elif model == "place":
        model_objects = Place.objects.all()
    elif model == "user":
        model_objects = User.objects.all()

    elif model == "delete_artist":
        pass
    elif model == "delete_artifact":
        pass
    elif model == "delete_museum":
        pass
    elif model == "delete_place":
        pass
    elif model == "delete_user":
        pass

    context = {
    }
    return HttpResponse("hoho")
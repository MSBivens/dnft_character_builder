from flask import render_template, redirect, request, session
from flask_app import app
import python_avatars as pa
from python_avatars.avatar import Avatar
from python_avatars.hair_colors import HairColor
from python_avatars.avatar_styles import AvatarStyle
from python_avatars.skin_colors import SkinColor
from python_avatars.top_types import TopType
from python_avatars.hair_types import HairType
from python_avatars.hat_types import HatType
from python_avatars.facial_hair_types import FacialHairType
from python_avatars.mouth_types import MouthType
from python_avatars.eye_types import EyeType
from python_avatars.eyebrow_types import EyebrowType
from python_avatars.accessory_types import AccessoryType
from python_avatars.clothing_types import ClothingType
from python_avatars.clothing_colors import ClothingColor
from python_avatars.clothing_graphics import ClothingGraphic
from python_avatars.background_colors import BackgroundColor

# new instance
my_avatar = Avatar()
    
@app.route('/')
def redirectGEThome():
    return redirect('/home')

@app.route('/home')
def GEThome():
    return render_template('home.html')

@app.route('/dashboard/<int:id>')
def GETdashboard(id):
    return render_template('dashboard.html')

@app.route('/about')
def GETabout():
    return render_template('about.html')

@app.route('/mint')
def GETmint():
    return render_template('mint.html')


# this route renders the page
@app.route('/customize')
def GETcustomize():
    toptypes = TopType.get_all()
    return render_template('customize.html', 
    avatar = my_avatar,
    haircolors = HairColor, 
    styles = AvatarStyle,
    skincolors = SkinColor,
    toptypes = toptypes,
    facial_hair_types = FacialHairType,
    mouthtypes = MouthType,
    eyetypes = EyeType,
    eyebrowtypes = EyebrowType,
    accessorytypes = AccessoryType,
    clothingtypes = ClothingType,
    clothingcolors = ClothingColor,
    clothinggraphics = ClothingGraphic,
    backgroundcolors = BackgroundColor
    )


# this route gives each attribute a random value
@app.route('/customize/random')
def GETcustomizerandom():
    my_avatar.style=str(AvatarStyle.pick_random()) 
    my_avatar.background_color=str(BackgroundColor.pick_random())
    my_avatar.top=str(TopType.pick_random()) 
    my_avatar.hat_color=str(ClothingColor.pick_random()) 
    my_avatar.eyebrows=str(EyebrowType.pick_random()) 
    my_avatar.eyes=str(EyeType.pick_random()) 
    my_avatar.mouth=str(MouthType.pick_random())
    my_avatar.facial_hair=str(FacialHairType.pick_random(favor=FacialHairType.NONE)) 
    my_avatar.skin_color=str(SkinColor.pick_random()) 
    my_avatar.hair_color=str(HairColor.pick_random()) 
    my_avatar.facial_hair_color=str(HairColor.pick_random())
    my_avatar.accessory=str(AccessoryType.pick_random(favor=AccessoryType.NONE)) 
    my_avatar.clothing=str(ClothingType.pick_random()) 
    my_avatar.clothing_color=str(ClothingColor.pick_random()) 
    my_avatar.shirt_graphic=str(ClothingGraphic.pick_random())

    # this updates the existing my_avatar.svg 
    my_avatar.render("flask_app/static/images/my_avatar.svg")
    return redirect('/customize')


# this route updates the attributes of the main instance with the corresponding selected values from the form
@app.route('/customize/update', methods=['POST'])
def POSTcustomize():
    my_avatar.title = request.form.get("title")
    my_avatar.top = request.form.get("top_type")
    my_avatar.hair_color = request.form.get("hair_color")
    my_avatar.style = request.form.get("style")
    my_avatar.background_color = request.form.get("background_color")
    my_avatar.skin_color = request.form.get("skin_color")
    my_avatar.hat_color = request.form.get("hat_color")
    my_avatar.facial_hair = request.form.get("facial_hair_type")
    my_avatar.facial_hair_color = request.form.get("facial_hair_color")
    my_avatar.mouth = request.form.get("mouth_type")
    my_avatar.eyes = request.form.get("eye_type")
    my_avatar.eyebrows = request.form.get("eyebrow_type")
    my_avatar.accessory = request.form.get("accessories_type")
    my_avatar.clothing = request.form.get("clothes_type")
    my_avatar.clothing_color = request.form.get("clothes_color")
    my_avatar.shirt_graphic = request.form.get("clothes_graphic_type")

    # this updates the existing my_avatar.svg 
    my_avatar.render("flask_app/static/images/my_avatar.svg")
    return redirect('/customize')
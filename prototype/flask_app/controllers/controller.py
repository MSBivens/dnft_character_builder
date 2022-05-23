from flask import render_template, redirect, request, session
from flask_app import app
import python_avatars as pa
from python_avatars.avatar import Avatar
from python_avatars.hair_colors import HairColor
from python_avatars.avatar_styles import AvatarStyle
from python_avatars.skin_colors import SkinColor
from python_avatars.top_types import TopType
from python_avatars.facial_hair_types import FacialHairType
from python_avatars.mouth_types import MouthType
from python_avatars.eye_types import EyeType
from python_avatars.eyebrow_types import EyebrowType
from python_avatars.accessory_types import AccessoryType
from python_avatars.clothing_types import ClothingType
from python_avatars.clothing_colors import ClothingColor
from python_avatars.clothing_graphics import ClothingGraphic
from python_avatars.background_colors import BackgroundColor

my_avatar = Avatar()


@app.route('/')
def redirectGEThome():
    # if 'userid' in session:
    #     return redirect('/dashboard')
    return redirect('/home')

@app.route('/home')
def GEThome():
    return render_template('home.html')

@app.route('/dashboard/<int:id>')
def GETdashboard(id):
    # if 'userid' not in session:
    #     return redirect('/home')
    return render_template('dashboard.html')

@app.route('/about')
def GETabout():
    return render_template('about.html')

@app.route('/mint')
def GETmint():
    # if 'userid' not in session:
    #     return redirect('/home')
    return render_template('mint.html')

@app.route('/customize')
def GETcustomize():
    # if 'userid' not in session:
    #     return redirect('/home')
    haircolor = my_avatar.hair_color
    toptypes = TopType.get_all()
    return render_template('customize.html', 
    haircolors = HairColor, 
    haircolor = haircolor,
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

@app.route('/customize/random')
def GETcustomizerandom():
    my_avatar = Avatar.random()
    my_avatar.render("flask_app/static/images/my_avatar.svg")
    return redirect('/customize')

@app.route('/customize/update', methods=['POST'])
def POSTcustomize():
    my_avatar.hair_color = request.form.get("hair_color")
    my_avatar.style = request.form.get("style")
    my_avatar.background_color = request.form.get("background_color")
    my_avatar.skin_color = request.form.get("skin_color")
    # my_avatar.top = request.form.get("head_top")
    my_avatar.facial_hair = request.form.get("facial_hair_type")
    my_avatar.facial_hair_color = request.form.get("facial_hair_color")
    my_avatar.mouth = request.form.get("mouth_type")
    my_avatar.eyes = request.form.get("eye_type")
    my_avatar.eyebrows = request.form.get("eyebrow_type")
    my_avatar.accessory = request.form.get("accessories_type")
    my_avatar.clothing = request.form.get("clothes_type")
    my_avatar.clothing_color = request.form.get("clothes_color")
    my_avatar.shirt_graphic = request.form.get("clothes_graphic_type")
    my_avatar.render("flask_app/static/images/my_avatar.svg")
    return redirect('/customize')
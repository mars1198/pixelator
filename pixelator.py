from PIL import Image
import glob
import os



def Pixel(path, string):
    for filename in glob.glob(string): #path of raw images
       img = Image.open(filename)
       imgSmall = img.resize((128,128),resample=Image.BILINEAR)
       result = imgSmall.resize(img.size,Image.NEAREST)
    # save resized images to new folder with existing filename
       result.save('{}{}{}'.format(path,'/',os.path.split(filename)[1]))


path = 'Resized_Shapes/Ginia munda munda'
string = 'images/Ginia munda munda/*.jpg' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Pixel(path, string)

path = 'Resized_Shapes/Ginia sublitoralis'
string = 'images/Ginia sublitoralis/*.jpg' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Pixel(path, string)

path = 'Resized_Shapes/Macedopyrgula pavlovici'
string = 'images/Macedopyrgula pavlovici/*.jpg' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Pixel(path, string)

path = 'Resized_Shapes/Macedopyrgula wagneri'
string = 'images/Macedopyrgula wagneri/*.jpg' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Pixel(path, string)

path = 'Resized_Shapes/Ohridopyrgula charensis'
string = 'images/Ohridopyrgula charensis/*.jpg' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Pixel(path, string)

path = 'Resized_Shapes/Ohridopyrgula macedonica'
string = 'images/Ohridopyrgula macedonica/*.jpg' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Pixel(path, string)

path = 'Resized_Shapes/Ohridopyrgula svnaum'
string = 'images/Ohridopyrgula svnaum/*.jpg' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)
Pixel(path, string)


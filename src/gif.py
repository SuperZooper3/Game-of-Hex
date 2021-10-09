import glob
import os
import datetime
from pygame import image
from settings import GIFSPEED
from PIL import Image
from platform import system
sys = system().lower()

# Base code from: https://pythonprogramming.altervista.org/pygame-draw-app-with-animation/

cnt = 0

def clearImg(): # Clear all the screenshots from the folder
    [os.remove(png) for png in glob.glob("img/sc/sfsc*png")]

def screenshot(screen): # Takes a screenshot of the gamescreen and saves it for gif making
    global cnt
    image.save(screen, f"img/sc/sfsc{cnt}.png")
    cnt += 1

def compileGif():
    frames = [] # Array to store all the frames in
    imgs = sorted(glob.glob("img/sc/sfsc*.png"), key=os.path.getmtime) # Get all the frames made by the screenshotter
    for i in imgs: 
        new_frame = Image.open(i) # Open the image
        frames.append(new_frame) # Load it onto an array
 
    # Save into a GIF file that loops forever
    t = round(datetime.datetime.now().timestamp()*10) # Time to timestamp the gif
    if len(frames) > 0:
        frames[0].save(f"img/snowflake{t}.gif", format='GIF',
                    append_images=frames[1:], # Load in every single frame
                    save_all=True, # Idk what this does :)
                    duration=GIFSPEED*10*len(frames), loop=0) # 0.3 seconds per frame, make that shit loop
        if sys == 'windows': # dosent work on mac :kekw:
            os.startfile(os.path.join(os.getcwd(), f"img/snowflake{t}.gif")) # Open the gif to watch it instantly

    for i in frames: i.close() # #savingram
import glob
import os
import datetime
from pygame import image
from settings import GIFSPEED, RESOLUTION, GIFCOMPRESSION
from PIL import Image
from platform import system

sys = system().lower()

# Base code from: https://pythonprogramming.altervista.org/pygame-draw-app-with-animation/

cnt = 0


def clearImg():  # Clear all the screenshots from the folder
    [os.remove(png) for png in glob.glob("img/sc/sfsc*png")]


def screenshot(screen, path="img/sc/sfsc"):  # Takes a screenshot of the gamescreen and saves it for gif making
    global cnt
    image.save(screen, f"{path}{cnt}.png")
    cnt += 1


def compileGif():
    frames = []  # Array to store all the frames in
    imgs = sorted(
        glob.glob("img/sc/sfsc*.png"), key=os.path.getmtime
    )  # Get all the frames made by the screenshotter
    for i in imgs:
        new_frame = Image.open(i)  # Open the image
        new_frame = new_frame.quantize(
            method=Image.MEDIANCUT
        )  # Conver the colours for nicer gifs

        new_frame = new_frame.resize(
            tuple(round(n / GIFCOMPRESSION) for n in RESOLUTION), Image.LANCZOS
        )  # Compress the gif

        frames.append(new_frame)  # Load it onto an array

    # Save into a GIF file that loops forever
    t = str(round(datetime.datetime.now().timestamp() * 10))[3:]  # Time to timestamp the gif
    
    if len(frames) > 0:
        frames[0].save(
            f"img/gif/snowflake{t}.gif",
            format="GIF",
            append_images=frames[1:],  # Load in every single frame
            save_all=True,  # Idk what this does :)
            duration=GIFSPEED * 400,
            loop=0,
            optimize=True,
        )
        if sys == "windows":  # dosent work on mac :kekw:
            os.startfile(
                os.path.join(os.getcwd(), f"img/gif/snowflake{t}.gif")
            )  # Open the gif to watch it instantly

    for i in frames:
        i.close()  # #savingram

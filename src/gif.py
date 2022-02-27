import datetime
import glob
import os
from platform import system
from typing import List

from PIL import Image, PngImagePlugin  # type: ignore
from pygame import display, image
import pygame
from settings import CROPPING, GIFCOMPRESSION, GIFSPEED, RESOLUTION

sys = system().lower()

# Base code from: https://pythonprogramming.altervista.org/pygame-draw-app-with-animation/

cnt: int = 0


def clearImg() -> None:  # Clear all the screenshots from the folder
    for png in glob.glob("img/sc/sfsc*png"):
        os.remove(png)


def screenshot(
    screen: pygame.Surface, path: str = "img/sc/sfsc"
) -> None:  # Takes a screenshot of the gamescreen and saves it for gif making
    global cnt
    image.save(screen, f"{path}{cnt}.png")
    im = Image.open(f"{path}{cnt}.png")
    im = im.crop((1, 1, RESOLUTION[0] - CROPPING, RESOLUTION[1]))
    im.save(f"{path}{cnt}.png")
    cnt += 1


def compileGif() -> None:
    frames: List[PngImagePlugin.PngImageFile] = []  # Array to store all the frames in
    imgs: List[str] = sorted(
        glob.glob("img/sc/sfsc*.png"), key=os.path.getmtime
    )  # Get all the frames made by the screenshotter
    for i in imgs:
        new_frame: PngImagePlugin.PngImageFile = Image.open(i)  # Open the image
        new_frame = new_frame.quantize(
            method=Image.MEDIANCUT
        )  # Conver the colours for nicer gifs

        new_frame = new_frame.resize(
            (
                round((RESOLUTION[0] - CROPPING) / GIFCOMPRESSION),
                round(RESOLUTION[1] / GIFCOMPRESSION),
            ),
            Image.LANCZOS,
        )  # Compress the gif

        frames.append(new_frame)  # Load it onto an array

    # Save into a GIF file that loops forever
    t: str = str(round(datetime.datetime.now().timestamp() * 10))[
        3:
    ]  # Time to timestamp the gif

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
            # Open the gif to watch it instantly
            os.startfile(  # type: ignore
                os.path.join(os.getcwd(), f"img/gif/snowflake{t}.gif")
            )

    # #savingram
    for i in frames:
        # For some reason, mypy thinks `i` is a str /shrug
        i.close()  # type: ignore

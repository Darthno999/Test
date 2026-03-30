'''
Created by Frederikme (TeetiFM)

This script is meant to be user friendly for beginning users.
Definitly take a look at quickstart.py for more features!
'''

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path


def _ensure_python_dependencies():
    required_modules = (
        "selenium",
        "undetected_chromedriver",
        "PIL",
        "deepface",
        "cv2",
        "numpy",
    )

    missing_modules = [module for module in required_modules if importlib.util.find_spec(module) is None]
    if not missing_modules:
        return

    print(f"Missing Python packages detected: {', '.join(missing_modules)}")
    print("Installing requirements from requirements.txt ...")

    requirements_path = Path(__file__).resolve().parent / "requirements.txt"
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(requirements_path)])


def _ensure_browser_installed():
    chrome_like_browser = (
        shutil.which("google-chrome")
        or shutil.which("google-chrome-stable")
        or shutil.which("chromium-browser")
        or shutil.which("chromium")
    )

    if chrome_like_browser:
        return

    raise RuntimeError(
        "No Chrome/Chromium browser detected. On Ubuntu, run:\n"
        "sudo apt update && sudo apt install -y chromium-browser"
    )


if __name__ == "__main__":
    _ensure_python_dependencies()
    _ensure_browser_installed()

    from tinderbotz.session import Session
    from tinderbotz.helpers.constants_helper import *

    # creates instance of session
    session = Session()

    # replace this with your own email and password!
    email = "example@gmail.com"
    password = "password123"

    # login using either your facebook account or google account (delete the line of code you don't need)
    session.login_using_facebook(email, password)
    session.login_using_google(email, password)

    # AI-based auto swipe (uses your filters + image scan before deciding like/dislike)
    # amount          -> number of profiles to process
    # profile_filters -> metadata filters (age, distance, gender, passions, bio keywords, ...)
    # image_filters   -> DeepFace filters (dominant gender/race/emotion + estimated age range)
    # sleep           -> base seconds to wait before swiping again
    session.like_with_ai_filters(
        amount=100,
        profile_filters={
            "min_age": 21,
            "max_age": 35,
            "max_distance": 50,
            "genders": ["Woman"],
            "bio_keywords": ["travel", "coffee"]
        },
        image_filters={
            "dominant_gender": "Woman",
            "dominant_emotion": "happy"
        },
        sleep=1
    )

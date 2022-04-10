import subprocess
import random

from constants import LANGUAGES

# Changes desktop language randomly
def languages():
    lang = random.choice(LANGUAGES)
    return f"""Set-Culture {lang}
    Set-WinSystemLocale -SystemLocale {lang}
    Set-WinUILanguageOverride -Language {lang}
    Set-WinUserLanguageList {lang} -Force;"""

# Changes colour theme to something a bit more eye straining
def themes():
    return """$p='HKCU:SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Accent'
    $m=(Get-ItemProperty -Path $p).AccentColorMenu
    $m=4278255564
    $s=(Get-ItemProperty -Path $p).StartColorMenu
    $s=4278248887
    $t=@(0xdb,0xfb,0x5a,0xff,0xd6,0xff,0x33,0xff,0xd1,0xfe,0x19,0xff,0xcc,0xff,0x00,0xff,0xb7,0xe5,0x00,0xff,0xa1,0xc8,0x03,0xff,0x83,0xa2,0x05,0xff,0x88,0x17,0x98,0x00)
    Set-ItemProperty -Path $p -Name AccentColorMenu -Value $m
    Set-ItemProperty -Path $p -Name AccentPalette -Value $t;"""

# Generates random RGB values
def randomiseRGB():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Sets window and highlight text/colour to random values (only affects some applications)
def colours():
    window = randomiseRGB()
    windowText = randomiseRGB()
    hilight = randomiseRGB()
    hilightText = randomiseRGB()

    return f"""$p='HKCU:Control Panel\Colors'
    $w='{window[0]} {window[1]} {window[2]}'
    $t='{windowText[0]} {windowText[1]} {windowText[2]}'
    $h='{hilight[0]} {hilight[1]} {hilight[2]}'
    $ht='{hilightText[0]} {hilightText[1]} {hilightText[2]}'
    Set-ItemProperty -Path $p -Name Window -Value $w
    Set-ItemProperty -Path $p -Name WindowText -Value $t
    Set-ItemProperty -Path $p -Name Hilight -Value $h
    Set-ItemProperty -Path $p -Name HilightText -Value $ht;"""

# Slowly makes the cursor larger
def cursor():
    return """$p='HKCU:Control Panel\Cursors'
    $s=(Get-ItemProperty -Path $p).CursorBaseSize
    $s=$s+1
    Set-ItemProperty -Path $p -Name CursorBaseSize -Value $s;"""

# Compiles all Powershell commands and executes at once
def registryPayload():
    STRING = languages() + themes() + colours() + cursor()
    subprocess.Popen(["powershell", "-Command", STRING])

if __name__ == '__main__':
    print(randomiseHex())

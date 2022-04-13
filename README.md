# 'malloc' Trollware

UNSW 22T1 COMP6841 'Something Awesome' project. For my project I started with no particular goal in mind, and ended with a barely-malicious executable that generally attempts to mess with and annoy the user.

Named 'malloc' due to various CS related puns around my name (Mal-achi).

| ![11 tabs, all playing 10 hours of elevator music](https://media.discordapp.net/attachments/825171172982521876/962269144454148106/unknown.png?width=940&height=527) |
|:--:| 
| *What an anxiety attack sounds like.* |

# Overview

‘malloc’ is a trollware designed to mess with the victim in a variety of ways. It’s mostly based on modern internet meme culture and does little to actively harm the user, though it does feature some very basic self perpetuation tactics to ensure the average person cannot get rid of it easily. The average COMP6841 student however would probably be able to easily remove the program and undo any of the changes it had caused.

# Features

There are two main separated categories: Preservation and Payload. Preservation largely attempts to make the executable longer-lived, and survive attempts by the average user to remove or disable it. Payload is the actual affect the executable has on the machine.

## Preservation
- Hides command line whilst executable is running.
- Clones executable to current user's folder in the C disk.
- Creates a shortcut to the cloned executable in shell:startup, letting it automatically run every time the computer is opened.
- Hides executable and shortcut in files.

## Payload
- Every 5 seconds, empties the recycling bin.
- Every 60 seconds, rolls a d20.
  - For 1-15, plays elevator music.
  - For 16-19, plays the vine boom sound.
  - For 20, plays Never Gonna Give You Up. This option could lead to overlapping sounds, as the full song is over two minutes long.
- Crashes Chrome, Opera, or Firefox if open, essentially forcing user to use Microsoft Edge.
  - It's also nice and opens Edge for you.
  - Additionally, internet dial up tone is played whenever a browser is crashed.
- Sets desktop background to Rick Astley.
- Crashes Task Manager, Command Line or Powershell if open, and opens 10 hour elevator music in Microsoft Edge.
  - Technically falls under Preservation, but also has some payload component to it so I put it here.
- Plays Windows XP startup sound when opening computer.
- Randomises computer (keyboard & default) language on each startup.
  - Does not change display language unless its already been installed by the user.
- Various registry key edits:
  - Changes windows colour theme to something kind of... off putting.
  - Randomises window & text colours, as well as highlighting text colours. Doesn't affect all applications.
  - Slowly makes the mouse cursor bigger.

# Reflection
My main rationale for writing a piece of trollware was I wanted to attempt to influence things outside the 'contraints' of the program. Most programs I've written in the past are mostly or wholly self contained, only changing files strictly tied to the script itself. This time though I wanted to attack things that were essentually completely unrelated, such as registry keys and the recycling bin. I figured this would be a bit more challenging as its something I've never done and have frankly been quite scared of attempting. Whilst my final result isn't nothing particularly spectacular, I'm still happy I accomplished this goal.

As someone coming from a background of never having messed with Windows itself through a script, this project resulted in many, many hours of research and reading of documentation to get a grasp on what I needed to do. Python luckily has an extensive list of libraries, many of which make operating system manipulation much easier to digest and accomplish.

I realised that I limited myself a bit by choosing Python, a language I've been using for many years and understand fairly well. I believe this project may have been far more challenging if I attempted it in say, Javascript or even C. Next time I would definitely stretch myself more by choosing an unfamiliar or new language I've never used before.

## Security Insights
Writing the trollware has made me realise how many things are available for a script to attack. I had never needed to use elevated permissions or ask for administrator rights whilst writing my program, and I was still able to create some degree of self perpetuity. Granted, Windows Defender did attempt to block running the file, but I take this as more of a success since it's apparently 'malicious' enough to cause an antivirus to pick up on it.

Possibly the most concerning thing I've noted is just how much can be done through Powershell. Where there wasn't a defined library for a certain feature I wanted to attempt, I simply had to run Powershell as a subprocess to execute commands to the same effect. This included modifying registry keys - whilst the most important keys (namely `HKEY_LOCAL_MACHINE`) are locked behind administrative authorization (thankfully), the fact that I was able to change any at all paves the way for legitimate malicious attacks that delete them altogether from the system.

## Final Thoughts
This project was a bit of a pain to do as much of what I attempted to accomplish had to come with a lot of internet deep diving. The bulk of the time I spent on this project was probably in researching exactly what actions and features were possible, as I wanted to strictly stick to things that did not require administrative permissions. There was also plenty of self testing, particularly with the editing of registry keys. Surprisingly there wasn't a lot of detailed documentation on what each of the keys represented in the system, so I needed to manually change them myself to see how they impacted my machine. 

Overall this project was a lot of fun though, and whilst I do wish I had the time to add more complex features I'm still quite happy with how this came out. The final trollware feels a bit more like a dump of random gimmicks found scattered across Stackoverflow I frankensteined together into this mess of an executable, but in a way I think that gave me more option for what to do instead of sticking to one specific theme. 

# Appendix
Thanks to the members of UNSW Boardgames and RPG Society for all of these cursed feature ideas.

Libraries used:
- [schedule](https://schedule.readthedocs.io/en/stable/)
- time
- [winshell](https://winshell.readthedocs.io/en/latest/)
- [os](https://docs.python.org/3/library/os.html) 
- [sys](https://docs.python.org/3/library/sys.html)
- win32com.client, win32gui, win32con
- [ctypes](https://docs.python.org/3/library/ctypes.html)
- [requests](https://docs.python-requests.org/en/latest/)
- [threading](https://docs.python.org/3/library/threading.html)
- [psutil](https://psutil.readthedocs.io/en/latest/)
- [shutil](https://docs.python.org/3/library/shutil.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)
- random
- [playsound](https://pypi.org/project/playsound/)

### Sources
- [python save image from url](https://stackoverflow.com/questions/30229231/python-save-image-from-url) (used in `changeBackground()`)
- [How to change language/region and speech in Windows 10 with Powershell script](https://stackoverflow.com/questions/51183960/how-to-change-language-region-and-speech-in-windows-10-with-powershell-script) (used in `languages()`)
- [How to open external programs in Python](https://stackoverflow.com/questions/37238645/how-to-open-external-programs-in-python) (used in `payload.py` and `powershellpayload.py`)
- [Check if a process is running or not on Windows?](https://stackoverflow.com/questions/7787120/check-if-a-process-is-running-or-not-on-windows) (used in `edgeForcer()` and `killTask()`)
- [changing desktop background in windows 10 via python](https://stackoverflow.com/questions/40941167/changing-desktop-background-in-windows-10-via-python) (used in `changeBackground()`)
- [How can I make a file hidden on Windows?](https://stackoverflow.com/questions/43441883/how-can-i-make-a-file-hidden-on-windows) (used in `cloneExe()` and `addStartup()`)
- [Registry keys to change personalization settings?](https://superuser.com/questions/1245923/registry-keys-to-change-personalization-settings) (referenced for `powershellpayload.py`)

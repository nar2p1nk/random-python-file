from moviepy.editor import * 
# import moviepy.editor as me
import argparse

# url = me.VideoFileClip("https://www.pornhub.com/embed/ph5f75bae6a2254")

# me.write_videofile(url,'hub.mp4')



def convertMp4(mp4,mp3):
    Vid = VideoFileClip(mp4)

    audio = Vid.audio
    audio.write_audiofile(mp3)

    audio.close()
    Vid.close()

parser = argparse.ArgumentParser()
parser.add_argument('-v','--video',help='name of mp4 file to convert',)
parser.add_argument('-a','--audio',help='name of mp3 file to save')
args = parser.parse_args()

convertMp4(args.video,args.audio)
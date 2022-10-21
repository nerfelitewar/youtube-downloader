'''
Requirements- python 3.8 or above
pip install pyautogui
pip install pytube
pip install colorama
'''
from time import sleep
import pyautogui as pg
from pytube import YouTube
from colorama import Fore

ask='YES'
while ask=='YES':
    ytUrl=pg.prompt('Enter Youtube video URL which you want to download',title='YT URL')
    ytDownLoc=pg.prompt('Where do you want to download this video:',title='FILE LOCATION',default=(r".\Yt_downloaded_videos")) ##FILE LOCATION
    setRes=pg.confirm('Set resolution of the video pixels',title='VIDEO RESOLUTION',buttons=['Lowest','360px','720px','Max','Get Audio'])

##main code- 
    yt = YouTube(str(ytUrl))
    print(Fore.RED+"Title: ", Fore.YELLOW+yt.title)
    sleep(2)
    print(Fore.GREEN+"Views: ",Fore.RED+str(yt.views)+Fore.RESET)

    if setRes=='Max':
         yd = yt.streams.get_highest_resolution()
    if setRes=='Lowest':
         yd = yt.streams.get_lowest_resolution()
    if setRes=='360px':
         yd = yt.streams.filter(res="360p")
    if setRes=='720px':
         yd = yt.streams.filter(res="720p")
    if setRes=='Get Audio':
         yd = yt.streams.get_audio_only()

    yd.download(str(ytDownLoc))

    tell=pg.alert('DOWNLOAD DONE',title='DOWNLOAD COMPLETE')
    print('DONE')
    ask=pg.confirm('Want to do again?',title='TRY AGAIN',buttons=["YES","NO"])



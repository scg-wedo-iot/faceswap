import subprocess as sp
from os.path import join as pjoin

'''
frame to video
ffmpeg -r 60 -f image2 -s 1920x1080 -i pic%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p test.mp4

Adding a mp3 to a video
Adding sound to a video is straightforward
ffmpeg -r 60 -f image2 -s 1280x720 -i pic%05d.png -i MP3FILE.mp3 -vcodec libx264 -b 4M -vpre normal -acodec copy OUTPUT.mp4
'''

list_models = ['25k', '50k', '100k', '150k', '200k', '250k',
               '300k', '350k', '375k', '400k', '450k', '500k', '525k']

for MODEL_ITE in list_models:
    FOLDER_IMAGE_SWAPPED = f'models_{MODEL_ITE}_market'
    FILENAME_OUT = f'god_market_swapped_{MODEL_ITE}.mkv'
    sp.run([f'python tools.py effmpeg -a gen-vid -r data/pong-god/video/wedo_god_market_sit_1.mp4 -m -i data/pong-god/face_swapped_b/450k_video -o {FILENAME_OUT}'], shell=True)

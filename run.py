import subprocess as sp
from os.path import join as pjoin

data_name = 'pong-god'
# input_format = 'frame' # frame or video
input_format = 'video' # frame or video
VIDEO_NAME = 'market'
# FILENAME_VIDEO = 'wedo_god_market_sit_1.mp4'
FILENAME_VIDEO = 'god_market_stand_cut.mov'

MODEL_ITE = '450k'
# mode = 'extract'
list_mode = ['convert-swap']
# list_mode = ['extract', 'convert-swap', 'convert']
# list_mode = ['convert-swap', 'convert']

list_models = ['25k', '50k', '100k', '150k', '200k', '250k',
               '300k', '350k', '375k', '400k', '450k', '500k', '525k']

FOLDER_DATA = pjoin('data', data_name)

if input_format == 'frame':
    input_img = pjoin(FOLDER_DATA, 'original')
    output_img_align = pjoin(FOLDER_DATA, 'alignmented')

elif input_format == 'video':
    input_img = pjoin(FOLDER_DATA, f'video_{VIDEO_NAME}', FILENAME_VIDEO)
    output_img_align = pjoin(FOLDER_DATA, f'alignmented_{VIDEO_NAME}')


alignment_dir = pjoin(FOLDER_DATA, 'alignments.fsa')

for mode in list_mode:

    for MODEL_ITE in list_models:
        model_dir = pjoin(FOLDER_DATA, f'models_{MODEL_ITE}')

        output_img_swapped = pjoin(FOLDER_DATA, 'face_swapped', f'{MODEL_ITE}_{input_format}_{VIDEO_NAME}')
        output_img_swapped_b = pjoin(FOLDER_DATA, 'face_swapped_b', f'{MODEL_ITE}_{input_format}_{VIDEO_NAME}')

        list_run = []
        list_pyfile = ['python', 'faceswap.py']
        list_run.extend(list_pyfile)
        if mode == 'extract':
            list_mode = ['extract', '-i', input_img, '-o', output_img_align]

        elif mode == 'convert':
            list_mode = ['convert', '-m', model_dir, '-i', input_img, '-o', output_img_swapped]

        elif mode == 'convert-swap':
            list_mode = ['convert', '-m', model_dir, '-i', input_img, '-o', output_img_swapped_b, '-s']

        else:
            raise ValueError(f'mode: {mode} not support')

        list_run.extend(list_mode)
        sp.run(list_run)
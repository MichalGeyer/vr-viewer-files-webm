# iterate over folders in ./pairs-user-study-webm and remove traced dots from the folder names

import os
for folder in os.listdir('./pairs-user-study-webm'):
    if folder.endswith('.'):
        new_folder = folder[:-1]
        os.rename('./pairs-user-study-webm/' + folder, './pairs-user-study-webm/' + new_folder)
        print('Renamed ' + folder + ' to ' + new_folder)

# itereate over pngs in './pairs-user-study-webm/images' and replace ..png with .png
# for file in os.listdir('./pairs-user-study-webm/images'):
#     if file.endswith('..png'):
#         new_file = file.replace('..png', '.png')
#         os.rename('./pairs-user-study-webm/images/' + file, './pairs-user-study-webm/images/' + new_file)
#         print('Renamed ' + file + ' to ' + new_file)
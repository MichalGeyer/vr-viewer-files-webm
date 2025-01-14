# iterate over folders in ./pairs-user-study-webm and remove traced dots from the folder names

import os


def remove_traced_dots(root):
    for folder in os.listdir(root):
        if folder.endswith('.'):
            new_folder = folder[:-1]
            os.rename(f'{root}/' + folder, f'{root}/' + new_folder)
            print('Renamed ' + folder + ' to ' + new_folder)

root = './pairs-user-study-webm/left'
remove_traced_dots(root)
root = './pairs-user-study-webm/right'
remove_traced_dots(root)

# for folder in os.listdir('./pairs-user-study-webm'):
#     if folder.endswith('.'):
#         new_folder = folder[:-1]
#         os.rename('./pairs-user-study-webm/' + folder, './pairs-user-study-webm/' + new_folder)
#         print('Renamed ' + folder + ' to ' + new_folder)

# for folder in os.listdir('./pairs-user-study-images'):
#     if folder.endswith('.'):
#         new_folder = folder[:-1]
#         os.rename('./pairs-user-study-images/' + folder, './pairs-user-study-images/' + new_folder)
#         print('Renamed ' + folder + ' to ' + new_folder)


# # itereate over pngs in './pairs-user-study-webm/images' and replace ..png with .png
# for file in os.listdir('./pairs-user-study-webm/images'):
#     if file.endswith('..png'):
#         new_file = file.replace('..png', '.png')
#         os.rename('./pairs-user-study-webm/images/' + file, './pairs-user-study-webm/images/' + new_file)
#         print('Renamed ' + file + ' to ' + new_file)
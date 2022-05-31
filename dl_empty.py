import os 
import shutil 

downloads = os.listdir('D:\Downloads')
to_move = r'D:\Downloads\pexels-photo-2885320.jpeg'
wallpapers = r'D:\Nathan\Pictures\Wallpapers'

# for dl in downloads:
#     print(dl)

shutil.move(to_move, wallpapers)
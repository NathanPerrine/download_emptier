import os 
import shutil 

downloads = os.listdir('D:\Downloads')
# to_move = r'D:\Downloads\pexels-photo-2885320.jpeg'
to_move = 'D:/Downloads/"blank - Copy (5).txt"'
wallpapers = r'D:\Nathan\Documents'

# for dl in downloads:
#     print(dl)

shutil.move(to_move, wallpapers)
import os
import re

project_directory = '/Users/fieldsbw/source/repos/python-projects/file-name-updater/'
picture_directory = project_directory+'northwest-profile-pics/'

for file in os.listdir(picture_directory):
    fileName, fileExt = os.path.splitext(file)
    fileName = fileName.replace("_w", "")
    newFileName = fileName+fileExt
    os.rename(picture_directory+file, newFileName)
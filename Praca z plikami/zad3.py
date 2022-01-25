# Lukasz Piasecki
# Programowanie w języku Python
# 16.11.2021

import os

os.chdir(".\\kwiatki")
directory = '.'

for filename in os.listdir(directory):
    prefix = filename.split(".jpg")[0]
    os.rename(filename, prefix+".png")
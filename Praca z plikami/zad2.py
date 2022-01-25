# Lukasz Piasecki
# Programowanie w języku Python
# 16.11.2021


import os


for path, subfiles, files in os.walk('.'):
    if len(files):
        for i in files:
            print(files)

# Lukasz Piasecki
# Programowanie w języku Python
# 27.11.2021

import re

with open('file.txt', 'r') as file, open('file2.txt', 'w') as writer:
    for line in file:
        tekst = line
        print(tekst)
        tekst = re.sub('nigdy', '', tekst)
        tekst = re.sub('dlaczego', '', tekst)
        tekst = re.sub('i ', '', tekst)
        tekst = re.sub('oraz', '', tekst)
        tekst = re.sub('się', '', tekst)
        writer.write(tekst)











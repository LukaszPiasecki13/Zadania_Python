# Lukasz Piasecki
# Programowanie w języku Python
# 27.11.2021

import re

with open('file.txt', 'r') as file, open('file2.txt', 'w') as writer:
    for line in file:
        tekst = line
        print(tekst)
        tekst = re.sub('dlaczego', 'czemu', tekst)
        tekst = re.sub('i ', 'oraz ', tekst)
        tekst = re.sub('oraz', 'i', tekst)
        tekst = re.sub('nigdy', 'prawie nigdy', tekst)
        writer.write(tekst)











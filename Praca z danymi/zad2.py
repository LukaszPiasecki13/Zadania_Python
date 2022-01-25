
import csv


data =[]
with open('file.csv', 'r+', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvwriter = csv.writer(csvfile)

    for row in csvreader:
        data.append(row)
        print(row)


print("Co chcesz zrobić?")
print("Usuń -1 ")
print("Dodaj - 2")

wybor = input("Wybierz opcję:")

if wybor == '2':
    print("Podaj dane nowej osoby")
    name = input("Name:")
    surname = input("Surname:")
    age = input("Age:")
    Nr = len(data)
    row = [Nr,name,surname,age]
    with open('file.csv', 'r+', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(len(data)):
            csvwriter.writerow(data[i])
        csvwriter.writerow(row)
elif wybor == '1':
    nr_usun =input("Podaj numer osoby którą chcesz usunąć")
    for i in range(len(data)):
        try:
            if data[i][0] == nr_usun:
                del data[i]
        except IndexError : {}

    with open('file.csv', 'r+', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(len(data)):
            csvwriter.writerow(data[i])
print(data)
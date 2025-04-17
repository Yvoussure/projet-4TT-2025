import csv


def fn_write_filee():
    with open('videogame_file.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["videogames", "date de sortie"])
        writer.writerows([["Cyberpunk 2077", 2021], ["Subnautica 2", 2025]])


def fn_read_file():
    with open('videogame_file.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)

def fn_script():
    fn_write_filee()
    fn_read_file()


fn_script()
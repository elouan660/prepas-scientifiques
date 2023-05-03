import csv

#Lycée: index 3

file_csv = open("prepa-scientifiques.csv","r",encoding="utf-8")
prepa_csv = csv.reader(file_csv,delimiter=";")
prepa_list = []

for ligne in prepa_csv:
    prepa_list.append(ligne)

def search_lycée(search):
    count=0
    for lycée in prepa_list:
        if search in prepa_list[count][3]:
            prepa = prepa_list[count][3]
            print(f"{prepa} Trouvé à l'index {count}")
        count += 1

html = f"""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" lang="fr">
        <title>Example</title>
    </head>
    <body>
        <h1>Voici des données concernant le {prepa}</h1>
        
    </body>
</html>

"""
file_html.write(html)
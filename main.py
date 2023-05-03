import csv
import tkinter as tk

fichier = open("prepa-scientifiques.csv","r",encoding="utf-8")
prepa_csv=csv.reader(fichier,delimiter=";")
prepa_
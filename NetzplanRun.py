# Alle Netzpläne in einem Verzeichnis erstellen
import os
from Netzplan import ErstelleNetzplan

curPfad = os.path.dirname(__file__)

txtFiles = [f for f in os.listdir(curPfad) if f.endswith(".txt")]

for txtFile in txtFiles:
    ErstelleNetzplan(os.path.join(curPfad, txtFile))
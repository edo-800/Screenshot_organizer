import os
import shutil

# 1. Trova in automatico il percorso del Desktop del utente Mac
percorso_desktop = os.path.expanduser("~/Desktop")

# 2. Definiamo la cartella dove si trovano gli screenshot e dove spostarli
cartella_origine = percorso_desktop
cartella_destinazione = os.path.join(percorso_desktop, "Screenshot_organizer")

# 3. Creiamo la cartella "screenshot" sul Desktop se non esiste già
os.makedirs(cartella_destinazione, exist_ok=True)

# 4. Leggiamo tutti i file presenti sul Desktop
tutti_i_file = os.listdir(cartella_origine)

print("Scansione del Desktop in corso...")
contatore_spostati = 0

# 5. Controlliamo i file uno ad uno
for singolo_file in tutti_i_file:
    
    # Se il file che stiamo esaminando è la nostra cartella, oppure contiene il nome della cartella di destinazione, SALTALO!
    if singolo_file == "Screenshot_organizer" or singolo_file == "screenshot":
        continue
        
    # Se supera il controllo sopra, applichiamo la logica
    if "Screenshot" in singolo_file or "Screen Recording" in singolo_file:
        
        posizione_vecchia = os.path.join(cartella_origine, singolo_file)
        posizione_nuova = os.path.join(cartella_destinazione, singolo_file)
        
        # Spostiamo il file dal Desktop alla cartella "Screenshot_organizer"
        shutil.move(posizione_vecchia, posizione_nuova)
        
        print("Spostato sul Desktop -> Screenshot_organizer: " + singolo_file)
        contatore_spostati = contatore_spostati + 1

print("Pulizia completata! Spostati in totale " + str(contatore_spostati) + " file.")
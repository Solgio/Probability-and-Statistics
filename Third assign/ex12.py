import random
import matplotlib.pyplot as plt

def simulate_game():
    # Inizializzazione la scacchiera
    pedine = [0] * 12
    mosse = 0

    while True:
        # Lancia dadi
        dadi = random.randint(1, 6) + random.randint(1, 6)
        
        # Mossa della pedina scelta
        if 2 <= dadi <= 12:
            colonna = dadi
            if pedine[colonna - 1] < 19:  # Se la pedina non è arrivata alla fine, la muovo
                pedine[colonna - 1] += 1
        
        mosse += 1
        
        # Se almeno una pedina ha raggiunto la fine, termina il gioco
        if any(pedina == 19 for pedina in pedine):
            break

    return pedine.index(19), mosse  # Ritorna la pedina vincente

# Simulazione di più giochi
simulazioni = 200000
risultati = [simulate_game() for _ in range(simulazioni)]

#--------------------------------------------------------PUNTO A--------------------------------------------------------------------------#

# Calcolo probabilità che la pedina 7 arrivi prima della 8
arrivo_colonna_7 = sum(1 for risultato in risultati if risultato[0] == 6) / simulazioni
arrivo_colonna_8 = sum(1 for risultato in risultati if risultato[0] == 7) / simulazioni

print(f"Probabilità che la pedina della colonna 7 arrivi prima di quella della colonna 8: {arrivo_colonna_7}")
print(f"Probabilità che la pedina della colonna 8 arrivi prima di quella della colonna 7: {arrivo_colonna_8}")

#--------------------------------------------------------PUNTO B--------------------------------------------------------------------------#

# Calcolare la probabilità che la pedina k arrivi per prima
probabilità_colonne = [sum(1 for risultato in risultati if risultato[0] == k) / simulazioni for k in range(12)]
print("Probabilità che la pedina della colonna k arrivi per prima:", probabilità_colonne)

#--------------------------------------------------------PUNTO C--------------------------------------------------------------------------#

# Calcolare la probabilità che il gioco duri esattamente N mosse (con N tra 1 e 200)
durata_esatta = [0] * 200  # Lista del numero di volte in cui un gioco e' durato esattamente N mosse
giochi_piu_di_200_mosse = 0  # Contatore dei giochi con durata maggiore di 200 mosse

# Conta le durate
for _, mosse in risultati:
    if 1 <= mosse <= 200:
        durata_esatta[mosse - 1] += 1
    elif mosse > 200:
        giochi_piu_di_200_mosse += 1

# Probabilita' di durata esatta per ogni N
probabilità_durata_esatta = [count / simulazioni for count in durata_esatta]

for N in range(1, 201):
    print(f"Probabilità che il gioco duri esattamente {N} mosse: {probabilità_durata_esatta[N - 1]}")

#--------------------------------------------------------PUNTO D--------------------------------------------------------------------------#

# Calcolare probabilita' dei giochi durati piu' di 100 mosse
giochi_piu_di_100_mosse = sum(1 for _, mosse in risultati if mosse > 100)
probabilità_piu_di_100_mosse = (giochi_piu_di_100_mosse + giochi_piu_di_200_mosse) / simulazioni
print(f"Probabilità che il gioco duri più di 100 mosse: {probabilità_piu_di_100_mosse}")

#--------------------------------------------------------PUNTO E--------------------------------------------------------------------------#

# Calcolare probabilita' dei giochi durati piu' di 200 mosse
probabilità_piu_di_200_mosse = giochi_piu_di_200_mosse / simulazioni
print(f"Probabilità che il gioco duri più di 200 mosse: {probabilità_piu_di_200_mosse}")


# ------------------------------------------------- PLOT PUNTO A ---------------------------------------------------------
# Grafico della probabilita' di vittoria per la pedina in colonna k
plt.figure(figsize=(10, 6))
plt.plot(range(1, 13), probabilità_colonne, marker='o', linestyle='-', color='b')
plt.title('Probabilità di vittoria della pedina in colonna k')
plt.xlabel('Colonna k')
plt.ylabel('Probabilità di vittoria')
plt.xticks(range(1, 13))
plt.grid(True)
plt.show()

# ------------------------------------------------- PLOT PUNTO C ---------------------------------------------------------
# Grafico della probabilita' di durata esatta in funzione di N
plt.figure(figsize=(10, 6))
plt.plot(range(1, 201), probabilità_durata_esatta, marker='x', linestyle='-', color='r')
plt.title('Probabilità che il gioco duri esattamente N mosse')
plt.xlabel('Numero di mosse N')
plt.ylabel('Probabilità di durata esatta')
plt.xticks(range(1, 201, 10))
plt.grid(True)
plt.show()
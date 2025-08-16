"""-----------------------------------------------METODO SEGUITO ALLA LETTERA (CAUSA OVERFLOW)------------------------------------------------"""
"""
import math
import random

def binomial_pmf(N, k):
    if 0 <= k <= N:
        return math.comb(N, k) * (0.5 ** k) * (0.5 ** (N - k))
    return 0

def probability_A_wins(N, M):
    k_min = math.floor((N - M) / 2) + 1
    return sum(binomial_pmf(N, k) for k in range(k_min, N + 1))

N_plus_M = 10**6  # Numero minimo di elettori
M = random.randint(0, 5000)  # Genera M casualmente tra 0 e 5000
N = N_plus_M - M

print(f"Numero di elettori già decisi (M): {M}")
print(f"Probabilità che vinca A: {probability_A_wins(N, M):.6f}")
"""
"""-----------------------------------------------CON UTILIZZO DI APPROSIMAZIONE DELLA DISTRIBUZIONE (APPROSIMAZIONE NORMALE)------------------------------------------------"""
"""
def probability_A_wins(N, M):
    # Approssimazione normale della distribuzione binomiale
    mu = N / 2  # Media della distribuzione binomiale
    sigma = math.sqrt(N / 4)  # Deviazione standard della distribuzione binomiale
    k_min = math.floor((N - M) / 2) + 1
    
    # Calcoliamo la probabilità cumulativa dalla distribuzione normale
    return 1 - norm.cdf(k_min, loc=mu, scale=sigma)

N_plus_M = 10**6  # Numero minimo di elettori
M = random.randint(0, 5000)  # Genera M casualmente tra 0 e 5000
N = N_plus_M - M

print(f"Numero di elettori già decisi (M): {M}")
print(f"Probabilità che vinca A: {probability_A_wins(N, M):.6f}")
"""
"""-----------------------------------------------CON UTILIZZO DEI LOGARITMI PER IL CALCOLO DELLA DISTRIBUZIONE------------------------------------------------"""
#Ottiene la cartella in cui salvare il file pdf alla fine dell'esecuzione
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "probabilita_vittoria.pdf")


import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
# Funzione per calcolare la densità della distribuzione binomiale evitando overflow
def binomial_pmf(N, k):
    if 0 <= k <= N:
        # Logaritmo del coefficiente binomiale
        log_binom = math.lgamma(N + 1) - (math.lgamma(k + 1) + math.lgamma(N - k + 1))
        # Calcolo della probabilità in logaritmi e poi esponenziazione per ottenere il valore reale
        return math.exp(log_binom + k * math.log(0.5) + (N - k) * math.log(0.5))
    else:
        return 0

# Funzione per calcolare la probabilità che vinca A
def probability_A_wins(N, M):
    k_min = math.floor((N - M) / 2) + 1
    #probability = sum(binomial_pmf(N, k) for k in range(k_min, N + 1))
    #return probability

    return binom.sf(k_min-1, N, 0.5)

# Definizione dei parametri
N_plus_M = 10**6  # Numero minimo di elettori
#M = random.randint(0, 5000)  # Genera M casualmente tra 0 e 5000
M_values=np.arange(0,5001,10)
#N = N_plus_M - M  # Calcola N come differenza

# Calcolo della probabilità che vinca A
prob = [probability_A_wins(N_plus_M-M, M) for M in M_values]

# Output dei risultati
# print(f"Numero di elettori già decisi (M): {M}")
# print(f"Numero di elettori indecisi (N): {N}")
# print(f"Probabilità che vinca A: {prob:.6f}")

plt.figure(figsize=(8,5))
plt.plot(M_values, prob, label='Probabilità di vittoria')
plt.xlabel("M")
plt.ylabel("Probabilità")
plt.title("Probabilità di vittoria elettorale in funzione di M")
plt.grid(True)
plt.legend()

plt.savefig(output_path, format="pdf")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Caricamento dei dati
data = pd.read_excel("/home/solgio/Desktop/Uni/Probability-and-Statistics/First assign/Meteo_Chioggia60.ods", sheet_name="Dati")

# Seleziona le colonne Tmin, Tmed, Tmax, Ptot
# Supponiamo che le colonne siano nelle posizioni 1, 2, 3, 4 (indici 0-based)
X = data.iloc[:, 1:5].values  # Usa .iloc per selezionare le colonne per indice

# Converti i dati in numeri, sostituendo i valori non numerici con NaN
X = pd.DataFrame(X).apply(pd.to_numeric, errors='coerce').values

# Rimuovi le righe che contengono NaN (valori mancanti o non numerici)
X = X[~np.isnan(X).any(axis=1)]

# Centra i dati (sottrai la media da ogni colonna)
X_centered = X - np.mean(X, axis=0)

# Calcola la matrice di covarianza
cov_matrix = np.cov(X_centered, rowvar=False)

# Autodecomposizione della matrice di covarianza
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Ordina autovalori e autovettori in ordine decrescente
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

lambda_matrix = np.diag(eigenvalues)

# Stampa autovalori e autovettori
print("Autovalori:", eigenvalues)
print("Autovettori:")
print(eigenvectors)
print("Matrice Covarianza:")
print(cov_matrix)

# Seleziona le prime due componenti principali
Q = eigenvectors[:, :2]  # Prime due colonne (direzioni principali)
Y = X_centered @ Q  # Trasformazione lineare dei dati

# Diagramma di dispersione delle prime due componenti principali
plt.scatter(Y[:, 0], Y[:, 1], color='blue', alpha=0.5)
plt.xlabel('Prima Componente Principale C1')
plt.ylabel('Seconda Componente Principale C2')
plt.title('Diagramma di Dispersione delle Prime Due Componenti Principali')
plt.grid(True)
plt.savefig('matrice_covarianza.pdf', format='pdf' , bbox_inches='tight')
plt.show()

with open('risultati_matrici.txt', 'w') as f:
    f.write("=== RISULTATI ANALISI ===\n\n")
    
    # Matrice diagonale di autovalori
    f.write("MATRICE DIAGONALE DI AUTOVALORI (Λ):\n")
    np.savetxt(f, lambda_matrix, fmt='%10.4f', delimiter='\t')
    f.write("\nAutovalori:\n")
    np.savetxt(f, eigenvalues.reshape(1, -1), fmt='%10.4f', delimiter='\t')
    
    # Matrice di autovettori
    f.write("\n\nMATRICE ORTONORMALE DI AUTOVETTORI (Q):\n")
    np.savetxt(f, eigenvectors, fmt='%10.4f', delimiter='\t')
   
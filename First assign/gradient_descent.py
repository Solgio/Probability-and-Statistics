import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Funzione per il calcolo del gradiente
def compute_gradient(x, y, a, b):
    n = len(x)
    error = y - (a * x + b)
    grad_a = -2 * np.sum(x * error) / n
    grad_b = -2 * np.sum(error) / n
    return grad_a, grad_b

# Funzione per il Gradient Descent
def gradient_descent(x, y, alpha=0.001, iterations=1000):
    # Inizializzazione dei parametri
    a, b = 0, 0
    
    # Ciclo di ottimizzazione
    for _ in range(iterations):
        grad_a, grad_b = compute_gradient(x, y, a, b)
        a -= alpha * grad_a
        b -= alpha * grad_b
    
    return a, b

# Funzione per scalare i dati (normalizzazione)
def scale_data(data):
    mean = np.mean(data)
    std = np.std(data)
    scaled_data = (data - mean) / std
    return scaled_data, mean, std

# Funzione per riportare i coefficienti alla scala originale
def rescale_coefficients(a, b, x_mean, x_std, y_mean, y_std):
    a_rescaled = a * (y_std / x_std)
    b_rescaled = b * y_std + y_mean - a_rescaled * x_mean
    return a_rescaled, b_rescaled

# Caricamento dei dati
try:
    # Carica il file Excel
    data = pd.read_excel("Meteo_Chioggia.ods", sheet_name="Dati")
    
    # Verifica i nomi delle colonne
    print("Nomi delle colonne:", data.columns)  # Stampa i nomi delle colonne per debug

    # Definisci i nomi delle colonne
    Tmin = data.columns[1]  # Seconda colonna (indice 1)
    Tmed = data.columns[2]  # Terza colonna (indice 2)
    Ptot = data.columns[4]  # Quinta colonna (indice 4)

    # Converti le colonne in numeri e rimuovi i valori non validi
    x1 = pd.to_numeric(data[Tmin], errors='coerce').values
    y1 = pd.to_numeric(data[Tmed], errors='coerce').values
    x2 = pd.to_numeric(data[Tmin], errors='coerce').values
    y2 = pd.to_numeric(data[Ptot], errors='coerce').values

    # Rimuovi i valori NaN
    mask1 = ~np.isnan(x1) & ~np.isnan(y1)
    x1, y1 = x1[mask1], y1[mask1]

    mask2 = ~np.isnan(x2) & ~np.isnan(y2)
    x2, y2 = x2[mask2], y2[mask2]

    # Scalatura dei dati
    x1_scaled, x1_mean, x1_std = scale_data(x1)
    y1_scaled, y1_mean, y1_std = scale_data(y1)

    x2_scaled, x2_mean, x2_std = scale_data(x2)
    y2_scaled, y2_mean, y2_std = scale_data(y2)

    # Esegui il Gradient Descent
    a1, b1 = gradient_descent(x1_scaled, y1_scaled, alpha=0.001, iterations=1000)
    a2, b2 = gradient_descent(x2_scaled, y2_scaled, alpha=0.001, iterations=1000)

    # Riporta i coefficienti alla scala originale
    a1_rescaled, b1_rescaled = rescale_coefficients(a1, b1, x1_mean, x1_std, y1_mean, y1_std)
    a2_rescaled, b2_rescaled = rescale_coefficients(a2, b2, x2_mean, x2_std, y2_mean, y2_std)

    # Plot dei diagrammi di dispersione con le rette di regressione
    plt.figure(figsize=(12, 6))

    # Plot per (Tmin, Tmed)
    plt.subplot(1, 2, 1)
    plt.scatter(x1, y1, color='blue', label='Dati')
    plt.plot(x1, a1_rescaled * x1 + b1_rescaled, color='red', label=f'Retta: y = {a1_rescaled:.2f}x + {b1_rescaled:.2f}')
    plt.xlabel('Tmin')
    plt.ylabel('Tmed')
    plt.legend()

    # Aggiungi il testo con i valori di a e b
    plt.text(0.05, 0.95, f'a = {a1_rescaled:.4f}\nb = {b1_rescaled:.4f}', 
             transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

    plt.title('Regressione (Tmin, Tmed)')

    # Plot per (Tmin, Ptot)
    plt.subplot(1, 2, 2)
    plt.scatter(x2, y2, color='green', label='Dati')
    plt.plot(x2, a2_rescaled * x2 + b2_rescaled, color='orange', label=f'Retta: y = {a2_rescaled:.2f}x + {b2_rescaled:.2f}')
    plt.xlabel('Tmin')
    plt.ylabel('Ptot')
    plt.legend()

    # Aggiungi il testo con i valori di a e b
    plt.text(0.05, 0.95, f'a = {a2_rescaled:.4f}\nb = {b2_rescaled:.4f}', 
             transform=plt.gca().transAxes, fontsize=10, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

    plt.title('Regressione (Tmin, Ptot)')

    plt.tight_layout()
    plt.savefig('gradient_descent_regression_plots.pdf')
    plt.show()

    # Stampa dei coefficienti
    print(f"Punto di minimo per (Tmin, Tmed): a* = {a1_rescaled:.4f}, b* = {b1_rescaled:.4f}")
    print(f"Punto di minimo per (Tmin, Ptot): a* = {a2_rescaled:.4f}, b* = {b2_rescaled:.4f}")

except Exception as e:
    print("Errore durante l'esecuzione del programma:", e)
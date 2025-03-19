# Probability-and-Statistics
Personal repository for exercises of Probability and Statistics.

## FIRST ASSIGN

### Original assign text
Sia $(xi, yi)i∈{1,...,n}$ un campione bi-variato di numerosità $n$.\
Poniamo 
$$
\begin{aligned} 
\phi(a, b) = \sum_{i=1}^n (y_i - (a \cdot x_i + b))^2
\end{aligned}
$$
Si scriva un programma che, dato $(xi, yi)i∈{1,...,n}$, calcoli un punto di minimo
di $ϕ$, cioè un punto $(a∗, b∗) ∈ R2$ tale che
$ϕ(a∗, b∗) = min{ϕ(a, b) : a, b ∈ R}.$\
Si considerino poi i due campioni bi-variati (Tmin, Tmed) e (Tmin, Ptot) del file Meteo_Chioggia60.ods e si crei, per ciascuno dei due campioni bi-variati, il corrispondente diagramma di dispersione col grafico della retta $t → a∗t + b∗$
determinata dal punto di minimo (a∗, b∗) calcolato col programma.\
Si determini inoltre l'autodecomposizione della matrice di covarianza del campione quattro-variato (Tmin, Tmed, Tmax, Ptot) e si identifichino le due direzioni più importanti (autovalori maggiori). Si crei il corrispondente diagramma di dispersione delle prime due componenti del campione quattro-variato nel nuovo sistema di coordinate (trasformazione lineare dei dati secondo la trasposta della matrice di autovettori ortogonali). \
Per la consegna servono:
- una giustificazione matematica della procedura utilizzata per il calcolo di un punto di minimo di $ϕ$;
- lo pseudo-codice del programma e il codice commentato in un linguaggio
standard come C++ o Python;
- i grafici dei due diagrammi di dispersione con le rette di regressione in formato pdf e i valori numerici dei punti di minimo utilizzati;
- il grafico del diagramma di dispersione delle due componenti più importanti dei dati trasformati con la matrice trasposta di autovettori.

### Problem resolution 
I applied the Gradient Descend method to elaborate the set of data and find the minimum values for $a$ and $b$. In particular this method uses the gradient of the function as subtracting value for the researce of the minimum. \
It can be exemplified as the path to choose while descending a mountain. The choice is to follow the direction of the steepest slope, the gradient in our case.
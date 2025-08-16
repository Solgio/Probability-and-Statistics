# Probability-and-Statistics

Personal repository for exercises of Probability and Statistics, useful for bonus exam points.

 ## 👥 Authors
- Lorenzo Soligo
- Tommaso Ceron
- Denis Parolin

## 1️⃣ First Assignment

This assignment focuses on linear regression and Principal Component Analysis (PCA) using a dataset of weather data from Chioggia.

### Problem Description ❗
Given a bivariate sample, find the minimum point of the sum of squared errors to determine the regression line. This is applied to two samples from the `Meteo_Chioggia60.ods` file: (Tmin, Tmed) and (Tmin, Ptot). The assignment also requires performing an eigendecomposition of the covariance matrix for the four-variate sample (Tmin, Tmed, Tmax, Ptot) to identify the two most important principal components.

### Implementation 💡 
The gradient descent method is used to find the minimum values for the regression line parameters, `a` and `b`. The covariance matrix is calculated and its eigenvalues and eigenvectors are found to determine the principal components.

### Scripts 💻
- `First assign/gradient_descent.py`: Implements the gradient descent algorithm for linear regression and generates plots.
- `First assign/matrice_covarianza.py`: Calculates the covariance matrix, performs PCA, and plots the principal components.

---

## 2️⃣ Second Assignment

This assignment explores the calculation of probabilities in an electoral scenario.

### Problem Description ❗
The goal is to determine the probability of a candidate 'A' winning an election. The total number of voters is 1,000,000. Some number of voters, M (from 0 to 5000), have already decided to vote for candidate B, while the remaining N voters are undecided and will vote for A or B with a 50% probability each. Candidate A wins if they receive more votes than candidate B.

### Implementation 💡 
The problem is modeled using the binomial distribution. The script calculates the probability of A winning for different values of M. Due to potential numerical overflow issues with large numbers, the final implementation uses the survival function (`sf`) from `scipy.stats.binom`, which is a robust way to compute `1 - cdf`. The script generates a plot showing the probability of A winning as a function of M.

### Scripts 💻
- `Second assign/foglio2statistica.py`: Contains the logic for calculating the win probability and generating the plot.

---

## 3️⃣ Third Assignment

This assignment involves a simulation of a board game to determine various probabilities related to the game's outcome.

### Problem Description ❗
The game consists of 12 pieces, corresponding to the numbers 2 through 12. On each turn, two six-sided dice are rolled, and the piece corresponding to the sum of the dice advances one step. The first piece to advance 19 steps wins. The simulation is used to answer questions about the game, such as:
- The probability of piece 7 winning before piece 8.
- The probability of each piece winning.
- The probability of the game lasting for a specific number of moves.
- The probability of the game lasting longer than 100 or 200 moves.

### Implementation 💡 
A Monte Carlo simulation is used to play the game a large number of times (200,000 simulations). The outcomes of these simulations are collected and analyzed to calculate the required probabilities. The script then generates plots to visualize the probability of each piece winning and the distribution of game durations.

### Scripts 💻
- `Third assign/ex12.py`: Implements the game simulation and calculates the various probabilities and generates plots.

# Probability-and-Statistics
Personal repository for exercises of Probability and Statistics.

## FIRST ASSIGN

### Original assign text (translated in English)
Let $(xi, yi)i∈{1,...,n}$ be a bivariate sample of size $n$.\
Let
$$
\phi(a, b) = \sum_{i=1}^n (y_i - (a \cdot x_i + b))^2
$$
Write a program that, given $(xi, yi)i∈{1,...,n}$, computes a minimum point
of $ϕ$, that is, a point $(a∗, b∗) ∈ R2$ such that
$$
ϕ(a∗, b∗) = min{ϕ(a, b) : a, b ∈ R}
$$
Then consider the two bivariate samples *(Tmin, Tmed)* and *(Tmin, Ptot)* of the *Meteo_Chioggia60.ods* file and create, for each of the two bivariate samples,
the corresponding scatter diagram with the graph of the line $t → a∗t + b∗$
determined by the minimum point $(a∗, b∗)$ calculated with the program.\
Furthermore, determine the eigendecomposition of the covariance matrix of the four-variate sample *(Tmin, Tmed, Tmax, Ptot)* and identify the two
most important directions (largest eigenvalues). Create the corresponding scatter diagram of the first two components of the four-variate sample
in the new coordinate system (linear transformation of the data according to the
transpose of the orthogonal eigenvector matrix).\
The following are required for the delivery:
- a mathematical justification of the procedure used to calculate a minimum point of $ϕ$;
- the pseudo-code of the program and the commented code in a standard language such as C++ or Python;
- the graphs of the two scatter diagrams with the regression lines in pdf format and the numerical values ​​of the minimum points used;
- the graph of the scatter diagram of the two most important components of the data transformed with the transposed matrix of eigenvectors.


### Problem resolution 
I applied the Gradient Descend method to elaborate the set of data and find the minimum values for $a$ and $b$. In particular this method uses the gradient of the function as subtracting value for the researce of the minimum. \
It can be exemplified as the path to choose while descending a mountain. The choice is to follow the direction of the steepest slope, the gradient in our case.
# Estimation of volume of ellipsoid using Monte Carlo

In the problem, we are given the semi-axes of the ellipsoid and are tasked to determine the volume of the ellipsoid using Monte Carlo.

## Introduction

The basic idea of estimating the volume is to construct a cuboid of dimensions {$2a$, $2b$, $2c$}, so as to enclose the ellipsoid within it. We then generate random points within our constructed cuboidal volume and note down the number of points that happen to fall within the ellisoid volume.

The following ratio is then calculated.

\begin{equation*}
\text{fraction of points within the ellisoid} = \frac{\text{No. of points within the ellipsoid}}{\text{Total no. of points}}
\end{equation*}

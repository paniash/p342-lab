# Random walk on 2D plane - discussion

## Basic idea and methodology

For each step that the walker takes, there is an equal probability to go in any direction, defined by our variable `theta`, which is generated using a pseudo-random number generator. The corresponding steps along the x and y directions are then given by `cos(theta)` and `sin(theta)`.

The walker takes N steps as defined in the problem to be 5 different values, which in this case is (250, 500, 750, 1000, 1500).

## Discussion on RMS distance vs `\sqrt{N}`

Theoretically, the RMS distance should be equal to `\sqrt{N}` upto a few orders. As a result, a linear plot is to be expected with `R_RMS` along y axis and `\sqrt{N}` along the x axis.

However, since we are averaging the values over 100 walks and not over an infinite amount, we expect some errors in the output of the simulation, which indeed is seen from the results!

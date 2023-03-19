import numpy as np
import matplotlib.pyplot as plt
np.random.seed(123)
final_tails = []

# Adding a larger outer range simulates a better bell curve
for x in range(100000):
    # Sets the tails array back to 0 for the random step
    tails = [0]
    for i in range(10):   
        # 0 for heads and 1 for tails
        coin = np.random.randint(0, 2)
        # Creates a list with the total amount of tails after each throw
        tails.append(tails[i] + coin)
    # Appends the final amount of tails from each tails list to a list of final throws
    final_tails.append(tails[-1])

# Plots a histogram of final amounts to show distribution
plt.hist(final_tails, bins=10)
plt.show()
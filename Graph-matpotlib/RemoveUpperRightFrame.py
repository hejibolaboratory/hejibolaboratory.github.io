import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.ylabel('I am a ylabel')
plt.xlabel('I am a loooooooooooo\noooooooooooong title')

# Iterating over all the axes in the figure
# and make the Spines Visibility as False
for pos in ['right', 'top', ]:
    plt.gca().spines[pos].set_visible(False)

plt.show()
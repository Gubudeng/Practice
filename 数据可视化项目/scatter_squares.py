import matplotlib.pyplot as plt

input_values = list(range(0,1000))
squares = [x**3 for x in input_values]

plt.scatter(input_values, squares, c=squares,cmap=plt.cm.Reds, edgecolors='none', s=40)

plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([0, 1001, 0, 1000000000])
plt.savefig('squares_plot1.png', bbox_inches='tight')


# Include a section line with your name
# Peter Shatara

# Work only with these imports:
from numpy import matrix, array, random, min, max
import pylab as plb

# Cerate a list A of 600 random numbers bound between (0:10)
A = list(random.randint(1, 10, 600))

# Create an array B with 500 elements bound in the range [-3*pi:2*pi]
B = random.uniform(-3 * plb.pi, 2 * plb.pi, 500)

def overwrite_elements(arr):
    # Using if, for or while, create a function that overwrites every element in A that falls outside 
    # of the interval [2:9), and overwrite that element with the average between the smallest and largest element in A
    avg = (9 + 1) / 2
    new_arr = []

    for value in arr:
        if value < 2 or value >= 9:
            # Normalize each list element to be bound between [0:0.1]
            new_arr.append(0.1 * (avg - 2) / (9 - 2))
        else:
            # Normalize each list element to be bound between [0:0.1]
            new_arr.append(0.1 * (value - 2) / (9 - 2))

    return new_arr

# Return the result from the function to C
C = overwrite_elements(A)

# Cast C as an array
C = array(C)

# Add C to B (think of C as noise) and record the result in D
D = plb.sort(A[0:500] + B) ## Also sorted so that plots are drawn correctly

# Create a figure, give it a title and specify your own size and dpi
plb.figure(figsize=(10, 6), dpi=120)
plb.title('Plot of sin(D) and cos(D)')

# Plot the sin of D, in the (2,1,1) location of the figure
plb.subplot(2, 1, 1)
plb.plot(D, plb.sin(D), color='red', linewidth=1.5, linestyle='-.', label='sin')

# Overlay a plot of cos using D, with different color, thickness and type of line
plb.plot(D, plb.cos(D), color='blue', linewidth=2.5, linestyle='--', label='cos')

# Create some space on top and boZom of the plot (on the y axis) and show the grid
plb.ylim(-1.5, 1.5)
plb.grid()

# Specify the following: title, Y-axis label and legend to fit in the best way
plb.legend(loc='best')

# Plot the tan of D, in location (2,1,2) with grid showing, X-axis label, Y-axis label and legend on top right
plb.subplot(2, 1, 2)
plb.plot(D, plb.tan(D), color='red', linewidth=1.5, linestyle='-.', label='tan')
plb.xlabel('X Axis', fontsize=9, position=(0.65, 0), rotation=6, color='gray', alpha=0.75)
plb.ylabel('Y Axis', fontsize=9, position=(0,0.75), color='gray', alpha=0.75)
plb.legend(loc='upper right')
plb.grid()

plb.show()

import numpy as np                              # NumPy is a library for numerical calculations
import matplotlib.pyplot as plt                 # Pyplot submodule from Matplotlib is for creating plots

def draw_matplotlib_heart():
    # Generate t values from 0 to 2π
    t = np.linspace(0, 2 * np.pi, 100)

    # Calculate x and y coordinates
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    # Plot the outline of the ♥
    plt.plot(x, y, 'r')
    
    # Fill the inside of the ♥
    plt.fill(x, y, 'r')
   
    # Ensure the axes have the same scale
    plt.axis('equal')
    
    # Display the plot
    plt.show()

draw_matplotlib_heart()



# Generating t values:
    # t = np.linspace(0, 2 * np.pi, 100) 
    # This line generates an array of 100 values (np.linspace) linearly spaced between 0 and 2 * np.pi (which is a full cycle from 0 to 2π) 
    # These t values represent the angles through which we compute the coordinates of the ♥

# Calculating x and y coordinates:
    # x = 16 * np.sin(t)**3 
    # This line computes the x coordinates of the ♥ based on the t values 
    # The np.sin(t) function computes the sine of each t value, and **3 cubes the result 
    # Multiplying by 16 scales and modifies the basic sine shape to form the top part of the ♥

    # y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    # This line calculates the y coordinates of the ♥ 
    # It combines multiple cosine terms with different coefficients (13 * np.cos(t), - 5 * np.cos(2*t), - 2 * np.cos(3*t), - np.cos(4*t)) to define the lower curve of the ♥



# Générer des valeurs de t :
    # t = np.linspace(0, 2 * np.pi, 100)
    # Cette ligne crée un tableau de 100 valeurs (np.linspace) réparties linéairement entre 0 et 2 * np.pi (soit une période complète de 0 à 2π)
    # Ces valeurs de t représentent les angles à travers lesquels nous calculons les coordonnées du ♥

# Calculer des coordonnées x et y :
    # x = 16 * np.sin(t)**3 
    # Cette ligne calcule les coordonnées x du ♥ en fonction des valeurs de t 
    # La fonction np.sin(t) calcule le sinus de chaque valeur de t, puis **3 élève le résultat au cube
    # En multipliant par 16, cela redimensionne et modifie la forme de base du sinus pour former la partie supérieure du ♥

    # y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    # Cette ligne calcule les coordonnées y du ♥
    # Elle combine plusieurs termes de fonctions cosinus avec des coefficients différents (13 * np.cos(t), - 5 * np.cos(2*t), - 2 * np.cos(3*t), - np.cos(4*t)) pour définir la courbe inférieure du ♥



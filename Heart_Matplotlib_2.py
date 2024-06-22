
import numpy as np
import matplotlib.pyplot as plt  

def draw_math_heart():
    # Generate x values from -2 to 2
    x = np.linspace(-2, 2, 400)
    
    # Calculate y coordinates for the upper part of the ♥
    y1 = np.sqrt(1 - (abs(x) - 1)**2)
    
    # Calculate y coordinates for the lower part of the ♥
    y2 = -3 * np.sqrt(1 - (abs(x) / 2)**0.5)

    # Plot the ♥ curves
    plt.plot(x, y1, 'r')
    plt.plot(x, y2, 'r')
    
    # Fill the space between the curves with red
    plt.fill_between(x, y1, y2, where=(y2 < y1), color='red')
    
    # Ensure the axes have the same scale
    plt.axis('equal')
    
    # Display the plot
    plt.show()

draw_math_heart()



# Generating x values :
    # x = np.linspace(-2, 2, 400)
    # This line generates an array of 400 values (np.linspace) evenly spaced between -2 and 2
    # These x values represent points along the horizontal axis where the y coordinates will be calculated to draw the ♥

# Calculating y coordinates to form the rounded upper part of the ♥ :
    # y1 = np.sqrt(1 - (np.abs(x) - 1)**2)
    # It uses np.abs(x) to get the absolute value of x, subtracts 1, squares that result, and takes the square root (np.sqrt)

# Calculating y coordinates to form the pointed lower part of the ♥ :
    # y2 = -3 * np.sqrt(1 - (np.abs(x) / 2)**0.5) 
    # It again uses np.abs(x) to get the absolute value of x, divides by 2, takes the square root (**0.5), then subtracts that from 1 and multiplies by -3

# Plotting the ♥ curves :
    # plt.plot(x, y1, 'r')      Plots the upper curve of the ♥ in red
    # plt.plot(x, y2, 'r')      Plots the lower curve of the ♥ in red

# Filling the space between the y1 and y2 curves in red :
    # plt.fill_between(x, y1, y2, where=(y2 < y1), color='red')
    # The where=(y2 < y1) condition ensures that the filling occurs only where y2 is below y1, ensuring that the space between the two parts of the ♥ is correctly colored

# Setting the axes scale :
    # plt.axis('equal')
    # Ensures that the x and y axes have the same scale, so the ♥ is proportionally represented correctly



# Génération des valeurs de x :
    # x = np.linspace(-2, 2, 400)
    # Cette ligne génère un tableau de 400 valeurs (np.linspace) réparties linéairement entre -2 et 2 
    # Ces valeurs de x représentent les points le long de l'axe horizontal où les coordonnées y seront calculées pour dessiner le ♥

# Calcul des coordonnées y pour former la partie supérieure arrondie du ♥ :
    # y1 = np.sqrt(1 - (np.abs(x) - 1)**2) 
    # Utilise la fonction np.abs(x) pour obtenir la valeur absolue de x, puis soustrait 1, élève cela au carré, et prend la racine carrée (np.sqrt)

# Calcul des coordonnées y pour former la partie inférieure du ♥ :
    # y2 = -3 * np.sqrt(1 - (np.abs(x) / 2)**0.5) 
    # Utilise à nouveau np.abs(x) pour obtenir la valeur absolue de x, la divise par 2, prend la racine carrée (**0.5), puis soustrait cela de 1 et multiplie par -3

# Tracé des courbes du ♥ :
    # plt.plot(x, y1, 'r')      Trace la courbe sup. du ♥ en rouge
    # plt.plot(x, y2, 'r')      Trace la courbe inf. du ♥ en rouge

# Remplissage de l'espace entre les courbes y1 et y2 en rouge :
    # plt.fill_between(x, y1, y2, where=(y2 < y1), color='red')
    # La condition where=(y2 < y1) garantit que le remplissage se fait seulement lorsque y2 est en dessous de y1, assurant ainsi que l'espace entre les deux parties du ♥ est correctement coloré

# Réglage de l'échelle des axes :
    # plt.axis('equal') 
    # Assure que les axes x et y ont la même échelle, pour que le ♥ soit représenté proportionnellement correctement

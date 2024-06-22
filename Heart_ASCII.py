
def draw_ascii_heart():
    heart = [
        "  ***     ***  ",          # Définir la forme du ♥ en utilisant des caractères ASCII
        "******* *******",          # Define the ♥ shape using ASCII characters
        " ************* ",  
        "  ***********  ",  
        "     *****    ",  
        "       *      "   
    ]
    
    for line in heart:              # Imprimer chaque ligne pour afficher le ♥
        print(line)                 # Print each line to display the ♥

draw_ascii_heart()

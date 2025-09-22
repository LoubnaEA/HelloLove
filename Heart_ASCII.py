
def draw_ascii_heart():
    heart = [
        "  ***     ***  ",          
        "******* *******",          # Define the ♥ shape using ASCII characters
        " ************* ",  
        "  ***********  ",  
        "     *****    ",  
        "       *      "   
    ]
    
    for line in heart:              
        print(line)                 # Print each line to display the ♥

draw_ascii_heart()


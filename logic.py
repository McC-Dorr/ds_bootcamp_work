# User wants a clothes rec based on weather temperature
# Define function for what clothes they should select based on temp
# Capture user temperature input
# Print recommended clothes

# Fixed the function that had flawed logic because of the order of elifs
def choose_clothes(temp):
    if temp > 80:
        return 'Wear a t-shirt and hula skirt.'
    elif temp > 60:
        return 'Wear long sleeves and shorts.'
    elif temp > 30:
        return 'Wear a coat over many layers and thick socks.'
    else:
        return "Consider carefully why you are going out! The temperature is freezing."  # Used double quotes because of the ' in don't

# Capture user input
current_temp = float(input("What is the temperature outside today:"))

# Use temperature to tell the user what to wear
clothing_suggestion = choose_clothes(current_temp)

# Tell them
print(clothing_suggestion)
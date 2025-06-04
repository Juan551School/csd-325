# Juan Macias Vasquez
# Date 06/01/2025
# Module 2.2 Assignment Miles to Kilometers (Debugging Version)

def Converter(miles):
    """Convert miles to kilometers."""
    return distance * 1.60934 # Multiples miles to get kilometers 

def main(): # Main interface for the user
    while True:
        try:
            miles = float(input("Enter the number of miles you drove: ")) # Gets input from user
            if miles < 0:
                print("Do Not Enter Negative Number. Please enter a valid number.") # Makes sure the number isnt negative
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.") # Makes sure a number is entered 

            # Output 
    kilometers = Converter(miles)
    print(f"\nYou entered: {miles} miles")
    print(f"That's equivalent to: {kilometers} kilometers")

if __name__ == "__main__":
    main()


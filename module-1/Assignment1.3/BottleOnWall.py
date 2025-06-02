# Juan Macias Vasquez
# Date 06/1/2025
# Module 1.3 Bottles of Beer

#Program

def beer_song(count):
    while count > 0:
        if count == 1:
            print(f"{count} bottle of beer on the wall, {count} bottle of beer.")
            print(f"Take one down and pass it around, 0 bottle(s) of beer on the wall.\n")
        else:
            print(f"{count} bottles of beer on the wall, {count} bottles of beer.")
            print(f"Take one down and pass it around, {count - 1} bottle(s) of beer on the wall.\n")
        count -= 1

# Main program
def main():
    try:
        bottles = int(input("Enter number of bottles: ")) #Get number of beers from user
        if bottles <= 0:
            print("Please enter a positive number.")# Make sure its positive
        else:
            beer_song(bottles)
            print("Time to buy more bottles of beer.")
    except ValueError:
        print("Please enter a valid integer.")# If not a number 

# Run the program
main()


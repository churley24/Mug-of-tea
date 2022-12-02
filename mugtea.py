# Camryn Hurley

class Point:
    """Represents a mug of tea"""

teaMug = Point()

teaMug.oz = 11
teaMug.tea = "earl grey"
teaMug.temp = "hot"


line = "This mug has %d ounces of %s tea in the mug." %(teaMug.oz, teaMug.tea)
print(line)

def tea_drinking_simulation(t):
    amount = teaMug.oz - t
    if amount == 0:
        print("The mug is empty.")
    elif amount < 0:
        print("There is not enough tea in the mug to drink that much.")
    else:
        print("The amount of tea remaining in the mug is", amount, "ounces")

tea_drinking_simulation(4)

#teaMug.oz represents how many ounces of tea is in the mug
#teaMug.tea is the type of tea, so in this case it is early grey
#teaMug.temp represents if the tea is hot or iced

#the parameter for tea_drinking_simulation takes the amount of tea to drink
#amount equals the attribute of how many ounces is in the mug minus the parameter
#I used if statments to print different things depending on the amount 

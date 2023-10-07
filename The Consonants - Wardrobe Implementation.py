import random

def collectClothes():
    tops = []
    bottoms = []
    shoes = []
    accessories = []

    while True:
        answer = str(input("Do you want to submit a top? (Yes/No)\n"))
        #print(answer)
        if answer.upper() == "YES":
            image = input("Upload your image:\n")
            tops.append(image)
        else:
            break
    while True:
        answer = input("Do you want to submit a bottom? (Yes/No)\n")
        if answer.upper() == "YES":
            image = input("Upload your image:\n")
            bottoms.append(image)
        else:
            break
    while True:
        answer = input("Do you want to submit shoes? (Yes/No)\n")
        if answer.upper() == "YES":
            image = input("Upload your image:\n")
            shoes.append(image)
        else:
            break
    while True:
        answer = input("Do you want to submit accessories? (Yes/No)\n")
        if answer.upper() == "YES":
            image = input("Upload your image:\n")
            accessories.append(image)
        else:
            break
    wardrobe = [tops,bottoms,shoes,accessories]
    return wardrobe
    
def chooseFit():
    wardrobe = collectClothes()
    accessories = random.choice(wardrobe[0])
    shoes = random.choice(wardrobe[1])
    bottom = random.choice(wardrobe[2])
    top = random.choice(wardrobe[3])

    print(f"Here's your fit! {top}, {bottom}, {shoes}, {accessories}")

chooseFit()
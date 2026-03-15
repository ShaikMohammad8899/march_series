print("--- Pizza  ---")
print("Menu: BBQ, Crispy Chicken Pizza, Panner Pizza, Corn Pizza, French Fries & Coke")

a = input("Enter the item name to see the price: ").lower()

if a=="bbq":
    print("The price for BBQ is 1000.")
    
elif a=="crispy chicken pizza":
    print("The price for Crispy Chicken Pizza is 800.")
    
elif a=="panner pizza":
    print("The price for Panner Pizza is 600.")
    
elif a=="corn pizza":
    print("The price for Corn Pizza is 400.")
    
elif a=="french fries & coke":
    print("The price for French Fries & Coke is 200.")
    
else:
    print("Sorry, that item is not available.")



















print("--- Welcome to the Bakery ---")
print("Price points: 1200, 1000, 800, 600")

cost= input("Enter the price to see the cake name: ")

if cost_input.replace('.', '', 1).isdigit():
    price = int(float(cost_input))
    
    if price == 1200:
        print("At 1200, you get: Red Velvet Cake")
        
    elif price == 1000:
        print("At 1000, you get: Choco Almond Cake")
        
    elif price == 800:
        print("At 800, you get: Butterscotch")
        
    elif price == 600:
        print("At 600, you get: Normal Cake")
        
    else:
        print("Rem prices -> Sorry cake is not available")

else:
    print("Error: Please enter a valid number for the price.")

print("-----------------------------")

# John Raven F. Caduyac
# CD-3L
# a simple inventory management system for chemical storage
import additional

chemicals = {}
def main():
    print("""
    ========================
    [1] Add New Chemical
    [2] View All Chemicals
    [3] Dispose Chemical
    [4] Clear all Chemicals
    [5] Restock Chemical
    [6] Execute experiment
    [7] Load Inventory
    [8] Save Inventory
    [0] Exit
        """)

def addstock(chemicals):
    print("ADD NEW CHEMICAL")
    stock_code = input("Enter Chemical Code: ")
    chem_name = input("Enter Chemical Name: ")
    chem_amount = int(input("Enter amount in ml: "))
    chem_expiry = input("Enter Expiry Date(e.g. 23Mar2024): ")
    chem_storage = input("Enter Storage Conditions(CHILLED/ROOM): ")
    if stock_code in chemicals:
        print("Chemical code already exist")
        return None
    chemicals[stock_code] = [chem_name, chem_amount, chem_expiry, chem_storage]
    print("The chemical has been successfully added!!!")
    return chemicals
    
def viewStocks(chemicals):
    if chemicals.items():
        for keys, items in chemicals.items():
            print("VIEW ALL CHEMICALS")
            print()
            print("Chemical Code:", keys)
            print("Name:", items[0])
            print("Amount:", items[1])
            print("Expiry:", items[2])
            print("Storage Conditions:", items[3])
    else:
        print("The Inventory is empty.")
    

def deleteStock(chemicals, chemical_to_delete):
    if chemical_to_delete in chemicals:
        del chemicals[chemical_to_delete]
        print("The chemical has been deleted")
        return chemicals
    else: 
        print("Chemical doesn't exist")

def deleteAllStock(chemicals):
    for keys in chemicals:
        del chemicals[keys]
        return chemicals

def restockChem(chemicals, stock_code):
    if stock_code in chemicals:
        amount = int(input("Enter amount to restock: "))
        chemicals[stock_code][1] += amount
        print("New amount of",chemicals[stock_code][0],"with chemical code",stock_code,":",chemicals[stock_code][1])
        return chemicals
    else:
        print("This chemical doesn't exist")
        return None

def consumeChem(chemicals, stock_code):
    print("Execute Experiment")
    amount_of_chemicals = int(input("Amount of chemicals used in experiment: "))
    for i in range(amount_of_chemicals):
        while True:
            stock_code = input("Enter Chemical Code: ")
            if stock_code in chemicals:
                amount_consumed = int(input("Enter amount to consume: "))
                if chemicals[stock_code][1] >= amount_consumed:
                    chemicals[stock_code][1] -= amount_consumed
                    print("Consumed",amount_consumed,"of",chemicals[stock_code][0],"with chemical code",stock_code)
                    break
                else:
                    print("Insufficient Stock")
            else:
                print("This chemical does not exist")
    print("Experiment over.")
    return chemicals


while True:
    main()
    choice = int(input("Enter choice: "))
    if choice == 1:
        addstock(chemicals)
    elif choice == 2:
        viewStocks(chemicals)
    elif choice == 3:
        print("DISPOSE CHEMICAL")
        chemical_to_delete = input("Enter Chemical Code: ")
        deleteStock(chemicals, chemical_to_delete)
    elif choice == 4:
        deleteAllStock(chemicals)
    elif choice == 5:
        print("RESTOCK CHEMICAL")
        stock_code = input("Enter Chemical Code: ")
        restockChem(chemicals, stock_code)
    elif choice == 6:
        consumeChem(chemicals, stock_code)
    elif choice == 7:
        Caduyac_ex7.loadInventory(chemicals)
        print("inventory.dat successfully loaded")
    elif choice == 8:
        Caduyac_ex7.saveInventory(chemicals)
        print("inventory.dat successfully saved")
    elif choice == 0:
        break
    else:
        print("Invalid Input")

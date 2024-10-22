def loadInventory(chemicals):
    inventory = open("inventory.dat", "r")
    for line in inventory:
        data = line[:-1].split(",")
        chemicals.update({data[0]: [data[1], data[2], data[3], data[4]]})
    inventory.close()


def saveInventory(chemicals):
    inventory = open("inventory.dat", "w")
    for keys, items in chemicals.items():
        data = keys+","+items[0]+","+str(items[1])+","+items[2]+","+items[3]
        inventory.write(data + "\n")
    inventory.close()
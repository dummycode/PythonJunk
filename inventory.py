stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 20}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total = item_total + v
    print("\nTotal number of items: " + str(item_total))

def addToInventory(inventory, items):
    for i in range(len(items)):
        inventory.setdefault(items[i], 0)
        inventory[items[i]] = inventory[items[i]] + 1
    return inventory

loot = ['gold coin', 'arrow', 'rope', 'dagger', 'gold coin', 'gold coin']

stuff = addToInventory(stuff, loot)
displayInventory(stuff)

# -*- coding: UTF-8 -*-
player= {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
player['ron']=2
print (player)
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory,addeditems):
    for i in addeditems:

        if i in inventory.keys():
            inventory[i]+=1
            print (inventory)
        else:
            inventory.setdefault(i,1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin','ruby']
inv = addToInventory(inv, dragonLoot)
print (inv)
displayInventory(inv)

slist = []
while True:
    item = input("Enter an item for your shopping list (type 'done' to finish): ")
    if item == 'done':
        print([slist])
        break
    else:
        slist.append(item)
        

# can firstly initialise item and use if item != 'done: as opposed to while true, this eliminates the need for 'break'
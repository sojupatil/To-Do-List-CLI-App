def todo_list():
    try:
        no_of_items = float(input("Enter number of items you want to add in list : "))
        no_of_items = round(no_of_items)
    except ValueError:
        print("Error : Please enter numeric value only")
        exit()

    items = []
    
    for n1 in range(no_of_items):
        item = input("Enter name of item to add in list : ")
        items.append(item)
    print(items)    

    if_remove = input("Do you want to remove any item from list? Yes / No : ")
    if_remove = if_remove.lower()

    
    if if_remove == "yes":
            number_to_remove = float(input("Enter number of items to remove : "))
            number_to_remove = round(number_to_remove)
            n2 = 1
            while n2 < (number_to_remove + 1):
             removable_item = input("Enter name of item you want to remove : ")
             if removable_item not in items:
                  print("Item not in basket")
             items.remove(removable_item)
             n2+=1
    else:
            print("Thanks for using This!")
    print(items)    
todo_list()

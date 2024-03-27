def add_to_shopping_list(shopping_list):
  
 while True:
    action = input("Enter 'add' to add an item, 'remove' to remove, or 'done' to finish: ")
    if action.lower() == "done":
      break

    elif action.lower() == "add":
      item = input("Enter an item to add: ")
      shopping_list.append(item)
      print(f"{item} added to the list.")

    elif action.lower() == "remove":
      if not shopping_list:
        print("The shopping list is empty.")
      else:
        item_to_remove = input("Enter the name of the item to remove: ")
        if item_to_remove in shopping_list:
          shopping_list.remove(item_to_remove)
          print(f"{item_to_remove} removed from the list.")
        else:
          print(f"Item '{item_to_remove}' not found in the list.")

    else:
      print("Invalid action. Please enter 'add', 'remove', or 'done'.")

def print_shopping_list(shopping_list):

  
  if not shopping_list:
    print("The shopping list is empty.")
  else:
    print("Shopping List:")
    for i, item in enumerate(shopping_list, start=1):
      print(f"{i}. {item}")

shopping_list = []
add_to_shopping_list(shopping_list)

print_shopping_list(shopping_list)
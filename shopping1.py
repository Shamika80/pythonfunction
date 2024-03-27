def add_to_shopping_list(shopping_list):
  
  while True:
    item = input("Enter an item to add to the shopping list (or 'done' to finish): ")
    if item.lower() == "done":
      break
    shopping_list.append(item)
  print("Items added to the shopping list!")

shopping_list = []
add_to_shopping_list(shopping_list)

print("Your shopping list:")
for item in shopping_list:
  print(f"- {item}")
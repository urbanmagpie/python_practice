# Dragon Feast List Manager

feast_list = ['lava peppers', 'goat cheese', 'crispy knight', 'fire-breath mints', '12 eggs of doom']

def print_feast_list(items):
    if not items:
        print("The hoard is empty. No feast shall be had!")
    elif len(items) == 1:
        print(f"You must acquire {items[0]}.")
    else:
        print(f"You must acquire {', '.join(items[:-1])}, and {items[-1]}.")

def add_item(item):
    feast_list.append(item)
    print(f" Added '{item}' to your feast.")

def remove_cursed_item(item):
    count = 0
    while item in feast_list:
        feast_list.remove(item)
        count += 1
    if count > 0:
        print(f" Removed {count} cursed instance(s) of '{item}' from the feast list.")
    else:
        print(f" No cursed item named '{item}' found.")

def replace_item(old_item, new_item):
    replaced = False
    for i in range(len(feast_list)):
        if feast_list[i] == old_item:
            feast_list[i] = new_item
            replaced = True
    if replaced:
        print(f" Replaced '{old_item}' with '{new_item}' in the feast list.")
    else:
        print(f" No item named '{old_item}' found to replace.")

# Demo of usage:
print_feast_list(feast_list)
add_item('pickled phoenix feathers')
add_item('crunchy troll toes')
print_feast_list(feast_list)
remove_cursed_item('unicorn jelly')  # no unicorn jelly yet, will show "not found"
add_item('unicorn jelly')
add_item('unicorn jelly')
remove_cursed_item('unicorn jelly')
replace_item('goat cheese', 'molten dragon cheese')
print_feast_list(feast_list)


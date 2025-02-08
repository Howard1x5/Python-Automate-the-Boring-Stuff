# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
#  with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas,
#  tofu, and cats'. But your function should be able to work with any list value passed to it. Be sure to test the case where an 
# empty list [] is passed to your function.

# Thoughts on the problem. 
# Take list of words and converty the list into a single string where:
    # each word is separated by a command and space ", " comma and space
    # the last word is preceded by "and" instead of a comma.
    # if the list is empty, return an empty string

# PseudoCode
# Define a function that takes a list as an argument.
# If the list is empty, return an empty string.
# If the list has one item, return that item.
# If the list has two items, return "item1 and item2".
# Otherwise:
#     - Get all items except the last one and join them with ", ".
#     - Add " and " before the last item.
#     - Return the final string.

def list_to_string(items):
    if not items: # if empty list
        return ''
    elif len(items) == 1: # if one item
        return items[0]
    elif len(items) == 2: # if two items
            return f'{items[0]} and {items[1]}'
    else:
         return ', '.join(items[:-1]) + f', and {items[-1]}'
    
# test the function
spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_string(spam))    
print(list_to_string(['single']))
print(list_to_string([]))


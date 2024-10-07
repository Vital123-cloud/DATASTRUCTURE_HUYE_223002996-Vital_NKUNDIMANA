# Two lists of friends
friends_list_1 = ["Alice", "Bob", "Charlie", "Diana"]
friends_list_2 = ["Eve", "Charlie", "Frank", "Bob", "Grace"]

# Print the initial lists
print("Friends list 1:", friends_list_1)
print("Friends list 2:", friends_list_2)

# Merge the two lists and remove duplicates by converting to a set
merged_friends = list(set(friends_list_1 + friends_list_2))

# Print the merged list without duplicates
print("Merged friends list (without duplicates):", merged_friends)

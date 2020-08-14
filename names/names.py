import time
from classes import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
#fill lists
name1_bst = BSTNode(names_1[0])
name2_bst = BSTNode(names_2[0])
for i in range(len(names_1)):
        if i != 0:
                name1_bst.insert(names_1[i])
                name2_bst.insert(names_2[i])

# Replace the nested for loops below with your improvements
for name in names_1:
        if name2_bst.contains(name):
                duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
breakpoint()

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

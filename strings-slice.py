# For understanding slicing we will use different methods, here we will cover 2 methods of string slicing, one using the in-build slice() method and another using the [:] array slice.
# --> Using the array slicing  [:: ] method
# Index tracker for positive and negative index: String indexing and slicing in python.

# ---> Using a slice() method
# The syntax of slice() is:

# slice(start, stop, step)
# slice() can take three parameters:

# start (optional) - Starting integer where the slicing of the object starts. Default to None if not provided.
# stop - Integer until which the slicing takes place. The slicing stops at index stop -1 (last element).
# step (optional) - Integer value which determines the increment between each index for slicing. Defaults to None if not provided.
String = "Python is a popular programming language";

# Using slice constructor
s1 = slice(6)
s2 = slice(1, 6)
s3 = slice(1, 5, 2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])


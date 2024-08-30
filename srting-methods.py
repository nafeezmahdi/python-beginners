# ---> String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string.

str = "Nafeez Mahdi"
# Returns true if the string ends with the specified value
print(str.endswith("di"));
# Returns a string where a specified value is replaced with a specified value
print(str.replace("Nafeez Mahdi", "N.M."))
# Searches the string for a specified value and returns the position of where it was found
print(str.find("Mahdi"));
# Returns the number of times a specified value occurs in a string
print(str.count("a"));
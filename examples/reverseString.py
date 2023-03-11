def reverse_string(string):
    # Use string slicing to reverse the order of the characters in the string
    reversed_string = string[::-1]
    
    # Return the reversed string
    return reversed_string

# Example usage
original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
print(reversed_string)

# In this example, the reverse_string() function takes a string as an argument and uses 
# string slicing to reverse the order of the characters in the string. 
# Finally, the reversed string is returned.
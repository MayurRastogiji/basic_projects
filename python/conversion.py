"""
Number Conversion Utility
========================

This module provides functions for converting numbers between different number systems:
- Decimal (base 10)
- Binary (base 2)
- Hexadecimal (base 16)

The module includes manual implementations of conversion algorithms to demonstrate
the mathematical principles behind number system conversions.

Functions:
----------
1. reverse(num) - Reverses a string or sequence
2. decimal_to_binary(num) - Converts decimal to binary using powers of 2
3. binary_to_decimal(num) - Converts binary to decimal using positional notation
4. binary_to_hexadecimal(num) - Converts binary to hex using 4-bit grouping
5. decimal_to_hex(num) - Converts decimal to hex via binary
6. hex_to_binary(num) - Converts hex to binary digit by digit
7. hex_to_decimal(num) - Converts hex to decimal via binary

Author: Mayur
Date: 2025
"""

'''Function to reverse a string or sequence'''
def reverse(num):
    """
    Reverses a string using Python's slice notation
    Args:
        num: String or sequence to reverse
    Returns:
        Reversed string/sequence
    """
    return num[::-1]

'''Convert a decimal number to binary string (manual method using powers of 2)'''     
def decimal_to_binary(num):
    """
    Converts a decimal number to binary using manual calculation with powers of 2
    Args:
        num: Decimal number to convert
    Returns:
        Binary representation as a string
    """
    digit = num  # Working copy of the number
    i = 0
    bin = 2 ** i  # Start with 2^0 = 1
    bin_string = ""
    
    # Handle special case of 0
    if num == 0:
        return "0"
    
    # Find the highest power of 2 that fits in the number
    while(num >= bin):
        i += 1
        bin = 2 ** i
    
    # Build binary string from left to right
    while(digit != 0 or i > 0):
        i -= 1
        bin = 2 ** i
        
        # If current power of 2 fits in remaining number, use it
        if (digit >= bin):
            digit -= bin  # Subtract the power of 2
            bin_string += "1"  # Add 1 to binary string
        else:
            bin_string += "0"  # Add 0 to binary string
    
    return bin_string

'''Convert binary to decimal using positional notation'''
def binary_to_decimal(num):
    """
    Converts a binary number to decimal using positional notation
    Each digit is multiplied by 2 raised to its position (from right to left, starting at 0)
    Args:
        num: Binary number as integer or string
    Returns:
        Decimal equivalent as integer
    """
    i = 0  # Position counter (power of 2)
    decimal_number = 0  # Accumulator for decimal result
    digit = int(num)  # Convert to integer for processing
    
    # Process each binary digit from right to left
    while(digit > 0):
        # Get rightmost digit and multiply by 2^i
        decimal_number += (digit % 10) * (2 ** i)
        i += 1  # Move to next position
        digit = digit // 10  # Remove rightmost digit
    
    return decimal_number

'''Convert binary to hexadecimal using 4-bit groups'''
def binary_to_hexadecimal(num):
    """
    Converts a binary number to hexadecimal by grouping 4 bits together
    Each group of 4 bits represents one hexadecimal digit
    Args:
        num: Binary number as integer or string
    Returns:
        Hexadecimal representation as string
    """
    digit = str(num)  # Work with string representation
    temp_hex = ""  # Accumulator for hex result
    
    # Hexadecimal dictionary mapping decimal values to hex characters
    hex_dic = {0:"0", 1:"1" ,2:"2" ,3:"3" ,4:"4" ,5:"5" ,6:"6" ,7:"7" ,8:"8" ,9:"9" ,10:"A" ,11:"B" ,12:"C" ,13:"D" ,14:"E" ,15:"F" }
    
    # Calculate how many complete 4-bit groups we have
    number_element = len(digit) / 4
    
    # Process complete 4-bit groups from right to left
    while (number_element > 0):
        temp_a = digit[-4:]  # Get last 4 bits
        digit = digit[:-4]   # Remove processed bits
        temp_b = binary_to_decimal(int(temp_a))  # Convert 4-bit group to decimal
        temp_hex += hex_dic[temp_b]  # Map to hex character
        number_element -= 1
        
        # Handle remaining bits if not a complete 4-bit group
        if (number_element < 1 and number_element > 0):
            temp_a = digit[-int((number_element*4)):]  # Get remaining bits
            temp_b = binary_to_decimal(int(temp_a))    # Convert to decimal
            temp_hex += hex_dic[temp_b]                # Map to hex character
            number_element -= 1
    
    return reverse(temp_hex)  # Reverse to get correct order

'''Convert decimal to hexadecimal by first converting to binary, then to hex'''
def decimal_to_hex(num):
    """
    Converts a decimal number to hexadecimal by first converting to binary
    Uses decimal_to_binary and binary_to_hexadecimal functions
    Args:
        num: Decimal number to convert
    Returns:
        Hexadecimal representation as string
    """
    return binary_to_hexadecimal(decimal_to_binary(num))

'''Convert hexadecimal to binary by converting each hex digit to 4-bit binary'''
def hex_to_binary(num):
    """
    Converts a hexadecimal number to binary by converting each hex digit to 4-bit binary
    Each hex digit is mapped to its decimal value, then converted to binary
    Args:
        num: Hexadecimal number as string
    Returns:
        Binary representation as string
    """
    temp_a = ""  # Accumulator for binary result
    
    # Hexadecimal to decimal mapping dictionary
    bin_dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15} 
    
    # Process each hex digit
    for i in num:
        temp_dec = bin_dic[i]  # Convert hex digit to decimal
        temp_bin = decimal_to_binary(temp_dec)  # Convert decimal to binary
        
        # Ensure each hex digit produces exactly 4 bits
        if len(temp_bin) == 4:
            temp_a += str(temp_bin)
        else: 
            # Pad with leading zeros if necessary
            temp_a += ((4-len(temp_bin))*("0")) + str(temp_bin)
    
    # Remove leading zeros from the final result
    for index, i in enumerate(temp_a):
        if i == "1":
            return temp_a[index:]
    
    return temp_a


'''Convert hexadecimal to decimal by first converting to binary, then to decimal'''
def hex_to_decimal(num):
    """
    Converts a hexadecimal number to decimal by first converting to binary
    Uses hex_to_binary and binary_to_decimal functions
    Args:
        num: Hexadecimal number as string
    Returns:
        Decimal representation as integer
    """
    return binary_to_decimal(hex_to_binary(num))

# Testing loop to verify all conversion functions work correctly
# This loop tests conversions for numbers 0 through 19999
for i in range(20000):
    # Convert decimal to binary
    binary = decimal_to_binary(i)
    
    # Convert binary back to decimal (should equal original i)
    decimal = binary_to_decimal(binary)
    
    # Convert decimal to hexadecimal (via binary)
    d_hex = decimal_to_hex(i)
    
    # Convert binary to hexadecimal directly
    b_hex = binary_to_hexadecimal(binary)
    
    # Convert hexadecimal back to decimal (should equal original i)
    hex_d = hex_to_decimal(d_hex)
    
    # Convert hexadecimal to binary
    hex_b = hex_to_binary(b_hex)
    
    # Display all conversion results
    print(f"binary of {i} is : {binary}")
    print(f"binary value for {b_hex} is : {hex_b}")
    print(f"decimal of {binary} is : {decimal}")
    print(f"decimal value for {d_hex} is :{hex_d}")
    print(f"hexadecimal value for {i} is :{d_hex}")
    print(f"hexadecimal value for {binary} is : {b_hex}")
    
    # Verify that all conversions are consistent
    if (i == decimal == hex_d):
        print("Correct")
    else:
        print("Wrong")
    print()
        


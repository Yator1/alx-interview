#!/usr/bin/python3
"""
Method to determine a data is a valid UTF-8 encoding
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data: List of integers where each integer represents 1 byte of data
        
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Mask to check if the most significant bit is set or not
    mask1 = 1 << 7
    # Mask to check if the second most significant bit is set or not
    mask2 = 1 << 6

    for num in data:
        # Get only the 8 least significant bits
        num = num & 255

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Count how many bytes this character has
            mask = 1 << 7
            while num & mask:
                n_bytes += 1
                mask = mask >> 1

            # 1 byte characters - normal ASCII
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False

        # If we are processing continuation bytes
        else:
            # Check if the byte starts with 10
            if not (num & mask1 and not (num & mask2)):
                return False
            
        # Reduce the number of bytes to process
        n_bytes -= 1

    # All bytes should be processed
    return n_bytes == 0

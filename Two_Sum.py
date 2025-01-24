def two_sum(nums, target):
    # Dictionary to store numbers and their indices
    num_indices = {}
    
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            return [num_indices[complement], i]
        
        # Store the current number and its index in the dictionary
        num_indices[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices:", result)  # Output: Indices: [0, 1]

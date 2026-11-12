# 1. Hashing Using a Dictionary (dict)
# Dictionaries are best when you need to map a key to a value (like counting occurrences or storing indices).

# --- Example A: Counting Frequency of Elements ---
def count_frequencies(arr):
    freq_map = {}  # Our hash table
    
    for num in arr:
        # O(1) lookup and update
        freq_map[num] = freq_map.get(num, 0) + 1
        
    return freq_map

numbers = [10, 20, 10, 30, 20, 10]
print("Frequencies:", count_frequencies(numbers))
# Output: Frequencies: {10: 3, 20: 2, 30: 1}


# --- Example B: Classic Two Sum Problem ---
# Find two numbers that add up to the target and return their indices
def two_sum(nums, target):
    seen = {}  # Stores {number: index}
    
    for i, num in enumerate(nums):
        needed = target - num
        
        # Instant O(1) check in the hash table
        if needed in seen:
            return [seen[needed], i]
            
        seen[num] = i
        
    return []

print("Two Sum Indices:", two_sum([2, 7, 11, 15], 9))
# Output: Two Sum Indices: [0, 1]
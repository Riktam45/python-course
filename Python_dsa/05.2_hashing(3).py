# 2. Hashing Using a Set (set)
# Sets are best when you only care if an item exists or not (no values needed, just unique keys).

# --- Example A: Check for Duplicates ---
def has_duplicates(arr):
    seen = set()  # Our hash set
    
    for item in arr:
        # Instant O(1) lookup
        if item in seen:
            return True
        seen.add(item)
        
    return False

print("Contains duplicate?", has_duplicates([1, 2, 3, 4, 2]))
# Output: Contains duplicate? True


# --- Example B: Find Common Elements (Intersection) ---
def find_common(list1, list2):
    set1 = set(list1)  # Convert first list to a hash set
    common = []
    
    for item in list2:
        # O(1) lookup instead of O(n) list search
        if item in set1:
            common.append(item)
            
    return common

print("Common elements:", find_common([1, 2, 3, 4], [3, 4, 5, 6]))
# Output: Common elements: [3, 4]
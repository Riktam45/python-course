"""
1. What is Hashing?
    Hashing in Data Structures and Algorithms (DSA) is a technique used to store and find data almost instantly. 
    Instead of searching through an entire list one by one, hashing jumps straight to the exact location where 
    the data is stored.

    In Python, hashing powers built-in data structures like dictionaries (dict) and sets (set).

2. How It Works (3 Simple Steps)? 
    i. Key: The data you want to store or find (e.g., "apple").

    ii. Hash Function: A math formula that converts your key into a number (called a hash code or index). 
                    Python has a built-in hash() function for this.

    iii. Hash Table: An array (like a list of buckets) that stores your data at that exact index number.

3. Hashing in Python
    In Python, you don't usually have to build a hash table from scratch—it is already built into two core 
    data structures:-

    i. Dictionaries (dict): Store key-value pairs (e.g., {"apple": 50, "banana": 20}).

    ii. Sets (set): Store unique items (e.g., {"apple", "banana"}).
"""

# 4. Example:- 

# Under the hood, Python hashes "Alice" to find its exact memory slot
phonebook = {"Riktam": "555-1234", "Bittu": "555-5678"}    
# Instant O(1) lookup—no looping required
print(phonebook["Riktam"])  # Output: 555-1234       
# You can inspect Python's built-in hash function directly
print(hash("Alice"))       # Output: a large integer (changes each run for security)

"""
5. Two Key Concepts to Know

    i. Hash Collisions: Sometimes, two different keys produce the exact same hash index 
                        (e.g., both "apple" and "banana" map to index 42). Hash tables handle this 
                        cleanly behind the scenes—usually by storing a small list of items at that single 
                        index (Chaining) or finding the next open slot (Open Addressing).

    ii. Hashable vs. Unhashable: To be used as a dictionary key or set item, data must be immutable 
                                 (cannot be changed after creation). If a key changed, its hash would change, 
                                 and Python would lose track of it.

    Hashable (Allowed): int, float, str, tuple

    Unhashable (Throws TypeError): list, dict, set

    
**Key Rule to Remember**
    In Python, only immutable (unchangeable) data types can be hashed and used as dictionary keys or 
    set elements—like int, str, and tuple. Mutable types like list or dict cannot be hashed because if 
    their content changes, their hash index would break.

6. Handling Collisions
    i. Separate Chaining (Using Extra Space): each slot (bucket) in the hash table as holding a 
                                              linked list (or a Python list) instead of a single item.

    How it works: If two keys land on index 3, they are both stored at index 3, chained together one after 
                  another. When searching, you go to index 3 and walk through that mini-list to find your 
                  exact key.

    ii. Open Addressing (Finding Another Empty Slot): Instead of creating lists inside a slot, everything stays 
                                                      directly inside the main hash table array
                                            
    How it works: If index 3 is already taken, the algorithm looks for the next available empty slot using 
                  a set rule (called probing):
                
        a. Linear Probing: Check the very next slot (3 + 1, 3 + 2, 3 + 3...) until an empty one is found.

        b. Quadratic Probing: Jump in bigger steps (3 + 1², 3 + 2², 3 + 3²...) to avoid clumping items together.
"""
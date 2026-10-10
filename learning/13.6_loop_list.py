loop_list = ["Alpha", "Beta", "Charlie", "Delta"]
for x in loop_list:
    print(x)

loop_list1 = ["A", "B", "C"]
for x in range(len(loop_list1)):
    print(loop_list1[x])

# The output shows the text values because the code uses loop_list1[i], 
# which looks up the actual item at that index position.
# Here is exactly how the print(loop_list1[i]) step translates the index numbers back into the words:
# When i is 0: print(loop_list1[i]) looks up index 0, which outputs apple.
# When i is 1: print(loop_list1[i]) looks up index 1, which outputs banana.
# When i is 2: print(loop_list1[i]) looks up index 2, which outputs cherry.
# If you were to change that line to just print(i), the output would change to the index numbers 0, 1, 2.


import a as a

lst = [1, 2, 3, 4, 5.3, 6, 7, 8, 9, 0]
evens = []
odds = []
for char in lst:
    if char % 2 == 1:
        odds.append(char)
    elif char % 2 == 0:
        evens.append(char)
    else:
        print(f"{char} must be a decimal.")
odds.append(11)
evens.append(12)

print(f"Here are the new lists: Evens: {evens} and odds: {odds}")
print(f"let's see what pops from the evens list: {evens.pop()}")
print(f"Here are the new lists after pop: Evens: {evens} and odds: {odds}")
print(f"And now for something completely different")


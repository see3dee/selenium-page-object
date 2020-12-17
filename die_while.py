import random

min = 1
max = 6
all_rolls = []
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixs = 0
tot_num_rolls = 0

while True:
    roll_again = input("Would you like to roll the die again? (Y/n)")

    if roll_again != 'n':
        roll = random.randint(min, max)
        if roll == 1:
            print(f"It's a {roll}")
            ones += 1
            all_rolls.append(roll)
            tot_num_rolls += 1
        elif roll == 2:
            print(f"It's a {roll}")
            twos += 1
            all_rolls.append(roll)
            tot_num_rolls += 1
        elif roll == 3:
            print(f"It's a {roll}")
            threes += 1
            all_rolls.append(roll)
            tot_num_rolls += 1
        elif roll == 4:
            print(f"It's a {roll}")
            fours += 1
            all_rolls.append(roll)
            tot_num_rolls += 1
        elif roll == 5:
            print(f"It's a {roll}")
            fives += 1
            all_rolls.append(roll)
            tot_num_rolls += 1
        else:
            print(f"It's a {roll}")
            sixs += 1
            all_rolls.append(roll)
            tot_num_rolls += 1
    else:
        break
print()
print()
print(f"OK, Sorry to see you go!!")
print()
print(f"Thanks for Playing!!!")
print()
print()
print(f"You rolled {tot_num_rolls} times!")

print()
print(f"You rolled a 1, {ones} out of {tot_num_rolls} times")
print(f"You rolled a 2, {twos} out of {tot_num_rolls} times")
print(f"You rolled a 3, {threes} out of {tot_num_rolls} times")
print(f"You rolled a 4, {fours} out of {tot_num_rolls} times")
print(f"You rolled a 5, {fives} out of {tot_num_rolls} times")
print(f"You rolled a 6, {sixs} out of {tot_num_rolls} times")
print()
print()
print(f"How does this compare with what is expected?")



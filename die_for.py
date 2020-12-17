import random

# min = 1
# max = 6
stats = {"tot_ones": 0, "tot_twos": 0, "tot_threes": 0, "tot_fours": 0,
         "tot_fives": 0, "tot_sixs": 0, "tot_num_rolls": 0, "min": 1, "max": 6}

all_rolls = []
how_many_rolls = int(input("How many times shall we roll the die? Please enter an integer."))

for i in range(how_many_rolls):
    roll = random.randint(stats["min"], stats["max"])
    if roll == 1:
        print(f"It's a {roll}")
        stats["tot_ones"] += 1
        all_rolls.append(roll)
        stats["tot_num_rolls"] += 1
    elif roll == 2:
        print(f"It's a {roll}")
        stats["tot_twos"] += 1
        all_rolls.append(roll)
        stats["tot_num_rolls"] += 1
    elif roll == 3:
        print(f"It's a {roll}")
        stats["tot_threes"] += 1
        all_rolls.append(roll)
        stats["tot_num_rolls"] += 1
    elif roll == 4:
        print(f"It's a {roll}")
        stats["tot_fours"] += 1
        all_rolls.append(roll)
        stats["tot_num_rolls"] += 1
    elif roll == 5:
        print(f"It's a {roll}")
        stats["tot_fives"] += 1
        all_rolls.append(roll)
        stats["tot_num_rolls"] += 1
    else:
        print(f"It's a {roll}")
        stats["tot_sixs"] += 1
        all_rolls.append(roll)
        stats["tot_num_rolls"] += 1

print(f"You said to roll the die {how_many_rolls} times and that resulted in {stats['tot_num_rolls']} rolls!")
print(f"Of the {how_many_rolls} rolls that you did:")
print(f"You rolled a one,   {stats['tot_ones']} times ")
print(f"You rolled a two,   {stats['tot_twos']} times ")
print(f"You rolled a three, {stats['tot_threes']} times ")
print(f"You rolled a four,  {stats['tot_fours']} times ")
print(f"You rolled a five,  {stats['tot_fives']} times ")
print(f"You rolled a six,   {stats['tot_sixs']} times ")
print()
print(f"Thanks for Playing!!!")
print()
print()



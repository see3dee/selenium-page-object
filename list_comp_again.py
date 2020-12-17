# list comp.
lst = [1, 2, 3, 4, 5.3, 6, 7, 8, 9, 0]


def dub_list(lst_in):
    out = [x * 2 for x in lst_in if x % 2 == 0]
    return out, sum(out), type(out)


print(dub_list(lst))

# Lists again
l1 = [2, 4, 6, 8, 9, 12, 45]


def sumlst(lst):
    return sum(lst)


def calc(lst):
    return sumlst(lst) / (lst[1] * l1.pop())


animals = ['pig', 'cat', 'dog', 'poodle', 'bear', 'dinosaur', 'sabor tooth tiger', 'pony', 'snake', 'snail']


def find_p(lstg):
    starts_p = [member for member in lstg if member.startswith('p')]
    return starts_p


def find_s(lstg):
    starts_s = [member for member in lstg if member.startswith('s')]
    return starts_s

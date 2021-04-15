HALF_LIFE_PERIOD = 12
atoms_init = int(input())
atoms_fin = int(input())
half_lives = 0
while atoms_init >= atoms_fin:
    atoms_init /= 2
    half_lives += 1
print(half_lives * HALF_LIFE_PERIOD)

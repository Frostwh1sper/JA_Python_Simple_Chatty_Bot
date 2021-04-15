yr = int(input())

print("Leap" if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0) else "Ordinary")

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

h = int(position[0])
v = int(position[1])

a = map[v-1]
a[h-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
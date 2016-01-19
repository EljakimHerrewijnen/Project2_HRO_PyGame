list = ""

for i in range(0, 18):
    for y in range(0,18):
        if y >= 17:
            list += "\n"
        if y >= 0 and y <= 6 and i >= 0 and i <= 7 :
            list += " swamp " 
        elif y == 8 or y == 9 or y == 7 or i == 8 or i == 9 or i == 7:
            list += " water "
        elif y >= 10 and y <=16 and i >= 0 and i <= 7:
            list += " Ice "
        elif y >= 0 and y <= 6 and i >= 10 and i <= 16:
            list += " Desert "
        elif y >= 10 and y <= 16 and i >= 10 and i <= 16:
            list += " Forest "
print(list)

#or i >= 17
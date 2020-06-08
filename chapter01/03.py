str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str2 = str1.replace(',', '').replace('.', '').split()
str3 = []
for i in range(len(str2)):
    str3 += str(len(str2[i]))
print(str3)



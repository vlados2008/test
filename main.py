



"""

    r - read 
    w - write
    a - append

"""

# file = open("./lesson34/practice/test.txt", 'a')
# file.write("\ncar")
# file.close()

# with 

with open("./lesson34/practice/test.txt", 'a', encoding='utf-8') as file:
   file.write("\nПривет 😊")
print(file)
file.write("\naudi")



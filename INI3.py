with open("/Users/wesmacdonald/Downloads/rosalind_ini3.txt") as file:
    string = file.readline()
    abcd = file.readline()
abcd_list = abcd.split()

a = int(abcd_list[0])
b = int(abcd_list[1])
c = int(abcd_list[2])
d = int(abcd_list[3])

a_b = string[a:b+1]
c_d = string[c:d+1]
print(f"{a_b} {c_d}")

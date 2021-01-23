alphabet ='abcdefghijklmnopqrstuvwxyz'
alpha_list = list(alphabet)
print(alpha_list)
print(" ")

for char in alpha_list:
    print(char)
print(" ")

for i in range(len(alpha_list)):
    print(alpha_list[i])
print(" ")

for count, item in enumerate(alpha_list):
    print(count, item)
print(" ")

for count, item in enumerate(alpha_list, start=12):
    print(count, item)
print(" ")
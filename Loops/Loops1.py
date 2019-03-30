print("Example for The for loop..!")
# number=int(input("Enter the Number Want to Multiply: "))
#
# for i in range(1,number):
#     for j in range(1,number):
#         print("{0}*{2}---->{1}".format(i,j*i,j))
#     print("\n")

print("This is very important Logic ")
numbers="23,45,656,88,6767,88,666,53,22,"
sums=int(0);
for i in range(0,len(numbers)):
    if numbers[i] in "0123456789":
        print(numbers[i],end="")

        sums+=int(numbers[i])
        print(sums)

print(len(numbers));

print("The number divisble by 2 range 1 to 100")
for i in range(0,100,2):
    print(i)







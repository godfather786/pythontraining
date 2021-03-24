num1 = 12
num2 = 4
print(bin(num1))  #1100
print(bin(num2))  #0100
print()
num3 = num1 & num2
print(num3,bin(num3))
print()
num4 = num1 ^ num2 #1000 xoring
print(num4,bin(num4))
print()

print("number 1",num1,num2)
num1 =num1 ^ num2
num2 =num1 ^ num2
num1= num1 ^ num2
print("number 2",num1,num2)
print()
name =12
name1 =4
print(name,name1)
name = name ^ name1
name1 =name ^ name1 #not swapping

print(name,name1)

num1 =12
num5 =num1 >> 2
print(num5,bin(num5))
print()
num6 =num1 << 2
print(num6,bin(num6))
print()
data = 8
key = 2
send_data = data >> key
print("information sent ",send_data)
receiver_data = data << key
print("information received",receiver_data)
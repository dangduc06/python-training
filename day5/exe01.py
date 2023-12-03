# Nhập số nguyên n bất kỳ. Viết chương trình in các số chẵn từ 1 đến n
user_input = int(input("nhap so n: "))

number = 1

while number <= user_input:

    if number % 2 == 0:
        print(number, end=' ')

    number = number + 1
print()


print(" Task 2 -  Program Mencetak Angka ".center(50, "="))

numbers = []
while True:
    num = input("Masukkan angka (atau -1 untuk berhenti): ")
    if num == '-1':
        break
    numbers.append(float(num))
total = sum(numbers)
print(f"{total:.2f}")
print(" Task 4 -  Program Operasi Angka ".center(50, "="))

grades = []
while True:
    grade = input("Masukkan nilai (atau -1 untuk berhenti): ")
    if grade == '-1':
        break
    grades.append(int(grade)) #memasukkan inputan ke variable grades bentuk integer

average = sum(grades) // len(grades) #membuat fungsi rata-rata
print(average)
for grade in grades:
    print(grade)
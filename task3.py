class BMI_Calculator:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

print(" Task 3 -  Program BMI Calculator ".center(50, "="))

berat = float(input("Masukkan berat (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))

person = BMI_Calculator(berat, tinggi)
print("Nilai BMI:", person.BMI_Value())
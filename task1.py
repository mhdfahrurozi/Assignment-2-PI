import datetime

def print_future_date(days):
    future_date = datetime.date.today() + datetime.timedelta(days=days)
    print(future_date.strftime("%A, %B %d, %Y"))

print(" Task 1 -  Program Mencetak Tanggal ".center(50, "="))
number_of_days = int(input("Masukkan jumlah hari: "))
print_future_date(number_of_days)
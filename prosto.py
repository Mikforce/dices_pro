def print_mesac(mounth):
    if mounth <= 2 or mounth == 12:
        print("Зима")
    elif mounth < 6 and mounth > 4:
        print("Весна")
    elif mounth <= 8 and mounth >=6:
        print("Лето")
    elif mounth <= 11 and mounth >=9:
        print("Осень")
    else:
        print("Нет месяца с таким номером")


a = int(input("Месяц: "))
print_mesac(a)
b = int(input("Месяц: "))
print_mesac(b)
c = int(input("Месяц: "))
print_mesac(c)
d = int(input("Месяц: "))
print_mesac(d)
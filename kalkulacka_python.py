prodlouzit = 'y'
while prodlouzit == 'y':
    f_num = float(input("Napište první číslo>>"))
    oper = input("Napište operace>>")
    s_num = float(input("Napište druhe číslo>>"))
    if oper == '+':
        print(f_num + s_num)
    elif oper == '-':
        print(f_num - s_num)
    elif oper == '*':
        print(f_num * s_num)
    elif oper == '/':
        print(f_num / s_num)
    else:
        print("Error")
    prodlouzit = input("Stisknite na 'y', abych pokračovat, nebo jine tlačítko, abych ukončit>>")
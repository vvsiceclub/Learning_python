my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in my_list:
    i = i.split(" ")
    print("Привет, {}!".format(i[-1].title()))
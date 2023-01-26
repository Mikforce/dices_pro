block1 = 0
block2 = 1
def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из игры?"): #При попытке выхода спрашиваем хочет ли человек выйти
        root.destroy() #Если человек нажмет да, приложение закроется




def but_1():  # когда нажимается кнопка1, закрывается одно окно и создается второе с игрой
    def on_closing():
        if messagebox.askokcancel("Выход из приложения", "А тебе это нужно?"): #При нажатии на крестик задаем вопрос а нужно ли это человеку
            tk.destroy() #И если человек нажмет да, то окно закроется
    root.destroy()
    tk = Tk()
    tk.protocol("WM_DELETE_WINDOW", on_closing)
    tk.title("Игра с ботом")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=600, height=400, highlightthickness=0)
    canvas.pack() #Это мы создали второе окно собственно


    our_image = PhotoImage(file="fon2.png")  #А это фон для второго приложения
    our_image = our_image.subsample(1, 1)  # Это отвечает за уменьшение фото с одной стороны и с другой
    our_label = Label(tk)
    our_label.image = our_image
    our_label["image"] = our_label.image
    our_label.place(x=0, y=0)  # Это расположение картинки по x и y

    lab1 = Label(tk)
    lab1.place(relx=0.12, rely=0.4, anchor=CENTER) #Первая картинка куба
    lab2 = Label(tk)
    lab2.place(relx=0.32, rely=0.4, anchor=CENTER) #Вторая картинка куба
    lab3 = Label(tk)
    lab3.place(relx=0.68, rely=0.4, anchor=CENTER)  # Первый куб бота
    lab4 = Label(tk)
    lab4.place(relx=0.88, rely=0.4, anchor=CENTER)  # Второй куб бота
    lab5 = Label(tk)
    lab5.place(relx=0.5, rely=0.8, anchor=CENTER)  #Это наше лицо




    def new_game():  #Часть ответственная за смену картинок
        global b1, b2, b3, b4, kartinca, wins, loose
        if block1 == 0:
            for i in range(10):
                b1 = 1
                b2 = 1
                b3 = 1
                b4 = 1
                num1_1 = randint(1, 6)  # Мы рандомно выбираем число от 1 до 6
                num1_2 = randint(1, 6)
                num2_1 = randint(1, 6)  # Мы рандомно выбираем число от 1 до 6 уже для бота
                num2_2 = randint(1, 6)
                if num1_1 == 1:  # И тут просто присваиваем соответствующюю числу картитнку
                    b1 = PhotoImage(file="kube1.png").subsample(2, 2)
                elif num1_1 == 2:
                    b1 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num1_1 == 3:
                    b1 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num1_1 == 4:
                    b1 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num1_1 == 5:
                    b1 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num1_1 == 6:
                    b1 = PhotoImage(file="kube6.png").subsample(2, 2)

                if num1_2 == 1:  # Делаем все то же самое и со вторым кубиком
                    b2 = PhotoImage(file="kube1.png").subsample(2, 2)
                elif num1_2 == 2:
                    b2 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num1_2 == 3:
                    b2 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num1_2 == 4:
                    b2 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num1_2 == 5:
                    b2 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num1_2 == 6:
                    b2 = PhotoImage(file="kube6.png").subsample(2, 2)

                if num2_1 == 1:  # И тут делаем то же самое для бота
                    b3 = PhotoImage(file="kube1.png").subsample(2, 2)
                elif num2_1 == 2:
                    b3 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num2_1 == 3:
                    b3 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num2_1 == 4:
                    b3 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num2_1 == 5:
                    b3 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num2_1 == 6:
                    b3 = PhotoImage(file="kube6.png").subsample(2, 2)

                if num2_2 == 1:  # И второй кубик бота
                    b4 = PhotoImage(file="kube1.png").subsample(2, 2)
                elif num2_2 == 2:
                    b4 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num2_2 == 3:
                    b4 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num2_2 == 4:
                    b4 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num2_2 == 5:
                    b4 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num2_2 == 6:
                    b4 = PhotoImage(file="kube6.png").subsample(2, 2)
                lab1["image"] = b1
                lab2["image"] = b2
                lab3["image"] = b3
                lab4["image"] = b4
                time.sleep(0.12)
                tk.update()
            sum1 = num1_1 + num1_2  #Сумма чисел наших кубиковв
            sum2 = num2_1 + num2_2  #Сумма чисел кубиков бота
            if sum1 > sum2:
                kartinca = 1  #Если выиграли мы
                wins += 1
            elif sum1 < sum2:
                kartinca = 2  #Если выиграл бот
                loose += 1
            else:
                kartinca = 0  #Если ничья
            if kartinca == 1:
                kartinca = PhotoImage(file="picture3.png")  #Наше довольное лицо(потому что мы выиграли)
            elif kartinca == 2:
                kartinca = PhotoImage(file="picture2.png")  #Наше недовольное лицо(проиграли)
            elif kartinca == 0:
                kartinca = PhotoImage(file="picture4.png")  #И наше обычное лицо(ничья)
            lab5["image"] = kartinca


    Button(tk, text="Сделать бросок", comman=new_game).place(x=200, y=50) #Кнопка начала игры
    Button(tk, text="Статистика", comman=stat).place(x=320, y=50) #Кнопка статистики





def but_2():  # когда нажимается кнопка2, закрывается одно окно и создается второе с игрой
    def on_closing():
        if messagebox.askokcancel("Выход из приложения", "А тебе это нужно?"): #При нажатии на крестик задаем вопрос а нужно ли это человеку
            tk.destroy() #И если человек нажмет да, то окно закроется
    root.destroy()
    tk = Tk()
    tk.protocol("WM_DELETE_WINDOW", on_closing)
    tk.title("Игра с игроком")
    tk.resizable(0, 0)
    tk.wm_attributes("-topmost", 1)
    canvas = Canvas(tk, width=600, height=400, highlightthickness=0)
    canvas.pack() #Блок с созданием второго окна


    our_image = PhotoImage(file="fon2.png")  # А это фон для второго приложения
    our_image = our_image.subsample(1, 1)  # Это отвечает за уменьшение фото с одной стороны и с другой
    our_label = Label(tk)
    our_label.image = our_image
    our_label["image"] = our_label.image
    our_label.place(x=0, y=0)  # Это расположение картинки по x и y

    lab1 = Label(tk)
    lab1.place(relx=0.12, rely=0.4, anchor=CENTER)  # Первая картинка куба
    lab2 = Label(tk)
    lab2.place(relx=0.32, rely=0.4, anchor=CENTER)  # Вторая картинка куба
    lab3 = Label(tk)
    lab3.place(relx=0.68, rely=0.4, anchor=CENTER)  # Первый куб бота
    lab4 = Label(tk)
    lab4.place(relx=0.88, rely=0.4, anchor=CENTER)  # Второй куб бота
    lab5 = Label(tk)
    lab5.place(relx=0.22, rely=0.8, anchor=CENTER)  #Первое лицо
    lab6 = Label(tk)
    lab6.place(relx=0.78, rely=0.8, anchor=CENTER)  #Второе лицо





    def new_game():  # Действия при нажатии кнопки 1
        global b1, b2, block1, block2, sum1
        sum1 = 0
        if block1 == 0:
            for i in range(10):
                b1 = 1
                b2 = 1
                num1_1 = randint(1, 6)  #Мы рандомно выбираем число от 1 до 6
                num1_2 = randint(1, 6)
                if num1_1 == 1:   #И тут просто присваиваем соответствующюю числу картитнку
                    b1 = PhotoImage(file="kube1.png").subsample(2, 2)
                elif num1_1 == 2:
                    b1 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num1_1 == 3:
                    b1 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num1_1 == 4:
                    b1 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num1_1 == 5:
                    b1 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num1_1 == 6:
                    b1 = PhotoImage(file="kube6.png").subsample(2, 2)

                if num1_2 == 1:   #Делаем все то же самое и со вторым кубиком
                    b2 = PhotoImage(file="kube1.png").subsample(2, 2)
                elif num1_2 == 2:
                    b2 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num1_2 == 3:
                    b2 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num1_2 == 4:
                    b2 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num1_2 == 5:
                    b2 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num1_2 == 6:
                    b2 = PhotoImage(file="kube6.png").subsample(2, 2)
                lab1["image"] = b1
                lab2["image"] = b2
                time.sleep(0.12)
                tk.update()
                block1 += 1   #Блокируем первую кнопку и розблокируем вторую
                block2 = 0
            sum1 = num1_1 + num1_2   #Первая сумма чисел на кубах













    def new_game2():  # Действия при нажатии кнопки 2
        global b3, b4, block1, block2, sum1, kartinca1, kartinca2, wins1, wins2
        if block2 == 0:   #Это блокировка кнопок, чтобы они нажимались строго по очереди
            for i in range(10):   #Начинаем перебирать картинки кубов и в конце выводить конечную
                b3 = 1
                b4 = 1
                kartinca1 = 1
                kartinca2 = 1
                num2_1 = randint(1, 6)  # Мы рандомно выбираем число от 1 до 6
                num2_2 = randint(1, 6)
                if num2_1 == 1:  # И тут просто присваиваем соответствующюю числу картитнку
                    b3 = PhotoImage(file="kube1.png").subsample(2, 2) #Это всё картинки кубов
                elif num2_1 == 2:
                    b3 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num2_1 == 3:
                    b3 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num2_1 == 4:
                    b3 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num2_1 == 5:
                    b3 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num2_1 == 6:
                    b3 = PhotoImage(file="kube6.png").subsample(2, 2)

                if num2_2 == 1:  # Делаем все то же самое и со вторым кубиком
                    b4 = PhotoImage(file="kube1.png").subsample(2, 2)
                elif num2_2 == 2:
                    b4 = PhotoImage(file="kube2.png").subsample(2, 2)
                elif num2_2 == 3:
                    b4 = PhotoImage(file="kube3.png").subsample(2, 2)
                elif num2_2 == 4:
                    b4 = PhotoImage(file="kube4.png").subsample(2, 2)
                elif num2_2 == 5:
                    b4 = PhotoImage(file="kube5.png").subsample(2, 2)
                elif num2_2 == 6:
                    b4 = PhotoImage(file="kube6.png").subsample(2, 2)
                lab3["image"] = b3
                lab4["image"] = b4
                time.sleep(0.12)
                tk.update()
                block2 += 1   #Снимаем блокировку с первой кнопки и ставим на вторую
                block1 = 0
            sum2 = num2_1 + num2_2   #Вторая сумма чисел на кубах
            if sum1 > sum2:
                kartinca = 1
                wins1 += 1
            elif sum1 < sum2:
                kartinca = 2
                wins2 += 1
            else:
                kartinca = 0
            if kartinca == 1:
                kartinca1 = PhotoImage(file="picture3.png")  #Даем переменным картинка1 и картинка2 значения картинок
                kartinca2 = PhotoImage(file="picture2.png")
            elif kartinca == 2:
                kartinca1 = PhotoImage(file="picture2.png")  #Тут делаем то же самое но только другие картинки
                kartinca2 = PhotoImage(file="picture3.png")
            elif kartinca == 0:
                kartinca1 = PhotoImage(file="picture4.png")  #А тут у нас ничья
                kartinca2 = PhotoImage(file="picture4.png")
            lab5["image"] = kartinca1
            lab6["image"] = kartinca2



    Button(tk, text="Сделать бросок", comman=new_game).place(x=87, y=30)  # Кнопка начала игры
    Button(tk, text="Статистика", comman=stat2).place(x=100, y=60)  # Кнопка статистики
    Button(tk, text="Сделать бросок", comman=new_game2).place(x=425, y=30)  # Кнопка начала игры
    Button(tk, text="Статистика", comman=stat2).place(x=437, y=60)  # Кнопка статистики






from tkinter import *  # библиотека
from random import *
import time, random
from tkinter import messagebox



def stat():
    print('Побед:', wins, 'Поражений:', loose)
def stat2():
    print("Победы игрока 1:", wins1, "  Победы игрока 2:", wins2)


wins = 0
loose = 0
wins1 = 0
wins2 = 0

root = Tk()  # импортирует команды из библиотеки
root.title('Игра в кости')
root['bg'] = 'white'
root.protocol("WM_DELETE_WINDOW", on_closing)
root.resizable(0, 0)
root.iconphoto(True, PhotoImage(file=("kube6.png")))
canvas = Canvas(root, width=600, height=600, highlightthickness=0)
canvas.pack()


our_image = PhotoImage(file="fon1.png") #А это будет фон
our_image = our_image.subsample(2, 1) #Это отвечает за уменьшение фото с одной стороны и с другой
our_label = Label(root)
our_label.image = our_image
our_label["image"] = our_label.image
our_label.place(x = 0, y = 0) #Это расположение картинки по x и y


b1 = PhotoImage(file="button1.png") #Даем переменной значение картинкм
b1 = b1.subsample(2,2) #Уменьшение с обеих сторон
Button(root, image=b1, highlightthickness=0, bd=0, command=but_1).place(x=365, y=230) #Создание кнопки и ее расположение


b2 = PhotoImage(file="button2.png") #Даем переменной значение картинкм
b2 = b2.subsample(2,2) #Уменьшение с обеих сторон
Button(root, image=b2, highlightthickness=0, bd=0, command=but_2).place(x=135, y=230) #Создание кнопки и ее расположение
root.mainloop()  # Чтобы появилось окно
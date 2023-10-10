from random import randint
from time import sleep

def pc(stn):
    hod = randint(1, 3)
    if stn == 4:
        hod = 3
    elif stn == 3:
        hod = 2
    elif stn == 2:
        hod = 1
    if stn <= 1:
        print("Вы победили!")
        exit()  
    return hod
    

stn = randint(4, 30)
print("В данный момент в куче", stn, "камней")
sleep(1)
print("Вы ходите первым, вы можете взять от 1 до 3х камней")
sleep(1)

pol_stn = 0

while stn >= 1:
    print("Ваш ход, сколько камней вы возьмете?")
    try:
        pol_stn = int(input())
        if pol_stn > 3 or pol_stn < 1:
            exit()
    except:
        print("Такого действия совершить нельзя") 
        sleep(1)
        print("Теперь игра начнется заново :( ")   
        exit()
    
    print("В кучке осталось", stn - pol_stn, "камней")
    stn = stn - pol_stn
    sleep(1)
    hod_comp = pc(stn)
    print("Теперь ходит компьютер")
    sleep(1)
    print("После хода компьютера осталось", stn - hod_comp, "камней")
    sleep(1)
    stn = stn - hod_comp
    if stn == 1:
        print("Победил компьютер(удивительно)")
        break



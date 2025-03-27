#esimene modul
def arithmetic(arv1:float,arv2:float,tehe:str):
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    kui sisend ei ole järjendis[+,-,/,*], siis tagastab sõne "tundmatu tehe"
    :param float arv1: sisesnd ujukomaavru tüübina
    :param float arv2: sisesnd ujukomaavru tüübina
    :param str tehe: Sisend listist [+,-,/,*]
    :rtype: varmääramata tüüp (float või str)
    """
    if tehe in ["+","-","/","*"]:
        if arv2==0 and tehe=="/":
            vastus="DEV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="tundmatu tehe"
    return vastus
#teine modul
from teema5_kasutajate_fun import *

a=float(input("arv1:"))
b=float(input("arv2:"))
t=input("tehe:")
vastus=arithmetic(a,b,t)
print(vastus)
#2
def is_year_leap(aasta:int)->bool:
    if aasta%4==0:
        v=True
    else:
        v=False
    return v
#3
def square(külg,float)->any:
    S=külg**2
    P=4*külg
    d=(2)**(1/2)*külg
    return S,P,d
#4
def season(param:int)->str:
    if param in [1,2,12]:
        H="talv"
    elif param in [3,4,5]:
        H="kevad"
    elif param in [6,7,8]:
        H="suvi"
    else:
        H="sügis"
    return H
#5
def bank(summa:float, aastad:int)->float:
    """kirjeldage funktsioon
    param...
    param...
    rtype:...hooajanimetus
    """
    for aasta in range(aasta):
        summa*=1.1
    return summa
from random import *
#6
def is_prime(a=randint(1,10000))->bool:
    print(a)
    v=True
    for jagaja in range(2,a):
        if a%jagaja==0:
            v=False
    return v
#7
def date(päev:int,kuu:int,aasta:int)->bool:
    if päev in range(1,32) and kuu in[1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and not is_year_leap(aasta):
        v=True
    if päev in range(1,31) and kuu in[4,6,9,11] and aasta>0:
        v=True
    else:
        False
    return v

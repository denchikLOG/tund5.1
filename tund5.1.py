#esimene modul
def arithmetic(arv1:float,arv2:float,tehe:str):
    """Funktsioon t��tab nagu lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    kui sisend ei ole j�rjendis[+,-,/,*], siis tagastab s�ne "tundmatu tehe"
    :param float arv1: sisesnd ujukomaavru t��bina
    :param float arv2: sisesnd ujukomaavru t��bina
    :param str tehe: Sisend listist [+,-,/,*]
    :rtype: varm��ramata t��p (float v�i str)
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

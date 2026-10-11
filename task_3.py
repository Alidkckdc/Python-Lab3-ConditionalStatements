a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
set_1='1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16'
print(set_1)
answer=int(input('Is your birthday in set_1, yes=1 no=0:'))
if answer==1:
    for i in range(17,32):
        a.remove(i)
    set_2='1,2,3,4,5,6,7,8'
    print(set_2)
    answer=int(input('Is your birthday in set_2, yes=1 no=0:'))
    if answer==1:
        for l in range(9,17):
            a.remove(l)
        set_3='1,2,3,4'
        print(set_3)
        answer=int(input('Is your birthday in set_3, yes=1 no=0:'))
        if answer==1:
            for m in range(5,9):
                a.remove(m)
            set_4='1,2'
            print(set_4)
            answer=int(input('Is your birthday in set_4, yes=1 no=0:'))
            if answer==1:
                a.remove(3)
                a.remove(4)
                set_5='1'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(2)
                else:
                    a.remove(1)
            else:
                a.remove(1)
                a.remove(2)
                set_5='3'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(4)
                else:
                    a.remove(3)
        else:
            for m in range(1,5):
                a.remove(m)
            set_4='5,6'
            print(set_4)
            answer=int(input('Is your birthday in set_4, yes=1 no=0:'))
            if answer==1:
                a.remove(7)
                a.remove(8)
                set_5='5'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(6)
                else:
                    a.remove(5)
            else:
                a.remove(6)
                a.remove(5)
                set_5='7'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(8)
                else:
                    a.remove(7)
    else:
        for l in range(1,9):
            a.remove(l)
        set_3='9,10,11,12'
        print(set_3)
        answer=int(input('Is your birthday in set_3, yes=1 no=0:'))
        if answer==1:
            for l in range(13,17):
                a.remove(l)
            set_4='9,10'
            print(set_4)
            answer=int(input('Is your birthday in set_4, yes=1 no=0:'))
            if answer==1:
                a.remove(11)
                a.remove(12)
                set_5='9'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(10)
                else:
                    a.remove(9)
            else:
                a.remove(9)
                a.remove(10)
                set_5='11'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(12)
                else:
                    a.remove(11)
        else:
            for l in range(9,13):
                a.remove(l)
            set_3='13,14,15,16'
            print(set_3)
            answer=int(input('Is your birthday in set_3, yes=1 no=0:'))
            if answer==1:
                for p in range(9,13):
                    a.remove(p)
                set_4='13,14'
                print(set_4)
                answer=int(input('Is your birthday in this set_4, yes=1 no=0:'))
                if answer==1:
                    a.remove(15)
                    a.remove(16)
                    set_5='15'
                    print(set_5)
                    answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                    if answer==1:
                        a.remove(16)
                    else:
                        a.remove(15)
                else:
                    a.remove(13)
                    a.remove(14)
                    set_5='13'
                    print(set_5)
                    answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                    if answer==1:
                        a.remove(14)
                    else:
                        a.remove(13)
else:
    for i in range(1,17):
        a.remove(i)
    set_2='17,18,19,20,21,22,23,24'
    print(set_2)
    answer=int(input('Is your birthday in set_2, yes=1 no=0:'))
    if answer==1:
        for y in range(25,32):
            a.remove(y)
        set_3='17,18,19,20'
        print(set_3)
        answer=int(input('Is your birthday in set_3, yes=1 no=0:'))
        if answer==1:
            for z in range(21,25):
                a.remove(z)
            set_4='17,18'
            print(set_4)
            answer=int(input('Is your birthday in set_4, yes=1 no=0:'))
            if answer==1:
                a.remove(19)
                a.remove(20)
                set_5='17'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(18)
                else:
                    a.remove(17)
            else:
                a.remove(17)
                a.remove(18)
                set_5='19'
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(20)
                else:
                    a.remove(19)
    else:
        for y in range(17,25):
            a.remove(y)
        set_3='25,26,27,28'
        print(set_3)
        answer=int(input('Is your birthday in set_3, yes=1 no=0:'))
        if answer==1:
            for j in range(29,32):
                a.remove(j)
            set_4='25,26'
            print(set_4)
            answer=int(input('Is your birthday in set_4, yes=1 no=0:'))
            if answer==1:
                a.remove(27)
                a.remove(28)
                set_5='25'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(26)
                else:
                    a.remove(25)
            else:
                a.remove(25)
                a.remove(26)
                set_5='27'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:')) 
                if answer==1:
                    a.remove(28)
                else:
                    a.remove(27)
        else:
            for j in range(25,29):
                a.remove(j)
            set_4='29,30'
            print(set_4)
            answer=int(input('Is your birthday in set_4, yes=1 no=0:'))
            if answer==1:
                a.remove(31)
                set_5='29'
                print(set_5)
                answer=int(input('Is your birthday in set_5, yes=1 no=0:'))
                if answer==1:
                    a.remove(30)
                else:
                    a.remove(29)
            else:
                a.remove(29)
                a.remove(30)
final=a[0]
print(f'Your birthday is {final}')
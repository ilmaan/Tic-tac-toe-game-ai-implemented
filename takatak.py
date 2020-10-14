print("++++++++++++++ WELCOME TO TIC TAK TOE ++++++++++++++")
print("^^^^^^^^^^^^ A-I DESIGNED ^^^^^^^^^^^^")


brd = [' ' for x in range(10)]

def insrtltr(letter,pos):
    brd[pos] = letter

def frespc(pos):
    return brd[pos] == ' '





def prinbrd(brd):
    print("++++++++++++++++")

    print("|" + brd[1] + "|" + brd[2] + "|" + brd[3] + "|" )
    
    print("_________________")

    print("|" + brd[4] + "|" + brd[5] + "|" + brd[6] + "|" )
    
    print("________________")

    print("|" + brd[7] + "|" + brd[8] + "|" + brd[9] + "|" )

    print("++++++++++++++")



def brdfull(brd):
    if brd.count(' ') >1:
        return False
    else:
        return True

def winr(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
     (b[4] == l and b[5] == l and b[6] == l) or 
     (b[7] == l and b[8] == l and b[9] == l) or 
     (b[1] == l and b[4] == l and b[7] == l) or 
     (b[2] == l and b[5] == l and b[8] == l) or 
     (b[3] == l and b[6] == l and b[9] == l) or 
     (b[1] == l and b[5] == l and b[9] == l) or 
     (b[3] == l and b[5] == l and b[7] == l))
            



def plmove():
    rn = True
    while rn:
        mv = input("**** SELECT A POSITION FROM 1-9 **** >: ")
        try:
            mv =int(mv)
            if mv>0 and mv<10:
                if frespc(mv):
                    rn = False
                    insrtltr('X' , mv)
                
                else:
                    print("")    

            else:
                print("ENTER IN CORRECT POSITION YOU DAMMIT :")

        except:
            print("PLEASE ENTER A NUMBER DAMN : ")

def cpmove():
    psblmv =[x for x , letter in enumerate(brd) if letter == ' ' and x!=0 ]
    mv = 0
     
    for let in ['O' , 'X']:
        for i in psblmv:
            brdcpy = brd[:]
            brdcpy[i] = let
            if winr(brdcpy, let):
                mv = i
                return mv
        

    crnrop = []
    for i in psblmv:
        if i in [1,3,7,9]:
            crnrop.append(i)

    if len(crnrop)>0:
        slctrndm(crnrop)
        return mv

    if 5 in psblmv:
        mv = 5
        return mv

    edgop = []
    for i in psblmv:
        if i in [2,4,6,8]:
            edgop.append(i)

    if len(edgop)>0:
        slctrndm(edgop)
        return mv

def slctrndm(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li(r)



def main():
    print("ZORAVAR")
    prinbrd(brd)

    while not(brdfull(brd)):
        if not(winr(brd , 'O')):
            plmove()
            prinbrd(brd)
        else:
            print("HAHAHAHAHA YOU ARE A LOOSER")
        if brdfull(brd):
            print("YOU DIDNT WIN NOR YOU LOOSE #LOOSER")
            break
        
        


    if not(winr(brd , 'X')):
        mv = cpmove()
        if mv == 0:
            print("YOU DIDNT WIN NOR YOU LOOSE #CHOOSER") 

        else:
            insrtltr('O' , mv)
            print("AI PLAYED ITS CHANCE ON POSITION ", mv,"::")
            prinbrd(brd)

    else:
        print("HOW THE HELL YOU WON AGAINST THE AI DAMN YOU JARVIS")


while True:
    x = input("WANT TO PLAY AND LOOSE AGAIN ????PRESS Y FOR YES N FOR NO : ")
    if x.lower() == 'y':
        brd = [' ' for x in range(10)]
        print("_______________")
        main()
        
    else:
        break    



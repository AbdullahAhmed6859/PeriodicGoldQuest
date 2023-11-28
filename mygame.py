import pygame   
import random
pygame.init()   #to import and initialise pygame
scrn=pygame.display.set_mode((1254,650))  #setting the screen
scrn.fill((pygame.Color("antiquewhite")))
pygame.display.set_caption("Periodic Gold Quest")     #title
x1=5+68+68+68+68
y1=5+68
x2=5+68+68+68+68+68
y2=5+68  #coordinates of character1
width=60
height=60     #dimentions of character1
vel=68     #velocity of character
run=True        #while exit not true
player1img=pygame.image.load("superhero (2).png")   #images of both players
player1img = pygame.transform.scale(player1img, (width, height)) #changing image size
player2img=pygame.image.load("superhero (3).png")
player2img = pygame.transform.scale(player2img, (width, height))
def player1():      #showing character on scrn
    scrn.blit(player1img, (x1,y1))         #blit is used to draw anything on window parameters: obj and cordinates
def player2():
    scrn.blit(player2img, (x2,y2))
def radioactive():
    pygame.draw.line(scrn, (pygame.Color("lightsteelblue4")),(209,345),(209,413+68),7)
def drawhome():
    xh=210
    yh=15
    pygame.draw.rect(scrn,(pygame.Color("darkseagreen2")),(xh,yh,72*4,77*2))
    font= pygame.font.Font("freesansbold.ttf", 38)
    head=font.render("HOME", True, (pygame.Color("darkseagreen3")))
    scrn.blit(head, (xh+(72),yh+3))
    font2= pygame.font.Font("freesansbold.ttf", 18)
    ins=font2.render("Hold on to 'i' for instructions", True, (pygame.Color("goldenrod3")))
    scrn.blit(ins, (821,5))

def instructions():
    font= pygame.font.Font("freesansbold.ttf", 20)
    scrn.fill((pygame.Color("antiquewhite")))
    pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod1")),(141,73,34,34))
    pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(141,73,34,34),1)
    i1=font.render("grp1 and grp7 elements reacting and ending at colored positions", True, (pygame.Color("azure4")))
    scrn.blit(i1, (270,73))
    pygame.draw.rect(scrn,(pygame.Color("pink2")),(141,113,34,34))
    pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(141,113,34,34),1)
    i2=font.render("grp2 and grp6 elements reacting and ending at colored positions", True, (pygame.Color("azure4")))
    scrn.blit(i2, (270,113))
    pygame.draw.rect(scrn,(pygame.Color("indianred2")),(141,153,34,34))
    pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(141,153,34,34),1)
    i3=font.render("poisonous elements return player to home", True, (pygame.Color("azure4")))
    scrn.blit(i3, (270,153))
    pygame.draw.rect(scrn,(pygame.Color("lightsteelblue3")),(141,193,34,34))
    pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(141,193,34,34),1)
    i4=font.render("radioactive elements attack opponent", True, (pygame.Color("azure4")))
    scrn.blit(i4, (270,193))
    pygame.draw.rect(scrn,(pygame.Color("cyan2")),(141,233,34,34))
    pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(141,233,34,34),1)
    i5=font.render("shield protects from attack of opponent", True, (pygame.Color("azure4")))
    scrn.blit(i5, (270,233))
    pygame.draw.rect(scrn,(pygame.Color("darkgoldenrod")),(141,273,34,34))
    pygame.draw.rect(scrn,(pygame.Color("gold1")),(141,273,34,34),3)
    i6=font.render("player wins when it reaches Gold(Au)", True, (pygame.Color("azure4")))
    scrn.blit(i6, (270,273))



def drawboard():        #drawing periodic table and color coding
    rows=9
    column=18
    x_co=5
    y_co=5
    atomicnum=1
    elements={}     #elements dictionary
    element_symbols="H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn, Fr, Ra, Ac, Th, Pa, U, Np, Pu, Am, Cm, Bk, Cf, Es, Fm, Md, No, Lr, Rf, Db, Sg, Bh, Hs, Mt, Ds, Rg, Cn, Nh, Fl, Mc, Lv, Ts, Og".split(", ")
    for x in range(len(element_symbols)):
        elements[x+1]=element_symbols[x]
    font= pygame.font.Font("freesansbold.ttf", 38)
    font2= pygame.font.Font("freesansbold.ttf", 20)
    for x in range(rows):
        for y in range(column):
            if x==0 and y>0 and y<17:
                pass
            elif x in (1,2) and y>1 and y<12:
                pass
            elif x in (7,8) and y<4:
                pass
            elif (y in (0,16) and x<7) or (x==4 and y==9) or (x==8 and y==9):
                pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod1")),(x_co,y_co,68,68))
                pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(x_co,y_co,68,68),1)
                element=font.render(elements[atomicnum], True, (pygame.Color("lightgoldenrod3")))
                scrn.blit(element, (x_co+10,y_co+30))
                num=font2.render(str(atomicnum), True, (pygame.Color("azure4")))
                scrn.blit(num, (x_co,y_co))
                atomicnum+=1
            elif (y in (1,15) and x<7) or (x==4 and y==4) or (x==6 and y==5):
                pygame.draw.rect(scrn,(pygame.Color("pink2")),(x_co,y_co,68,68))
                pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(x_co,y_co,68,68),1)
                element=font.render(elements[atomicnum], True, (pygame.Color("pink3")))
                scrn.blit(element, (x_co+10,y_co+30))
                num=font2.render(str(atomicnum), True, (pygame.Color("azure4")))
                scrn.blit(num, (x_co,y_co))
                atomicnum+=1
            elif y==10 and x==5:
                pygame.draw.rect(scrn,(pygame.Color("darkgoldenrod")),(x_co-1,y_co,69,68))
                pygame.draw.rect(scrn,(pygame.Color("gold1")),(x_co,y_co,68,68),3)
                element=font.render(elements[atomicnum], True, (pygame.Color("gold1")))
                scrn.blit(element, (x_co+10,y_co+30))
                num=font2.render(str(atomicnum), True, (pygame.Color("azure4")))
                scrn.blit(num, (x_co,y_co))
                atomicnum+=1
            elif (x in (4,5) and y==11) or (x==3 and y==14) or (x==3 and y in (6,8)) or (x==5 and y==12) or (x==4 and y==13) or (x==6 and y==3):
                pygame.draw.rect(scrn,(pygame.Color("indianred2")),(x_co,y_co,68,68))
                pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(x_co,y_co,68,68),1)
                element=font.render(elements[atomicnum], True, (pygame.Color("indianred3")))
                scrn.blit(element, (x_co+10,y_co+30))
                num=font2.render(str(atomicnum), True, (pygame.Color("azure4")))
                scrn.blit(num, (x_co,y_co))
                atomicnum+=1
            elif (x==3 and y in (3,4,5,7)) or (x==1 and y==13) or (x==4 and y==3) or (x==5 and y in (4,5,7,9,13)):
                pygame.draw.rect(scrn,(pygame.Color("cyan2")),(x_co,y_co,68,68))
                pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(x_co,y_co,68,68),1)
                element=font.render(elements[atomicnum], True, (pygame.Color("cyan3")))
                scrn.blit(element, (x_co+10,y_co+30))
                num=font2.render(str(atomicnum), True, (pygame.Color("azure4")))
                scrn.blit(num, (x_co,y_co))
                atomicnum+=1
            elif x>6:
                pygame.draw.rect(scrn,(pygame.Color("lightsteelblue3")),(x_co,y_co,68,68))
                pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(x_co,y_co,68,68),1)
                element=font.render(elements[atomicnum], True, (pygame.Color("lightsteelblue4")))
                scrn.blit(element, (x_co+10,y_co+30))
                num=font2.render(str(atomicnum), True, (pygame.Color("azure4")))
                scrn.blit(num, (x_co,y_co))
                atomicnum+=1
            else:
                pygame.draw.rect(scrn,(pygame.Color("lightgoldenrod4")),(x_co,y_co,68,68),1)
                element=font.render(elements[atomicnum], True, (pygame.Color("antiquewhite3")))
                scrn.blit(element, (x_co+10,y_co+30))
                num=font2.render(str(atomicnum), True, (pygame.Color("azure4")))
                scrn.blit(num, (x_co,y_co))
                atomicnum+=1
            if x==5 and y==2:
                atomicnum=72
            elif x==6 and y==2:
                atomicnum=104
            elif x==7 and y==3:
                atomicnum=58
            elif x==8 and y==3:
                atomicnum=90
            
            x_co+=68
        y_co+=68
        x_co=5


def dice_simulation(num):
    h,w=150,150
    x=7
    y=490
    images=["dice.1.png","dice.2.png","dice.3.png","dice.4.png","dice.5.png","dice.6.png"]
    diceimg=pygame.image.load(images[num-1])   #images of both players
    diceimg = pygame.transform.scale(diceimg, (h, w))
    scrn.blit(diceimg, (x,y))

def gamewin():      #main game window with all display helper functions
    scrn.fill((pygame.Color("antiquewhite")))       #to hide previous traces with black colour(bg) 
    drawboard()
    drawhome()
    player1()
    player2()
    radioactive()
    dice_simulation(num)

def views(view):
    if view=="i":
        instructions()
    if view=="g":
        gamewin()
turn=0    
while run:
    
    pygame.time.delay(100)     #timeclock alternative
    for event in pygame.event.get():   #all inputs from user are events
        if event.type==pygame.QUIT:
            run=False             #for quitting the game
        view="g"
        keys=pygame.key.get_pressed()   
        num=random.randint(1,6)
        if keys[pygame.K_LEFT] and x1>vel and turn%2==0:     #changing coordinates with key press
            x1-=vel*num                 #conditions to handle moving out of scrn(coordinates from top left)
            turn+=1
        elif keys[pygame.K_RIGHT] and x1<1254-width-vel and turn%2==0:
            x1+=vel*num
            turn+=1
        elif keys[pygame.K_UP] and y1>vel and turn%2==0:
            y1-=vel*num
            turn+=1
        elif keys[pygame.K_DOWN] and y1<650-height-vel and turn%2==0:          #for changing position on arrow key presses
            y1+=vel*num
            turn+=1
        elif keys[pygame.K_LEFT] and x2>vel and turn%2!=0:     #changing coordinates with key press
            x2-=vel*num
            turn+=1                  #conditions to handle moving out of scrn(coordinates from top left)
        elif keys[pygame.K_RIGHT] and x2<1254-width-vel and turn%2!=0:
            x2+=vel*num
            turn+=1
        elif keys[pygame.K_UP] and y2>vel and turn%2!=0:
            y2-=vel*num
            turn+=1
        elif keys[pygame.K_DOWN] and y2<650-height-vel and turn%2!=0:          #for changing position on arrow key presses
            y2+=vel*num
            turn+=1
        elif keys[pygame.K_i]:
            view="i"

        views(view)
                
        
               
        

        pygame.display.update()     #to update changes on screen
        turn+=1


    

pygame.quit()

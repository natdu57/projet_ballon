
import  pygame
import time
from random import*


blue = (113,177,227) #valeur max =255.
white = (255,255,255)

pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66
nuageW = 300
nuageH = 300


surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Ballon Volant")
clock = pygame.time.Clock()


img = pygame.image.load('Ballon01.png')
img_nuage01 = pygame.image.load('NuageHaut.png')
img_nuage02 = pygame.image.load('NuageBas.png')

def score(compte) :
    police = pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("score : " + str(compte), True, white)
    surface.blit(texte, [10,0])

def nuages(x_nuage, y_nuage, espace):
    surface.blit(img_nuage01, (x_nuage, y_nuage))
    surface.blit(img_nuage02,(x_nuage,y_nuage+ nuageH +espace))


def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type ==pygame.KEYUP:
            continue
        return event.key

    return  None

def creaTexteObjs (texte, font):
    texteSurface = font.render(texte,True,white)
    return texteSurface, texteSurface.get_rect()


def msgSurface (texte):
    GOTexte = pygame.font.Font('BradBunR.ttf', 150)
    petitTexte = pygame.font.Font('BradBunR.ttf',20)

    titreTexteSurf, titreTexteRect = creaTexteObjs(texte, GOTexte)
    titreTexteRect.center = surfaceW/2,((surfaceH/2)-50)
    surface.blit(titreTexteSurf, titreTexteRect)

    petitTexteSurf, petitTexteRect = creaTexteObjs\
        ("appuyer sur une touche pour continuer", petitTexte )
    petitTexteRect.center = surfaceW/2, ((surfaceH/2) +50)
    surface.blit(petitTexteSurf, petitTexteRect)

    pygame.display.update()
    time.sleep(2)

    while rejoueOuQuitte() == None :
        clock.tick()

    main()

def gameOver():
    msgSurface("Boom!")

def ballon(x,y, image):
    surface.blit(image, (x,y))

def main():
    x=150
    y=200
    y_move=0

    x_nuage = surfaceW
    y_nuage = randint(-300,10)
    espace = ballonH*3
    nuage_vitesse = 3

    score_actuel = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -1
            if event.type ==pygame.KEYUP :
                y_move = 1

        y += y_move

        surface.fill(blue)
        ballon(x,y,img)

        nuages(x_nuage,y_nuage, espace)

        score(score_actuel)

        x_nuage -=nuage_vitesse


        if y>surfaceH -40 or y <-10:
            gameOver()

        if x_nuage < (-1*nuageW):
            x_nuage = surfaceW
            y_nuage = randint(-300,10)

            if 3 <= score_actuel < 5:
                nuage_vitesse = 4
                espace = ballonH*2.8
            if 7 <= score_actuel < 8 :
                nuage_vitesse = 5
                espace = ballonH*2.7
            if 8 <= score_actuel < 10 :
                nuage_vitesse = 6
                espace = ballonH*2.5
            if 10 <= score_actuel <22:
                nuage_vitesse = 8
                espace = ballonH*2.2
            if 22 <= score_actuel:
                nuage_vitesse = 10
                espace = ballonH*2



        if x +ballonW > x_nuage + 40 :
            if y < y_nuage + nuageH  -50:
                if x - ballonW < x_nuage +nuageW -20 :
                    #print("touche haut!!!")
                    gameOver()

        if x +ballonW >x_nuage + 40 :
            if y +ballonH > y_nuage + nuageH + espace +50 :
                if x -ballonW < x_nuage+ nuageW - 20:
                    #print("touche bas!!!")
                    gameOver()

        if x_nuage < (x-nuageW)<x_nuage+nuage_vitesse :
            score_actuel +=1

        pygame.display.update()



main()
pygame.quit()
quit()
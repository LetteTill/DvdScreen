from random import *

wrong = False
wrongy = False

alien = Actor('alien')
alien.topright = 0, 10

WIDTH = 650
HEIGHT = 500



def draw():
    screen.clear()
    alien.draw()
    
def update():
    global wrong
    global wrongy
    #print(wrong)
    if wrong == False:
        alien.x += 2
    elif wrong ==True:
        alien.x -= 2
    if wrongy == False:
        alien.y += 2
    elif wrongy ==True:
        alien.y -= 2
    
        
    #alien.y += randint(2,10)
    if alien.left >= WIDTH - alien.width:
        wrong = True
        alien.x
    if alien.left <= 0:
        wrong = False
    if alien.bottom >= HEIGHT:
        wrongy = True
        alien.y
    if alien.top <= 0 :
        wrongy = False
   # if alien.y > HEIGHT:
      #  alien.y = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)


def set_alien_normal():
    alien.image = 'alien'
    

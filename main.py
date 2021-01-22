# Tutorial: https://pygame-zero.readthedocs.io/en/stable/introduction.html

alien = Actor('alien')
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
    screen.clear()
    alien.draw()

alien.topright = 0, 10

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("Ow!")
    else:
        print("LMAO")     

def on_mouse_down(pos):
    if alien.collidepoint(pos):
      print("OW!")
      set_alien_hurt()
    else:
       print("LMAO")  

def set_alien_hurt():
    alien.image = 'alien_hurt'
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien' 
      
               
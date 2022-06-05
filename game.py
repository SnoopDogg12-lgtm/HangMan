import pygame
import sys

# wwindow properties
WINDOW_SIZE = (700,700)
SCREEN = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("HangMan")
picture = pygame.image.load("background.jpg")
background = pygame.transform.scale(picture, (700, 700))
RED=(255,0,0)
BLACK = (0,0,0)

pygame.init()
pygame.font.init()

game_font = pygame.font.SysFont('arial', 30)
game_font_2 = pygame.font.SysFont('Comic Sans', 30)
menu_font = pygame.font.SysFont('papyrus', 50)
menu_font_2 = pygame.font.SysFont('perpetua', 50)
number_of_spaces = 8

#properties for the spaces
x=20
y=300
width = 25
height = 5
thickness = 10

spaces = []
letters = []
guessed_letters = []
user_input = ""
letter = "apple"
letter_lenght = len(letter)


#print(pygame.font.get_fonts())

class Game:
   def __init__(self) -> None:
       self.attempts = 0
       self.attempts_array = []

   def draw_spaces(self):
      for i in range(len(letter)):
         #pygame.draw.line(SCREEN, RED, (70 + i * 40, 80 + i * 40), (150 + i * 40, 80 + i * 40))
         rex = pygame.draw.rect(SCREEN, BLACK, (x + i * 30,y,width,height))
         spaces.append(rex)

   def draw_text(self,user_input,x,y):
      textsurface = game_font.render(user_input, False, (BLACK))
      SCREEN.blit(textsurface,(x + 3,y - 30))

   def handle_input(self):
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
               user_input = "a"
            if event.key == pygame.K_b:
               user_input = "b"
            if event.key == pygame.K_c:
               user_input = "c"
            if event.key == pygame.K_d:
               user_input = "d"
            if event.key == pygame.K_e:
               user_input = "e"
            if event.key == pygame.K_f:
               user_input = "f"
            if event.key == pygame.K_g:
               user_input = "g"
            if event.key == pygame.K_h:
               user_input = "h"
            if event.key == pygame.K_i:
               user_input = "i"
            if event.key == pygame.K_j:
               user_input = "j"
            if event.key == pygame.K_k:
               user_input = "k"
            if event.key == pygame.K_l:
               user_input = "l"
            if event.key == pygame.K_m:
               user_input = "m"
            if event.key == pygame.K_n:
               user_input = "n"
            if event.key == pygame.K_o:
               user_input = "o"
            if event.key == pygame.K_p:
               user_input = "p"
            if event.key == pygame.K_q:
               user_input = "q"
            if event.key == pygame.K_r:
               user_input = "r"
            if event.key == pygame.K_s:
               user_input = "s"
            if event.key == pygame.K_t:
               user_input = "t"
            if event.key == pygame.K_u:
               user_input = "u"
            if event.key == pygame.K_v:
               user_input = "v"
            if event.key == pygame.K_w:
               user_input = "w"
            if event.key == pygame.K_x:
               user_input = "x"
            if event.key == pygame.K_y:
               user_input = "y"
            if event.key == pygame.K_z:
               user_input = "z"
            if user_input in letter:
                print("yes")
                letter_index = letter.index(user_input)
                #here we even check if the same letter occurs more than once
                for letter_index in (idx for idx,l in enumerate(letter) if l==user_input):
                    self.draw_text(user_input, spaces[letter_index].x, spaces[letter_index].y)
                    guessed_letters.append(user_input)
            elif user_input not in letter:
               self.attempts += 1
            if len(guessed_letters) == letter_lenght:
               print("yea") 

   def main_loop(self):
    SCREEN.blit(background, (0, 0))
    running = True
    while running:
        textsurface = game_font_2.render("Guess a letter by pressing a key on the keyboard", False, (BLACK))
        SCREEN.blit(textsurface,(90,600))
        self.draw_spaces()
        self.handle_input()
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        pygame.display.update()

class Menu:
   def __init__(self) -> None:
       pass
      
   def menu_screen(self):
         running = True
         while running:
            SCREEN.fill((0,250,100))
            textsurface = menu_font.render("Hang Man", False, (255, 255, 255))
            textsurface2 = menu_font_2.render("Press P to play", False, (255, 255, 255))
            SCREEN.blit(textsurface,(220,210))
            SCREEN.blit(textsurface2,(210,310))
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
                  if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_p:
                        Game().main_loop()
            pygame.display.flip()
            pygame.display.update()


menu = Menu()
menu.menu_screen()
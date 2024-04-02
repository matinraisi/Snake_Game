from tkinter import *
from random import randint
import os
import sys
# ----------------------------------------------
class Snake:
    def __init__(self) :
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squeers  =[]
            
        for i in range(0,BODY_SIZE):
            self.coordinates.append([0,0])
        for x , y in self.coordinates:
            squre = convas.create_rectangle(x,y, x + SPASE_SIZE , y+SPASE_SIZE , fill=SNAKE_COLOR , tag="snake" )
            self.squeers.append(squre)

class Food:
    def __init__(self):
        x = randint(0 , (GAME_WIDTH // SPASE_SIZE) - 1) * SPASE_SIZE
        y = randint(0 , (GAME_HEIGHT // SPASE_SIZE) - 1) * SPASE_SIZE
        self.coordinates = [x,y]
        convas.create_rectangle(x,y, x + SPASE_SIZE , y + SPASE_SIZE , fill=FOOD_COLOR , tag="food" )
        

def next_turn(snake , food):
    x , y = snake.coordinates[0]

    if direction == "up":
        y -= SPASE_SIZE
    elif direction == "down":
        y += SPASE_SIZE
    elif direction == "left":
        x -= SPASE_SIZE
    elif direction == "right":
        x += SPASE_SIZE
    
    snake.coordinates.insert(0, [x , y])
    print(snake.coordinates)
    square = convas.create_rectangle(x ,y , x + SPASE_SIZE , y + SPASE_SIZE , fill=SNAKE_COLOR)
    snake.squeers.insert(0 , square)
    
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        lable.config(text=f"score: {score}")
        convas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        convas.delete(snake.squeers[-1])
        del snake.squeers[-1]
        
    if check_game_over(snake):
        game_over()
    else:
        window.after(SLOWNESS , next_turn , snake , food) 
    
def change_direction(new_dir):
    global direction
    
    if new_dir == "left":
        if direction != "right":
            direction = new_dir
    elif new_dir == "right":
        if direction != "left":
            direction = new_dir
    elif new_dir == "up":
        if direction != "down":
            direction = new_dir
    elif new_dir == "down":
        if direction != "up":
            direction = new_dir


def check_game_over(snake):
    x , y = snake.coordinates[0]
    
    if x < 0 or x > GAME_WIDTH:
        return True
    if y < 0 or y > GAME_HEIGHT:
        return True
    
    for sar in snake.coordinates[1:]:
        if x == sar[0] and y == sar[1]:
            return True
        
    return False

def game_over():
    # pass
    convas.delete(ALL)
    convas.create_text(convas.winfo_width() / 2 , convas.winfo_height() / 2  ,font=("Terminal"  , 80) ,  text="GAME OVER ^_~" , fill="red" , tag="gameover")
    

def restar_program():
    path = sys.executable
    os.execl(path , path , *sys.argv)
# ----------------------------------------------
# ==============================================
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPASE_SIZE = 25
SLOWNESS = 200
BODY_SIZE = 2
SNAKE_COLOR = "YELLOW"
FOOD_COLOR = 'RED'
BG_COLOR = "black"
score = 0
direction = 'down' 
# ==============================================
window = Tk()
window.title("Snake Game")
window.resizable(False,False)

lable = Label(window , text=f"Score : {score}" , font=("Roman", 30))
lable.pack()

convas = Canvas(window , bg=BG_COLOR , height=GAME_HEIGHT , width=GAME_WIDTH )
convas.pack()


BtnRestar = Button(window , text="restart" , fg='red' , command=restar_program)
BtnRestar.pack()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x =int((screen_width / 2) - (window_width / 2))
y =int((screen_height / 2) - (window_height / 2))
# print(x,y)
# window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind("<Left>" , lambda event:change_direction("left"))
window.bind("<Right>", lambda event:change_direction("right"))
window.bind("<Up>", lambda event:change_direction("up"))
window.bind("<Down>", lambda event:change_direction("down"))



snake = Snake()
food = Food()
next_turn(snake , food)
window.mainloop()
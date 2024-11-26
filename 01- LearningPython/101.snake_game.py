# Made by Nevoada
# Inspired by : Cjyyaotse (Snake code) and BroCode.

# Import the necessary modules.
from tkinter import *
import random

# Constants.
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
BACKGROUND_COLOR = "#000000"  # Dark Black.
SPEED = 225  # The lower the number, the faster the game is.
BODY_PARTS = 3
SCORE = 0
SPACE_SIZE = 25  # Square area.
DIRECTION = "down"
SNAKE_COLOR = "Orange"
FOOD_COLOR = "Red"


# Define the Snake class.
class Snake:

    # Calling the constructor for our Snake.
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        # Initialize snake coordinates.
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Create snake squares on the canvas.
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)


# Define the Food class.
class Food:

    # Generating random coordinates for the food.
    def __init__(self):
        x = random.randint(0, int((WINDOW_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE
        y = random.randint(0, int((WINDOW_HEIGHT / SPACE_SIZE) - 1)) * SPACE_SIZE

        self.coordinates = [x, y]

        # Create food oval on the canvas.
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags="food")


# Define the main game loop function.
def next_turn(snake, food):
    x_snake, y_snake = snake.coordinates[0]  # Head coordinates.

    # Moving the snake.
    if DIRECTION == "up":
        y_snake -= SPACE_SIZE

    elif DIRECTION == "down":
        y_snake += SPACE_SIZE

    elif DIRECTION == "left":
        x_snake -= SPACE_SIZE

    elif DIRECTION == "right":
        x_snake += SPACE_SIZE

    # Updating the coordinates of our snake, forward.
    snake.coordinates.insert(0, (x_snake, y_snake))  # HERE # 0 = The head / Insert new x_snake and y in this new
    # location.

    # Updating the canvas of our snake, forward.
    square = canvas.create_rectangle(x_snake, y_snake, x_snake + SPACE_SIZE, y_snake + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x_snake == food.coordinates[0] and y_snake == food.coordinates[1]:

        #  Updating score variable and label.
        global SCORE
        SCORE = SCORE + 1
        label.config(text="SCORE = {}".format(SCORE))

        # Delete food object.
        canvas.delete("food")

        # Create a new food object.
        food = Food()

    else:

        #  Deleting the last coordinate of the snake.
        del snake.coordinates[-1]

        #  Deleting the last square of the snake.
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collision(snake):
        game_over()

    else:
        # Recalling the function for the next movement.
        window.after(SPEED, next_turn, snake, food)  # Don't use parenthesis on next_turn.


# Define which direction take.
def change_direction(new_direction):
    global DIRECTION

    # Change direction and verifying if the direction isn`t the opposite to the current one.
    if (new_direction == "up" and DIRECTION != "down") or \
            (new_direction == "down" and DIRECTION != "up") or \
            (new_direction == "left" and DIRECTION != "right") or \
            (new_direction == "right" and DIRECTION != "left"):
        DIRECTION = new_direction


#  Detect collisions.
def check_collision(snake):
    x_snake, y_snake = snake.coordinates[0]  # Snake's head.

    if x_snake < 0 or x_snake >= WINDOW_WIDTH:  # Detecting collision of the head with x-axis walls.
        print("You hit a x axis wall, GAME OVER.")

    elif y_snake < 0 or y_snake >= WINDOW_WIDTH:  # Detecting collision of the head with y-axis walls.
        print("You hit y axis wall, GAME OVER.")

    for body_part in snake.coordinates[1:]:  # Detecting collision of the head with Snake own body.
        if x_snake == body_part[0] and y_snake == body_part[1]:
            print("You hit yourself, GAME OVER.")
            return True

    return False


# Shows game over screen.
def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font="Consolas, 70", text="GAME OVER",
                       fill="red", tags="game_over")


# Create the main window skeleton.
window = Tk()
window.title("Snakey Adventure")
window.geometry("{width}x{height}".format(width=WINDOW_WIDTH, height=WINDOW_HEIGHT))

# Create a label for displaying the score.
label = Label(text="SCORE = {}".format(SCORE),
              font=("Consolas", 25),
              bg="White",
              fg="Black",
              width=WINDOW_WIDTH,
              )

# Create a blackboard for drawing the game.
canvas = Canvas(window,
                bg=BACKGROUND_COLOR,
                height=WINDOW_HEIGHT,
                width=WINDOW_WIDTH)


# Update, get screen dimensions and calculate window position.
def set_window_geometry():
    window.update()  # Refresh the window to make sure window geometry will work.
    screen_height = window.winfo_screenheight()  # SCREEN
    screen_width = window.winfo_screenwidth()
    window_width = window.winfo_width()  # WINDOW
    window_height = window.winfo_height()
    x_axis = int((screen_width / 2) - (window_width / 2))
    y_axis = int((screen_height / 2) - (window_height / 2))
    window.geometry(f"{window_width}x{window_height}+{x_axis}+{y_axis}")  # Set the window's geometry.


set_window_geometry()


# Defining keybindings.
def set_keybindings():
    window.bind("<Left>", lambda event: change_direction('left'))
    window.bind("<Right>", lambda event: change_direction('right'))
    window.bind("<Up>", lambda event: change_direction('up'))
    window.bind("<Down>", lambda event: change_direction('down'))


set_keybindings()


# INITIALIZING EVERYTHING! Objects, Widgets, Game Loops, Window.
def initializing():
    # Widgets and Objects.
    label.pack()  # Display the widgets (label and canvas).
    canvas.pack()
    snake = Snake()  # Creating object from the previous Classes.
    food = Food()

    # Main loops.
    next_turn(snake, food)  # Start the main game loop.
    window.mainloop()  # Start the Tkinter main event loop.


initializing()

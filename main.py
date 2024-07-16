from PIL import Image, ImageTk
import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Змейка")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg='black')
        self.canvas.pack()

        self.snake = [(20, 20), (20, 30), (20, 40)]
        self.food = self.create_food()
        self.direction = 'Right'
        self.score = 0

        self.draw_snake()
        self.draw_food()

        # Создаем фрейм для кнопок управления
        self.control_frame = tk.Frame(root)
        self.control_frame.pack()

        # Создаем кнопки управления с изображениями стрелок
        self.create_control_buttons()

        self.move()

    def draw_snake(self):
        self.canvas.delete('snake')
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x+10, y+10, fill='green', outline='black', tags='snake')

    def draw_food(self):
        x, y = self.food
        self.canvas.create_oval(x, y, x+10, y+10, fill='red', outline='black', tags='food')

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return (x, y)

    def move(self):
        head_x, head_y = self.snake[0]

        if self.direction == 'Right':
            new_head = (head_x + 10, head_y)
        elif self.direction == 'Left':
            new_head = (head_x - 10, head_y)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + 10)
        elif self.direction == 'Up':
            new_head = (head_x, head_y - 10)

        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.score += 1
            self.food = self.create_food()
            self.draw_food()
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()

        self.draw_snake()

        # Проверяем, столкнулась ли змейка со стеной
        if head_x < 0 or head_x >= 400 or head_y < 0 or head_y >= 400:
            self.game_over()
            return

        # Проверяем, столкнулась ли змейка сама с собой
        for segment in self.snake[1:]:
            if new_head == segment:
                self.game_over()
                return

        self.root.after(100, self.move)

    def create_control_buttons(self):
        # Загружаем изображения стрелок и создаем кнопки
        img_up = Image.open("arrow_up.png").resize((50, 50))
        img_down = Image.open("arrow_down.png").resize((50, 50))
        img_left = Image.open("arrow_left.png").resize((50, 50))
        img_right = Image.open("arrow_right.png").resize((50, 50))

        self.img_up = ImageTk.PhotoImage(img_up)
        self.img_down = ImageTk.PhotoImage(img_down)
        self.img_left = ImageTk.PhotoImage(img_left)
        self.img_right = ImageTk.PhotoImage(img_right)

        # Размещаем кнопки в фрейме
        btn_up = tk.Button(self.control_frame, image=self.img_up, command=lambda: self.change_direction('Up'))
        btn_down = tk.Button(self.control_frame, image=self.img_down, command=lambda: self.change_direction('Down'))
        btn_left = tk.Button(self.control_frame, image=self.img_left, command=lambda: self.change_direction('Left'))
        btn_right = tk.Button(self.control_frame, image=self.img_right, command=lambda: self.change_direction('Right'))

        # Упаковываем кнопки в фрейме
        btn_up.grid(row=0, column=1)
        btn_left.grid(row=1, column=0)
        btn_right.grid(row=1, column=2)
        btn_down.grid(row=2, column=1)

    def change_direction(self, direction):
        if (direction == 'Up' and self.direction != 'Down') or \
           (direction == 'Down' and self.direction != 'Up') or \
           (direction == 'Left' and self.direction != 'Right') or \
           (direction == 'Right' and self.direction != 'Left'):
            self.direction = direction

    def game_over(self):
        self.canvas.delete('all')
        self.canvas.create_text(200, 200, text=f"Game Over!\nScore: {self.score}", fill='white', font=('Arial', 24, 'bold'))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

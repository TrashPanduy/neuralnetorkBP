import tkinter as tk

class DrawingGridApp:
    def __init__(self, master, rows=20, columns=20, cell_size=20):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.grid_data = [[0 for _ in range(columns)] for _ in range(rows)]

        self.canvas = tk.Canvas(master, width=columns * cell_size, height=rows * cell_size, bg='white')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.bottom_frame = tk.Frame(master, height=(rows * cell_size) // 2)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.draw_grid()
        self.bind_events()

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='black')

    def bind_events(self):
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)
        self.master.bind('<Button-1>', self.save_grid_to_file)

    def on_mouse_drag(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= col < self.columns and 0 <= row < self.rows:
            self.grid_data[row][col] = 1
            self.update_cell(row, col)

    def update_cell(self, row, col):
        x1 = col * self.cell_size
        y1 = row * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')

    def save_grid_to_file(self, event=None):
        with open('gridData.txt', 'w') as file:
            for row in self.grid_data:
                file.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingGridApp(root)
    root.mainloop()

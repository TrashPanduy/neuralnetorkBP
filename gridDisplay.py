import tkinter as tk
from tkinter import Button
from tkinter import Entry
from tkinter import Label

class DrawingGridApp:
    def __init__(self, master, rows=20, columns=20, cell_size=20):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.cell_size = cell_size
        self.grid_data = [[0 for _ in range(columns)] for _ in range(rows)]

        self.canvas = tk.Canvas(master, width=columns * cell_size, height=rows * cell_size, bg='white')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.bottom_frame = tk.Frame(master)
        self.bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # Create a frame for the label and text field
        self.input_frame = tk.Frame(self.bottom_frame)
        self.input_frame.pack(pady=10)

        # Create a label
        self.label = tk.Label(self.input_frame, text="Input:")
        self.label.pack(side=tk.LEFT)

        # Create a text field
        self.text_field = tk.Entry(self.input_frame)
        self.text_field.pack(side=tk.LEFT, padx=5)

        self.draw_grid()
        self.bind_events()
        self.generate_buttons()

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
        with open('/Users/michaelowen/VSCode_Files/neuralnetorkBP/dataPackets/gridData.txt', 'a') as file:
            for row in self.grid_data:
                file.write(''.join(map(str, row)))
            temp_arr = []
            input_value = self.text_field.get()
            for i in range(10):
                if str(i) == input_value:
                    temp_arr.append('1')
                else:
                    temp_arr.append('0')
            temp_string = ''.join(temp_arr)
            file.write('\n' + temp_string + '\n')

    def clear_grid(self):
        # Reset the grid data
        self.grid_data = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

        # Clear the canvas
        self.canvas.delete("all")  # Clear all drawings from the canvas
        self.draw_grid()  # Redraw the empty grid
 
    def generate_buttons(self):
        save_button = Button(self.bottom_frame, text="Save Data", command=self.save_grid_to_file)
        save_button.pack(pady=10)

        clear_button = Button(self.bottom_frame, text="Clear Grid", command=self.clear_grid)
        clear_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingGridApp(root)
    root.mainloop()

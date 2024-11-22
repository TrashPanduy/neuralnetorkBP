#what do I want to add to this?
#output average error  
#access to create data tab
#display expected and outputed values from network
#add a function for multiple formulas & implement formula select
#fully setup output layer functionality for increased dataRange
import subprocess
from tkinter import *
from Main import trainNetwork,initializeLayers,checkAcuracy,Node

class Controller:
    def __init__(self):
        self.root = Tk()
        self.root.title("Neural Network Controller")
        self.root.geometry('1100x800')
        self.label=None

        # Create a frame
        self.frame = Frame(self.root)
        self.frame.pack(padx=10, pady=10)


        self.entries = []
        self.hyper_values_input()

        self.retrieve_button = Button(self.root, text="Change Values", command=self.set_hyper_data)
        self.retrieve_button.pack(pady=10)

        self.retrieve_button = Button(self.root, text="train Network", command=self.run_neural_network)
        self.retrieve_button.pack(pady=10)

    def hyper_values_input(self):
        labels = [
            "Hidden layers:",
            "Hidden Nodes:",
            "Learn Rate:",
            "Pixels:",
            "Learnig Data file: "
        ]
        labels2 = [
            "Learning Iterations:",
            "starting weights(lower):",
            "starting weights(higher!):",
            "Digits Training For -1: ",
            "Validation Data File: "
        ]
        default_values = self.get_hyper_data()
        Pointer = 0
        for i in range(len(labels)):
            # First column
            label = Label(self.frame, text=labels[i])
            label.grid(row=i, column=0, padx=5, pady=5)
            entry = Entry(self.frame)
            entry.insert(0, default_values[Pointer])
            Pointer = Pointer + 1
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.entries.append(entry)  # Store reference to entry

            # Second column with unique labels
            label2 = Label(self.frame, text=labels2[i])
            label2.grid(row=i, column=2, padx=5, pady=5)
            entry2 = Entry(self.frame)
            entry2.insert(0, default_values[Pointer])
            Pointer = Pointer + 1
            entry2.grid(row=i, column=3, padx=5, pady=5)
            self.entries.append(entry2)  # Store reference to entry

    def set_hyper_data(self):
        # Retrieve and print the values from all entry fields
        with open('/Users/michaelowen/VSCode_Files/neuralnetorkBP/dataPackets/hyperValues.txt', 'w') as hyper_data_file:
            for i, entry in enumerate(self.entries):
                val = entry.get()
                value = entry.get()
                print(f"Entry {i + 1}: {value}")
                hyper_data_file.write(f"{value}\n")

    def get_hyper_data(self):
        hyper_data_file = open('/Users/michaelowen/VSCode_Files/neuralnetorkBP/dataPackets/hyperValues.txt','r')
        values_array = hyper_data_file.read().splitlines()
        values = []
        for line in values_array[:-2]:
            try:
                values.append(int(line))
            except ValueError:
                values.append(float(line))
        values.append(values_array[-2])
        values.append(values_array[-1])
        return values

    def run_neural_network(self):
        self.display_progress()
        self.root.update()
        try:
            tempArr = []
            for entry in self.entries:
                tempArr.append(entry.get())
            accuracy = trainNetwork(int(tempArr[0]),int(tempArr[1]),int(tempArr[2]),float(tempArr[3]),float(tempArr[4]),float(tempArr[5]),int(tempArr[6]),int(tempArr[7]))
            print(accuracy)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred: {e}")
        
        self.display_progress(str(accuracy) + " Out of 26")

    def display_progress(self, result="training... "):
        # Create a new frame only once if it doesn't exist, else update the existing label
        if self.label is None:
            display_frame = Frame(self.root, bg="blue")
            display_frame.pack(padx=10, pady=10)

            # Create the label and keep a reference to it
            self.label = Label(display_frame, text=result)
            self.label.pack(pady=10)
        else:
            # Update the existing label's text
            self.label.config(text=result)

if __name__ == "__main__":
    app = Controller()
    app.root.mainloop()
import tkinter as tk

window = tk.Tk()
class UI:
    def __init__(self):
        self.answerFrame = tk.LabelFrame(text = "Revealed")
    def draw_array(self, array):
        for i in range(len(array)):
            for j in range(len(array[i])):
               window.grid(row =  i, column = j)
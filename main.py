import tkinter as tk

window = tk.Tk()
class UI:
    def __init__(self):
        self.answerFrame = tk.LabelFrame(text = "Revealed")
        self.wordFrame = tk.LabelFrame(text = "Input words here")
        self.buttonFrame = tk.Frame()
    def draw_array(self, array):
        for i in range(len(array)):
            for j in range(len(array[i])):
               window.grid(row =  i, column = j)
               
class Logic:
    def __init__(self):
       pass 
logic = Logic()
ui = UI()


               
if __name__ == "__main__":
    window.mainloop()

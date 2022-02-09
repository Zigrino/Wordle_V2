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
        self.dict = [] #dictionary if I can get it to work
        self.winword = "witch"
        self.NumberOfGuessedWords = 0  
    def checkWord(self, word):
        if len(word)==True:
            return True 
        else:
            return False
    def generateColor(self, letter):
        for i in winword:
            if letter == i:
                return "green"
        if i in winword:
            return "yellow"
        else:
            return "grey"
    def proccessWord(self, inputWord, outputArray):
        word = inputWord.get()
        if checkWord(word):
            inputWord.destroy()
            for i in range(len(outputArray)):
                outputArray[i].config(text = word[i], color = generateColor(word[i]))
                outputArray[i].grid(row = self.NumberOfGuessedWords, column = i)



logic = Logic()
ui = UI()


               
if __name__ == "__main__":
    window.mainloop()

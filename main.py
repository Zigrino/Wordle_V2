import tkinter as tk

window = tk.Tk()
class UI:
    def __init__(self, logic):
        self.answerFrame = tk.LabelFrame(text = "Revealed")
        self.wordFrame = tk.LabelFrame(text = "Input words here")
        self.buttonFrame = tk.Frame()
        self.checkButton = tk.Button(text = "Submit", command = self.proccessWord)
        self.wordArray = [tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame)]
        self.GuessedWordArray = [[tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], ]
    def draw_array(self, array):
        for i in range(len(array)):
            for j in range(len(array[i])):
               array[i][j].grid(row =  i, column = j)
    def draw_list(self, list):
        for i in range(len(list)):
            list[i].grid(row = i, column = 0)
               
    def draw(self):
        self.answerFrame.pack()
        self.wordFrame.pack()
        self.buttonFrame.pack()
        self.draw_array(self.GuessedWordArray)
        self.draw_list(self.wordArray)
        self.checkButton.pack()
    def proccessWord(self):
        logic.proccessWord(self.wordArray[logic.NumberOfGuessedWords], self.GuessedWordArray)
class Logic:
    def __init__(self):
        self.dict = [] #dictionary if I can get it to work
        self.winword = "witch"
        self.NumberOfGuessedWords = 0  
    def checkWord(self, word):
        if len(word)==5:
            return True 
        else:
            return False
    def generateColor(self, letter, position):
        if letter == self.winword[position]:
            return "green"
        if letter in self.winword:
            return "yellow"
        else:
            return "grey"
    def proccessWord(self, inputWord, outputArray):
        print("proccessing word")
        word = inputWord.get()
        if self.checkWord(word):
            inputWord.destroy()
            for i in range(len(outputArray[self.NumberOfGuessedWords])):
                outputArray[self.NumberOfGuessedWords][i].config(text = word[i], bg = self.generateColor(word[i], i), fg = "blue")
                print(word[i])
                outputArray[self.NumberOfGuessedWords][i].grid(row = self.NumberOfGuessedWords, column = i)
            self.NumberOfGuessedWords += 1



 

logic = Logic()
ui = UI(logic)
ui.draw()




               
window.mainloop()

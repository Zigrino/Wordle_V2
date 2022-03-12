import tkinter as tk
from textblob import TextBlob
import random
from list import WordList
from nltk.corpus import words

window = tk.Tk()
wordList = WordList()
with open("english_words.txt") as word_file:
    english_words = set(word.strip().lower() for word in word_file)
class UI:
    def __init__(self, logic):
        self.answerFrame = tk.LabelFrame(text = "Revealed")
        self.wordFrame = tk.LabelFrame(text = "Input words here")
        self.buttonFrame = tk.Frame()
        self.checkButton = tk.Button(text = "Submit", command = self.proccessWord)
        self.wordArray = [tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame), tk.Entry(self.wordFrame)]
        self.GuessedWordArray = [[tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], [tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame), tk.Label(self.answerFrame)], ]
        self.keyboardFrame = tk.LabelFrame(text =  "Keyboard")
        self.keyboardstr = "qwertyuiopasdfghjklzxcvbnm"
        self.keyboard = []
        self.errorFrame = tk.Frame()
        self.errorLabel = tk.Label(self.errorFrame)
        for i in self.keyboardstr:
            self.keyboard.append(tk.Label(self.keyboardFrame, text = i))
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
        self.errorFrame.pack()
        self.errorLabel.pack()
        self.checkButton.pack()
        self.keyboardFrame.pack()
        for i in range(len(self.keyboard)):
            if i <= 10:
                collumn = i
                row = 1
            elif i <= 19:
                collumn = i-10
                row = 2
            elif i <= 26:
                collumn = i-19
                row = 3
            self.keyboard[i].grid(row = row, column = collumn)

    def proccessWord(self):
        logic.proccessWord(self.wordArray[logic.NumberOfGuessedWords], self.GuessedWordArray, self.keyboard, self.errorLabel)
    def enterPressed(self, e):
        self.checkButton.invoke()
class Logic:
    def __init__(self):
        self.dict = [] #dictionary if I can get it to work
        #self.winwords = ["witch", "witty", "sloth", "bride", "bribe", "brass"]
        self.winwords = wordList.wordList
        self.winword = random.choice(self.winwords)
        while self.winword not in english_words:
            self.winword = random.choice(self.winword)
        self.NumberOfGuessedWords = 0  
        self.keyboardstr = "qwertyuiopasdfghjklzxcvbnm"
    def checkWord(self, word, error):

        if len(word)!=5:
            error.config(text = "not 5 letters long")
            return False
        if word not in english_words:
            error.config(text = "not in word list")
            return False
        if word in english_words and len(word) == 5: 
            error.config(text = "")
            return True
        #if blob.correct() != word:
        #    return False
        else:
            return False
    def generateColor(self, letter, position, keyboard):
        lettercount = 0
        for i in self.winword:
            if i == letter:
               lettercount += 1 
        if letter == self.winword[position]:
            keyboard[self.keyboardstr.index(letter)].config(bg = "green")
            return "green"
        if letter in self.winword:
            keyboard[self.keyboardstr.index(letter)].config(bg = "yellow")
            return "yellow"
        else:
            keyboard[self.keyboardstr.index(letter)].config(bg = "grey")
            return "grey"
    def proccessWord(self, inputWord, outputArray, keyboard, error):
        print("proccessing word")
        word = inputWord.get()
        if self.checkWord(word, error):
            inputWord.destroy()
            for i in range(len(outputArray[self.NumberOfGuessedWords])):
                outputArray[self.NumberOfGuessedWords][i].config(text = word[i], bg = self.generateColor(word[i], i, keyboard), fg = "blue")
                print(word[i])
                outputArray[self.NumberOfGuessedWords][i].grid(row = self.NumberOfGuessedWords, column = i)
            self.NumberOfGuessedWords += 1
    def cheat(self, e):
        print(self.winword)



 

logic = Logic()
ui = UI(logic)
ui.draw()
window.bind("<Return>", ui.enterPressed)
window.bind("/", logic.cheat)


               
window.mainloop()

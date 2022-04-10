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
        self.keyboardFrame = tk.LabelFrame(text =  "Letters")
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
            if i <= 9:
                collumn = i
                row = 1
            elif i <= 18:
                collumn = i-10
                row = 2
            elif i <= 25:
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
        self.wordcounts = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
        self.timesinword = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
        #self.winword = "salvo"
        for i in self.winword:
            self.wordcounts[i] += 1
        print(self.wordcounts)
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
    def generateColor(self, letter, position, keyboard, word):
        green = False
        yellow = False
        grey = False
        print(letter)
         
        if letter == self.winword[position]:
            self.timescounted[letter] += 1
            keyboard[self.keyboardstr.index(word[i])].config(bg = "green")
            green = True
        elif letter in self.winword:
            self.timescounted[letter] += 1
            if keyboard[self.keyboardstr.index(letter)].cget("bg") != "green":
                keyboard[self.keyboardstr.index(letter)].config(bg = "yellow")
            for i in range(len(word)):
               if word[i] == self.winword[i] and word[i] == letter:
                   print('has green at possition', i)
            yellow = True



        else:
            keyboard[self.keyboardstr.index(letter)].config(bg = "grey")
            grey = True
        
        if green:
            return "green"
        elif yellow:
            return "yellow"
        elif grey:
            return "grey"
    def proccessWord(self, inputWord, outputArray, keyboard, error):
        print("proccessing word")
        word = inputWord.get()
        color_list = ["grey", "grey", "grey", "grey", "grey"]
        timescounted = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
        if self.checkWord(word, error):
            inputWord.destroy()
            '''
            for i in range(len(outputArray[self.NumberOfGuessedWords])):
                outputArray[self.NumberOfGuessedWords][i].config(text = word[i], bg = self.generateColor(word[i], i, keyboard, word), fg = "blue")
                outputArray[self.NumberOfGuessedWords][i].grid(row = self.NumberOfGuessedWords, column = i)
            self.NumberOfGuessedWords += 1
            '''
             
            for i in word:
                self.timesinword[i]+=1


            for i in range(5):
                if self.winword[i] == word[i]:
                    color_list[i] = "green"
                    timescounted[word[i]]+=1
            for i in range(5):
                if word[i] in self.winword and timescounted[word[i]] < self.wordcounts[word[i]] and color_list[i] == "grey":
                    color_list[i] = "yellow"    
                    timescounted[word[i]] += 1
                
            print(timescounted)

            for i in range(len(color_list)):
                print("#######################")
                if keyboard[self.keyboardstr.index(word[i])].cget("bg") == "green":
                    print("green passed")
                    pass
                elif keyboard[self.keyboardstr.index(word[i])].cget("bg") == "yellow" and color_list[i] == "green":
                    print("yellow turning green")
                    keyboard[self.keyboardstr.index(word[i])].config(bg = "green")
                elif keyboard[self.keyboardstr.index(word[i])].cget("bg") == "grey":
                    print("was grey")
                    keyboard[self.keyboardstr.index(word[i])].config(bg = color_list[i])
                elif keyboard[self.keyboardstr.index(word[i])].cget("bg") == "white":
                    print("was white")
                    keyboard[self.keyboardstr.index(word[i])].config(bg = color_list[i])
                else:
                    print("else, idk how")
                    keyboard[self.keyboardstr.index(word[i])].config(bg = color_list[i])
                print(color_list[i])
                print(keyboard[self.keyboardstr.index(word[i])].cget('bg'))
                


                        
                    
            for i in range(len(outputArray[self.NumberOfGuessedWords])):
                outputArray[self.NumberOfGuessedWords][i].config(text = word[i], bg = color_list[i], fg = "blue")
                outputArray[self.NumberOfGuessedWords][i].grid(row = self.NumberOfGuessedWords, column = i)
            self.NumberOfGuessedWords += 1

                    
                    
        if word == self.winword:
            tk.messagebox.showinfo("", "You Win! :D")
    def cheat(self, e):
        print(self.winword)



 

logic = Logic()
ui = UI(logic)
ui.draw()
window.bind("<Return>", ui.enterPressed)
window.bind("/", logic.cheat)


               
window.mainloop()

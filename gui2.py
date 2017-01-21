from tkinter import*
import nltk
from nltk.tokenize import word_tokenize
text=""

def callback(event):
    global text
    text=text1.get()
    text=word_tokenize(text)
    SCORE=getSentiment(text)
    print(SCORE)
    
   
def loadPositive():
    """
    loading positive dictionary
    """
    myfile = open('C:\\Users\Dell\Desktop\\positive2.csv', "r")
    positives = myfile.readlines()
    positive = [pos.strip().lower() for pos in positives]
    return positive

def loadNegative():
    """
    loading positive dictionary
    """
    myfile = open('C:\\Users\Dell\Desktop\\negative2.csv', "r")
    negatives = myfile.readlines()
    negative = [neg.strip().lower() for neg in negatives]
    return negative
    
def countNeg(text, negative):
    """
    counts negative words in cleantext
    """
    negs = [word for word in text if word in negative]
    return len(negs)

def countPos(text, positive):
    """
    counts negative words in cleantext
    """
    pos = [word for word in text if word in positive]
    return len(pos)   
       
    
def getSentiment(text):
    """
    counts negative and positive words in cleantext and returns a score accordingly
    """
    positive = loadPositive()
    negative = loadNegative()
    return (countPos(text, positive) - countNeg(text, negative))

print(text)
root = Tk()
label1=Label(root,text="Enter the text about SRM")
label1.pack(fill=X)
text1=Entry(root)
text1.pack()
button1 = Button(text='Sentimental Analysis')
button1.bind("<Button-1>",callback)
button1.pack()
print(text)
SCORE=getSentiment(text)
print(SCORE)
label2=Label(root,text=SCORE)
label2.pack()
root.mainloop()




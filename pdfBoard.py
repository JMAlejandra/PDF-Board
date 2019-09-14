# =================================================================
# IMPORTS ALL LIBRARIES NECESSARY FOR THE SCRIPT
# =================================================================
import random
import tkinter as tk
from tkinter import filedialog
from os import startfile
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Frame, KeepInFrame
from reportlab.lib.styles import ParagraphStyle

# =================================================================
# INPUT FILE MANAGEMENT
# =================================================================

# OPENS A FILE DIALOG AND REQUESTS THE FILE TO BE OPENED
root = tk.Tk()
root.withdraw()
inputRoute = filedialog.askopenfilename()
file = open(inputRoute,'r')

# READS THE FILE LINE BY LINE AND SAVES IT IN CLIENT LIST
clientList = []
count = 0
with file as openFile:
    for line in openFile:
        count = count + 1
        line = line.rstrip()
        clientList.append(line)

# =================================================================
# PDF FORMATTING 
# =================================================================

# OPENS A FILE DIALOG TO DETERMINE WHERE THE USER WANTS TO SAVE THE FILE
options = {}
options['title'] = 'Save PDF File As...'
outputRoute = filedialog.asksaveasfilename(**options)
if not outputRoute.endswith('.pdf'):
    outputRoute = outputRoute + '.pdf'

# CREATES THE CANVAS
c = canvas.Canvas(outputRoute)

# CREATES A LIST OF X AND Y COORDENATES AND CREATES THE GRID
xl = [75, 165, 255, 345, 435, 525]
yl = [680, 600, 520, 440, 360, 280]
c.grid(xl,yl)
textobject = c.beginText(xl[0],yl[0])
c.drawText(textobject)

# ESTABLISHES THE COORDENATES AND SIZE OF THE OUTTER BLUE RECTANGLE
cx, cy = 75 , 725
width = 450
height = 80

# SETS THE FILL COLOR AND CREATES THE OUTTER RECTANGLE FOR THE TITLE
c.setFillColorRGB(60/255, 59/255, 110/255)
c.rect(cx,cy,width,height,fill=1)

# ESTABLISHES THE COORDENATES AND SIZE OF THE OUTTER BLUE RECTANGLE
cx, cy = 85 , 735
width = 430
height = 60


# SETS THE FILL COLOR AND CREATES THE INNER RECTANGLE FOR THE TITLE
c.setFillColorRGB(178/255, 34/255, 52/255)
c.rect(cx,cy,width,height,fill=1)

# CREATES THE TITLE
s = "DEBATE BINGO" 
frame1 = Frame(cx, cy, width, height, showBoundary=0)
style = ParagraphStyle(
    name='Normal',
    fontSize=45,
    alignment = 1,
    textColor = 'White'
)
story = [Paragraph(s, style)]
story_inframe = KeepInFrame(width, height, story)
frame1.addFromList([story_inframe], c)

# CREATES A LIST OF FRAMES FOR EACH INDIVIDUAL GRID ELEMENT
gridFramesList = []
frameWidth = 90
frameHeight = 80
for i in range(5):
    for j in range(5):
        gFrame = Frame(xl[i], yl[j]-frameHeight, frameWidth, frameHeight, showBoundary=0)
        gridFramesList.append(gFrame)

# ESTABLISHES THE STYLE TO BE APPLIED TO THE GRID 
styleGrid = ParagraphStyle(
    name='Normal',
    fontSize=10,
    alignment = 1,
    textColor = 'Black',
    spaceShrinkage = 0.05
)        

# =================================================================
# BINGO CARD CREATION
# =================================================================

# CREATES AND SHUFFLES A LIST OF ELEMENT NUMBERS TO PICK FROM THE LIST OF OPTIONS 
random.seed()
numList = list(range(0,count))
random.shuffle(numList)

# CREATES AND FILLS THE BINGOBOARD LIST ACCORDING TO THE SHUFFLED ELEMENT LIST AND PRINTS IT TO A FRAME IN THE GRIDFRAMESLIST
bingoBoard = []
for i in range(25):
    bingoBoard.append(clientList[numList.pop(0)])
    story = [Paragraph(bingoBoard[i], styleGrid)]
    story_inframe = KeepInFrame(frameWidth, frameHeight, story)
    gridFramesList[i].addFromList([story_inframe], c)

# =================================================================
# CREDITS
# =================================================================
c.drawString(400, 10, 'Developed by Alex J.')

# =================================================================
# CLOSES THE PDF FILE 
# =================================================================
c.showPage()
c.save()


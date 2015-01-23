import Tkinter as tk
from PIL import ImageTk, Image
import random, time

places={"Washington":"Olympia",
          "Oregon":"Salem",
          "California":"Sacramento",
          "Ohio":"Columbus",
          "Nebraska":"Lincoln",
          "Colorado":"Denver",
          "Michigan":"Lansing",
          "Massachusetts":"Boston",
          "Florida":"Tallahassee",
          "Texas":"Austin",
          "Oklahoma":"Oklahoma City",
          "Hawaii":"Honolulu",
          "Alaska":"Juneau",
          "Utah":"Salt Lake City",
          "New Mexico":"Santa Fe",
          "North Dakota":"Bismarck",
          "South Dakota":"Pierre",
          "West Virginia":"Charleston",
          "Virginia":"Richmond",
          "New Jersey":"Trenton",
          "Minnesota":"Saint Paul",
          "Illinois":"Springfield",
          "Indiana":"Indianapolis",
          "Kentucky":"Frankfort",
          "Tennessee":"Nashville",
          "Georgia":"Atlanta",
          "Alabama":"Montgomery",
          "Mississippi":"Jackson",
          "North Carolina":"Raleigh",
          "South Carolina":"Columbia",
          "Maine":"Augusta",
          "Vermont":"Montpelier",
          "New Hampshire":"Concord",
          "Connecticut":"Hartford",
          "Rhode Island":"Providence",
          "Wyoming":"Cheyenne",
          "Montana":"Helena",
          "Kansas":"Topeka",
          "Iowa":"Des Moines",
          "Pennsylvania":"Harrisburg",
          "Maryland":"Annapolis",
          "Missouri":"Jefferson City",
          "Arizona":"Phoenix",
          "Nevada":"Carson City",
          "New York":"Albany",
          "Wisconsin":"Madison",
          "Delaware":"Dover",
          "Idaho":"Boise",
          "Arkansas":"Little Rock",
          "Louisiana":"Baton Rouge"}

alphabetized = sorted(places)
index = 0

def changeState():
     global img
     startButton.config(state=tk.DISABLED)

     img = Image.open(alphabetized[index] + ".png")
     img = ImageTk.PhotoImage(img)
     display.config(image=img)
     window.update()

def submitAnswer():
     global index
     img = None
     if stateEntry.get() == alphabetized[index] and capitalEntry.get() == places[alphabetized[index]]:
          img = Image.open("correct.png")
     else:
          img = Image.open("incorrect.png")
          stateEntry.delete(0, tk.END)
          capitalEntry.delete(0, tk.END)
          stateEntry.insert(0, alphabetized[index])
          capitalEntry.insert(0, places[alphabetized[index]])
     img = img.resize((800,500), Image.ANTIALIAS)
     img = ImageTk.PhotoImage(img)
     display.config(image=img)
     window.update()

     time.sleep(.5)
     index = index + 1
     changeState()
           
window = tk.Tk()

img = Image.open("states.png")
img = ImageTk.PhotoImage(img)
display = tk.Label(window, image=img)
display.grid(row=0,columnspan=3)

stateName = tk.Label(window, text="State:")
stateName.grid(row=1, column=0, sticky=tk.E)
capitalName = tk.Label(window, text="Capital:")
capitalName.grid(row=2, column=0, sticky=tk.E)

stateEntry = tk.Entry(window, width=50)
stateEntry.grid(row=1, column=1)
capitalEntry = tk.Entry(window, width=50)
capitalEntry.grid(row=2, column=1)

startButton = tk.Button(window, text="START", command=changeState)
startButton.grid(row=1, column=2, sticky=tk.W)
submitButton = tk.Button(window, text="SUBMIT", command=submitAnswer)
submitButton.grid(row=2, column=2, sticky=tk.W)

window.mainloop()


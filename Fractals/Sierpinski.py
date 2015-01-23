import Tkinter as tk 
from math import cos, sin, pi

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __sub__(self, other):
		return Point(self.x-other.x, self.y-other.y)

	def __add__(self, other):
		return Point(self.x+other.x, self.y+other.y)

	def __rmul__(self, n):
		return Point(n*self.x, n*self.y)

	def __div__(self, n):
		if n == 0:
			raise ValueError
		else:
			return Point(self.x/n, self.y/n)

def draw(A, B, C, iteration):
	if iteration < 1: return

	midAB = A + (B-A)/2
	midBC = B + (C-B)/2
	midAC = A + (C-A)/2
	canvas.create_polygon(midAB.x, midAB.y, midBC.x, midBC.y, midAC.x, midAC.y, fill='white')
	window.update()

	draw(midAB, B, midBC, iteration-1)
	draw(A, midAB, midAC, iteration-1)
	draw(midAC, midBC, C, iteration-1)


def drawSierpinski():
	canvas.delete("all")
	iteration = entry.get()
	if iteration.isdigit():
		button.config(state=tk.DISABLED)
		A = Point(100, 370)
		B = Point(300, 370-400*sin(pi/3))
		C = Point(500, 370)
		canvas.create_polygon(A.x, A.y, B.x, B.y, C.x, C.y, fill='black')
		draw(A, B, C, int(iteration))
		button.config(state=tk.NORMAL)


window = tk.Tk()
window.title("Sierpinski")
canvas = tk.Canvas(window, width=600, height=400)
canvas.grid(row=1, columnspan=2)

entry = tk.Entry(window)
entry.insert(0, "Enter the iteration")
entry.grid(row=0, column=0, sticky=tk.E)

button = tk.Button(window, text="Run", command=drawSierpinski)
button.grid(row=0, column=1, sticky=tk.W)


window.mainloop()
import Tkinter as tk 
import tkMessageBox
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

def draw(start, end, iteration, n):
	if iteration < 1: return

	firstThird = start + (end-start)/3
	secondThird = start + (2*(end-start))/3


	angle = (cos(-pi/3), sin(-pi/3))
	vector = secondThird - firstThird
	rotated = Point(vector.x*angle[0] - vector.y*angle[1], vector.x*angle[1]+vector.y*angle[0])
	final = firstThird + rotated


	if n is not None:
		canvas.delete(n)
	a = canvas.create_line(firstThird.x, firstThird.y, final.x, final.y, width=2)
	b = canvas.create_line(final.x, final.y, secondThird.x, secondThird.y, width=2)
	c = canvas.create_line(start.x, start.y, firstThird.x, firstThird.y, width=2)
	d = canvas.create_line(secondThird.x, secondThird.y, end.x, end.y, width=2)
	window.update()
	
	draw(firstThird, final, iteration-1, a)
	draw(final, secondThird, iteration-1, b)
	draw(start, firstThird, iteration-1, c)
	draw(secondThird, end, iteration-1, d)


def drawCurve():
	canvas.delete("all")
	iteration = iterate.get()
	if iteration.isdigit():
		curve.config(state=tk.DISABLED)
		snowflake.config(state=tk.DISABLED)
		draw(Point(0, 300), Point(700, 300), int(iteration), None)
		curve.config(state=tk.NORMAL)
		snowflake.config(state=tk.NORMAL)

def drawSnowflake():
	canvas.delete("all")
	iteration = iterate.get()
	if iteration.isdigit():
		curve.config(state=tk.DISABLED)
		snowflake.config(state=tk.DISABLED)
		draw(Point(180, 100), Point(520, 100), int(iteration), None)
		draw(Point(350, 100+340*sin(pi/3)), Point(180, 100), int(iteration), None)
		draw(Point(520, 100), Point(350, 100+340*sin(pi/3)), int(iteration), None)
		curve.config(state=tk.NORMAL)
		snowflake.config(state=tk.NORMAL)


window = tk.Tk()
window.title("Koch")
canvas = tk.Canvas(window, width = 700, height = 400)
canvas.grid(row=1, columnspan=3)

curve = tk.Button(window, text="Koch curve", command=drawCurve)
curve.grid(row=0, column=0)

snowflake = tk.Button(window, text="Koch snowflake", command=drawSnowflake)
snowflake.grid(row=0, column=2)

iterate = tk.Entry(window)
iterate.insert(0, "Enter the iteration")
iterate.grid(row=0, column=1)

window.mainloop()
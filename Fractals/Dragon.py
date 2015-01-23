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

def drawDragon(totalLines, cursor, iteration):
	if iteration < 0: return
	lines = []

	color = None
	if iteration > 4:
		color = "red4"
	elif iteration > 2 and iteration <= 4:
		color = "red3"
	elif iteration > 1 and iteration <= 2:
		color = "orange red"
	elif iteration > 0 and iteration <= 1:
		color = "dark orange"
	else:
		color = "DarkGoldenRod2"

	for start, end in reversed(totalLines):
		vec = end - start
		vec = cursor + Point(vec.x*cos(-pi/2)-vec.y*sin(-pi/2), vec.x*sin(-pi/2)+vec.y*cos(-pi/2))
		canvas.create_line(cursor.x, cursor.y, vec.x, vec.y, width=2, fill = color)
		lines.append((cursor, vec))
		cursor = vec
	window.update()
	totalLines = totalLines + lines
	drawDragon(totalLines, cursor, iteration-1)
	

window = tk.Tk()
window.title("Dragon")
canvas = tk.Canvas(window, width=700, height=500)
canvas.pack()

start = Point(540, 330)
end = Point(547, 330)
canvas.create_line(start.x, start.y, end.x, end.y, width=2, fill="red4")
drawDragon([(start, end)], end, 11)

window.mainloop()
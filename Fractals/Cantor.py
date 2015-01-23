import Tkinter as tk 

def cantor(x, y, len):
	if len >= 1:
		canvas.create_line(x, y, x+len, y, width=10)
		window.update()

		y = y + 40
		cantor(x + 2*len/3, y, len/3)
		cantor(x, y, len/3)
		


window = tk.Tk()
window.title("Cantor")
canvas = tk.Canvas(window, width=500, height=300)
canvas.pack()

cantor(10, 30, 480)

window.mainloop()
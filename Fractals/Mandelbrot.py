import Tkinter as tk
from PIL import ImageTk, Image
import time

def drawMandelbrot(img, iteration):
	im = Image.new("RGB", (WIDTH, HEIGHT), 'white')
	w = float(WIDTH)
	h = float(HEIGHT)
	for m in range(0,HEIGHT):
		for n in range(0, WIDTH):
			c_real = (n/w)*3.5-2.5
			c_imag = (m/h - .5) * 2
			z_real = 0
			z_imag = 0
			z_temp_real = None
			z_temp_imag = None
			for count in range(iteration):
				z_temp_real = z_real
				z_temp_imag = z_imag
				z_real = z_temp_real*z_temp_real - z_temp_imag*z_temp_imag + c_real
				z_imag = 2.0 * z_temp_real * z_temp_imag + c_imag
			if z_real*z_real + z_imag*z_imag < 2:
				im.putpixel((n, m),0)



	counter_label.config(text="     n = %d"%iteration)
	img[0] = ImageTk.PhotoImage(im)
	display.config(image=img[0])
	window.update()




			
WIDTH = 650
HEIGHT = 400

window = tk.Tk()
window.title("Mandelbrot")
counter_label = tk.Label(window, text="     n = 0", font = "-weight bold")
counter_label.pack(anchor=tk.W)
display = tk.Label(window)
display.pack()
img = [None]

for n in [1,1,2,3,4,5,6,7,8,9,10,20,40,100]:
	drawMandelbrot(img, n)


window.mainloop()
import Tkinter as tk 
import tkMessageBox
import random

window = tk.Tk()
window.title("Sudoku Solver")
grid = []

for i in range(9):
	for j in range(9):

		entry = tk.Entry(window, text=str((i,j)), width=3)
		if j == 2 and i == 2:
			entry.grid(row=i, column=j, padx=(0,5), pady=(0,5))
		elif j == 6 and i == 2:
			entry.grid(row=i, column=j, padx=(5,0), pady=(0,5))
		elif j == 2 and i == 6:
			entry.grid(row=i, column=j, padx=(0,5), pady=(5,0))
		elif j == 6 and i == 6:
			entry.grid(row=i, column=j, padx=(5,0), pady=(5,0))
		elif j == 2:
			entry.grid(row=i, column=j, padx=(0,5))
		elif j == 6:
			entry.grid(row=i, column=j, padx=(5,0))
		elif i == 2:
			entry.grid(row=i, column=j, pady=(0,5))
		elif i == 6:
			entry.grid(row=i, column=j, pady=(5,0))
		else:
			entry.grid(row=i, column=j)

		grid.append(entry)


def validInput(grid):
	for cell in grid:
		if cell is not None and cell.get() != "":
			try:
				value = int(cell.get())
				if value > 9 or  value < 1: 
					raise Exception
			except ValueError:
				tkMessageBox.showinfo("Input must be a number!")
				return False
			except Exception:
				tkMessageBox.showinfo("Input must be in the range [1-9]!")
				return False
	return True

def valid(grid):
	#check rows:
	for i in range(0, 81, 9):
		row = [grid[j].get() for j in range(i, i+9) if grid[j].get()]
		if len(row) != len(set(row)): return False
	for i in range(9):
		column = [grid[j].get() for j in range(i, 81, 9) if grid[j].get()]
		if len(column) != len(set(column)): return False
	for i in [10, 13, 16, 37, 40, 43, 64, 67, 70]:
		temp = grid[i-9-1:i-9+2] + grid[i-1:i+2] +  grid[i+9-1:i+9+2]
		box = [temp[j].get() for j in range(9) if temp[j].get()]
		if len(box) != len(set(box)): return False

	return True

def prepare(grid):
	for cell in grid:
		if cell is not None and cell.get() != "":
			cell.config(state=tk.DISABLED)
	submit.config(state=tk.DISABLED)

def algo(grid, index):
	if not valid(grid):
		return False
	elif index == len(grid):
		return True
	elif grid[index]['state'] == 'disabled':
		return algo(grid, index + 1)
	else:
		nums = range(1,10)
		random.shuffle(nums)
		for i in nums:
			grid[index].insert(0, str(i))
			window.update()
			if not algo(grid, index+1):
				grid[index].delete(0, tk.END)
				window.update()
			else:
				return True
	return False

def solve():
	if not validInput(grid):
		return
	if not valid(grid):
		tkMessageBox.showinfo("The problem is invalid!")
		return
	prepare(grid)
	status['text'] = 'Solving...'
	if algo(grid, 0): 
		status['text'] = "Success!"
	else:
		status['text'] = "FAILUURE!"


submit = tk.Button(window, text="Solve", command=solve)
submit.grid(row = 10, columnspan=5)
status = tk.Label(window, text="Enter a puzzle")
status.grid(row = 10, column=6, columnspan=5, pady=3)


window.mainloop()

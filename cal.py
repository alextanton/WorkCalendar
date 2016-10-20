from Tkinter import * 
import ttk
import calendar

root = Tk()
root.title("Sup")

root.config(height=500, width=500)
frame = Frame(root, width="200")
var = StringVar(root)

def main():
	var.set("Select One")
	menu = OptionMenu(root, var, "Alex", "Dave", "Harambe")
	menu.place(relx=.25, rely=.1)

	button = Button(root, text="enter", command=selectDates)
	button.place(relx=.5, rely=.1)

	frame.place(relx=.5, rely=.5, anchor=CENTER)

	drawCalendar("gainsboro")

	root.mainloop()


def drawCalendar(color):
	cal = calendar.TextCalendar(calendar.SUNDAY)
	row = 0
	col = 0
	for day in ["Sun", "Mo", "Tu", "Wed", "Th", "Fri", "Sat"]:
		lbl1 = Label(frame, text=day, pady=3, padx=3, background=color)
		lbl1.grid(row = row, column = col)
		col = col + 1
	row = 1
	col = 0
	for i in cal.itermonthdays(2016,10):
		lbl1 = Label(frame, text=i, pady=3, padx=3, background=color)
		if(col < 7):
			lbl1.grid(row = row, column = col)
			col = col + 1
		else:
			row = row + 1
			col = 1
			lbl1.grid(row = row, column = 0)

def selectDates():
	name = var.get()

main()
from Tkinter import * 
import ttk
import calendar
import json
import datetime

currentMonth = datetime.date.today().month

months = []
for i in calendar.month_name:
	if(i != ""):
		months.append(i)

file = open("workconfig.json")
data = json.load(file)
names = []

labelArr = []
projectLabels = []
projects = []

root = Tk()
root.title("Work Calendar")

root.config(height=500, width=500)
frame = Frame(root, width="200")
var = StringVar(root)
month = StringVar(root)

def main():
	month.set("Month")
	monthMenu = OptionMenu(root, month, *months)
	monthMenu.place(relx=.32, rely=.68)

	button = Button(root, text="enter", command=clickMonth)
	button.place(relx=.57, rely=.68)

	var.set("Select One")
	menu = OptionMenu(root, var, *names)
	menu.place(relx=.32, rely=.25)

	button = Button(root, text="enter", command=clickEnter)
	button.place(relx=.57, rely=.25)

	frame.place(relx=.5, rely=.5, anchor=CENTER)

	drawCalendar("gainsboro", currentMonth)

	root.mainloop()


def drawCalendar(color, month):
	global labelArr
	cal = calendar.TextCalendar(calendar.SUNDAY)
	row = 0
	col = 0
	for day in ["Sun", "Mo", "Tu", "Wed", "Th", "Fri", "Sat"]:
		lbl1 = Label(frame, text=day, pady=3, padx=3, background=color)
		lbl1.grid(row = row, column = col)
		col = col + 1
	row = 1
	col = 0
	for i in cal.itermonthdays(2016, month):
		lbl1 = Label(frame, text=i, pady=3, padx=3, background=color)
		labelArr.append(lbl1)
		if(col < 7):
			lbl1.grid(row = row, column = col)
			col = col + 1
		else:
			row = row + 1
			col = 1
			lbl1.grid(row = row, column = 0)
			labelArr.append(lbl1)

def clickEnter():
	global labelArr
	for i in labelArr:
		i.configure(background="gainsboro")
	selectProjects()
	redrawCalLabels("red", None)

def selectProjects():
	global projectLabels
	global projects
	removeLabels(projectLabels)
	projectLabels = []
	name = var.get()
	for i in data["Schedule"]["Employees"]:
		if(i["name"] == name):
			projects = i["Projects"]
	dates = getEndDates(projects)
	y = .03
	for pro in range(len(dates)):
		y=y+.04
		end = dates[pro][0]+"/"+dates[pro][1]+"/"+dates[pro][2]
		proLabel = Label(root, text=str(projects[pro]) + " end: " + dates[pro][0]+"/"+dates[pro][1]+"/"+dates[pro][2], padx=3, pady=3)
		projectLabels.append(proLabel)
		proLabel.place(relx=.1, rely=y)

def removeLabels(array):
	for i in array:
		i.place_forget()


def getEndDates(pros):
	dates = []
	for i in pros:
		for p in data["ProjectList"]["Projects"]:
			if(i == p["name"]):
				end = p["end"].split("/")
				dates.append(end)
				end = formatDate(end)
	return dates

def formatDate(end):
	return datetime.date(int(end[2]), int(end[0]), int(end[1]))

def getNames():
	for i in data["Schedule"]["Employees"]:
		names.append(i["name"])

def clickMonth():
	calendarLabelZero()
	monthClicked = month.get()
	monthNum = months.index(monthClicked)
	global labelArr
	labelArr = []
	drawCalendar("gainsboro", monthNum+1)
	if(var.get() == "Select One"):
		return
	redrawCalLabels("red", None)
	

def redrawCalLabels(color, end):
	if(month.get() != "Month"):
		m = months.index(month.get())
		m = m+1
	else:
		m = datetime.date.today().month
	d = 1
	for i in labelArr:
		if(int(i.cget("text")) == 0):
			continue
		delta = datetime.date(2016, m, int(i.cget("text"))) - formatDate(getEndDates([projects[0]])[0])
		if(delta.days <= 0):
			i.configure(background=color)
		d = d + 1

def calendarLabelZero():
	global labelArr
	for i in labelArr:
		i.configure(text=0)
		i.configure(background="gainsboro")

getNames()
main()
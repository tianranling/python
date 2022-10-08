import tkinter
import threading
import detetime
import time
app = tkinter.TK()
app.overrideredirect(True)
app.attributes('topmost',1)
app.geometry('100*20+25+25')

labelDateTime = tkinter.Label(app,width=100)
labelDateTime.pack(fill=tkinter.BOTH,expand=tkinter.YES)
x=tkinter.IntVar(value=0)
y=tkinter.IntVar(value=0)
Move = tkinter.IntVar(value=0)
def onLeftButtonUp(event):
	canMove.set(0)
	labelDateTime.bind('<ButtonRelease1>',onLeftButtonUp)
def onLeftButtonMove(event):
	if canMove.get()==0:
		return
	newx = app.winfo_x()+(event.x-X.get())
	newy = app.winfo_y()+(event.y-Y.get())
	g = '100*20+'str(newx)+'+'+str(newy)
	app.geometry(g)
	labelDateTime.bind('<B1-Motion>',onLeftButtonMove)

	def nowDateTime():
		while still.get()==1:
			s = str(datetime.datetime.now())
			labelDateTime['text'] = s
			time.sleep(0.0)
	t = threading.thread(target=nowdateTime)
	t.daemon = Ture
	t.start()
	app.mainloop()
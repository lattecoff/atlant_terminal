"""

"""

import tkinter as tk
from tkinter import ttk


import serial
import serial.tools.list_ports



user_comport = serial.Serial(bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

comports_ls = list()
baudrates_ls = ["2400", "4800", "9600", "19200", "38400", "57600", "115200"]


"""
@return ls - list available comports.
"""
def get_available_comports():
	ls = []
	ports = serial.tools.list_ports.comports()

	for num in ports:
		ls.append(num.device)


	return ls


"""
@brief Selected number comport.
"""
def comport_selected(event):
	user_comport.port = cbox_avail_comp.get()
	field_out.insert(tk.END, user_comport.port + '\n')



"""
@brief Selected baudrate comport.
"""
def baudrate_selected(event):
	user_comport.baudrate = cbox_speed_comp.get()
	field_out.insert(tk.END, str(user_comport.baudrate) + '\n')


"""
@brief Open/Close comport.
"""
def comport_switch_state():
	if user_comport.is_open == False:
		user_comport.open()
		btn_comport_open.config (text="Close", fg="red")
	else:
		user_comport.close()
		btn_comport_open.config (text="Open", fg="green")



win = tk.Tk()
win.title("Atlant Terminal v0.1")
win.geometry("920x640")


comports_ls = get_available_comports()
print(comports_ls)


cbox_avail_comp = ttk.Combobox(win, values=comports_ls, state="readonly")
cbox_avail_comp.pack()
cbox_avail_comp.bind("<<ComboboxSelected>>", comport_selected)

cbox_speed_comp = ttk.Combobox(win, values=baudrates_ls)
cbox_speed_comp.pack()
cbox_speed_comp.bind("<<ComboboxSelected>>", baudrate_selected)

lbl_comp_num = tk.Label(win, text=str(user_comport.port))
lbl_comp_num.pack()

btn_comport_open = tk.Button(win, text="Open", fg="green", command=comport_switch_state)
btn_comport_open.pack()

field_out = tk.Text(win, height = 30, width = 124, font =("Arial", 9))
field_out.pack()



win.mainloop()
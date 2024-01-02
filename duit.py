from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Hitung Hitung")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

def add_data():
    global total_uang
    print( 'jumlah uang', jumlah_uang.get())
    print( 'keterangan', keterangan.get())
    total_uang.set(f"Total: {str(int(total_uang.get().split(' ')[1]) + int(jumlah_uang.get()))}")
    list_uang.insert('end', f'Rp. {jumlah_uang.get()}, {keterangan.get()}')
    
    jumlah_uang.set('')
    keterangan.set('')

ttk.Label(mainframe, text="Jumlah Uang").pack()

jumlah_uang = StringVar()
jumlah_uang_entry = ttk.Entry(mainframe, width=20, textvariable=jumlah_uang)
jumlah_uang_entry.pack()

ttk.Label(mainframe, text="Keterangan").pack()

keterangan = StringVar()
keterangan_entry = ttk.Entry(mainframe, width=20, textvariable=keterangan)
keterangan_entry.pack()

ttk.Button(mainframe, text="Tambah Catatan", command=add_data).pack()

list_uang = Listbox(mainframe, height=32)
list_uang.pack()
s = ttk.Scrollbar(root, orient=VERTICAL, command=list_uang.yview)
s.grid(column=1, row=0, sticky=(N,S))
list_uang['yscrollcommand'] = s.set

total_uang = StringVar(value="Total: 0")
ttk.Label(root, textvariable=total_uang).grid(column=0, row=1)

root.geometry('300x200')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.mainloop()


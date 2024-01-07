from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Hitung Hitung")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

def add_data(_args = False):
    global total_uang
    print( 'jumlah uang', jumlah_uang.get())
    print( 'keterangan', keterangan.get())

    try:
        total_uang = int(total_uang) + int(jumlah_uang.get())
        total_uang_text.set(f"Total: Rp. {str(total_uang)}")
        list_uang.insert('end', f'Rp. {jumlah_uang.get()}, {keterangan.get()}')
    
        jumlah_uang.set('')
        keterangan.set('')
    except:
        messagebox.showerror("Ups, ada error", "Harap isi jumlah uang dengan angka")
    

leftframe = ttk.Frame(mainframe, padding="3 3 12 12")
leftframe.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(leftframe, text="Jumlah Uang").grid(column=0, row=0, sticky=(N))

jumlah_uang = StringVar()
jumlah_uang_entry = ttk.Entry(leftframe, width=20, textvariable=jumlah_uang)
jumlah_uang_entry.grid(column=0, row=1, sticky=(N))

ttk.Label(leftframe, text="Keterangan").grid(column=0, row=2, sticky=(N))

keterangan = StringVar()
keterangan_entry = ttk.Entry(leftframe, width=20, textvariable=keterangan)
keterangan_entry.grid(column=0, row=3, sticky=(N))

ttk.Button(leftframe, text="Tambah Catatan", command=add_data).grid(column=0, row=4, sticky=(N), pady=10)

list_uang = Listbox(mainframe, height=10, width=40)
list_uang.grid(column=1, row=0, sticky=(E, W, N, S))
s = ttk.Scrollbar(mainframe, orient=VERTICAL, command=list_uang.yview)
s.grid(column=2, row=0, sticky=(N,S))
list_uang['yscrollcommand'] = s.set

total_uang = 0
total_uang_text = StringVar(value=f"Total: Rp. {total_uang}")
ttk.Label(root, textvariable=total_uang_text).grid(column=0, row=1)

mainframe.columnconfigure(0, weight=1)

root.geometry('600x300')

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# Tombol Enter untuk menambahkan data
root.bind("<Return>", add_data)

root.mainloop()


from tkinter import Tk, Label, Button, Entry, Text, Canvas, Frame, END, W, E

class F1App:
    def __init__(self, master):
        self.master = master
        master.title("Driver F1")

        self.frame_input = Frame(master)
        self.frame_input.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.label = Label(self.frame_input, text="Masukkan nama pembalap F1:")
        self.label.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = Entry(self.frame_input, width=30)
        self.entry.grid(row=0, column=1, padx=5)

        self.button = Button(self.frame_input, text="Tambahkan", command=self.tambah_pembalap)
        self.button.grid(row=0, column=2, padx=5)

        # Canvas (bendera kotak-kotak)
        self.canvas = Canvas(master, width=120, height=60, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=3, pady=5)

        kotak_size = 20
        for i in range(3):
            for j in range(6):
                warna = "black" if (i + j) % 2 == 0 else "white"
                self.canvas.create_rectangle(j * kotak_size, i * kotak_size,
                                             (j + 1) * kotak_size, (i + 1) * kotak_size,
                                             fill=warna, outline="gray")
                
        self.text_output = Text(master, height=8, width=50)
        self.text_output.grid(row=2, column=0, columnspan=3, pady=10)

    def tambah_pembalap(self):
        nama = self.entry.get()
        if nama.strip():
            self.text_output.insert(END, f"{nama} merupakan pembalap F1!\n")
            self.entry.delete(0, END)

root = Tk()
app = F1App(root)
root.mainloop()

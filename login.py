import tkinter
from tkinter import *
from tkinter import messagebox as mb

datUser = 'admin'
datPassword = '12345'


class DemoLogin:
    def __init__(self, induk, judul):
        self.induk = induk

        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)

        self.aturKomponen()

        self.entUser.focus_set()

    def aturKomponen(self):
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)

        # atur frame data
        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)

        # atur input username
        Label(frData, text='nama pengguna:').grid(row=0, column=0, sticky=W)
        self.entUser = Entry(frData)
        self.entUser.grid(row=0, column=1)

        # atur input password
        Label(frData, text='kata kunci:').grid(row=1, column=0, sticky=W)
        self.entPass = Entry(frData, show='*')
        self.entPass.grid(row=1, column=1)

        # atur cek --> perlihatkan kata kunci
        self.cek = IntVar()

        self.cbShowPass = Checkbutton(frData, text='lihat kata kunci',
                                      variable=self.cek, command=self.lihatPassword)
        self.cbShowPass.grid(row=2, column=1, sticky=E)

        # atur frame tombol
        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)

        # atur tombol login
        self.btnLogin = Button(frTombol, text='Login', command=self.prosesLogin)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)

        self.btnBatal = Button(frTombol, text='Batal', command=self.Tutup)
        self.btnBatal.pack(side=LEFT, fill=BOTH, expand=YES)

    def prosesLogin(self, event=None):
        # ambil data input dari pengguna
        nmUser = self.entUser.get()
        passUser = self.entPass.get()

        # logika pemrograman
        if nmUser == '':
            mb.showwarning('Pesan Salah', 'Nama User tidak boleh kosong!', parent=self.induk)
            self.entUser.focus_set()
        elif passUser == '':
            mb.showwarning('Pesan Salah', 'Kata Kunci tidak boleh kosong!', parent=self.induk)
            self.entPass.focus_set()
        elif (nmUser == datUser) and (passUser == datPassword):
            mb.showinfo("Login", "Selamat Tahun Baru 2013!!!", parent=self.induk)
            self.Tutup()
        else:
            mb.showwarning('Pesan Salah', 'Nama Pengguna atau Kata Kunci SALAH!!', parent=self.induk)
            self.Hapus()

    def lihatPassword(self, event=None):
        nilaiCek = self.cek.get()

        if nilaiCek == 1:
            self.entPass['show'] = ''
        else:
            self.entPass['show'] = '*'

    def Tutup(self, event=None):
        self.induk.destroy()

    def Hapus(self, event=None):
        self.entUser.delete(0, END)
        self.entPass.delete(0, END)
        self.entUser.focus_set()


if __name__ == '__main__':
    root = Tk()

    app = DemoLogin(root, ":: Demo Login Password ::")

    root.mainloop()
import tkinter as tk
from tkinter import messagebox, ttk

class ProgramGajiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Menghitung Gaji Karyawan")
        self.root.geometry("550x500")
        self.root.resizable(False, False)
        
        # Konstanta
        self.GAJI_POKOK = 3700000
        
        # Header
        header = tk.Label(
            root, 
            text="💼 Program Menghitung Gaji Karyawan 💼",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=15
        )
        header.pack(fill="x")
        
        # Frame utama
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.pack(fill="both", expand=True)
        
        # Input Nama Karyawan
        tk.Label(
            main_frame, 
            text="Nama Karyawan:",
            font=("Arial", 11)
        ).grid(row=0, column=0, sticky="w", pady=10)
        
        self.entry_nama = tk.Entry(main_frame, font=("Arial", 11), width=30)
        self.entry_nama.grid(row=0, column=1, pady=10, padx=10)
        
        # Input Ketidakhadiran
        tk.Label(
            main_frame, 
            text="Ketidakhadiran (hari):",
            font=("Arial", 11)
        ).grid(row=1, column=0, sticky="w", pady=10)
        
        self.entry_ketidakhadiran = tk.Entry(main_frame, font=("Arial", 11), width=30)
        self.entry_ketidakhadiran.grid(row=1, column=1, pady=10, padx=10)
        
        # Frame untuk opsi izin (awalnya tersembunyi)
        self.frame_izin = tk.Frame(main_frame)
        self.frame_izin.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Checkbox Izin
        self.var_izin = tk.BooleanVar()
        self.check_izin = tk.Checkbutton(
            self.frame_izin,
            text="Karyawan memiliki surat izin",
            variable=self.var_izin,
            font=("Arial", 10),
            command=self.toggle_total_izin
        )
        self.check_izin.pack(anchor="w")
        
        # Input Total Izin (tersembunyi awalnya)
        self.frame_total_izin = tk.Frame(self.frame_izin)
        
        tk.Label(
            self.frame_total_izin,
            text="Total izin tahun ini:",
            font=("Arial", 10)
        ).grid(row=0, column=0, sticky="w", padx=(20, 5))
        
        self.entry_total_izin = tk.Entry(self.frame_total_izin, font=("Arial", 10), width=10)
        self.entry_total_izin.grid(row=0, column=1)
        
        # Info gaji pokok
        info_frame = tk.Frame(main_frame, bg="#ecf0f1", relief="solid", bd=1)
        info_frame.grid(row=3, column=0, columnspan=2, pady=15, sticky="ew")
        
        tk.Label(
            info_frame,
            text=f"Gaji Pokok: Rp {self.GAJI_POKOK:,.0f}",
            font=("Arial", 11, "bold"),
            bg="#ecf0f1"
        ).pack(pady=10)
        
        # Tombol Hitung
        btn_hitung = tk.Button(
            main_frame,
            text="🧮 Hitung Gaji",
            command=self.hitung_gaji,
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        btn_hitung.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Tombol Reset
        btn_reset = tk.Button(
            main_frame,
            text="🔄 Reset",
            command=self.reset_form,
            font=("Arial", 10),
            bg="#95a5a6",
            fg="white",
            padx=20,
            pady=5,
            cursor="hand2"
        )
        btn_reset.grid(row=5, column=0, columnspan=2)
        
    def toggle_total_izin(self):
        """Tampilkan/sembunyikan input total izin"""
        if self.var_izin.get():
            self.frame_total_izin.pack(anchor="w", pady=5)
        else:
            self.frame_total_izin.pack_forget()
            self.entry_total_izin.delete(0, tk.END)
    
    def validasi_input(self):
        """Validasi semua input"""
        nama = self.entry_nama.get().strip()
        if not nama:
            messagebox.showwarning("Peringatan", "Nama karyawan harus diisi!")
            return False
        
        try:
            ketidakhadiran = int(self.entry_ketidakhadiran.get())
            if ketidakhadiran < 0:
                messagebox.showwarning("Peringatan", "Ketidakhadiran tidak boleh negatif!")
                return False
        except ValueError:
            messagebox.showwarning("Peringatan", "Ketidakhadiran harus berupa angka!")
            return False
        
        # Validasi total izin jika checkbox dicentang
        if self.var_izin.get() and ketidakhadiran > 0:
            try:
                total_izin = int(self.entry_total_izin.get())
                if total_izin < 0:
                    messagebox.showwarning("Peringatan", "Total izin tidak boleh negatif!")
                    return False
            except ValueError:
                messagebox.showwarning("Peringatan", "Total izin harus berupa angka!")
                return False
        
        return True
    
    def hitung_gaji(self):
        """Hitung gaji berdasarkan ketidakhadiran"""
        if not self.validasi_input():
            return
        
        nama = self.entry_nama.get().strip()
        ketidakhadiran = int(self.entry_ketidakhadiran.get())
        gaji = self.GAJI_POKOK
        
        # Kasus 1: Tidak ada ketidakhadiran - dapat bonus
        if ketidakhadiran == 0:
            bonus = (20 / 100) * gaji
            total_gaji = gaji + bonus
            
            pesan = f"🎉 SELAMAT!\n\n"
            pesan += f"Nama Karyawan: {nama}\n"
            pesan += f"Ketidakhadiran: {ketidakhadiran} hari\n\n"
            pesan += f"Gaji Pokok: Rp {gaji:,.0f}\n"
            pesan += f"Bonus (20%): Rp {bonus:,.0f}\n"
            pesan += f"{'='*40}\n"
            pesan += f"TOTAL GAJI: Rp {total_gaji:,.0f}"
            
            messagebox.showinfo("Hasil Perhitungan Gaji", pesan)
        
        # Kasus 2: Ada ketidakhadiran
        elif ketidakhadiran > 0:
            # Dengan surat izin
            if self.var_izin.get():
                try:
                    total_izin = int(self.entry_total_izin.get())
                    total_ketidakhadiran = total_izin + ketidakhadiran
                    
                    # Masih dalam batas izin (≤ 12 hari)
                    if total_ketidakhadiran <= 12:
                        pesan = f"✅ GAJI TETAP\n\n"
                        pesan += f"Nama Karyawan: {nama}\n"
                        pesan += f"Ketidakhadiran: {ketidakhadiran} hari (dengan izin)\n"
                        pesan += f"Total izin tahun ini: {total_ketidakhadiran} hari\n\n"
                        pesan += f"Status: Masih dalam batas izin (≤12 hari)\n\n"
                        pesan += f"TOTAL GAJI: Rp {gaji:,.0f}"
                        
                        messagebox.showinfo("Hasil Perhitungan Gaji", pesan)
                    
                    # Melebihi batas izin (> 12 hari)
                    else:
                        batas_izin = total_ketidakhadiran - 12
                        denda = (1 / 100) * batas_izin * gaji
                        total_gaji = gaji - denda
                        
                        pesan = f"⚠️ MELEBIHI BATAS IZIN\n\n"
                        pesan += f"Nama Karyawan: {nama}\n"
                        pesan += f"Total izin tahun ini: {total_ketidakhadiran} hari\n"
                        pesan += f"Melebihi batas: {batas_izin} hari\n\n"
                        pesan += f"Gaji Pokok: Rp {gaji:,.0f}\n"
                        pesan += f"Denda (1%/hari): Rp {denda:,.0f}\n"
                        pesan += f"{'='*40}\n"
                        pesan += f"TOTAL GAJI: Rp {total_gaji:,.0f}"
                        
                        messagebox.showwarning("Hasil Perhitungan Gaji", pesan)
                
                except ValueError:
                    messagebox.showerror("Error", "Total izin harus berupa angka!")
                    return
            
            # Tanpa surat izin - langsung kena denda
            else:
                denda = (1 / 100) * ketidakhadiran * gaji
                total_gaji = gaji - denda
                
                pesan = f"⚠️ KETIDAKHADIRAN TANPA IZIN\n\n"
                pesan += f"Nama Karyawan: {nama}\n"
                pesan += f"Ketidakhadiran: {ketidakhadiran} hari (tanpa izin)\n\n"
                pesan += f"Gaji Pokok: Rp {gaji:,.0f}\n"
                pesan += f"Denda (1%/hari): Rp {denda:,.0f}\n"
                pesan += f"{'='*40}\n"
                pesan += f"TOTAL GAJI: Rp {total_gaji:,.0f}"
                
                messagebox.showwarning("Hasil Perhitungan Gaji", pesan)
    
    def reset_form(self):
        """Reset semua input"""
        self.entry_nama.delete(0, tk.END)
        self.entry_ketidakhadiran.delete(0, tk.END)
        self.entry_total_izin.delete(0, tk.END)
        self.var_izin.set(False)
        self.frame_total_izin.pack_forget()
        self.entry_nama.focus()

# Jalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramGajiGUI(root)
    root.mainloop()
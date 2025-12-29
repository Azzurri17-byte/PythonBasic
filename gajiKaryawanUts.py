import tkinter as tk
from tkinter import ttk

class ModernAlert:
    """Custom modern alert dialog - Pop-up alert yang lebih keren dari messagebox standar"""
    def __init__(self, parent, title, message, alert_type="info"):
        self.result = None
        
        # Buat window baru untuk alert
        self.top = tk.Toplevel(parent)
        self.top.title("")
        self.top.geometry("450x280")
        self.top.resizable(False, False)
        self.top.configure(bg="white")
        
        # Set window agar selalu di depan parent dan grab focus
        self.top.transient(parent)
        self.top.grab_set()
        
        # Konfigurasi icon dan warna berdasarkan tipe alert
        icons = {
            "info": ("ℹ️", "#3498db"),       # Biru untuk info
            "success": ("✓", "#27ae60"),     # Hijau untuk sukses
            "warning": ("⚠", "#f39c12"),     # Kuning/Orange untuk warning
            "error": ("✕", "#e74c3c")        # Merah untuk error
        }
        
        icon, color = icons.get(alert_type, icons["info"])
        
        # Header dengan ikon
        header = tk.Frame(self.top, bg=color, height=70)
        header.pack(fill="x")
        
        # Label icon di header
        tk.Label(
            header,
            text=icon,
            font=("Arial", 32),
            bg=color,
            fg="white"
        ).pack(pady=15)
        
        # Title alert
        tk.Label(
            self.top,
            text=title,
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=(20, 10))
        
        # Frame untuk pesan
        msg_frame = tk.Frame(self.top, bg="white")
        msg_frame.pack(pady=10, padx=30, fill="both", expand=True)
        
        # Label pesan dengan word wrap
        tk.Label(
            msg_frame,
            text=message,
            font=("Arial", 10),
            bg="white",
            fg="#34495e",
            justify="left",
            wraplength=380  # Batas lebar teks sebelum wrap ke baris baru
        ).pack()
        
        # Tombol OK
        btn = tk.Button(
            self.top,
            text="OK",
            command=self.close,
            font=("Arial", 10, "bold"),
            bg=color,
            fg="white",
            width=15,
            height=2,
            relief="flat",
            cursor="hand2",
            bd=0
        )
        btn.pack(pady=20)
        
        # Hover effect untuk tombol OK
        btn.bind("<Enter>", lambda e: btn.config(bg=self._darken_color(color)))
        btn.bind("<Leave>", lambda e: btn.config(bg=color))
        
        # Posisikan alert di tengah layar
        self.center_window()
        
    def _darken_color(self, color):
        """Fungsi untuk membuat warna lebih gelap saat hover"""
        colors = {
            "#3498db": "#2980b9",
            "#27ae60": "#229954",
            "#f39c12": "#e67e22",
            "#e74c3c": "#c0392b"
        }
        return colors.get(color, color)
    
    def center_window(self):
        """Fungsi untuk menempatkan alert di tengah layar"""
        self.top.update_idletasks()
        x = (self.top.winfo_screenwidth() // 2) - (450 // 2)
        y = (self.top.winfo_screenheight() // 2) - (280 // 2)
        self.top.geometry(f"450x280+{x}+{y}")
    
    def close(self):
        """Fungsi untuk menutup alert"""
        self.top.grab_release()
        self.top.destroy()

# CLASS PROGRAM GAJI GUI - Aplikasi Utama
class ProgramGajiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Gaji Karyawan")
        self.root.geometry("900x800")
        self.root.configure(bg="#ecf0f1")
        
        # Konstanta gaji pokok
        self.GAJI_POKOK = 3700000
        
        # SETUP SCROLLABLE CONTAINER
        # Main container untuk semua elemen
        main_container = tk.Frame(root, bg="#ecf0f1")
        main_container.pack(fill="both", expand=True)
        
        # Canvas untuk membuat konten bisa di-scroll
        canvas = tk.Canvas(main_container, bg="#ecf0f1", highlightthickness=0)
        
        # Scrollbar vertikal
        scrollbar = tk.Scrollbar(main_container, orient="vertical", command=canvas.yview)
        
        # Frame yang akan berisi semua konten
        scrollable_frame = tk.Frame(canvas, bg="#ecf0f1")
        
        # Update scroll region saat konten berubah
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        # Tempatkan scrollable_frame di dalam canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        
        # Fungsi untuk center konten di canvas
        def update_scroll_region(event=None):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas_width = canvas.winfo_width()
            frame_width = scrollable_frame.winfo_reqwidth()
            x_position = max(0, (canvas_width - frame_width) // 2)
            canvas.coords(canvas.find_all()[0], x_position, 0)
        
        # Bind event untuk update posisi center
        scrollable_frame.bind("<Configure>", update_scroll_region)
        canvas.bind("<Configure>", update_scroll_region)
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack canvas dan scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # CONTENT WRAPPER
        # Wrapper untuk centering card
        content_wrapper = tk.Frame(scrollable_frame, bg="#ecf0f1")
        content_wrapper.pack(expand=True, pady=30)
        
        # CARD CONTAINER
        # Card utama dengan border
        card = tk.Frame(content_wrapper, bg="white", relief="raised", bd=2)
        card.pack(padx=40)
        
        # HEADER SECTION
        # Frame header dengan background gelap
        header_frame = tk.Frame(card, bg="#2c3e50", height=100)
        header_frame.pack(fill="x")
        
        # Icon emoji di header
        tk.Label(
            header_frame,
            text="💼",
            font=("Arial", 36),
            bg="#2c3e50",
            fg="white"
        ).pack(pady=(10, 0))
        
        # Judul aplikasi di header
        tk.Label(
            header_frame,
            text="Sistem Perhitungan Gaji Karyawan",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        ).pack(pady=(0, 10))
        
        # CONTENT AREA
        # Frame untuk semua konten form
        content = tk.Frame(card, bg="white")
        content.pack(fill="both", padx=50, pady=30)
        
        # INFO GAJI POKOK
        # Card info gaji pokok dengan background biru
        info_card = tk.Frame(content, bg="#3498db", height=60)
        info_card.pack(fill="x", pady=(0, 25))
        
        # Label gaji pokok
        tk.Label(
            info_card,
            text=f"Gaji Pokok: Rp {self.GAJI_POKOK:,.0f}",
            font=("Arial", 14, "bold"),
            bg="#3498db",
            fg="white"
        ).pack(pady=15)
        
        # INPUT NAMA KARYAWAN
        # Label untuk input nama
        tk.Label(
            content,
            text="Nama Karyawan",
            font=("Arial", 10),
            bg="white",
            fg="#000000"
        ).pack(anchor="w", pady=(0, 5))
        
        # Entry field untuk nama karyawan
        self.entry_nama = tk.Entry(
            content,
            font=("Arial", 12),
            bg="#ecf0f1",
            relief="flat",
            bd=0
        )
        self.entry_nama.pack(fill="x", ipady=10, ipadx=10, pady=(0, 15))
        
        # INPUT KETIDAKHADIRAN
        # Label untuk input ketidakhadiran
        tk.Label(
            content,
            text="Jumlah Ketidakhadiran (hari)",
            font=("Arial", 10),
            bg="white",
            fg="#000000"
        ).pack(anchor="w", pady=(0, 5))
        
        # Entry field untuk jumlah ketidakhadiran
        self.entry_ketidakhadiran = tk.Entry(
            content,
            font=("Arial", 12),
            bg="#ecf0f1",
            relief="flat",
            bd=0
        )
        self.entry_ketidakhadiran.pack(fill="x", ipady=10, ipadx=10, pady=(0, 15))
        
        # CHECKBOX IZIN
        # Frame untuk checkbox dengan background abu-abu
        izin_frame = tk.Frame(content, bg="#ecf0f1", relief="flat")
        izin_frame.pack(fill="x", pady=15)
        
        # Variable boolean untuk checkbox
        self.var_izin = tk.BooleanVar()
        
        # Checkbox untuk surat izin
        self.check_izin = tk.Checkbutton(
            izin_frame,
            text="  Karyawan memiliki surat izin resmi",
            variable=self.var_izin,
            font=("Arial", 11),
            bg="#ecf0f1",
            activebackground="#ecf0f1",
            command=self.toggle_total_izin,  # Panggil fungsi saat checkbox di-klik
            cursor="hand2"
        )
        self.check_izin.pack(anchor="w", padx=15, pady=10)
        
        # INPUT TOTAL IZIN (DINAMIS)
        # Frame untuk input total izin 
        self.izin_input_frame = tk.Frame(content, bg="white")
        
        # Label untuk input total izin
        tk.Label(
            self.izin_input_frame,
            text="Total izin tahun ini",
            font=("Arial", 10),
            bg="white",
            fg="#7f8c8d"
        ).pack(anchor="w", pady=(0, 5))
        
        # Entry field untuk total izin
        self.entry_total_izin = tk.Entry(
            self.izin_input_frame,
            font=("Arial", 12),
            bg="#ecf0f1",
            relief="flat",
            bd=0
        )
        self.entry_total_izin.pack(fill="x", ipady=10, ipadx=10)
        
        # TOMBOL AKSI
        # Frame untuk tombol-tombol (selalu di bawah)
        btn_frame = tk.Frame(content, bg="white")
        btn_frame.pack(pady=30, side="bottom")
        
        # Tombol Hitung Gaji 
        self.btn_hitung = tk.Button(
            btn_frame,
            text="Hitung Gaji",
            command=self.hitung_gaji,  # Panggil fungsi hitung_gaji saat diklik
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            width=18,
            height=2,
            relief="flat",
            cursor="hand2",
            bd=0
        )
        self.btn_hitung.pack(side="left", padx=10)
        
        # Tombol Reset
        self.btn_reset = tk.Button(
            btn_frame,
            text="Reset",
            command=self.reset_form,  # Panggil fungsi reset_form saat diklik
            font=("Arial", 12, "bold"),
            bg="#95a5a6",
            fg="white",
            width=18,
            height=2,
            relief="flat",
            cursor="hand2",
            bd=0
        )
        self.btn_reset.pack(side="left", padx=10)
        
        # HOVER EFFECTS UNTUK TOMBOL
        # Hover effect tombol Hitung (warna gelap saat mouse di atas)
        self.btn_hitung.bind("<Enter>", lambda e: self.btn_hitung.config(bg="#229954"))
        self.btn_hitung.bind("<Leave>", lambda e: self.btn_hitung.config(bg="#27ae60"))
        
        # Hover effect tombol Reset
        self.btn_reset.bind("<Enter>", lambda e: self.btn_reset.config(bg="#7f8c8d"))
        self.btn_reset.bind("<Leave>", lambda e: self.btn_reset.config(bg="#95a5a6"))
        
        # MOUSE WHEEL SCROLLING
        # Fungsi untuk scroll pakai mouse wheel
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    # FUNGSI TOGGLE INPUT TOTAL IZIN
    def toggle_total_izin(self):
        """Tampilkan/sembunyikan input total izin berdasarkan checkbox"""
        if self.var_izin.get():
            # Jika checkbox dicentang, tampilkan input total izin
            self.izin_input_frame.pack(fill="x", pady=(0, 15), before=self.izin_input_frame.master.winfo_children()[-1])
        else:
            # Jika checkbox tidak dicentang, sembunyikan dan kosongkan input
            self.izin_input_frame.pack_forget()
            self.entry_total_izin.delete(0, tk.END)
    
    # FUNGSI TAMPILKAN ALERT
    def show_alert(self, title, message, alert_type="info"):
        """Tampilkan custom modern alert"""
        ModernAlert(self.root, title, message, alert_type)

    # FUNGSI VALIDASI INPUT
    def validasi_input(self):
        """Validasi semua input sebelum perhitungan"""
        
        # Validasi nama karyawan tidak boleh kosong
        nama = self.entry_nama.get().strip()
        if not nama:
            self.show_alert("Input Tidak Lengkap", "Silakan masukkan nama karyawan terlebih dahulu.", "warning")
            return False
        
        # Validasi ketidakhadiran harus angka dan tidak negatif
        try:
            ketidakhadiran = int(self.entry_ketidakhadiran.get())
            if ketidakhadiran < 0:
                self.show_alert("Input Tidak Valid", "Jumlah ketidakhadiran tidak boleh bernilai negatif.", "error")
                return False
        except ValueError:
            self.show_alert("Input Tidak Valid", "Jumlah ketidakhadiran harus berupa angka.", "error")
            return False
        
        # Validasi total izin jika checkbox dicentang
        if self.var_izin.get() and ketidakhadiran > 0:
            try:
                total_izin = int(self.entry_total_izin.get())
                if total_izin < 0:
                    self.show_alert("Input Tidak Valid", "Total izin tidak boleh bernilai negatif.", "error")
                    return False
            except ValueError:
                self.show_alert("Input Tidak Valid", "Total izin harus berupa angka.", "error")
                return False
        
        return True

    # FUNGSI HITUNG GAJI - LOGIKA UTAMA
    def hitung_gaji(self):
        """Hitung gaji berdasarkan ketidakhadiran dan izin"""
        
        # Validasi input dulu
        if not self.validasi_input():
            return
        
        # Ambil data dari input
        nama = self.entry_nama.get().strip()
        ketidakhadiran = int(self.entry_ketidakhadiran.get())
        gaji = self.GAJI_POKOK
        
        # KASUS 1: TIDAK ADA KETIDAKHADIRAN (DAPAT BONUS)
        if ketidakhadiran == 0:
            bonus = (20 / 100) * gaji
            total_gaji = gaji + bonus
            
            # Format pesan hasil
            message = f"Nama: {nama}\n"
            message += f"Ketidakhadiran: {ketidakhadiran} hari\n\n"
            message += f"Gaji Pokok: Rp {gaji:,.0f}\n"
            message += f"Bonus Kehadiran (20%): + Rp {bonus:,.0f}\n"
            message += f"━━━━━━━━━━━━━━━━━━━━━━━\n"
            message += f"Total Gaji: Rp {total_gaji:,.0f}"
            
            # Tampilkan alert sukses
            self.show_alert("Selamat! Bonus Kehadiran", message, "success")
        
        # KASUS 2: ADA KETIDAKHADIRAN
        elif ketidakhadiran > 0:
            
            # Sub Kasus A: Dengan Surat Izin
            if self.var_izin.get():
                total_izin = int(self.entry_total_izin.get())
                total_ketidakhadiran = total_izin + ketidakhadiran
                
                # Cek apakah masih dalam batas izin (≤ 12 hari)
                if total_ketidakhadiran <= 12:
                    # Gaji tetap, tidak ada potongan
                    message = f"Nama: {nama}\n"
                    message += f"Ketidakhadiran: {ketidakhadiran} hari (berizin)\n"
                    message += f"Total izin tahun ini: {total_ketidakhadiran}/12 hari\n\n"
                    message += f"Status: Masih dalam batas izin\n"
                    message += f"━━━━━━━━━━━━━━━━━━━━━━━\n"
                    message += f"Total Gaji: Rp {gaji:,.0f}"
                    
                    self.show_alert("Gaji Tetap", message, "info")
                
                else:
                    # Melebihi batas izin, kena denda untuk kelebihan hari
                    batas_izin = total_ketidakhadiran - 12
                    denda = (1 / 100) * batas_izin * gaji
                    total_gaji = gaji - denda
                    
                    message = f"Nama: {nama}\n"
                    message += f"Total izin tahun ini: {total_ketidakhadiran} hari\n"
                    message += f"Melebihi batas izin: {batas_izin} hari\n\n"
                    message += f"Gaji Pokok: Rp {gaji:,.0f}\n"
                    message += f"Denda (1%/hari): - Rp {denda:,.0f}\n"
                    message += f"━━━━━━━━━━━━━━━━━━━━━━━\n"
                    message += f"Total Gaji: Rp {total_gaji:,.0f}"
                    
                    self.show_alert("Melebihi Batas Izin", message, "warning")
            
            # Sub Kasus B: Tanpa Surat Izin (Langsung Kena Denda) 
            else:
                denda = (1 / 100) * ketidakhadiran * gaji
                total_gaji = gaji - denda
                
                message = f"Nama: {nama}\n"
                message += f"Ketidakhadiran: {ketidakhadiran} hari (tanpa izin)\n\n"
                message += f"Gaji Pokok: Rp {gaji:,.0f}\n"
                message += f"Denda (1%/hari): - Rp {denda:,.0f}\n"
                message += f"━━━━━━━━━━━━━━━━━━━━━━━\n"
                message += f"Total Gaji: Rp {total_gaji:,.0f}"
                
                self.show_alert("Potongan Gaji", message, "warning")
    
    # FUNGSI RESET FORM
    def reset_form(self):
        """Reset semua input ke kondisi awal"""
        self.entry_nama.delete(0, tk.END)
        self.entry_ketidakhadiran.delete(0, tk.END)
        self.entry_total_izin.delete(0, tk.END)
        self.var_izin.set(False)
        self.izin_input_frame.pack_forget()
        self.entry_nama.focus()  # Set fokus ke input nama

# JALANKAN APLIKASI
if __name__ == "__main__":
    root = tk.Tk()
    app = ProgramGajiGUI(root)
    root.mainloop()
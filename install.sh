#!/bin/bash
# Konfigurasi warna
hijau="\033[1;32m"
merah="\033[1;31m"
biru="\033[1;34m"
putih="\033[0m"

# Fungsi untuk instalasi paket
pasang_paket() {
    echo -e "${biru}>${putih} memasang paket: ${hijau}$1${putih}"
    if sudo apt-get install -y $1; then
        echo -e "${biru}>${putih} ${hijau}berhasil${putih} memasang paket $1"
    else
        echo -e "${biru}>${putih} ${merah}gagal${putih} memasang paket $1"
        exit 1
    fi
}

# Fungsi untuk memasang modul python
pasang_modul_python() {
    echo -e "${biru}>${putih} memasang modul python: ${hijau}$1${putih}"
    if pip3 install $1; then
        echo -e "${biru}>${putih} ${hijau}berhasil${putih} memasang modul $1"
    else
        echo -e "${biru}>${putih} ${merah}gagal${putih} memasang modul $1"
        exit 1
    fi
}

echo -e "${biru}>${putih} Persiapan Instalasi Dependensi"
echo -e "${biru}>${putih} Mempersiapkan instalasi dependensi..."
sleep 2

# Update repositori paket
echo -e "${biru}>${putih} Memperbarui repositori paket..."
sudo apt-get update

# Memasang dependensi yang dibutuhkan
pasang_paket "default-jdk"
pasang_paket "aapt zipalign"
pasang_paket "apktool"
pasang_paket "imagemagick"
pasang_paket "python3 python3-pip"

# Memasang modul Python
pasang_modul_python "Pillow"

echo -e "${biru}>${putih} ${hijau}Semua dependensi berhasil dipasang!${putih}"
echo -e "${biru}>${putih} Gunakan perintah ${hijau}python3 aplikasi.py${putih} untuk memulai program"
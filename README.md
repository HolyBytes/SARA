## 🚨 Peringatan Penting

Alat ini dibuat hanya untuk tujuan pendidikan dan tidak boleh digunakan untuk merugikan orang lain. Penulis tidak bertanggung jawab atas masalah atau kerusakan yang disebabkan oleh program ini. Penggunaan untuk kegiatan ilegal dapat dikenakan sanksi hukum.

## ✨ Fitur Utama

Pengguna dapat mengubah sesuai keinginan:
- `app_icon` - Ubah ikon aplikasi
- `app_name` - Ubah nama aplikasi
- `alert_title` - Ubah judul peringatan
- `alert_desc` - Ubah deskripsi peringatan
- `key_pass` - Ubah kunci untuk membuka perangkat

## 📥 Cara Instalasi

### Untuk Ubuntu, Kali Linux, dan macOS:
```bash
git clone https://github.com/HolyBytes/SARA.git
cd SARA
sudo bash install.sh
```

### Untuk Termux Android (Butuh ROOT):
```bash
apt-get install tsu git imagemagick python -y
python3 -m pip install Pillow
git clone [https://github.com/R1punk/SARA](https://github.com/HolyBytes/SARA.git)
cd SARA
tsu
bash installtermux.sh
python3 tehsara.py
```

## ❓ Pemecahan Masalah

### Masalah Umum dan Solusinya

1. **Error: "Aapt not installed"**
   - Solusi: Pasang aapt dengan perintah `sudo apt-get install aapt` atau `pkg install aapt` (Termux)
   - Alternatif: Periksa path aapt dengan `which aapt` dan tambahkan ke PATH

2. **Error: "Cannot connect to Termux-API"**
   - Solusi: Pastikan Termux-API sudah terpasang dari Play Store
   - Solusi: Jalankan `pkg install termux-api` di Termux

3. **Error: "Failed to build APK"**
   - Solusi: Pastikan Apktool versi 2.4.0 terpasang
   - Solusi: Jalankan `sudo apt-get install apktool` atau `pkg install apktool`
   - Coba ulang dengan `apktool b temp -o app.apk`

4. **Error: "Signing failed"**
   - Solusi: Pastikan Java terpasang dengan benar
   - Periksa keberadaan keystore dengan `ls -la keystore.jks`
   - Regenerasi keystore: `keytool -genkey -v -keystore keystore.jks -alias alias_name -keyalg RSA -keysize 2048 -validity 10000`

5. **Error: "Imagemagick failure"**
   - Solusi: Pasang ulang Imagemagick dengan `sudo apt-get install imagemagick`
   - Untuk Termux: `pkg install imagemagick`

6. **Error: "Permission denied"**
   - Solusi: Jalankan sebagai root dengan `sudo` atau `tsu` (Termux)
   - Periksa izin file dengan `ls -la` dan perbaiki dengan `chmod +x namafile`

### Tips Tambahan

- Selalu perbarui repositori dengan `apt update` atau `pkg update` sebelum pemasangan
- Pastikan semua dependensi terpasang dengan benar
- Gunakan versi Python 3.7 atau lebih baru untuk kompatibilitas terbaik
- Jika mengalami error saat kompilasi, coba hapus folder temp dan coba lagi


## 📜 Lisensi

Hak Cipta https://github.com/HolyBytes

## ⚠️ Ingat Selalu

Alat ini dibuat untuk tujuan pendidikan saja. Kami tidak bertanggung jawab dan tidak mendukung penggunaan alat ini untuk aktivitas berbahaya, merugikan, atau ilegal.

---

Terima kasih sudah menggunakan alat ini dengan bijak! Jika ada pertanyaan atau saran, jangan ragu untuk berkontribusi atau membuat issue di repositori GitHub kami.

# Presentasi Proyek Minggu-15: Mini Simulasi Sistem Operasi
Topik : CPU Scheduling (FCFS) & Memory Management (FIFO)



## Anggota kelompok
1. Andri Dwi Yuliyanto (250202976)
2. Farhan Ramdhani (250202938)
3. Muhammad Fajri Abdullah (250202979)
4. M. Habibi Nur Ramadhan (250202949)
5. Rafi Nurul Fauzan (250202961) 



---

## 1. Pendahuluan
### Latar Belakang: Manajemen Sumber Daya Ekosistem Game
Sistem operasi modern wajib mengelola sumber daya secara efisien untuk menjaga performa. Dua tantangan kritisnya adalah pembagian waktu CPU dan keterbatasan RAM.

Studi Kasus: Simulasi ini mengambil konteks Ekosistem Game, di mana interaksi pengguna melibatkan proses update yang memakan waktu (CPU) dan perpindahan antar aplikasi yang intensif memori (RAM).
Dua Fenomena Utama:
- Antrean Update Game: Mengelola urutan instalasi/pembaruan berdasarkan waktu kedatangan pengguna.
- Manajemen Slot RAM: Mengelola pergantian aplikasi dalam memori fisik yang sangat terbatas (3 slot).

---

## 2. Arsitektur & Alur Data
### A. Desain Modular (Struktur Sistem)

- `main.py` : Titik masuk utama aplikasi yang menyediakan antarmuka menu (CLI) untuk interaksi pengguna.
- `scheduling.py` (CPU Core): Berisi implementasi algoritma FCFS untuk menghitung metrik waktu tunggu dan penyelesaian.
- `memory.py` (Memory Manager): Mengelola simulasi Page Replacement FIFO pada slot RAM yang terbatas.
- `utils.py` (Data Access Layer): Menangani pembacaan file eksternal (CSV) dari folder data/.

### B. Mekanisme Alur Data
#### 1. CPU Scheduling (FCFS)
- Prinsip: "First-Come, First-Served" – Proses dieksekusi berdasarkan urutan waktu kedatangan (Arrival Time).
- Proses: Data dari processes.csv diurutkan, lalu dihitung secara sekuensial (tanpa jeda).
- Output: Metrik efisiensi berupa Waiting Time (WT) dan Turnaround Time (TAT).

#### 2. Manajemen Memori (FIFO)
- Prinsip: "First-In, First-Out" – Jika RAM (3 slot) penuh, aplikasi yang masuk paling awal akan dihapus (evict) untuk memberi ruang aplikasi baru.
- Proses: Setiap akses aplikasi dicek: HIT (sudah ada di RAM) atau MISS (Page Fault).
- Output: Skor Hit Ratio untuk mengukur efisiensi pemuatan data.

---

## 3. Dockerisasi & Skenario Live Demo
#### A. Implementasi Docker 
- Solusi: Menjamin aplikasi berjalan sama di semua perangkat ("anti-error" beda OS).
- Konfigurasi:
    - Base Image: python:3.11-slim (Ringan & Cepat).
    - Isolasi: Semua file (.py & .csv) dibungkus dalam direktori `/app`.
    - Otomatisasi: Sistem langsung menjalankan main.py saat kontainer aktif.

#### B. Panduan Eksekusi (Live Demo)

- Build: 
```bash
docker build -t mini-os-simulator .
```
Fungsi : Merakit aplikasi menjadi satu image utuh.

Run: 
```bash
docker run -it mini-os-simulator
```
Fungsi: Menjalankan simulasi secara interaktif via terminal.

---
## 4. Hasil & Analisis
### A. Analisis CPU Scheduling (FCFS)
- Dataset: processes.csv (Satuan: Menit).
- Hasil: Berhasil menghitung metrik waktu secara otomatis dan sekuensial.
- Analisis: Satuan menit mencerminkan realita durasi update game. Namun, terdapat risiko Convoy Effect (proses singkat terhambat oleh proses lama di depannya).
- Kesimpulan: Stabil untuk urutan instalasi, namun efisiensi sangat bergantung pada urutan dataset.

### B. Analisis Manajemen Memori (FIFO)
- Dataset: pages.csv (Urutan Akses Aplikasi).
- Hasil: Tercatat Page Fault saat aplikasi baru diakses melebihi kapasitas 3 slot RAM.
- Analisis: Mekanisme pop(0) konsisten menghapus aplikasi yang pertama kali masuk. Hit Ratio menjadi indikator utama efisiensi penggunaan memori.
- Kesimpulan: Sangat mudah diprediksi, namun kurang optimal jika ada aplikasi penting yang sering dipanggil tapi terhapus karena faktor waktu masuk.

---

## 5. Kontributor 
| Nama dan NIM | Peran | Kontribusi |
|:---|:---|:----------|
| Farhan Ramdhani (250202938) | Project Lead & Integrator | <br> - Membuat struktur menu utama di main.py. <br> - Menggabungkan kode FCFS dan FIFO ke branch utama.<br>- Memastikan alur program antar modul tidak bentrok. |
| M. Habibi Nur Ramadhan (250202949) | Developer 1 (CPU Scheduling) | - Membuat logika algoritma FCFS di scheduling.py. <br>- Menghitung otomatis Start, Finish, TAT, dan WT.<br>- Menampilkan hasil penjadwalan dalam bentuk tabel. |
| Andri Dwi Yuliyanto (250202976) | Developer 2 (Page Replacement) |- Mengimplementasikan algoritma FIFO di memory.py. <br>- Menghitung Page Faults. <br>- Menampilkan visualisasi perpindahan frame. |
| Rafi nurul fauzan (250202961) | DevOps & Docker Engineer | - Membuat Dockerfile. <br>- Menangani konfigurasi. <br>- Memastikan aplikasi dapat berjalan di dalam container Docker.|
| Muhammad Fajri Abdullah (250202979 | Data Engineer & QA | - Menyiapkan dataset processes.csv dan pages.csv. <br>- Melakukan testing menyeluruh. <br>- Menyusun dokumentasi laporan.|

---
---
---
Terimakasih 
===
----
-----
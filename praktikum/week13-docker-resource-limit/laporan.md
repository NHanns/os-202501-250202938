
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Farhan Ramdhani  
- **NIM**   : 250202938  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

### 1. Isolasi Resource (Cgroups) :

Docker menggunakan fitur kernel Linux yang disebut Control Groups (cgroups) untuk membatasi, mencatat, dan mengisolasi penggunaan sumber daya (CPU, memori, disk I/O) pada setiap container.

### 2. CPU Shares & Quotas :

Pembatasan CPU memungkinkan kita menentukan berapa banyak waktu pemrosesan yang dapat digunakan container dari total CPU host, mencegah satu container memonopoli seluruh tenaga prosesor.

### 3. Memory Limit & OOM Killer :

Membatasi memori memastikan container tidak menggunakan RAM melebihi jatahnya. Jika container melampaui batas ini, kernel akan memicu Out Of Memory (OOM) Killer untuk menghentikan proses demi menjaga stabilitas sistem host.

### 4. Monitoring Efisiensi :

Penggunaan sumber daya yang terukur memungkinkan administrator untuk melakukan density packing (menjalankan banyak container di satu server) secara efisien tanpa risiko tabrakan resource.

---

## Ketentuan Teknis
- Sistem operasi host bebas (Windows/macOS/Linux). Disarankan memakai **Docker Desktop** (atau Docker Engine di Linux).
- Program berbasis **terminal**.
- Fokus penilaian pada **keberhasilan build & run container**, **penerapan resource limit**, serta **kualitas analisis**.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week13-docker-resource-limit/
├─ code/
│  ├─ Dockerfile
│  └─ app.*
├─ screenshots/
│  └─ hasil_limit.png
└─ laporan.md
```

---

## Langkah Pengerjaan
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
- Membangun Image :
docker build -t week13-resource-limit .

- Menjalankan Tanpa Batasan (Gambar 1) :
docker run --rm week13-resource-limit

- Menjalankan dengan Limit CPU & RAM (Gambar 2) :
docker run --rm --cpus="0.5" --memory="512m" week13-resource-limit

- Menjalankan untuk Tes OOM (Gambar 3) :
docker run --name tes-limit --cpus="0.5" --memory="50m" week13-resource-limit

- Mengecek Status OOM Killed (Gambar 3) :
docker inspect tes-limit --format='{{.State.OOMKilled}}'

- Monitoring Real-time (Gambar 4) :
docker stats
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram :

## 1. Kondisi Normal (Baseline)
![alt text](../week13-docker-resource-limit/screenshots/(1)%20Kondisi%20Normal%20(Baseline).png)
- Pada pengujian tahap pertama, container dijalankan tanpa adanya batasan sumber daya (default). Berdasarkan hasil output, aplikasi Python berhasil melakukan komputasi berat dengan waktu eksekusi yang sangat cepat, yaitu 1.1546 detik. Alokasi memori juga berjalan lancar hingga tahap 10 (total ~100 MB) tanpa hambatan, karena container memiliki akses penuh ke sumber daya host.

---

## 2. Dampak Limitasi CPU
![alt text](../week13-docker-resource-limit/screenshots/(2)%20Dampak%20Limitasi%20CPU.png)
- Pada pengujian kedua, diberikan batasan CPU sebesar 0.5 core. Hasilnya menunjukkan penurunan performa yang signifikan, di mana waktu eksekusi meningkat menjadi 2.3285 detik (hampir dua kali lipat lebih lambat dibandingkan kondisi normal). Hal ini membuktikan bahwa pembatasan CPU secara langsung mempengaruhi kecepatan pemrosesan data pada aplikasi.

---

## 3. Bukti OOM Killed (Limit RAM)
![alt text](../week13-docker-resource-limit/screenshots/(3)%20Bukti%20OOM%20Killed%20(Limit%20RAM).png)
- Pengujian ini dilakukan dengan membatasi memori (RAM) sangat ketat, yaitu hanya 50 MB. Saat aplikasi mencoba mengalokasikan data melebihi batas tersebut, Docker secara otomatis menghentikan paksa (kill) container tersebut. Hasil perintah inspect menunjukkan status 'true' pada OOMKilled, yang mengonfirmasi bahwa mekanisme pembatasan memori Docker bekerja dengan baik untuk menjaga kestabilan sistem host.

---

## 4. Monitoring Real-Time
![alt text](../week13-docker-resource-limit/screenshots/(4)%20Monitoring%20Real-Time.png)
- Melalui perintah docker stats, dilakukan monitoring secara real-time terhadap container yang sedang berjalan. Terlihat pada tabel statistik bahwa penggunaan CPU % tertahan di angka 51.05% (sesuai limit 0.5 core) dan MEM LIMIT terdeteksi sebesar 512 MiB. Screenshot ini menjadi bukti visual bahwa Docker secara aktif menjaga penggunaan resource agar tidak melebihi batas yang telah ditentukan dalam konfigurasi.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

- Limitasi Berpengaruh pada Kecepatan: Pembatasan CPU (--cpus) terbukti secara langsung memperlambat waktu komputasi aplikasi; dalam percobaan ini, penggunaan 0.5 core meningkatkan waktu eksekusi dari ~1.1 detik menjadi ~2.3 detik.

- Keamanan Memori melalui OOM: Docker berhasil menghentikan aplikasi secara paksa (status OOMKilled: true) ketika penggunaan memori melebihi ambang batas yang ditentukan (50MB), membuktikan bahwa sistem proteksi resource bekerja sesuai konfigurasi.

- Transparansi Resource: Melalui fitur docker stats, kita dapat memantau secara real-time bahwa container benar-benar patuh pada batasan yang diberikan, yang sangat penting untuk manajemen infrastruktur cloud.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori? 

   **Jawaban :**  Untuk mencegah fenomena "Noisy Neighbor", di mana satu container yang boros sumber daya (atau mengalami memory leak) menghabiskan seluruh tenaga server sehingga menyebabkan container lain atau sistem host itu sendiri menjadi tidak stabil atau crash.

2. Apa perbedaan VM dan container dalam konteks isolasi resource?

   **Jawaban :**  VM (Virtual Machine) membatasi resource secara kaku di tingkat hardware virtual sejak awal (mengalokasikan porsi RAM/CPU tetap dari host), sedangkan Container berbagi kernel host yang sama dan pembatasannya bersifat lebih fleksibel melalui cgroups di tingkat sistem operasi.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?  

   **Jawaban :**  Aplikasi akan mengalami penghentian paksa oleh sistem (OOM Killed) jika mencoba mengalokasikan RAM melebihi batas yang ditentukan Docker. Hal ini mencegah aplikasi tersebut merusak stabilitas aplikasi lain, namun aplikasi itu sendiri tidak akan bisa menyelesaikan tugasnya jika batasannya terlalu kecil.

---

## Refleksi Diri
Tuliskan secara singkat:
### 1.Apa bagian yang paling menantang minggu ini?  

**Jawaban :**   Bagian paling menantang adalah menangani error SyntaxError: Non-UTF-8 code dan build error pada Docker snapshot yang sempat menghentikan proses pembuatan image. Selain itu, melakukan monitoring docker stats tepat pada saat aplikasi berjalan cepat juga membutuhkan ketelitian.


### 2.Bagaimana cara Anda mengatasinya?  

**Jawaban :**  Saya mengatasinya dengan memastikan file kode disimpan menggunakan encoding UTF-8 secara manual di VS Code, melakukan pembersihan cache Docker menggunakan perintah docker builder prune, serta memodifikasi beban kerja skrip Python agar berjalan sedikit lebih lama sehingga pemantauan resource lebih mudah dilakukan.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_

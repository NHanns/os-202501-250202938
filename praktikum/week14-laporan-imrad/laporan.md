<center>

# Analisis Perbandingan Algoritma Penjadwalan FCFS dan SJF
**Nama**: Farhan Ramdhani | **NIM**: 250202938 | **Kelas**: 1IKRB

---

</div>

## 1. Pendahuluan (Introduction)

### A. Latar Belakang

Dalam ekosistem sistem operasi modern, manajemen proses merupakan tanggung jawab fundamental `kernel` untuk mengoptimalkan penggunaan unit pemrosesan pusat atau `CPU Utilization` (*Silberschatz et al., 2018*). Tantangan utama muncul ketika terdapat antrean proses yang kompetitif dalam memperebutkan slot eksekusi pada ready queue. Tanpa mekanisme penjadwalan yang efisien, sistem dapat mengalami penurunan performa secara drastis, ketidakadilan distribusi sumber daya, hingga risiko starvation pada proses-proses tertentu (*Stallings, 2017*).

Praktikum ini mengevaluasi dua algoritma dasar: `First Come First Served (FCFS)` yang bekerja berdasarkan prinsip antrean linier kronologis, dan `Shortest Job First (SJF)` yang menggunakan pendekatan optimasi berbasis durasi eksekusi terkecil. Pemahaman mengenai karakteristik kedua algoritma ini sangat krusial untuk meminimalkan waktu tunggu rata-rata `(Average Waiting Time)` dan meningkatkan throughput sistem secara keseluruhan (*Silberschatz et al., 2018*).

---

### B. Rumusan Masalah

**1.** Bagaimana perbedaan performa antara algoritma *`First Come First Served`* `(FCFS)` dan *`Shortest Job First`* `(SJF)` dalam menangani proses dengan *`Burst Time`* yang bervariasi?

**2.** Seberapa besar pengaruh urutan kedatangan proses terhadap efisiensi waktu tunggu pada algoritma `FCFS`?

---

### C. Tujuan

**1.** Mengukur dan membandingkan efisiensi kedua algoritma berdasarkan metrik *`Average Waiting Time`* `(AWT)`.

**2.** Menganalisis korelasi antara *`Burst Time`* dengan nilai *`Average Turnaround Time`* `(ATRT)`.

---

## 2. Metode (Methods)

* **Lingkungan Uji**: Simulasi dijalankan pada lingkungan Python menggunakan skrip `scheduling_simulation.py` dengan dukungan pustaka `csv` untuk pemrosesan data input secara otomatis.
* **Parameter/Dataset**: Dataset `dataset.csv` mencakup 4 proses (P1-P4) dengan rincian *`Arrival Time`* (0, 1, 2, 3) dan `*Burst Time*` yang bervariasi antara 3 ms hingga 8 ms.
* **Langkah Eksperimen**: 
    1. Program membaca file `dataset.csv` dan menyimpan data ke dalam struktur list.
    2. Melakukan pengurutan proses berdasarkan waktu kedatangan untuk simulasi `FCFS`.
    3. Menghitung waktu tunggu (*`Waiting Time`*) dengan rumus $WT = Start Time - Arrival Time$.
    4. Menghitung waktu putar (*`Turnaround Time`*) dengan rumus $TAT = Finish Time - Arrival Time$.
* **Cara Pengukuran**: Efisiensi dinilai berdasarkan perbandingan rata-rata statistik waktu tunggu `(AWT)` dan waktu putar `(ATRT)` dari seluruh proses yang berhasil dieksekusi.

---

## 3. Hasil (Results)
Hasil simulasi menunjukkan keunggulan signifikan dari algoritma `SJF` dibandingkan `FCFS`.

---

![alt text](../week14-laporan-imrad/screenshots/hasil_simulasi%20week%209.png.png)

---

## **Tabel Perbandingan Metrik Performa Penjadwalan**

| Algoritma | Average Waiting Time (AWT) | Average Turnaround Time (ATRT) |
| :--- | :--- | :--- |
| **FCFS** | 12.80 ms | 19.40 ms |
| **SJF** | 9.00 ms | 15.60 ms |

</div>

**Ringkasan Temuan**: 
1. **Reduksi Waktu Tunggu yang Signifikan**: Implementasi algoritma `SJF` berhasil mereduksi rata-rata waktu tunggu sebesar **29.7%** (dari 12.80 ms menjadi 9.00 ms). Hal ini membuktikan bahwa pengurutan berdasarkan durasi terkecil sangat efektif dalam meminimalkan antrean kumulatif.

2. **Optimalisasi Siklus Hidup Proses**: Nilai *`Average Turnaround Time`* pada `SJF` menunjukkan penurunan sebesar **3.80 ms**. Temuan ini mengindikasikan bahwa secara kolektif, sistem mampu menyelesaikan seluruh rangkaian tugas dalam waktu yang lebih singkat dibandingkan metode antrean linier.

3. **Penyelesaian Masalah Penundaan**: Melalui visualisasi Gantt Chart, teramati bahwa `SJF` memberikan prioritas pada proses ringan (P3 dan P5), sehingga mencegah terjadinya penumpukan waktu tunggu yang ekstrem bagi proses-proses kecil di dalam sistem.

4. **Analisis Efisiensi**: Data menunjukkan bahwa semakin tinggi variasi *`Burst Time`* dalam sebuah antrean, semakin besar keunggulan efisiensi yang ditawarkan oleh algoritma `SJF` dibandingkan `FCFS`.

---

## 4. Pembahasan (Discussion)
### A. Interpretasi Hasil

Tingginya nilai `AWT` pada `FCFS` disebabkan karena proses yang datang lebih awal (P1) harus diselesaikan sepenuhnya sebelum proses berikutnya dapat dimulai, tanpa melihat efisiensi waktu eksekusi. Hal ini memicu penundaan bagi proses lain yang mungkin memiliki beban kerja lebih ringan. Sebaliknya, `SJF` melakukan evaluasi terhadap `*Burst Time*` yang tersedia, sehingga meminimalkan beban tunggu bagi mayoritas proses dalam antrean.

### B. Perbandingan Teori 

Temuan ini memvalidasi teori *`Shortest-Job-First Scheduling`* yang menyatakan bahwa algoritma ini optimal karena secara matematis memberikan rata-rata waktu tunggu minimum untuk sekumpulan proses statis maupun dinamis.

### C. Keterbatasan

 Simulasi ini bersifat *`non-preemptive`*. Dalam kondisi sistem *`real-time`* yang sangat dinamis dengan kedatangan proses yang terus-menerus, algoritma `SJF` mungkin memerlukan mekanisme *`preemption`* agar tidak terjadi *`starvation`* pada proses dengan durasi besar yang terus tergeser oleh proses kecil yang baru datang.

---

## 5. Kesimpulan
1. **SJF secara konsisten lebih unggul** daripada `FCFS` dalam mengoptimalkan waktu tunggu rata-rata pada dataset yang memiliki variasi durasi kerja.
2. **Urutan Kedatangan** pada `FCFS` dapat menjadi faktor penghambat efisiensi jika proses awal memiliki durasi kerja yang panjang (*`Convoy Effect`*).
3. **Simulasi Python** menyediakan validasi empiris yang akurat untuk memahami mekanisme internal penjadwalan `CPU` pada sistem operasi secara kuantitatif.

---

## Daftar Pustaka
1. Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts*. 10th Edition. Wiley.

2. Stalling, W. (2017). *Operating Systems: Internals and Design Principles*. 9th Edition. Pearson.
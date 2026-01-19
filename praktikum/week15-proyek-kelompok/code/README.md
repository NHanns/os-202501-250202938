
```markdown
# 🎮 Mini OS Simulator - Simulasi Penjadwalan CPU & Manajemen Memori

Aplikasi terminal untuk simulasi **FCFS Scheduling** dan **FIFO Page Replacement** dengan tema Gaming.

## 📋 Fitur
- ✅ **Modul 1**: CPU Scheduling FCFS (Antrean Update Game)
- ✅ **Modul 2**: Memory Management FIFO (RAM HP Gaming)
- ✅ Dataset gaming-themed (PUBG, Delta Force, dll)
- ✅ Menu CLI interaktif
- ✅ Output tabel ASCII yang rapi

## 🚀 Cara Menjalankan

### 1. Local (Python langsung)
```bash
cd code/
python main.py
```
*Pilih menu 1 (FCFS) atau 2 (FIFO)*

### 2. Docker (Recommended untuk Demo)
```bash
cd code/
docker build -t week15-proyek-kelompok .
docker run --rm week15-proyek-kelompok          # Demo cepat
docker run --rm -it week15-proyek-kelompok      # Interactive
```

## 📁 Struktur Folder
```
code/
├── main.py          # Menu utama CLI
├── scheduling.py    # FCFS Algorithm
├── memory.py        # FIFO Page Replacement
├── utils.py         # Data loader (CSV parser)
├── data/
│   ├── processes.csv
│   └── pages.csv
├── Dockerfile
└── README.md

📁 ../screenshots/     ← BUAT FOLDER INI!
│   ├── demo_run.png
│   └── hasil_tabel.png
└── ../laporan.md
```

## 📊 Contoh Output

**FCFS (Menu 1):**
```
Rata-rata Waktu Tunggu (WT): 4.75
Rata-rata Total Waktu (TAT): 10.75
```

**FIFO (Menu 2):**
```
HP Anda mengalami 6 kali loading ulang
Hit Ratio: 14.29%
```

## 📸 Screenshot Presentasi
```
demo_run.png:    docker run --rm week15-proyek-kelompok
hasil_tabel.png: docker run --rm -it week15-proyek-kelompok (menu 1/2)
```

## 🧑‍💻 Demo Commands
```bash
docker build -t week15-proyek-kelompok .
docker run --rm week15-proyek-kelompok
docker run --rm -it week15-proyek-kelompok
```

## 👥 Pembagian Kerja
```
Project Lead: [Nama] - Docker + Integrasi
Dev 1: [Nama] - FCFS Scheduling
Dev 2: [Nama] - FIFO Memory
QA/Docs: [Nama] - Testing + README
```

## ✅ Status Proyek
```
✅ Code berjalan (local + Docker)
✅ 2 Modul OS (FCFS + FIFO)
✅ Dataset gaming theme
✅ Tabel output rapi
✅ Docker reproducible
🎯 SIAP PRESENTASI!
```

```

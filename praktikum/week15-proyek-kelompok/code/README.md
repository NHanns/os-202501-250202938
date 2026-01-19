
Proyek Simulator OS Kelompok

Fitur
- Simulasi FCFS CPU Scheduling  
- Simulasi FIFO Memory Management
- Tema data game (PUBG, Genshin, dll)
- Tabel output ASCII rapi
- Support Python lokal + Docker

Struktur Folder
```
code/
├── main.py        # Menu utama
├── scheduling.py  # FCFS logic  
├── memory.py      # FIFO logic
├── utils.py       # CSV parser
├── data/
│   ├── processes.csv
│   └── pages.csv
├── Dockerfile
└── README.md
```

Cara Menjalankan

 1. Persiapan
Buka Command Prompt (CMD) di folder proyek:
```
os-202501-250202938\praktikum\week15-proyek-kelompok>
```
2. Versi Local (Python langsung)
```
cd code
python main.py
```
- Pilih menu 1 atau 2
- Tekan Enter setelah selesai
- Pilih menu 3 untuk keluar

 3. Versi Docker
```
Langkah 1: Build 
docker build -t week15-proyek-kelompok .

Langkah 2: Jalankan demo
docker run --rm week15-proyek-kelompok

Langkah 3: Jalankan interaktif (bisa pilih menu)
docker run --rm -it week15-proyek-kelompok
```

Konfigurasi Dataset
Edit file di folder `code/data/`:

processes.csv (FCFS):
```
ProcessID,ArrivalTime,BurstTime
PUBG,0,5
Delta Force,1,7
Arena Breakout,2,4
War Thunder,3,8
```
![Dataset](data/processes.csv)

pages.csv (FIFO):
```
PUBG, Delta Force, Arena Breakout, War Thunder, PUBG, Delta Force, War Thunder
```

![Dataset](data/pages.csv)

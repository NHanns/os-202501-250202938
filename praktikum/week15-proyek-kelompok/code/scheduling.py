import os
import csv

def read_processes(filename):
    processes = []
    # Mengambil path folder tempat file scheduling.py berada
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Menggabungkan dengan folder data
    file_path = os.path.join(current_dir, 'data', filename)

    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                processes.append({
                    'ProcessID': row['ProcessID'],
                    'ArrivalTime': int(row['ArrivalTime']),
                    'BurstTime': int(row['BurstTime'])
                })
        return processes
    except Exception as e:
        print(f"Error membaca file: {e}")
        return []

def fcfs_algorithm(data_proses):
    # 1. Urutkan berdasarkan Arrival Time (Waktu Klik Update)
    data_proses.sort(key=lambda x: x['ArrivalTime'])

    # Menambahkan judul konteks simulasi agar lebih jelas
    print("\n" + "="*85)
    print(" " * 30 + "ANTREAN UPDATE GAME")
    print("="*85)
    print(f"{'Game ID':<20} | {'Arrival':<8} | {'Burst':<6} | {'Start':<6} | {'Finish':<7} | {'WT':<5} | {'TAT':<4}")
    print("-" * 85)

    current_time = 0
    total_wt = 0
    total_tat = 0

    for p in data_proses:
        # Jika CPU/Disk menganggur menunggu jadwal update berikutnya
        if current_time < p['ArrivalTime']:
            current_time = p['ArrivalTime']
        
        # Start: Waktu mulai proses patching/install
        start_time = current_time
        # Finish: Waktu game selesai di-update
        finish_time = start_time + p['BurstTime']
        
        # Perhitungan TAT (Total durasi) & WT (Waktu Pending)
        tat = finish_time - p['ArrivalTime']
        wt = tat - p['BurstTime']
        
        total_wt += wt
        total_tat += tat
        
        # Cetak baris data dengan format kolom yang rapi
        print(f"{p['ProcessID']:<20} | {p['ArrivalTime']:<8} | {p['BurstTime']:<6} | "
              f"{start_time:<6} | {finish_time:<7} | {wt:<5} | {tat:<4}")
        
        # Update current_time ke waktu selesai proses terakhir
        current_time = finish_time

    # Statistik Rata-rata
    n = len(data_proses)
    print("-" * 85)
    print(f"Rata-rata Waktu Tunggu / Pending (WT)  : {total_wt/n:.2f}")
    print(f"Rata-rata Total Waktu Selesai (TAT)   : {total_tat/n:.2f}")
    print("="*85)
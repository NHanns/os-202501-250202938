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
    data_proses.sort(key=lambda x: x['ArrivalTime'])

    # 1. Tentukan lebar tiap kolom (Sesuaikan angka ini jika kolom kurang lebar)
    # Total lebar akan otomatis menyesuaikan
    w = {
        'id': 20, 'arr': 15, 'bur': 15, 
        'sta': 12, 'fin': 12, 'wt': 10, 'tat': 10
    }
    
    # Hitung total lebar untuk garis pembatas (jumlah semua kolom + spasi antar kolom)
    total_width = sum(w.values()) + 10 

    print("\n" + " " * (total_width // 3) + "ANTREAN UPDATE GAME")
    print("-" * total_width)
    
    # 2. Header
    header = (f"{'Game ID':<{w['id']}} {'Arrival':<{w['arr']}} {'Burst':<{w['bur']}} "
              f"{'Start':<{w['sta']}} {'Finish':<{w['fin']}} {'WT':<{w['wt']}} {'TAT':<{w['tat']}}")
    print(header)
    
    sub_header = (f"{'(Nama)':<{w['id']}} {'(Menit ke-)':<{w['arr']}} {'(Durasi Menit)':<{w['bur']}} "
                  f"{'(Menit ke-)':<{w['sta']}} {'(Menit ke-)':<{w['fin']}} {'(Menit)':<{w['wt']}} {'(Menit)':<{w['tat']}}")
    print(sub_header)
    print("-" * total_width)

    current_time = 0
    total_wt = 0
    total_tat = 0

    # 3. Data Rows
    for p in data_proses:
        if current_time < p['ArrivalTime']:
            current_time = p['ArrivalTime']
        
        start_time = current_time
        finish_time = start_time + p['BurstTime']
        tat = finish_time - p['ArrivalTime']
        wt = tat - p['BurstTime']
        
        total_wt += wt
        total_tat += tat
        
        print(f"{p['ProcessID']:<{w['id']}} {p['ArrivalTime']:<{w['arr']}} {p['BurstTime']:<{w['bur']}} "
              f"{start_time:<{w['sta']}} {finish_time:<{w['fin']}} {wt:<{w['wt']}} {tat:<{w['tat']}}")
        
        current_time = finish_time

    n = len(data_proses)
    print("-" * total_width)
    print(f"Rata-rata WT  : {total_wt/n:.2f} Menit")
    print(f"Rata-rata TAT : {total_tat/n:.2f} Menit")
    print("-" * total_width)
import csv
import os
import re

def load_processes(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, 'data', file_name)
    data = []
    if not os.path.exists(target_path):
        return data

    with open(target_path, mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                data.append({
                    'ProcessID': row['ProcessID'],
                    'ArrivalTime': int(row['ArrivalTime']),
                    'BurstTime': int(row['BurstTime'])
                })
            except Exception as e:
                print(f"[ERROR] Data bermasalah: {e}")
    return data

def load_pages(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_dir, 'data', file_name)

    if not os.path.exists(target_path):
        return []
    with open(target_path, mode='r') as file:
        content = file.read().strip()
        if not content: return []
        
        # PERBAIKAN: Pisahkan string berdasarkan koma atau baris baru
        # Kami tidak menggunakan .isdigit() agar nama aplikasi (string) bisa masuk
        raw_items = re.split(r'[,\n]+', content)
        # Menghapus spasi di sekitar nama aplikasi
        return [item.strip() for item in raw_items if item.strip()]

if __name__ == "__main__":
    # Bagian debugging tetap sangat berguna untuk Anggota 5 (QA)
    print("\n=== DEBUGGING DATA ENGINEER (ANGGOTA 5) ===")
    halaman = load_pages("pages.csv")
    print(f"-> Data Pages Terbaca: {halaman}")
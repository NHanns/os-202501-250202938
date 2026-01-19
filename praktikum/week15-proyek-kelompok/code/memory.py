def fifo_algorithm(daftar_klik_game, capacity=3):
    """Fungsi export untuk main.py - sesuai spesifikasi tugas"""
    simulasi_fifo_game(daftar_klik_game, kapasitas_ram=capacity)

def simulasi_fifo_game(daftar_klik_game, kapasitas_ram=3):
    """Fungsi utama simulasi FIFO (tetap sama)"""
    memori_ram = []
    page_faults = 0 
    
    print(f"\nKapasitas RAM HP: {kapasitas_ram} Slot Game")
    print(f"{'Step':<5} | {'Game Dibuka':<15} | {'Isi RAM Sekarang':<45} | {'Status'}")
    print("-" * 90)

    for step, game in enumerate(daftar_klik_game, 1):
        status = ""
        if game not in memori_ram:
            page_faults += 1
            status = "MISS (Loading Ulang)"
            
            if len(memori_ram) >= kapasitas_ram:
                game_dibuang = memori_ram.pop(0) 
                memori_ram.append(game)
                status += f" -> {game_dibuang} DIBUANG"
            else:
                memori_ram.append(game)
        else:
            status = "HIT (Lancar)"
        
        print(f"{step:<5} | {game:<15} | {str(memori_ram):<45} | {status}")

    total = len(daftar_klik_game)
    hits = total - page_faults
    print("-" * 90)
    print(f"Hasil Akhir: HP Anda mengalami {page_faults} kali loading ulang dan {hits} kali lancar.")
    print(f"Skor Kelancaran (Hit Ratio): {(hits/total)*100:.2f}%")

# HAPUS/HAPUSKAN test code di bawah (penyebab error awal)
# urutan_game = [...]  
# simulasi_fifo_game(urutan_game)
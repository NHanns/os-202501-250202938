import csv
import os

# ===============================
# BACA DATA DARI CSV
# ===============================
def read_processes(filename):
    processes = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            processes.append({
                'id': row['ProcessID'],
                'arrival': int(row['ArrivalTime']),
                'burst': int(row['BurstTime'])
            })
    return processes


# ===============================
# FCFS
# ===============================
def fcfs(processes):
    time = 0
    processes.sort(key=lambda x: x['arrival'])

    print("\n=== FCFS Scheduling ===")
    print("ID\tStart\tFinish\tWaiting\tTurnaround")

    for p in processes:
        if time < p['arrival']:
            time = p['arrival']

        start = time
        finish = time + p['burst']
        waiting = start - p['arrival']
        turnaround = finish - p['arrival']

        print(f"{p['id']}\t{start}\t{finish}\t{waiting}\t{turnaround}")
        time = finish


# ===============================
# SJF NON-PREEMPTIVE
# ===============================
def sjf(processes):
    time = 0
    completed = []
    n = len(processes)

    print("\n=== SJF Scheduling ===")
    print("ID\tStart\tFinish\tWaiting\tTurnaround")

    while len(completed) < n:
        ready = [p for p in processes
                 if p['arrival'] <= time and p not in completed]

        if ready:
            p = min(ready, key=lambda x: x['burst'])

            start = time
            finish = time + p['burst']
            waiting = start - p['arrival']
            turnaround = finish - p['arrival']

            print(f"{p['id']}\t{start}\t{finish}\t{waiting}\t{turnaround}")

            time = finish
            completed.append(p)
        else:
            time += 1


# ===============================
# MAIN PROGRAM
# ===============================
if __name__ == "__main__":
    processes = read_processes("data/processes.csv")

    fcfs(processes.copy())
    sjf(processes.copy())

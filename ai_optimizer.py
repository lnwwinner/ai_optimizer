import psutil
import os
import time
import json
from datetime import datetime

with open("config.json") as f:
    config = json.load(f)

CPU_THRESHOLD = config["cpu_threshold"]
RAM_THRESHOLD = config["ram_threshold"]
DISK_THRESHOLD = config["disk_threshold"]
INTERVAL = config["check_interval"]

LOG_FILE = "logs/optimizer.log"

def log(msg):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")
    print(msg)

def clean_temp():
    log("Cleaning temp files...")
    os.system("del /s /f /q %temp%\\* >nul 2>&1")

def fix_disk():
    log("Fixing high disk usage...")
    os.system("sc stop SysMain")
    os.system("sc config SysMain start=disabled")
    os.system("sc stop WSearch")
    os.system("sc config WSearch start=disabled")

def reset_network():
    log("Resetting network...")
    os.system("ipconfig /flushdns")
    os.system("netsh winsock reset >nul")

def kill_heavy_process():
    log("Killing heavy processes...")
    for proc in psutil.process_iter(['pid','name','memory_percent']):
        try:
            if proc.info['memory_percent'] > 10:
                proc.kill()
                log(f"Killed {proc.info['name']}")
        except:
            pass

def optimize():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log(f"CPU={cpu}% RAM={ram}% DISK={disk}%")

    if ram > RAM_THRESHOLD:
        clean_temp()
        kill_heavy_process()

    if disk > DISK_THRESHOLD:
        fix_disk()

    if cpu > CPU_THRESHOLD:
        kill_heavy_process()

    if cpu < 20 and ram < 50:
        log("System stable")

while True:
    optimize()
    time.sleep(INTERVAL)

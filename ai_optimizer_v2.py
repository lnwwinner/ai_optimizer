import psutil
import time
from datetime import datetime
import os

from self_learning import SelfLearningModel

model = SelfLearningModel()
LOG_FILE = "logs/optimizer.log"


def log(msg):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")
    print(msg)


def clean_temp():
    os.system("del /s /f /q %temp%\\* >nul 2>&1")


def fix_disk():
    os.system("sc stop SysMain")
    os.system("sc config SysMain start=disabled")


def kill_heavy():
    for p in psutil.process_iter(['memory_percent']):
        try:
            if p.info['memory_percent'] > 10:
                p.kill()
        except:
            pass


def evaluate(before, after):
    return 1 if after < before else 0


while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log(f"CPU={cpu} RAM={ram} DISK={disk}")

    decision = model.predict(cpu, ram, disk)

    before = cpu + ram + disk

    if decision == 1:
        log("AI Action: Optimize")
        clean_temp()
        kill_heavy()
        fix_disk()
    else:
        log("AI Action: Skip")

    time.sleep(2)

    cpu2 = psutil.cpu_percent()
    ram2 = psutil.virtual_memory().percent
    disk2 = psutil.disk_usage('/').percent

    after = cpu2 + ram2 + disk2

    reward = evaluate(before, after)

    model.add_sample(cpu, ram, disk, reward)
    model.train()

    log(f"Reward={reward}")

    time.sleep(5)

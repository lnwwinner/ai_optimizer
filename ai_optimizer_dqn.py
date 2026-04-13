import psutil
import time
import os
import numpy as np
from datetime import datetime

from dqn_agent import DQNAgent

agent = DQNAgent()

LOG_FILE = "logs/dqn_optimizer.log"

ACTIONS = ["idle","clean","kill","disk","full"]

def log(msg):
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {msg}\n")
    print(msg)

def clean_temp():
    os.system("del /s /f /q %temp%\\* >nul 2>&1")

def kill_heavy():
    for p in psutil.process_iter(['memory_percent']):
        try:
            if p.info['memory_percent'] > 10:
                p.kill()
        except:
            pass

def fix_disk():
    os.system("sc stop SysMain")
    os.system("sc config SysMain start=disabled")

def do_action(a):
    if a == 1:
        clean_temp()
    elif a == 2:
        kill_heavy()
    elif a == 3:
        fix_disk()
    elif a == 4:
        clean_temp(); kill_heavy(); fix_disk()

def get_state():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return np.array([cpu/100, ram/100, disk/100])

def score(s):
    return sum(s)

while True:
    state = get_state()
    action = agent.act(state)

    log(f"Action={ACTIONS[action]}")

    before = score(state)

    do_action(action)

    time.sleep(2)

    next_state = get_state()
    after = score(next_state)

    reward = 1 if after < before else -1

    agent.remember(state, action, reward, next_state)
    agent.replay()

    log(f"Reward={reward} Epsilon={agent.epsilon}")

    time.sleep(5)

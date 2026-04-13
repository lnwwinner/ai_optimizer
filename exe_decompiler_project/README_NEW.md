# 🧠 AI Malware Analysis Platform

## 🔥 Overview
ระบบวิเคราะห์ malware ด้วย AI + Sandbox + Behavior Analysis

---

## ⚙️ System Requirements

- Python **3.10 (แนะนำ)**
- Windows OS
- VirtualBox (สำหรับ Sandbox)

---

## ⚙️ Installation (มาตรฐานเดียวกับสคริปต์)

### 1. Clone repo
```
git clone https://github.com/lnwwinner/ai_optimizer.git
cd exe_decompiler_project
```

---

### 2. Create Virtual Environment
```
python -m venv venv
```

---

### 3. Activate Environment
```
venv\Scripts\activate
```

---

### 4. Install Dependencies
```
pip install -r requirements.txt
```

หรือใช้:
```
install.bat
```

---

## 🚀 Run System

### ✅ Recommended
```
run.bat
```

---

### ⚙️ Manual Run (ต้อง activate ก่อนทุกครั้ง)

```
venv\Scripts\activate
```

#### API
```
python api/server.py
```

#### Dashboard
```
python web/dashboard.py
```

---

## 🌐 Access

- API → http://localhost:5000
- Dashboard → http://localhost:7000

---

## 🔥 Workflow

Upload → Static → String → AI → Sandbox → Behavior → Fusion → Result

---

## 🔒 Security Principles

- ใช้ Virtual Environment ทุกครั้ง
- Lock version dependencies
- ห้ามรัน malware บนเครื่องจริง
- ใช้ VM เท่านั้น

---

## 📂 Logs

```
logs/YYYY-MM-DD.log
```

---

## 🧠 Development Philosophy

- Security First
- Environment Isolation
- Version Locking

---

## 💀 Status

Ready for real usage (controlled environment)

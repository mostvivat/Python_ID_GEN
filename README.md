## ID Test Data Generator (GUI)

This is a simple Python GUI application that generates **valid ID card numbers** using the correct 13-digit format with a checksum. Built with `Tkinter`, this tool is useful for developers, testers, or anyone needing mock ID data.

---

## 🖼️ Features

- ✅ One-click ID card number generation
- ✅ Follows official 13-digit Thai ID checksum rule
- ✅ Minimal and user-friendly interface
- ✅ Packaged as `.exe` for Windows (optional)

---

## 🛠️ Requirements

- Python 3.6+
- Tkinter (comes built-in with Python)

---

## 🚀 How to Run


### Option 1: Run from Source

1. Clone or download the repo
2. Open terminal or command prompt
3. Run:

```bash
python id_gen.py
```

Option 2: Run as .exe (Windows only)
If you want to build or use the executable version:
Package your app:
```bash
python -m PyInstaller --onefile --windowed id_gen.py
```
Find the .exe inside the dist/ folder:
```bash
dist/id_gen.exe
```


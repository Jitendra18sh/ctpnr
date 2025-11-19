# ctpnr

A lightweight command-line tool to fetch **Indian Railways PNR Status** using the ConfirmTKT API.

---

## 📦 Installation

Install locally from the project folder:

```bash
pip install ctpnr
````

---

## 🚀 Usage

### Basic Usage

```bash
ctpnr 6261386648
```

### Raw JSON Output

```bash
ctpnr 6261386648 --json
```

---

## ⭐ Example Output

### Command:

```bash
ctpnr 6261386648
```

### Result:

```
===== PNR STATUS =====
PNR: 6261386648
Train: 12792 - SECUNDERABAD EX
From: DNR → To: NGP
Date of Journey: 24-11-2025
Class: SL
Chart Prepared: False

--- Passenger Status ---
Passenger 1:
  Booking Status : PQWL 65
  Current Status : PQWL 44
  Prediction     : 60% Chance

Passenger 2:
  Booking Status : PQWL 66
  Current Status : PQWL 45
  Prediction     : 59% Chance

Departure Time     : 12:15
Arrival Time       : 11:00
Expected Platform  : 4
=======================
```

---

## 📚 Features

* ✔ Fast CLI tool
* ✔ JSON output mode
* ✔ Accurate prediction (from ConfirmTKT API)
* ✔ Cross-platform (Windows, macOS, Linux)

---

## 🔮 Upcoming Improvements (Optional)

I can add more features if you want:

* 🎨 **Colored Terminal Output**
* 💾 **Caching** (faster next runs)
* 🔁 **Auto retry on failed API**
* 🖥 **GUI Version**
* 📦 **Publish to PyPI**

Just say:
**“add colors”**
or **“publish to PyPI”**
or **“make GUI version”**

---

## 📄 License

MIT License © 2025

```

---
<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#34d399&height=180&section=header&text=CSV%20Pivot%20Lite&fontSize=42&fontColor=ffffff" alt="CSV Pivot Lite banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=34D399&center=true&vCenter=true&width=650&lines=Turn%20flat%20CSV%20rows%20into%20useful%20summaries." alt="Animated project tagline"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/csv-pivot-lite?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/csv-pivot-lite?style=for-the-badge" alt="Top language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/csv-pivot-lite?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/csv-pivot-lite?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="CSV Pivot Lite illustration"/></p>

## 🚀 Overview

CSV Pivot Lite turns a flat CSV file into a grouped summary table. Choose row and column dimensions, then aggregate a numeric field or count records using Python's built-in CSV tools.

## ✨ Features

- 📊 Pivot by any two CSV columns
- 🧮 Count, sum, average, minimum, or maximum
- 🧾 Write a new CSV report without changing the source
- ⚙️ Sort dimensions for repeatable output

## 🎬 Demo

~~~bash
python main.py sales.csv --rows region --columns quarter --values revenue --agg sum
~~~

No hosted service or account is required.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/csv-pivot-lite.git
cd csv-pivot-lite
python main.py --help
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
csv-pivot-lite/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working command-line core
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional richer reports
- [ ] 🧰 More edge-case fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#34d399,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>

# HEA_Shuffler 🧪🔀

[![Documentation Status](https://img.shields.io/badge/docs-GitHub--Pages-blue)](https://<your-username>.github.io/HEA_Shuffler/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)

## Overview

**HEA_Shuffler** is a robust and flexible Monte Carlo-based tool designed for atom substitution in VASP POSCAR files. It supports multielement randomization (e.g., high-entropy alloys or SQS-like configurations) and evaluates short-range ordering (SRO) for each trial.

Inspired by SQS but using brute-force Monte Carlo, it's ideal for:
- Alloy structure generation
- Entropic sampling of substitution patterns
- VASP input automation
- High-throughput material discovery

## 🚀 Features

- Interactive CLI for atom substitutions
- Monte Carlo trial sampling
- SRO scoring of each structure
- Auto-naming and sorting of output POSCARs
- VASP-compatible atom ordering
- Optional visualization of substitution sites

## 🧰 Requirements

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install pymatgen matplotlib
```

## 🧪 Example Usage

```bash
python brute-montecarlo-substitutor.py
```

Then follow prompts like:

```text
Enter the name of your POSCAR file (e.g., POSCAR): POSCAR
Which atom do you want to substitute (e.g., Co)? Co
How many atoms do you want to substitute? [1 <= n <= 12] 8
Enter the substituting atom(s), separated by spaces (e.g., Mn Ni): Mn Fe
How many Monte Carlo trials to attempt? 10
```

Each structure will be saved as `POSCAR_trial_N.vasp` with SRO scores printed in summary.

## 📁 Project Structure

```
HEA_Shuffler/
│
├── brute-montecarlo-substitutor.py  # Main script
├── POSCAR                          # Example input structure
├── requirements.txt               # Python dependencies
├── LICENSE
├── README.md
└── .github/workflows/ci.yml       # Optional GitHub Action
```

## 🧪 Tests

Test scripts and validation samples coming soon in `/tests`.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

## 🧠 Citation / Credit

If you use this in your work, please cite this repo or credit the authors.

---

**Developed by:** [@ndandu](https://github.com/ndandu)  
High-Entropy Alloy Materials Discovery · 2025

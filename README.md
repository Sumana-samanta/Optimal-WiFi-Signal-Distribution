# Optimal-WiFi-Signal-Distribution
Determining an optimal path for WiFi signal propagation from a router to a target location while minimizing signal loss and avoiding obstacles.
#!/usr/bin/env python3
"""
WiFi Signal Distribution using A* Search Algorithm

Example:
  python3 wifi_signal_astar.py \
    --grid-size 5 \
    --start 0,0 \
    --goal 4,4 \
    --out result.txt
"""


# WiFi Signal Planner 📡

A Python-based system for planning WiFi network coverage and analyzing signal propagation in indoor environments.

## 📋 Project Overview

This project implements:
- **Signal Propagation Model**: Free space path loss calculations
- **Coverage Mapping**: Generate heatmaps of WiFi signal distribution
- **Device Positioning**: Optimal placement of access points and clients
- **Data Processing**: Convert device coordinates to signal strength maps

## 🏗️ Project Structure
```bash
wifi-signal-planner/
├── scripts/
│   └── points_to_signal_csv.py      ✅ Main processing script
├── src/
│   └── wifi_planner/
│       └── signal_model.py          ✅ Signal calculations
├── data/
│   └── devices.csv                  ✅ Sample WiFi devices
├── results/
│   └── output.csv                   ✅ Generated signal map
├── tests/
│   └── test_signal_model.py         ✅ Unit tests
└── README.md                        ✅ Documentation
```

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas numpy
```

## Run Signal Processing
```bash
python scripts/points_to_signal_csv.py \
  --grid-size 10 \
  --points data/devices.csv \
  --out results/output.csv
```
or
```bash
python scripts\points_to_signal_csv.py --grid-size 10 --points data\devices.csv --out results\output.csv
```

## How It Works
- Input: CSV file with device coordinates (x, y)
- Processing: Apply signal propagation model
- Output: CSV with signal strength at each point





# 🏏 DLS Calculator (Duckworth-Lewis-Stern Method)

A modern, web-based tool built with **Flask** to calculate revised targets and par scores for limited-overs cricket matches (ODI and T20) interrupted by weather or other factors.

## 🌟 Features
- **Accurate Calculations**: Handles pre-innings delays, mid-innings interruptions, and second-innings targets.
- **Dynamic UI**: Responsive input fields that adapt based on the chosen match scenario.
- **Dark Mode**: Fully integrated dark/light mode toggle with persistent settings using `localStorage`.
- **Clean Results**: Professional dashboard-style output for par scores, revised targets, and required run rates.

## 🔗 Live Server
https://dls-calculator.onrender.com
---

## 📖 What is DLS?
The **Duckworth–Lewis–Stern (DLS)** method is a mathematical formulation designed to calculate the target score for the team batting second in a limited-overs cricket match interrupted by weather or other circumstances.

It operates on the principle that a batting team has two key **resources**:
1. **Overs** remaining.
2. **Wickets** in hand.

When a match is shortened, the target score is adjusted based on the percentage of resources lost by both teams.

---

## 🛠️ Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Deployment**: Configured for Render (via `Procfile`)

---

## 🚀 Installation & Local Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/PranavShende/DLS_Calculator.git](https://github.com/PranavShende/DLS_Calculator.git)
   cd DLS_Calculator


## Create and activate a virtual environment:
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate


## Install Dependencies
pip install -r requirements.txt


## Run the application 
python app.py

## 📂 Project Structure
```text
DLS_Calculator/
├── static/
│   ├── style.css    # Modern UI styling & Dark Mode variables
│   └── index.js     # UI logic & Theme switching
├── templates/
│   ├── index.html   # Main calculator interface
│   └── result.html  # Standardized results dashboard
├── app.py           # Flask server & Routing logic
├── dls.py           # Core DLS mathematical functions
├── overs.py         # Overs management logic
├── resources.py     # DLS Resource tables
├── requirements.txt # Project dependencies
└── Procfile         # Deployment configuration
```


## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## Developed by Pranav Shende



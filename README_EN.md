# Bonpreu Data Engineer Demo

📄 Versions: [Català](README.md) | [English](README_EN.md)

This project is a **demo ETL (Extract, Transform, Load) pipeline** created to showcase key knowledge for the role of **Data Engineer** at Bon Preu S.A.U.

---

## 🎯 Project Objective
- **Extract**: get sales data from a CSV file.  
- **Transform**: clean and enrich the data (e.g., compute totals).  
- **Load**: load the data into a MySQL database.  
- **Visualization**: connect MySQL to Power BI to create dashboards.  
- **Best practices**: automated tests, Docker, and CI/CD (GitHub Actions).  

---

## 🛠 Challenges faced and solved
- Initial development on **MacOS with M3 chip, VSC and Docker Desktop**.  
- Power BI only works on Windows → without a PC, I used an **old Mac with Windows 10 in BootCamp**.  
- Docker didn’t work properly in this setup → I created an **Ubuntu VM with VirtualBox**.  
- There, I deployed MySQL via Docker Compose and connected it to Power BI on Windows.  
- Required configuring Power Query properly to clean and import the data.  

This process shows adaptability and problem-solving in mixed environments.

---

## 📂 Project Structure

```
bonpreu-data-engineer-demo/
├─ data/
│   └─ input.csv              # Synthetic dataset with sales data (2,000 rows)
├─ etl/
│   └─ etl_main.py            # Main ETL script
├─ tests/
│   └─ test_etl.py            # Automated tests with pytest
├─ powerBI/
│   ├─ Bon Preu Dashboard.pbix    # Complete Power BI dashboard
│   ├─ Bbonpreu-theme.json        # Bon Preu corporate theme for Power BI
│   ├─ Power_BI_Dashboard_p1.jpg
│   ├─ Power_BI_Dashboard_p2.jpg
│   ├─ Power_BI_Dashboard_p3.jpg
│   └─ Power_BI_DAX.jpg
├─ .github/
│   └─ workflows/
│       └─ ci.yml             # GitHub Actions workflow (CI/CD)
├─ .dockerignore
├─ .gitignore
├─ .env.example               # Example environment variables
├─ docker-compose.yml         # To launch MySQL + ETL with Docker
├─ Dockerfile                 # Build ETL container image
├─ requirements.txt           # Python dependencies
├─ generate_data.py           # Script to regenerate input.csv with synthetic data
├─ wait-for-db.sh             # Script - prevents ETL from starting before MySQL is ready
└─ README.md
```

---

## 🧑🏽‍💻 How to run or view the project (Step by step)

### 1️⃣ Download the project (clone)
**Choose a folder (e.g. Documents) - Clone the repo (use the link) - Enter the project folder**
```bash
cd ~/Documents
git clone https://github.com/rogerloop/bonpreu-data-engineer-demo.git
cd bonpreu-data-engineer-demo
```

### 2️⃣ Prepare the .env file (important)
The repo includes a `.env.example`. Locally you must create a `.env` from it for connections (MySQL, etc.) to work. Rename or copy it:  

macOS / Linux
```bash
cp .env.example .env
```
Windows (CMD)
```bash
copy .env.example .env
```
Windows (PowerShell)
```bash
Copy-Item .env.example .env
```

Then, edit `.env` if needed with any text editor (VS Code, Notepad, nano…) to set real or test credentials. (Important: `.env` must be in `.gitignore` and never pushed to GitHub).

### 3️⃣ Choose execution mode
Pick one of the three execution modes:  
- **Option A — Local execution (Python venv):** best if you want to customize or modify the code.  
- **Option B — Docker (ETL container):** useful if you don’t want Python locally; only Docker is required. Good to test ETL in isolation.  
- **Option C — Docker Compose (recommended full demo):** starts MySQL + ETL with 1 command. Recommended for demo reproduction.  

---

## 🚀 Option A — Local execution

1. Create virtual environment and install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
2. Run the ETL:
```bash
python etl/etl_main.py
```
3. Run tests:
```bash
pytest tests/
```

---

## 🐳 Option B — Run with Docker (ETL in container)

Build and run ETL container:
```bash
docker build -t bonpreu-etl-demo .
docker run --rm bonpreu-etl-demo
```

---

## 🐙 Option C — Run with Docker Compose (MySQL + ETL)

Pre-requisite: create `.env` from `.env.example`
```bash
cp .env.example .env
# (optional) edit credentials if needed
docker compose up --build
```
- This launches a container with MySQL and runs the ETL.  
- If you don’t want to load data into MySQL, comment out `load(df)` in `etl/etl_main.py`.  

---

### ✅ Tests

This project includes basic tests with pytest.  
They run locally and automatically with GitHub Actions on every push.

```bash
pytest tests/
```

---

### 🐙 CI/CD Automation with GitHub Actions

The workflow is in `.github/workflows/ci.yml` and runs:  
- Install dependencies  
- Run tests  
- Build Docker image  

Check results in the **Actions** tab in GitHub.

---

### 📊 Power BI Dashboard (Windows only)

The project includes a dashboard connected to the `sales_staging` table in MySQL.  
- You can find the Power BI file here:  
  [Download BonPreu Power BI Demo](https://github.com/rogerloop/bonpreu-data-engineer-demo/blob/main/powerBI/Bon%20Preu%20Dashboard.pbix)

⚠️ Reminder: If `.env` or MySQL credentials are changed, update Power BI connection details in Power Query.  

#### Example visuals:
- Bar chart → total sales by product  
- Line chart → sales trend by date  
- KPI → total revenue (sum of sales)  
- Example DAX → Calendar table for time intelligence  

#### Screenshots:
![Power BI Dashboard Demo Page 1](powerBI/Power_BI_Dashboard_p1.jpg)

![Power BI Dashboard Demo Page 2](powerBI/Power_BI_Dashboard_p2.jpg)

![Power BI Dashboard Demo Page 3](powerBI/Power_BI_Dashboard_p3.jpg)

![Power BI Dashboard Demo DAX Example](powerBI/Power_BI_DAX.jpg)

---

### 🔗 Tools & Technologies
- Python Pandas  
- SQLAlchemy  
- MySQL  
- Docker  
- GitHub Actions  
- Power BI  

---

👨‍💻 Author  
Roger Defez  
📍 Osona  
[LinkedIn](https://www.linkedin.com/in/roger-defez/) | [GitHub](https://github.com/rogerloop)

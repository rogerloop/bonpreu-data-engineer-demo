"""
Script per generar un dataset sintètic de vendes per Bon Preu Demo.
Crea un fitxer CSV amb 2000 registres (date, product, quantity, price).
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os

def generate_dataset(output_path="data/input.csv", n_rows=2000, seed=42):
    np.random.seed(seed)

    # Catàleg de productes (nom i preu base en €)
    products = [
        ("Pa", 1.20),
        ("Llet", 0.95),
        ("Formatge", 2.60),
        ("Iogurt", 0.55),
        ("Poma", 0.70),
        ("Plàtan", 0.50),
        ("Tomàquet", 1.10),
        ("Enciam", 0.90),
        ("Oli d'oliva", 6.50),
        ("Arròs", 1.30),
        ("Pasta", 1.10),
        ("Pollastre", 5.20),
        ("Tonyina (llauna)", 1.40),
        ("Aigua mineral", 0.35),
        ("Cervesa", 0.85),
        ("Vi negre", 5.90),
        ("Sucre", 1.00),
        ("Sal", 0.40),
        ("Ou", 0.25),
        ("Cafè", 3.80),
        ("Te", 2.10),
        ("Xocolata", 1.80),
        ("Galetes", 1.50),
        ("Paper higiènic", 0.45),
    ]

    # Dates (gener - juny 2025)
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 6, 30)
    days = (end_date - start_date).days + 1

    # Generació de mostres
    dates = [
        start_date + timedelta(days=int(x))
        for x in np.random.randint(0, days, size=n_rows)
    ]
    prod_idx = np.random.randint(0, len(products), size=n_rows)

    rows = []
    for i in range(n_rows):
        name, base_price = products[prod_idx[i]]
        price = round(float(base_price * (1 + np.random.uniform(-0.1, 0.1))), 2)
        quantity = int(np.clip(np.random.poisson(4) + 1, 1, 20))
        rows.append((dates[i].strftime("%Y-%m-%d"), name, quantity, price))

    df = pd.DataFrame(rows, columns=["date", "product", "quantity", "price"])

    # Assegurem que existeix la carpeta data/
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Dataset generat: {output_path} ({len(df)} files)")

if __name__ == "__main__":
    generate_dataset()
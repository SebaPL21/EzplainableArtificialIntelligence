import csv
import numpy as np
import pandas as pd

def generate_data(n_samples, n_features, noise=0.1):
    # Utwórz dane wejściowe
    X = np.random.rand(n_samples, n_features)
    # Utwórz etykiety klas
    y = np.where(X[:, 0] > 0.5, 1, 0)
    # Dodaj hałas do danych
    X += np.random.normal(scale=noise, size=X.shape)
    return X, y

# Wygeneruj dane
n_features = 20
X, y = generate_data(1000, n_features)

# Utwórz obiekt DataFrame
columns = [f"feature_{i+1}" for i in range(n_features)]
df = pd.DataFrame(data=X, columns=columns)
df["class"] = y

# Otwórz plik CSV
sciezka_pliku = "data.csv"
with open(sciezka_pliku, mode='w', newline='') as plik_csv:
    writer = csv.writer(plik_csv)
    # Zapisz nagłówki
    writer.writerow(df.columns)
    # Zapisz dane
    for index, wiersz in df.iterrows():
        writer.writerow(wiersz)

# Wyświetl dane
print(df)

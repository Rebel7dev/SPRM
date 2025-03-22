import pandas as pd
import numpy as np

def fetch_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
    df = pd.read_csv(url, names=column_names)
    print("Dane z repozytorium:")
    print(df.head())
    return df

def read_csv_file(filename):
    try:
        df = pd.read_csv(filename)
        print("Dane z pliku CSV:")
        print(df.head())
    except Exception as e:
        print(f"Błąd wczytywania pliku CSV: {e}")

def generate_data():
    num_samples = 150
    car_data = pd.DataFrame({
        "engine_size": np.random.uniform(1.0, 5.0, num_samples),
        "fuel_efficiency": np.random.uniform(5.0, 20.0, num_samples),
        "horsepower": np.random.uniform(70, 400, num_samples),
        "weight": np.random.uniform(800, 2500, num_samples),
        "class": np.random.choice(["Sedan", "SUV", "Hatchback"], num_samples)
    })
    print("Wygenerowane dane:")
    print(car_data.head())

def main():
    print("Zadanie 1:")
    fetch_data()

    print("\n\nZadanie 2:")
    read_csv_file("iris.csv")

    print("\n\nZadanie 3:")
    generate_data()

if __name__ == "__main__":
    main()
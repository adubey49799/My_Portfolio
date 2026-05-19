"""
Lab 4: Getting Started with Pandas
Course: Data Science and Big Data Analytics

Instructions covered:
- Work with Pandas Series
- Load and clean the Automobile dataset
- Analyze company, price, and mileage details
- Combine DataFrames using concat and merge

Required input file:
    Lab 4 - Automobile.xls

Output file created:
    Lab_4_Automobile_Cleaned.csv
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import pandas as pd


# -----------------------------------------------------------------------------
# Helper function: read the Excel .xls file.
# Pandas reads old .xls files using the optional xlrd package.
# If xlrd is not installed, this script attempts a LibreOffice conversion fallback.
# -----------------------------------------------------------------------------
def load_automobile_file(file_path: str | Path) -> pd.DataFrame:
    file_path = Path(file_path)

    try:
        # Preferred method for .xls files when xlrd is available.
        return pd.read_excel(file_path, engine="xlrd")
    except ImportError:
        print("Note: xlrd is not installed. Trying LibreOffice CSV conversion fallback.\n")
    except Exception as exc:
        print(f"Excel read failed with: {exc}")
        print("Trying LibreOffice CSV conversion fallback.\n")

    # Fallback: convert the .xls file to .csv using LibreOffice if available.
    libreoffice_cmd = shutil.which("libreoffice") or shutil.which("soffice")
    if libreoffice_cmd is None:
        raise RuntimeError(
            "Could not read .xls file because xlrd is missing and LibreOffice was not found. "
            "Install xlrd using: pip install xlrd"
        )

    with tempfile.TemporaryDirectory() as tmp_dir:
        subprocess.run(
            [libreoffice_cmd, "--headless", "--convert-to", "csv", "--outdir", tmp_dir, str(file_path)],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        csv_path = Path(tmp_dir) / f"{file_path.stem}.csv"
        return pd.read_csv(csv_path)


# Display settings make the output easier to read in terminal or screenshots.
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)
pd.set_option("display.max_rows", 100)


print("=" * 90)
print("PART 1: WORKING WITH SERIES")
print("=" * 90)

# 1. Create and display a one-dimensional array-like object (Series).
print("\nTask 1: Create and display a Pandas Series")
student_scores = pd.Series([85, 90, 78, 92, 88], name="Student Scores")
print(student_scores)

# 2. Create two Series and perform arithmetic operations.
print("\nTask 2: Series arithmetic operations")
series_a = pd.Series([2, 4, 6, 8, 10])
series_b = pd.Series([1, 3, 5, 7, 9])

print("Series A:")
print(series_a)
print("\nSeries B:")
print(series_b)

print("\nAddition result:")
print(series_a + series_b)

print("\nSubtraction result:")
print(series_a - series_b)

print("\nMultiplication result:")
print(series_a * series_b)

print("\nDivision result:")
print(series_a / series_b)


print("\n" + "=" * 90)
print("PART 2: WORKING WITH THE AUTOMOBILE DATASET")
print("=" * 90)

# 3. Load the Automobile dataset.
print("\nTask 3: Load the dataset 'Lab 4 - Automobile.xls'")
input_file = Path("Lab 4 - Automobile.xls")

# The following line helps the script run when the file is kept beside the script.
if not input_file.exists():
    input_file = Path(__file__).resolve().parent / "Lab 4 - Automobile.xls"

automobile_df = load_automobile_file(input_file)
print(f"Dataset loaded successfully with {automobile_df.shape[0]} rows and {automobile_df.shape[1]} columns.")
print("Columns:", list(automobile_df.columns))

# 4. Print first five and last five rows.
print("\nTask 4: First five rows")
print(automobile_df.head())

print("\nTask 4: Last five rows")
print(automobile_df.tail())

# 5. Remove records containing '?', 'n.a', or NaN values and save cleaned CSV.
print("\nTask 5: Remove '?', 'n.a', and NaN values and save cleaned DataFrame")
cleaned_df = automobile_df.replace(["?", "n.a"], pd.NA).dropna()
cleaned_csv_file = Path("Lab_4_Automobile_Cleaned.csv")
cleaned_df.to_csv(cleaned_csv_file, index=False)
print(f"Original shape: {automobile_df.shape}")
print(f"Cleaned shape: {cleaned_df.shape}")
print(f"Cleaned CSV saved as: {cleaned_csv_file.resolve()}")

# Make sure numeric columns are treated as numeric for price and mileage calculations.
cleaned_df["price"] = pd.to_numeric(cleaned_df["price"], errors="coerce")
cleaned_df["average-mileage"] = pd.to_numeric(cleaned_df["average-mileage"], errors="coerce")

# 6. Find the most expensive car in the dataset.
print("\nTask 6: Most expensive car in the dataset")
most_expensive_car = cleaned_df.loc[cleaned_df["price"].idxmax()]
print("Company:", most_expensive_car["company"])
print("Price:", most_expensive_car["price"])
print("Full row:")
print(most_expensive_car)

# 7. Print all Toyota cars.
print("\nTask 7: Details of cars manufactured by Toyota")
toyota_cars = cleaned_df[cleaned_df["company"].str.lower() == "toyota"]
print(toyota_cars)

# 8. Count total number of cars per company.
print("\nTask 8: Total number of cars per company")
car_count_by_company = cleaned_df["company"].value_counts()
print(car_count_by_company)

# 9. Display the most expensive car from each company.
print("\nTask 9: Most expensive car from each company")
most_expensive_by_company = cleaned_df.loc[cleaned_df.groupby("company")["price"].idxmax()]
print(most_expensive_by_company[["company", "body-style", "horsepower", "average-mileage", "price"]].sort_values("company"))

# 10. Calculate average mileage for each company.
print("\nTask 10: Average mileage for each car company")
average_mileage_by_company = cleaned_df.groupby("company")["average-mileage"].mean().sort_values(ascending=False)
print(average_mileage_by_company)

# 11. Sort all cars in ascending order by price.
print("\nTask 11: Cars sorted by price in ascending order")
sorted_by_price = cleaned_df.sort_values(by="price", ascending=True)
print(sorted_by_price)


print("\n" + "=" * 90)
print("PART 3: COMBINING DATAFRAMES")
print("=" * 90)

# 12. Create two DataFrames from dictionaries and concatenate them.
print("\nTask 12: Create GermanCars and JapaneseCars DataFrames, then concatenate")
GermanCars = {"Company": ["Ford", "Mercedes", "BMV", "Audi"], "Price": [23845, 171995, 135925, 71400]}
japaneseCars = {"Company": ["Toyota", "Honda", "Nissan", "Mitsubishi "], "Price": [29995, 23600, 61500, 58900]}

german_cars_df = pd.DataFrame(GermanCars)
japanese_cars_df = pd.DataFrame(japaneseCars)
combined_cars_df = pd.concat([german_cars_df, japanese_cars_df], ignore_index=True)

print("German cars DataFrame:")
print(german_cars_df)
print("\nJapanese cars DataFrame:")
print(japanese_cars_df)
print("\nConcatenated DataFrame:")
print(combined_cars_df)

# 13. Create and merge Car_Price and Car_Horsepower DataFrames on Company.
print("\nTask 13: Merge Car_Price and Car_Horsepower DataFrames on Company")
Car_Price = {"Company": ["Toyota", "Honda", "BMV", "Audi"], "Price": [23845, 17995, 135925, 71400]}
car_Horsepower = {"Company": ["Toyota", "Honda", "BMV", "Audi"], "horsepower": [141, 80, 182, 160]}

car_price_df = pd.DataFrame(Car_Price)
car_horsepower_df = pd.DataFrame(car_Horsepower)
merged_cars_df = pd.merge(car_price_df, car_horsepower_df, on="Company")

print("Car price DataFrame:")
print(car_price_df)
print("\nCar horsepower DataFrame:")
print(car_horsepower_df)
print("\nMerged DataFrame:")
print(merged_cars_df)

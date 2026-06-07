"""
Lab 7: Data Wrangling
Dataset: Cancer.csv / Lab 7 - Cancer.xls

This script completes the required Lab 7 tasks:
1. Data exploration
2. Handling missing values
3. Filtering repeated patient records
4. Reshaping and one-hot encoding doctor visits
5. Row-wise classification with apply()

Before running:
- Place this script in the same folder as Cancer.csv or Lab 7 - Cancer.xls.
- If using the .xls file, install xlrd if needed:
    pip install xlrd
"""

from pathlib import Path
import pandas as pd


# ------------------------------------------------------------
# Helper function: load either Cancer.csv or Lab 7 - Cancer.xls
# ------------------------------------------------------------
def load_cancer_dataset() -> pd.DataFrame:
    """Read the cancer dataset from CSV first; otherwise read the Excel file."""
    csv_path = Path("Cancer.csv")
    xls_path = Path("Lab 7 - Cancer.xls")

    if csv_path.exists():
        print("Reading dataset from Cancer.csv ...")
        return pd.read_csv(csv_path)

    if xls_path.exists():
        print("Reading dataset from Lab 7 - Cancer.xls ...")
        return pd.read_excel(xls_path)

    raise FileNotFoundError(
        "Dataset not found. Place Cancer.csv or Lab 7 - Cancer.xls in the same folder as this script."
    )


# ------------------------------------------------------------
# Part 1: Data Exploration
# ------------------------------------------------------------
print("\n==============================")
print("PART 1: DATA EXPLORATION")
print("==============================")

# 1. Read in the dataset Cancer.csv / Excel equivalent.
df = load_cancer_dataset()
print("\n1. First five rows of the dataset:")
print(df.head())

# Some missing values in this dataset may be represented as '?' instead of true NaN.
# Replacing '?' with pd.NA makes missing-value handling consistent.
df = df.replace("?", pd.NA)

# 2. Display the data types of each column.
print("\n2. Data types of each column:")
print(df.dtypes)

# 3. Use describe() to generate summary statistics.
print("\n3. Summary statistics using describe():")
print(df.describe(include="all"))

# 4. Group the dataset by class and doctor_name.
print("\n4. Grouped count by class and doctor_name:")
grouped_df = df.groupby(["class", "doctor_name"]).size().reset_index(name="record_count")
print(grouped_df)


# ------------------------------------------------------------
# Part 2: Handling Missing Values
# ------------------------------------------------------------
print("\n================================")
print("PART 2: HANDLING MISSING VALUES")
print("================================")

# 5. Provide a summary of missing values within the dataset.
print("\n5. Missing values by column:")
missing_summary = df.isna().sum()
print(missing_summary)

# 6. Drop all rows that contain missing data.
df_clean = df.dropna().copy()
print("\n6. Shape before and after dropping rows with missing values:")
print(f"Original shape: {df.shape}")
print(f"Cleaned shape : {df_clean.shape}")
print(f"Rows dropped  : {df.shape[0] - df_clean.shape[0]}")

# Convert numeric-looking columns back to numeric after replacing '?'.
for col in df_clean.columns:
    if col not in ["class", "doctor_name"]:
        try:
            df_clean[col] = pd.to_numeric(df_clean[col])
        except (ValueError, TypeError):
            # Keep the original column if it cannot be safely converted.
            pass

# 7. Summarize number of unique values in each column.
print("\n7. Number of unique values in each column:")
unique_summary = df_clean.nunique().sort_values(ascending=False)
print(unique_summary)

print("\nInteresting findings:")
print("- patient_id has many unique values, which is expected because it identifies patients.")
print("- class has only two unique values, representing benign and malignant records.")
print("- doctor_name has a small number of unique values, which makes it suitable for one-hot encoding.")

# 8. Find duplicate values in patient_id and the most frequent patient_id.
print("\n8. Duplicate patient_id frequency:")
patient_id_counts = df_clean["patient_id"].value_counts()
duplicate_patient_ids = patient_id_counts[patient_id_counts > 1]
print(duplicate_patient_ids)

most_frequent_patient_id = patient_id_counts.idxmax()
most_frequent_count = patient_id_counts.max()
print(f"\nMost frequent patient_id: {most_frequent_patient_id}")
print(f"Number of appearances   : {most_frequent_count}")


# ------------------------------------------------------------
# Part 3: Filtering Data
# ------------------------------------------------------------
print("\n======================")
print("PART 3: FILTERING DATA")
print("======================")

# 9. Remove patients where patient_id appears more than two times.
patient_counts = df_clean["patient_id"].value_counts()
valid_patient_ids = patient_counts[patient_counts <= 2].index
filtered_df = df_clean[df_clean["patient_id"].isin(valid_patient_ids)].copy()

print("\n9. Shape before and after removing patient_id values appearing more than two times:")
print(f"Before filtering: {df_clean.shape}")
print(f"After filtering : {filtered_df.shape}")
print(f"Rows removed    : {df_clean.shape[0] - filtered_df.shape[0]}")


# ------------------------------------------------------------
# Part 4: Reshaping Data
# ------------------------------------------------------------
print("\n=======================")
print("PART 4: RESHAPING DATA")
print("=======================")

# 10. Create categorical_df with patient_id and doctor_name. Add doctor_count = 1.
categorical_df = filtered_df[["patient_id", "doctor_name"]].copy()
categorical_df["doctor_count"] = 1
print("\n10. categorical_df:")
print(categorical_df.head())

# 11. Pivot the DataFrame so each doctor's name becomes a column.
# Using values=['doctor_count'] intentionally creates a MultiIndex column structure,
# which allows us to demonstrate droplevel() in the next step.
doctor_pivot_df = pd.pivot_table(
    categorical_df,
    index="patient_id",
    columns="doctor_name",
    values=["doctor_count"],
    aggfunc="sum",
    fill_value=0,
)
print("\n11. Pivoted doctor visit DataFrame with MultiIndex columns:")
print(doctor_pivot_df.head())

# 12. Drop the multi-index from columns using droplevel().
doctor_pivot_df.columns = doctor_pivot_df.columns.droplevel(0)

# 13. Display the one-hot encoded DataFrame.
doctor_onehot_df = doctor_pivot_df.reset_index()
print("\n13. One-hot encoded doctor visit DataFrame:")
print(doctor_onehot_df.head())

# 14. Join this one-hot encoded DataFrame back to the original filtered dataset using merge().
combined_df = filtered_df.merge(doctor_onehot_df, on="patient_id", how="left")

# 15. Display the final combined DataFrame.
print("\n15. Final combined DataFrame:")
print(combined_df.head())

# 16. Drop the doctor_name column from the combined DataFrame.
combined_df = combined_df.drop(columns=["doctor_name"])
print("\n16. Combined DataFrame after dropping doctor_name:")
print(combined_df.head())


# ------------------------------------------------------------
# Part 5: Row-wise Operations
# ------------------------------------------------------------
print("\n===========================")
print("PART 5: ROW-WISE OPERATIONS")
print("===========================")

# 17. Define the required function.
def celltypelabel(x):
    """Classify cell type based on cell size and shape uniformity."""
    if (x["cell_size_uniformity"] > 5) & (x["cell_shape_uniformity"] > 5):
        return "normal"
    else:
        return "abnormal"


# 18. Use apply() to create a new column cell_type_label.
combined_df["cell_type_label"] = combined_df.apply(celltypelabel, axis=1)
print("\n18. Updated DataFrame with cell_type_label:")
print(combined_df.head())

# Save final output files so they can be submitted or screenshot easily.
combined_df.to_csv("lab7_final_combined_dataframe.csv", index=False)
grouped_df.to_csv("lab7_grouped_class_doctor_summary.csv", index=False)
missing_summary.to_csv("lab7_missing_values_summary.csv", header=["missing_count"])
unique_summary.to_csv("lab7_unique_values_summary.csv", header=["unique_count"])
duplicate_patient_ids.to_csv("lab7_duplicate_patient_id_summary.csv", header=["frequency"])

print("\n==============================")
print("LAB 7 SCRIPT COMPLETED")
print("==============================")
print("Output files created:")
print("- lab7_final_combined_dataframe.csv")
print("- lab7_grouped_class_doctor_summary.csv")
print("- lab7_missing_values_summary.csv")
print("- lab7_unique_values_summary.csv")
print("- lab7_duplicate_patient_id_summary.csv")

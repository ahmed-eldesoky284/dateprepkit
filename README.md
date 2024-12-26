# 🎈 Data Preparation with DataPrepKit

A Streamlit app for data preparation using `DataPrepKit`. This app provides an interactive user interface for file upload, data display, and basic data preparation operations.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://dateprepkit.streamlit.app)

### How to run it on your own machine

1. Install the requirements
```sh
$ pip install -r requirements.txt
```

2. Run the app
```sh
$ streamlit run app.py
```

## Requirements

- Python 3.6 or higher
- Streamlit
- Pandas

## How to Use

1. Run the app using the following command:
```sh
streamlit run app.py
```
Open your browser and navigate to the address displayed in the console to view the app.
Upload your data file (CSV, Excel, JSON, or TXT) and use the various tools for data preparation.
Features

File Upload: Supports CSV, Excel, JSON, and TXT files.
Data Display: Display the first few rows of the data.
Data Summary: Show a statistical summary of numerical data.
Handling Missing Values: Options to remove missing values or impute them with a specified value.
Categorical Data Encoding: Convert categorical data to numerical format using one-hot encoding.

# DataPrepKit

DataPrepKit is a Python utility class for simplifying common data preparation tasks such as reading data from different file formats, generating summary statistics, handling missing values, and encoding categorical data.

## Installation

You can install DataPrepKit using pip:

```
pip install dateprepkit
```

# Usage

To use DataPrepKit in your Python project, follow the steps below:

```
# Import DataPrepKit
from DataPrepKit.DataPrepKit import DataPrepKit
# Initialize DataPrepKit with a DataFrame
prep_kit = DataPrepKit()
```
1. Reading Data
Use the read_data method to load data from various file formats such as CSV, Excel, JSON, or TXT:
```
# Read data from a CSV file
csv_data = prep_kit.read_data('student-dataset.csv', 'csv')
```

2. Generating Data Summary
Generate summary statistics for the loaded data using the data_summary method:
```
# Generate a data summary
summary = prep_kit.data_summary()
print("Data Summary:")
print(summary)
```

3. Handling Missing Values
Handle missing values in the DataFrame by either removing or imputing them using the handle_missing_values method:
```
# Handle missing values by removing
cleaned_data = prep_kit.handle_missing_values(strategy='remove')
print("\nData after handling missing values (removed):")
print(cleaned_data)
```

4. Encoding Categorical Data
Encode categorical columns in the DataFrame using one-hot encoding with the encode_categorical_data method:
```
# Encode categorical data
encoded_df = prep_kit.encode_categorical_data(categorical_columns=['Gender', 'City'])
print("\nEncoded DataFrame:")
print(encoded_df)
```

Example

Here's a complete example of how to use DataPrepKit:
```
# Import DataPrepKit
from DataPrepKit.DataPrepKit import DataPrepKit
# Initialize DataPrepKit with a DataFrame
prep_kit = DataPrepKit()

# Read data from a CSV file
csv_data = prep_kit.read_data('student-dataset.csv', 'csv')

# Generate a data summary
summary = prep_kit.data_summary()
print("Data Summary:")
print(summary)

# Handle missing values by removing
cleaned_data = prep_kit.handle_missing_values(strategy='remove')
print("\nData after handling missing values (removed):")
print(cleaned_data)

# Encode categorical data
encoded_df = prep_kit.encode_categorical_data(categorical_columns=['Gender', 'City'])
print("\nEncoded DataFrame:")
print(encoded_df)
```
## Developer

Developed by [Ahmed Eldesoky].

## License

This project is licensed under the [MIT License](LICENSE).

Make sure the `LICENSE` file is present in the root of your GitHub repository for the link to work correctly.


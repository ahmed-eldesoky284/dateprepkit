import pandas as pd

class DataPrepKit:
    def __init__(self, data=None):
        self.data = data

    def read_data(self, filepath, format="csv", delimiter=None):
        """
        Reads data from a file based on the given format.
        Supports CSV, Excel, JSON, and TXT file formats.
        """
        if format == "csv":
            return pd.read_csv(filepath)
        elif format == "excel":
            return pd.read_excel(filepath)
        elif format == "json":
            return pd.read_json(filepath)
        elif format == "txt":
            # If delimiter is not specified, we try common ones
            if delimiter is None:
                delimiter = '\t'  # Default to tab-delimited for txt files
            return pd.read_csv(filepath, delimiter=delimiter)
        else:
            raise ValueError(f"Unsupported file format: {format}")

    def data_summary(self):
        """
        Provides a statistical summary of numeric data columns in the dataframe.
        """
        numeric_data = self.data.select_dtypes(include=['number'])

        summaries = {}

        if not numeric_data.empty:
            summaries['Mean'] = numeric_data.mean()
            summaries['Median'] = numeric_data.median()
            summaries['Std'] = numeric_data.std()
            mode_values = numeric_data.mode().iloc[0]
            summaries['Mode'] = mode_values
            summaries['Min'] = numeric_data.min()
            summaries['Max'] = numeric_data.max()
        else:
            summaries['Message'] = "No numeric data available for summary."

        return summaries

    def handle_missing_values(self, strategy='remove', value=None):
        """
        Handles missing values based on the chosen strategy.
        - 'remove' removes rows with missing values.
        - 'impute' fills missing values with a given value.
        """
        if not isinstance(self.data, pd.DataFrame):
            raise ValueError("Input 'data' must be a DataFrame.")

        if strategy == 'remove':
            df_cleaned = self.data.dropna()
        elif strategy == 'impute':
            if value is None:
                raise ValueError("Value parameter must be provided for imputation strategy.")
            df_cleaned = self.data.fillna(value)
        else:
            raise ValueError("Invalid strategy! Please choose 'remove' or 'impute'.")

        return df_cleaned

    def encode_categorical_data(self, categorical_columns):
        """
        Encodes categorical columns into numeric values using one-hot encoding.
        """
        encoded_df = pd.get_dummies(self.data, columns=categorical_columns, drop_first=True)
        return encoded_df

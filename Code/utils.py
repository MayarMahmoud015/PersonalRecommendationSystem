
def load_data(file_path):
    """Load data from a CSV file."""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None


def clean_data(data):
    """Clean the dataset by removing NAN values."""
    return data.dropna()

def remove_columns(data, columns_to_remove):
    """Remove specified columns from the DataFrame."""
    columns_to_drop = [col for col in columns_to_remove if col in data.columns]
    return data.drop(columns=columns_to_drop)

def remove_duplicates(data):
    """Remove the duplicates from the DataFrame."""
    return data.drop_duplicates()
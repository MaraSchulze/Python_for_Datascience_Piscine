import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a data frame from a csv file and returns the data frame.
    """
    # Load file
    try:
        df = pd.read_csv(path)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    # Print dimensions
    print("Loading dataset of dimensions", df.shape)

    # Return data frame
    return df

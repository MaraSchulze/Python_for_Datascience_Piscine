import matplotlib.pyplot as plt
from load_csv import load


def convert(x: str) -> int:
    """
    Converts a number string into an int.
    """
    # Sets the factor and extracts the number string
    if len(x) > 1 and x[-1] == "M":
        x = x[:-1]
        factor = 1000000
    elif len(x) > 1 and x[-1] == "k":
        x = x[:-1]
        factor = 1000
    else:
        factor = 1

    # Converts the string into an int
    result = None
    try:
        result = int(float(x) * factor)
    except ValueError as e:
        print(f"Error: {e}")

    # Returns result
    return result


def main():
    """
    Loads population_total.csv and displays the life expectancy
    for Germany and France with matplotlib.
    """
    # Loads csv file into data frame
    df = load("population_total.csv")
    if df is None:
        return

    # Extract the rows for the 2 countries.
    df.set_index("country", inplace=True)
    data = df.loc[["Germany", "France"], "1800":"2051"]
    Y1 = data.iloc[0]
    Y2 = data.iloc[1]

    # Convert the strings to numbers
    Y1 = Y1.apply(convert)
    Y2 = Y2.apply(convert)

    # Plot year against population for the 2 contries
    plt.plot(Y1.index, Y1.values, label="Germany", color="blue")
    plt.plot(Y1.index, Y2.values, label="France", color="green")

    # Add labels, title, legend and adjust ticks for both axes
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.xticks(Y1.index[::40])
    tick_positions = [0, 20_000_000, 40_000_000, 60_000_000, 80_000_000,
                      100_000_000]
    tick_labels = ['', '20M', '40M', '60M', '80M', '100M']
    plt.yticks(tick_positions, tick_labels)
    plt.legend()
    plt.title("Population Projections")

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()

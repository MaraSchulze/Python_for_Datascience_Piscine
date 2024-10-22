import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    Loads life_expectancy_years.csv and displays the life expectancy
    for Germany with matplotlib.
    """
    # Loads csv file into data frame
    df = load("life_expectancy_years.csv")
    if df is None:
        return

    # Extract header row and Germany row. Drop first column, since they are
    # strings. Transform into a series, since the data frame has only one row.
    Y = df.loc[df["country"] == "Germany"].drop(columns="country")
    Y = Y.squeeze()

    # Plot year against life expectancy in Germany
    plt.plot(Y.index, Y.values)

    # Add labels and title and adjust ticks for x-axis
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("Germany Life expectancy Projections")
    plt.xticks(ticks=Y.index[::40])

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()

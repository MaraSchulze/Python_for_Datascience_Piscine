import matplotlib.pyplot as plt
import math
from load_csv import load


def transform(x: float) -> float:
    """
    Transforms to a logarithmic scaling.
    """
    return 50.0 * math.log(x) - 250.0


def main():
    """
    Makes a scatter plot for every county"s life expectancy projected on gdp.
    """
    # Loads csv files into data frames
    df_life_expactancy = load("life_expectancy_years.csv")
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if df_life_expactancy is None or df_gdp is None:
        return

    # Get the column for year 1900
    Y = df_life_expactancy["1900"]
    X = df_gdp["1900"]

    # Transform X data so that a logarithmic scaling can be reached in graphic
    X = X.apply(transform)

    # Plot year against life expectancy in Germany
    plt.scatter(X, Y)

    # Add labels and title and adjust ticks for x-axis
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Life Expectancy")
    plt.title("1900")

    # Customize x-ticks
    custom_ticks = list(range(300, 1000, 100)) + list(range(1000, 11000, 1000))
    custom_ticks = [transform(x) for x in custom_ticks]
    custom_labels = [""] * 17
    custom_labels[0] = "300"
    custom_labels[7] = "1k"
    custom_labels[16] = "10k"
    plt.xticks(custom_ticks, custom_labels)

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    
    line_xs = range(df['Year'].min(), 2051)
    line_ys = [line.intercept + line.slope*x for x in line_xs]
    
    ax.plot(line_xs, line_ys, color='b')
    
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    line2 = linregress(x=df_recent['Year'], y=df_recent['CSIRO Adjusted Sea Level'])
    
    line2_xs = range(2000, 2051)
    line2_ys = [line2.intercept + line2.slope*x for x in line2_xs]
    
    ax.plot(line2_xs, line2_ys, color='b')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
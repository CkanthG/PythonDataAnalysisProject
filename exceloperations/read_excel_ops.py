import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def read_excel():
    excel_data = read_excel_data('Dealers')
    # print(excel_data.head())
    # print(excel_data.describe())
    # print(excel_data.info())
    # Filter data
    filtered_data = excel_data[excel_data['DealerId'] > 10]
    print(filtered_data)
    # Sort data
    sorted_data = excel_data.sort_values(by='DealerId', ascending=False)
    print(sorted_data)
    # Transform data
    excel_data['full_address'] = excel_data['DealerCity'] + ", " + excel_data['DealerCountry']
    print(excel_data)
    # Calculate mean of a column
    mean_value = excel_data['DealerId'].mean()
    print(mean_value)
    # Group data by a column and calculate mean for each group
    grouped_data = excel_data.groupby('DealerName')['DealerId'].mean()
    print(grouped_data)
    # Calculate standard deviation
    std_deviation = np.std(excel_data['DealerId'])
    print(std_deviation)


def create_histogram():
    excel_data = read_excel_data('Customers')
    # Create a histogram
    plt.hist(excel_data['City'])
    plt.xlabel('Customer Name')
    plt.ylabel('Email')
    plt.title('Histogram of Column')
    plt.show()


def create_scatter_plot():
    excel_data = read_excel_data('Customers')
    # Create a scatter plot
    plt.scatter(excel_data['Country'], excel_data['DealerId'])
    plt.xlabel('Customer Name')
    plt.ylabel('Email')
    plt.title('Scatter Plot')
    plt.show()


def read_excel_data(name):
    excel_data = pd.read_excel('files/DealerCustomerAndBookingsInformation.xlsx', sheet_name=name)
    return excel_data

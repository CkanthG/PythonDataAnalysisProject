import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as px1
import seaborn as sns
import matplotlib.pyplot as plt


def read_excel(sheet):
    df_sheet_index = pd.read_excel('files/DealerCustomerAndBookingsInformation.xlsx', sheet_name=sheet)
    return df_sheet_index


def work_with_plotly():
    work_with_plotly_to_generate_bar_chart()
    work_with_plotly_to_generate_scatter_and_bar_plot()
    work_with_plotly_to_generate_scatter_3d_plot()
    work_with_plotly_to_generate_scatter_plot()
    work_with_plotly_to_generate_pie_chart()
    work_with_plotly_to_generate_histogram()
    work_with_plotly_to_generate_box_plot()
    work_with_plotly_to_generate_line_plot()
    work_with_plotly_to_generate_violin_plot()
    work_with_seaborn_to_generate_count_plot()


def work_with_seaborn_to_generate_count_plot():
    df_sheet_index = read_excel(3)
    print(df_sheet_index.info())
    booking_status = df_sheet_index['BookingStatus']

    # count plot on single categorical variable
    sns.countplot(x=booking_status, data=df_sheet_index)

    # Show the plot
    plt.show()


def work_with_plotly_to_generate_violin_plot():
    df_sheet_index = read_excel(3)
    print(df_sheet_index.info())

    # plotting the violin chart
    fig = px.violin(df_sheet_index, y="BookingId", x="BookingStatus")

    # showing the plot
    fig.show()


def work_with_plotly_to_generate_line_plot():
    df_sheet_index = read_excel(2)
    print(df_sheet_index.info())

    # plotting the line chart
    fig = px.line(df_sheet_index, y="BookingId", x="BookingDate")

    # showing the plot
    fig.show()


def work_with_plotly_to_generate_box_plot():
    df_sheet_index = read_excel(1)
    print(df_sheet_index.info())
    city = df_sheet_index['City']
    postcode = df_sheet_index['Postcode']
    # plotting histogram for x
    fig = go.Figure()

    # updating the figure with y
    fig.add_trace(go.Box(y=city))

    # updating the figure with y1
    fig.add_trace(go.Box(y=postcode))

    fig.show()


def work_with_plotly_to_generate_histogram():
    df_sheet_index = read_excel(1)
    print(df_sheet_index.info())
    city = df_sheet_index['City']
    # plotting histogram for y
    fig = go.Figure(data=[go.Histogram(y=city)])

    fig.show()


def work_with_plotly_to_generate_pie_chart():
    df_sheet_index = read_excel(3)
    print(df_sheet_index.info)

    dealer_id = df_sheet_index['DealerId']
    booking_slot = df_sheet_index['Id']
    # plotting pie chart
    fig = go.Figure(data=[go.Pie(labels=dealer_id,
                                 values=booking_slot)])

    fig.show()


def work_with_plotly_to_generate_bar_chart():
    df_sheet_index = read_excel(3)
    print(df_sheet_index.info)
    # work_with_plotly_to_generate_scatter_plot()
    # bookings on x-axis
    bookings = df_sheet_index['BookingId']
    # print(bookings)
    bookings_slot = df_sheet_index['BookingSlot']
    print(bookings_slot)
    # plotting corresponding y for each
    # country in x
    fig = go.Figure([go.Bar(x=bookings,
                            y=bookings_slot)])
    fig.show()


def work_with_plotly_to_generate_scatter_plot():
    # generating 150 random integers
    # from 1 to 50
    x = np.random.randint(low=1, high=50, size=150) * 0.1

    # generating 150 random integers
    # from 1 to 50
    y = np.random.randint(low=1, high=50, size=150) * 0.1

    # plotting scatter plot
    fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))

    fig.show()


def work_with_plotly_to_generate_scatter_3d_plot():
    df_sheet_index = read_excel(1)
    print(df_sheet_index.info())

    email = df_sheet_index['Email']
    customer_name = df_sheet_index['Customer Name']
    city = df_sheet_index['City']

    # plotting the figure
    fig = px.scatter_3d(df_sheet_index, x=email, y=customer_name, z=city)

    fig.show()


def work_with_plotly_to_generate_scatter_and_bar_plot():
    df_sheet_index = read_excel(1)
    print(df_sheet_index.info())
    plot = px1.Figure(data=[px1.Scatter(
        x=df_sheet_index['Email'],
        y=df_sheet_index['City'],
        mode='markers', )
    ])

    # Add dropdown
    plot.update_layout(
        updatemenus=[
            dict(buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
                direction="down",
            ),
        ]
    )

    plot.show()

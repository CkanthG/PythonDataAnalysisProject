import exceloperations as eop
import exceloperations.read_excel_ops as exo
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')# Press ⌘F8 to toggle the breakpoint.
    exo.read_excel()
    exo.create_histogram()
    exo.create_scatter_plot()
    eop.work_with_plotly()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm, How Are You Today!\nWelcome to Data Analysis')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

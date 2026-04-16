# Quantium Virtual Experience Program

## Task 1
Set up the local Python development environment using a virtual environment and installed required packages like pandas and dash.

## Task 2
Processed raw transaction CSV files into a single clean output file.

### Steps performed
- Combined 3 CSV files
- Filtered only Pink Morsel sales
- Created a new Sales column using quantity × price
- Kept only Sales, Date, and Region columns
- Saved the final output as `formatted_output.csv`

## Tools Used
- Python
- Pandas
- Dash


## Task 3
Created a Dash application with:
- Header for the visualiser
- Line chart of Pink Morsel sales over time
- Date-sorted sales data
- Axis labels for Date and Sales

### Insight
Sales significantly increased after the price increase on 15 January 2021.

## Task 4
Improved the Dash application by:
- Adding a region filter with radio buttons
- Allowing users to view sales for north, east, south, west, or all regions
- Styling the app with a cleaner and more visually appealing layout
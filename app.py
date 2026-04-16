import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Step 1: processed file read
df = pd.read_csv("formatted_output.csv")

# Step 2: convert Date column ko datetime 
df["Date"] = pd.to_datetime(df["Date"])

# Step 3: Date sort
df = df.sort_values("Date")

# Step 4: find total sales per day
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Step 5: line chart create
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)


fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    title_x=0.5
)

# Step 6: Dash app create 
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
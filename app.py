import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f7fb",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.H1(
            "Soul Foods Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#1f3b73",
                "marginBottom": "10px"
            }
        ),

        html.P(
            "Filter sales by region to explore Pink Morsel performance over time.",
            style={
                "textAlign": "center",
                "color": "#4a4a4a",
                "fontSize": "16px",
                "marginBottom": "25px"
            }
        ),

        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "20px",
                "borderRadius": "12px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.08)",
                "maxWidth": "1200px",
                "margin": "0 auto"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "bold",
                        "fontSize": "18px",
                        "color": "#1f3b73",
                        "marginBottom": "12px",
                        "display": "block"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "20px"},
                    labelStyle={
                        "marginRight": "20px",
                        "fontSize": "16px",
                        "color": "#333"
                    }
                ),

                dcc.Graph(id="sales-chart")
            ]
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    daily_sales = filtered_df.groupby("Date", as_index=False)["Sales"].sum()

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({selected_region.title()})"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        title_x=0.5,
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(color="#333")
    )

    fig.update_traces(line=dict(width=3))

    fig.add_vline(
        x="2021-01-15",
        line_width=2,
        line_dash="dash",
        line_color="red"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)
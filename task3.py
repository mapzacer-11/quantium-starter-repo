import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# Layout
app.layout = html.Div(

    style={
        "backgroundColor": "#f4f7fb",
        "minHeight": "100vh",
        "padding": "40px",
        "fontFamily": "Segoe UI, Arial, sans-serif"
    },

    children=[

        html.Div(

            style={
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "18px",
                "boxShadow": "0px 8px 20px rgba(0,0,0,0.15)",
                "maxWidth": "1200px",
                "margin": "auto"
            },

            children=[

                html.H1(
                    "📈 Pink Morsel Sales Dashboard",
                    style={
                        "textAlign": "center",
                        "color": "#1f3b73",
                        "fontSize": "38px",
                        "marginBottom": "10px"
                    }
                ),

                html.P(
                    "Interactive Regional Sales Analysis",
                    style={
                        "textAlign": "center",
                        "fontSize": "18px",
                        "color": "gray",
                        "marginBottom": "30px"
                    }
                ),

                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "South", "value": "south"},
                        {"label": "East", "value": "east"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={
                        "display": "flex",
                        "justifyContent": "center",
                        "gap": "25px",
                        "fontSize": "18px",
                        "marginBottom": "25px"
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
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    daily_sales = (
        filtered_df
        .groupby("date", as_index=False)["sales"]
        .sum()
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title="Pink Morsel Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Sales"
        },
        markers=True
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red",
        line_width=3,
        annotation_text="Price Increase",
        annotation_position="top right"
    )

    fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        title_x=0.5,
        height=650,
        font=dict(size=15),
        margin=dict(l=40, r=40, t=70, b=40)
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
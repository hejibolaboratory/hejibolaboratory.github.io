import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(
    x=[1,2,3,4,5,6,7,8]
        ,y=[691.0689655,	544.8275862	,440.1034483,	402.2068966	,342.5517241,	344.0714286,	458.5185185,	442.8148148],
       
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=[103.5789313,	54.77916169,	71.6339437,	63.5239132,	57.36063695,	59.84044868,	55.10159283,	63.13051485],
            visible=True)

            
    ))

fig.update_yaxes(range=[0, 800])
fig.update_xaxes(title_text="Time of Day")
fig.update_yaxes(title_text="Total Sleep Time (TST, minutes)")

fig.show(color_continuous_scale='gray',
    binary_string=True)
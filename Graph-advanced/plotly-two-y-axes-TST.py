'''
https://plotly.com/python-api-reference/generated/plotly.graph_objects.Scatter.html
'''
import plotly.graph_objects as go
from plotly.subplots import make_subplots

LabelDictForAllEnglish= {
    'xlabel':"Time of Day",
    "y1name":"ToTal Sleep Time",
"y2name":"Wake After Sleep Onset",
    "y1label":"ToTal Sleep Time(TST,minutes)",
"y2label":"Wake After Sleep Onset(WASO,minutes)",
'ticktext' : ['Prelight1', 'Prelight2', 'Prelight3', 'Outbound', 'Inbound', 'Postflight1','Postflight2','Postflight3']
}

LabelDictForAllChinese= {
    'xlabel':"时间",
    "y1name":"总睡眠时长",
"y2name":"睡后觉醒时长",
    "y1label":"总睡眠时长(TST,分)",
"y2label":"睡后觉醒时长(WASO,分)",
'ticktext' : ['飞行前三天', '飞行前二天', '飞行前一天', '去程', '返程', '飞行后一天','飞行后二天','飞行后三天']
}

LabelDictForAll =LabelDictForAllChinese

# Create figure with secondary y-axis
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(  x=[1,2,3,4,5,6,7,8]
        ,y=[691.0689655,	544.8275862	,440.1034483,	402.2068966	,342.5517241,	344.0714286,	458.5185185,	442.8148148],
       
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=[103.5789313,	54.77916169,	71.6339437,	63.5239132,	57.36063695,	59.84044868,	55.10159283,	63.13051485]),
             name=LabelDictForAll["y1name"]),
       

    secondary_y=False,
)

fig.add_trace(
    go.Scatter(x=[1,2,3,4,5,6,7,8], y=[11.65517241,	33.68965517	,36.96551724,	38.68965517	,29.86206897,	29.42857143,	35.96296296	,34.51851852], 
     error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=[5.540415463,	13.47842157,	15.44662268,	16.16708083,	13.08738828,	12.0268904,	13.32062312,	14.76354295]),
    name=LabelDictForAll["y2name"]),

    secondary_y=True,
    
)

fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [1,2, 3,4, 5,6 ,7,8],
        ticktext = LabelDictForAll["ticktext"]
    )
)

# Add figure title
#fig.update_layout(title_text="Double Y Axis Example")

# https://newbedev.com/plotly-how-to-set-line-color
fig['data'][0]['line']['color']="black"
fig['data'][1]['line']['color']="black"
fig['data'][1]['line']['dash']="dot"
# # One of the following dash styles:
#    [‘solid’, ‘dot’, ‘dash’, ‘longdash’, ‘dashdot’, ‘longdashdot’]

#https://plotly.com/python-api-reference/generated/plotly.graph_objects.scatter.html#plotly.graph_objects.scatter.Marker


fig['data'][1]['marker']['symbol']='diamond-dot'
fig['data'][1]['marker']['size']=10

fig.update_yaxes(range=[0, 1000],secondary_y=False)
fig.update_yaxes(range=[0, 200],secondary_y=True)

# Set x-axis title
fig.update_xaxes(title_text=LabelDictForAll["xlabel"])

# Set y-axes titles
fig.update_yaxes(title_text=LabelDictForAll["y1label"], secondary_y=False)
fig.update_yaxes(title_text=LabelDictForAll["y2label"], secondary_y=True)

#https://community.plotly.com/t/having-a-transparent-background-in-plotly-express/30205/2

layout = go.Layout(
    xaxis = dict(

      showticklabels = True,
         linecolor = '#636363',
      linewidth = 2,
    )  ,

   yaxis = dict(
       # to increase data ink-ratio, we do not need grid. 
      #zeroline=True,
      #showline = True,
      #gridcolor = '#bdbdbd',
      #gridwidth = 2,
      #zerolinecolor = '#bdbdbd',
      #zerolinewidth = 2,
      linecolor = '#636363',
      linewidth = 2,
   ),
   yaxis2 = dict(
      zeroline = True,
      showline = True,
      overlaying = 'y',
      side = 'right',      
      linecolor = '#636363',
      linewidth = 2,
   )
)
fig.update_layout(layout)

fig.update_layout({
'plot_bgcolor': 'rgba(255, 255, 255, 0)',
'paper_bgcolor': 'rgba(255, 255, 255, 0)',
})

fig.update_layout(legend=dict(x=0.5,y=1))

fig.show()

#https://community.plotly.com/t/image-export-how-to-set-dpi-alternatively-how-to-scale-down-using-width-and-height/49536
#Image export using the "kaleido" engine requires the kaleido package,
#which can be installed using pip:
#    $ pip install -U kaleido

import plotly.io as pio
#save a figure of 300dpi, with 1.5 inches, and  height 0.75inches
pio.write_image(fig, "/Users/ucdlab/Documents/GitHub/hejibolaboratory.github.io/Graph-advanced/TST-WASO.png", width=1.5*2*300, height=0.75*2*300, scale=1)



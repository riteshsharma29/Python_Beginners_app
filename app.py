import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import configparser
import os
from whitenoise import WhiteNoise
import sys

'''
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/
'''

# read configuration
config = configparser.ConfigParser()
config.read(os.path.join("config","dash_playlist.cfg"))

# read dashboard tab titles/headers
tab_header = config["TAB_HEADER_LIST"]["TAB_HEADER"]
tab_header = tab_header.replace("[", "").replace("]", "")
tab_header = tab_header.split(",")

# read dashboard playlist titles/headers
title_list_1 = config["TAB_PLAYLIST_HEADER"]["TAB1_LIST_HEADER"]
title_list_2 = config["TAB_PLAYLIST_HEADER"]["TAB2_LIST_HEADER"]
title_list_3 = config["TAB_PLAYLIST_HEADER"]["TAB3_LIST_HEADER"]
title_list_4 = config["TAB_PLAYLIST_HEADER"]["TAB4_LIST_HEADER"]
title_list_5 = config["TAB_PLAYLIST_HEADER"]["TAB5_LIST_HEADER"]

# read dashboard playlist url's
url_list_1 = config["TAB_PLAYLIST_URL_LIST"]["TAB1_URL_LIST"]
url_list_2 = config["TAB_PLAYLIST_URL_LIST"]["TAB2_URL_LIST"]
url_list_3 = config["TAB_PLAYLIST_URL_LIST"]["TAB3_URL_LIST"]
url_list_4 = config["TAB_PLAYLIST_URL_LIST"]["TAB4_URL_LIST"]
url_list_5 = config["TAB_PLAYLIST_URL_LIST"]["TAB5_URL_LIST"]

# read dashboard playlist img's
img_list_1 = config["TAB_PLAYLIST_IMG_LIST"]["TAB1_IMG_LIST"]
img_list_2 = config["TAB_PLAYLIST_IMG_LIST"]["TAB2_IMG_LIST"]
img_list_3 = config["TAB_PLAYLIST_IMG_LIST"]["TAB3_IMG_LIST"]
img_list_4 = config["TAB_PLAYLIST_IMG_LIST"]["TAB4_IMG_LIST"]
img_list_5 = config["TAB_PLAYLIST_IMG_LIST"]["TAB5_IMG_LIST"]

##################################################################################################################################

def Populate_Tab(title_list_name,url_list_name,img_list_name):

    title_list_name = title_list_name.replace("[", "").replace("]", "")
    title_list_name = title_list_name.split(",")

    url_list_name = url_list_name.replace("[", "").replace("]", "")
    url_list_name = url_list_name.split(",")

    img_list_name = img_list_name.replace("[", "").replace("]", "")
    img_list_name = img_list_name.split(",")

    tab_content_1 = [dbc.CardHeader(title_list_name[0].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[0].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[0].strip(chr(34)),
        )
    ]
)),]
    tab_content_2 = [dbc.CardHeader(title_list_name[1].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[1].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[1].strip(chr(34)),
        )
    ]
)),]
    tab_content_3 = [dbc.CardHeader(title_list_name[2].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[2].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[2].strip(chr(34)),
        )
    ]
)),]
    tab_content_4 = [dbc.CardHeader(title_list_name[3].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[3].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[3].strip(chr(34)),
        )
    ]
)),]
    tab_content_5 = [dbc.CardHeader(title_list_name[4].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[4].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[4].strip(chr(34)),
        )
    ]
)),]
    tab_content_6 = [dbc.CardHeader(title_list_name[5].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[5].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[5].strip(chr(34)),
        )
    ]
)),]
    tab_content_7 = [dbc.CardHeader(title_list_name[6].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[6].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[6].strip(chr(34)),
        )
    ]
)),]
    tab_content_8 = [dbc.CardHeader(title_list_name[7].strip(chr(34))),
                      dbc.CardBody(html.A(
    href=url_list_name[7].strip(chr(34)),target="_blank",
    children=[
        html.Img(
            src=img_list_name[7].strip(chr(34)),
        )
    ]
)),]

    row_1 = dbc.Row(
        [
            dbc.Col(dbc.Card(tab_content_1, color="primary", outline=True)),
            dbc.Col(dbc.Card(tab_content_2, color="secondary", outline=True)),
            dbc.Col(dbc.Card(tab_content_3, color="info", outline=True)),
            dbc.Col(dbc.Card(tab_content_4, color="success", outline=True)),
        ],
        className="mb-4",
    )

    row_2 = dbc.Row(
        [
            dbc.Col(dbc.Card(tab_content_5, color="success", outline=True)),
            dbc.Col(dbc.Card(tab_content_6, color="warning", outline=True)),
            dbc.Col(dbc.Card(tab_content_7, color="danger", outline=True)),
            dbc.Col(dbc.Card(tab_content_8, color="secondary", outline=True)),
        ],
        className="mb-4",
    )

    tab_rowlist = [row_1, row_2]

    return tab_rowlist


##################################################################################################################################

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# settings required to host files on Heroku
server = app.server
server.wsgi_app = WhiteNoise(server.wsgi_app, root="assets/")

app.layout = html.Div([
    html.Div([
        html.H1('PYTHON BEGINNERS DASHBOARD', style={"color": "blue", "fontStyle": "italic", "fontWeight": "bold"}),
        html.Div([
            html.P('Connect & Get Python E-Books Free: ', style={"color": "green", "fontStyle": "italic", "fontWeight": "bold"}),
            html.A(
                html.Img(src='/assets/linkedin.png', className='img'),
                href='https://www.linkedin.com/in/ritesh-sharma5/', target='_blank'
            ),
            html.A(
                html.Img(src='/assets/youtube.png', className='img', ),
                href='https://www.youtube.com/channel/UCmH_jmNBR5O9o8UA8UHjwag', target='_blank'
            ),
            html.A(
                html.Img(src='/assets/github.png', className='img',
                         id='github'),
                href='https://github.com/riteshsharma29', target='_blank'
            ),
        ])
    ], id='header-div'),
    html.Br(),
    html.Hr(),
    dbc.Tabs([
       dbc.Tab([
           html.Ol([
               html.Br(),
               html.P('Below are few of many best websites available to start your Python journey. Click on each image item to explore and take desired learning pathway.', style={"color": "blue", "fontStyle": "italic", "fontWeight": "bold"}),
               html.Div(Populate_Tab(title_list_1,url_list_1,img_list_1)),
           ])], label=tab_header[0].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.P('Below are few of many best Python E-Books available to start as a Beginner. These E-Books are heavy in size so please feel free to connect me by clicking top right LinkedIn icon and will provide any of these to you absolutely free !!!', style={"color": "blue", "fontStyle": "italic", "fontWeight": "bold"}),
                html.Div(Populate_Tab(title_list_2,url_list_2,img_list_2)),
           ])], label=tab_header[1].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.P('Below are Links to websites which provides Free/Discount Python Ceritfied Courses. Click on each image item to Signup and explore Python Certification Courses', style={"color": "blue", "fontStyle": "italic", "fontWeight": "bold"}),
                html.Div(Populate_Tab(title_list_3,url_list_3,img_list_3)),
            ])], label=tab_header[2].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.P('Below are Links to websites which provides interactive playground to practice and sharpen your Python skills in order to make you competitive professionally. Many companies now-a-days worldwide expect candidates to solve coding challenges before they are hired. So get your hands dirty by exploring these coding playgrounds.', style={"color": "blue", "fontStyle": "italic", "fontWeight": "bold"}),
                html.Div(Populate_Tab(title_list_4,url_list_4,img_list_4)),
            ])], label=tab_header[3].strip(chr(34))),
        dbc.Tab([
            html.Ol([
                html.Br(),
                html.P('Below are Links to Largest Python network on Linkedin and useful Blog websites. Please feel free to join these network and checkout these Blogs to stay connected with the Python commnunity. These resources allows to share and learn best Python work going around the world. Most importantly you can post your Python query once you join in <Python Developers Community (moderated)> group on LinkedIn and awesome community will respond with numerous answers.', style={"color": "blue", "fontStyle": "italic", "fontWeight": "bold"}),
                html.Div(Populate_Tab(title_list_5,url_list_5,img_list_5)),
            ])], label=tab_header[4].strip(chr(34))),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)


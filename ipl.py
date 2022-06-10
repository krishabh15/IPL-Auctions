# -*- coding: utf-8 -*-
from tkinter import font
from turtle import width
import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(page_title='IPL AUCTIONS',  layout='wide', page_icon=':ipl:')

#this is the header
 

t1, t2 = st.columns((0.07,1)) 
#my_name = '<p style="font-family:Caveat; color:Black;">By Rishabh Khanna</p>'
t1.image('./Indian_Premier_League_Official_Logo.svg.png', width = 100)
t2.title("IPL AUCTIONS- PLAYER VALUATION")
#t2.markdown(my_name, unsafe_allow_html=True)
t2.markdown("By Rishabh Khanna")


## Data

with st.spinner('Loading Report...'):

    #Batter Data

    st.subheader("BATSAMAN", anchor=None)

    df = pd.read_csv('./bat.csv')
    
    list = st.selectbox('Player', df, help = 'Filter report to show only one Player')
    st.dataframe(df[df['Player']== list])


    #chart_data = df[] # ['Selling Price (Crore Rs)', 'Valuation (Crore Rs.)', 'Difference (Crore Rs.)']
    fig = px.line(df.sort_values(by=['Difference (Crore Rs.)']).iloc[0:], x='Player', y='Difference (Crore Rs.)')
    st.plotly_chart(fig, use_container_width=True)

    x_axis = df['Player']

    # Create traces
    layout = dict(
                xaxis=dict(title='Player'),
                yaxis=dict(title='Crores'))
    fig = go.Figure(layout =layout)
    fig.add_trace(go.Scatter(x=x_axis, y=df['Selling Price (Crore Rs)'],
                        mode='lines',
                        name='Selling Price'))
    fig.add_trace(go.Scatter(x=x_axis, y=df['Valuation (Crore Rs.)'],
                        mode='lines',
                        name='Valuation'))
    st.plotly_chart(fig, use_container_width=True)
    
    #Bowler Data

    st.subheader("BOWLERS", anchor=None)

    df = pd.read_csv('./bowl.csv')
    
    list = st.selectbox('Player', df, help = 'Filter report to show only one Player')
    st.dataframe(df[df['Player']== list])

    #list = []
    #list.extend(df['Player'].tolist())

    #st.selectbox('All', list, help = 'Filter report to show only one Player')
    #if list=='All':
    #    st.dataframe(df)
    #else: 
    #    st.dataframe(df[df['Player']== list])


    #chart_data = df[] # ['Selling Price (Crore Rs)', 'Valuation (Crore Rs.)', 'Difference (Crore Rs.)']
    fig = px.line(df.sort_values(by=['Difference (Crore Rs.)']).iloc[0:], x='Player', y='Difference (Crore Rs.)')
    st.plotly_chart(fig, use_container_width=True)

    x_axis = df['Player']

    # Create traces
    layout = dict(
                xaxis=dict(title='Player'),
                yaxis=dict(title='Crores'))
    fig = go.Figure(layout =layout)
    fig.add_trace(go.Scatter(x=x_axis, y=df['Selling Price (Crore Rs)'],
                        mode='lines',
                        name='Selling Price'))
    fig.add_trace(go.Scatter(x=x_axis, y=df['Valuation (Crore Rs.)'],
                        mode='lines',
                        name='Valuation'))
    st.plotly_chart(fig, use_container_width=True)

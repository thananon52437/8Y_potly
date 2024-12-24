from django.shortcuts import render
import pandas as pd
import plotly.express as px

def line_chart_view(request):
    # โหลดข้อมูล CSV
    file_path = 'data/Apple.csv'  # ระบุที่เก็บไฟล์ CSV
    df = pd.read_csv(file_path)
    
    # แปลงข้อมูล
    df['Close/Last'] = df['Close/Last'].str.replace('$', '').astype(float)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')  # เรียงตามวันที่
    
    # สร้างกราฟด้วย Plotly
    fig = px.line(df, x='Date', y='Close/Last', title='Apple Stock Prices Over Time')
    chart_html = fig.to_html(full_html=False)
    
    return render(request, 'line_chart.html', {'chart': chart_html})

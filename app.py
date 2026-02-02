from flask import Flask, render_template, jsonify
import pandas as pd
import json
from datetime import datetime

app = Flask(__name__)

def load_dashboard_data():
    """Load data from Excel file and convert to JSON format for charts"""
    try:
        # Read all sheets from Excel
        excel_file = 'data/qa_dashboard_data.xlsx'
        
        # Read monthly data
        monthly_df = pd.read_excel(excel_file, sheet_name='MonthlyData')
        
        # Read division data
        division_df = pd.read_excel(excel_file, sheet_name='DivisionData')
        
        # Read current month summary
        summary_df = pd.read_excel(excel_file, sheet_name='CurrentMonth')
        
        # Prepare data for frontend
        data = {
            'months': monthly_df['Month'].tolist(),
            'totalEngagement': monthly_df['TotalEngagement'].tolist(),
            'reportsGenerated': monthly_df['ReportsGenerated'].tolist(),
            'issuesRaised': monthly_df['IssuesRaised'].tolist(),
            'divisions': {},
            'currentMonth': {}
        }
        
        # Process division trends
        divisions = ['ConcreteRepairs', 'MembraneRoofing', 'Facade', 'Tanking', 'OldSansom']
        division_names = ['Concrete Repairs', 'Membrane Roofing', 'Facade', 'Tanking', 'Old Sansom']
        division_colors = ['#f87171', '#60a5fa', '#a78bfa', '#fbbf24', '#34d399']
        
        for i, div in enumerate(divisions):
            data['divisions'][div] = {
                'name': division_names[i],
                'color': division_colors[i],
                'trend': division_df[div].tolist()
            }
        
        # Process current month data
        for _, row in summary_df.iterrows():
            div_key = row['Division'].replace(' ', '')
            data['currentMonth'][div_key] = {
                'name': row['Division'],
                'total': int(row['TotalEngagement']),
                'pass': int(row['Pass']),
                'fail': int(row['Fail']),
                'na': int(row['NA']),
                'reports': int(row['Reports']),
                'issues': int(row['Issues'])
            }
        
        # Calculate totals for current month
        data['totals'] = {
            'engagement': int(summary_df['TotalEngagement'].sum()),
            'reports': int(summary_df['Reports'].sum()),
            'issues': int(summary_df['Issues'].sum())
        }
        
        return data
        
    except Exception as e:
        print(f"Error loading data: {e}")
        return get_default_data()

def get_default_data():
    """Return default data if Excel file is not available"""
    return {
        'months': ['Oct', 'Nov', 'Dec', 'Jan'],
        'totalEngagement': [520, 580, 630, 680],
        'reportsGenerated': [110, 125, 136, 152],
        'issuesRaised': [8, 10, 11, 14],
        'divisions': {
            'ConcreteRepairs': {
                'name': 'Concrete Repairs',
                'color': '#f87171',
                'trend': [95, 100, 108, 124]
            },
            'MembraneRoofing': {
                'name': 'Membrane Roofing',
                'color': '#60a5fa',
                'trend': [70, 75, 83, 87]
            },
            'Facade': {
                'name': 'Facade',
                'color': '#a78bfa',
                'trend': [78, 85, 89, 82]
            },
            'Tanking': {
                'name': 'Tanking',
                'color': '#fbbf24',
                'trend': [45, 48, 55, 67]
            },
            'OldSansom': {
                'name': 'Old Sansom',
                'color': '#34d399',
                'trend': [232, 272, 295, 320]
            }
        },
        'currentMonth': {
            'ConcreteRepairs': {'name': 'Concrete Repairs', 'total': 124, 'pass': 83, 'fail': 2, 'na': 4, 'reports': 28, 'issues': 2},
            'MembraneRoofing': {'name': 'Membrane Roofing', 'total': 87, 'pass': 50, 'fail': 2, 'na': 11, 'reports': 19, 'issues': 3},
            'Facade': {'name': 'Facade', 'total': 82, 'pass': 70, 'fail': 1, 'na': 9, 'reports': 18, 'issues': 2},
            'Tanking': {'name': 'Tanking', 'total': 67, 'pass': 26, 'fail': 0, 'na': 1, 'reports': 15, 'issues': 0},
            'OldSansom': {'name': 'Old Sansom', 'total': 320, 'pass': 241, 'fail': 10, 'na': 18, 'reports': 72, 'issues': 7}
        },
        'totals': {
            'engagement': 680,
            'reports': 152,
            'issues': 14
        }
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    data = load_dashboard_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

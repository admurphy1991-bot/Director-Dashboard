# QA Director Dashboard

A professional, interactive dashboard for tracking QA engagement metrics across multiple divisions.

## Features

- 📊 Real-time metrics visualization
- 📈 Trend analysis across months
- 🏢 Division-specific breakdowns
- 📄 Print-friendly reports
- 📱 Responsive design for mobile/tablet/desktop
- 📂 Excel-based data updates (no coding required!)

## Live Demo

Your dashboard will be available at: `https://your-app-name.onrender.com`

## Metrics Tracked

- **Total QA Engagement** - Overall quality assurance activities
- **Reports Generated** - Number of QA reports created
- **Issues Raised** - Quality issues identified
- **Pass/Fail/N/A Status** - Detailed breakdown by division
- **Division Trends** - Historical performance by team

## Divisions

1. Concrete Repairs
2. Membrane Roofing
3. Facade
4. Tanking
5. Old Sansom

## Technology Stack

- **Backend:** Python Flask
- **Frontend:** HTML5, TailwindCSS, Chart.js
- **Data:** Excel (XLSX) via pandas
- **Hosting:** Render (Free tier available)

## Quick Start

See `DEPLOYMENT_INSTRUCTIONS.md` for complete setup and update instructions.

### Update Data

1. Edit `data/qa_dashboard_data.xlsx`
2. Upload to GitHub
3. Dashboard auto-updates in 2-5 minutes

## Project Structure

```
qa-dashboard/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── Procfile                    # Render deployment config
├── runtime.txt                 # Python version
├── templates/
│   └── index.html             # Dashboard HTML template
├── data/
│   └── qa_dashboard_data.xlsx # Your data source
└── DEPLOYMENT_INSTRUCTIONS.md # Full guide
```

## Local Development

```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000
```

## Data Format

The dashboard reads from three Excel sheets:

1. **MonthlyData** - Overall monthly trends
2. **DivisionData** - Division-specific trends
3. **CurrentMonth** - Latest month detailed breakdown

See the Excel file for examples and the Instructions sheet for details.

## Support

For issues or questions, refer to `DEPLOYMENT_INSTRUCTIONS.md` or check the Render deployment logs.

## License

Proprietary - Internal use only

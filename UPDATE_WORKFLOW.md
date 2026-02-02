# 🔄 DATA UPDATE WORKFLOW

## Visual Guide: How Updates Work

```
┌─────────────────────────────────────────────────────────────────┐
│  YOUR COMPUTER                                                  │
│                                                                 │
│  1. Edit qa_dashboard_data.xlsx                                │
│     ├── Update MonthlyData sheet                               │
│     ├── Update DivisionData sheet                              │
│     └── Update CurrentMonth sheet                              │
│                                                                 │
│  2. Save the file                                              │
│                                                                 │
└─────────────────┬───────────────────────────────────────────────┘
                  │
                  │ Upload via GitHub web interface
                  │ or git push
                  ↓
┌─────────────────────────────────────────────────────────────────┐
│  GITHUB (github.com/your-username/qa-dashboard)                 │
│                                                                 │
│  data/qa_dashboard_data.xlsx ← Your updated file               │
│                                                                 │
└─────────────────┬───────────────────────────────────────────────┘
                  │
                  │ Automatic webhook
                  │ triggers deployment
                  ↓
┌─────────────────────────────────────────────────────────────────┐
│  RENDER (render.com)                                            │
│                                                                 │
│  1. Detects changes in GitHub                                  │
│  2. Pulls latest code                                          │
│  3. Installs dependencies (2-3 min)                            │
│  4. Starts Flask app                                           │
│  5. Dashboard goes live with new data! ✅                      │
│                                                                 │
└─────────────────┬───────────────────────────────────────────────┘
                  │
                  │ Accessible via URL
                  ↓
┌─────────────────────────────────────────────────────────────────┐
│  YOUR DASHBOARD                                                 │
│                                                                 │
│  https://qa-dashboard-xxxx.onrender.com                        │
│                                                                 │
│  🎨 Updated charts and metrics                                 │
│  📊 New data displayed                                         │
│  📱 Accessible from any device                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Timeline

```
You upload to GitHub          0:00
  ↓
GitHub receives file          0:10 (10 seconds)
  ↓
Render detects change         0:30 (30 seconds)
  ↓
Render builds app            0:30-4:00 (2-5 minutes)
  ↓
Dashboard live with updates   5:00 ✅
```

## Three Files Power Your Dashboard

```
qa_dashboard_data.xlsx
│
├── MonthlyData sheet ────────→ Total Engagement Trend chart
│                          └──→ Reports & Issues Trend chart
│
├── DivisionData sheet ───────→ Division Engagement Trends chart
│
└── CurrentMonth sheet ───────→ Current month metrics
                          ├──→ Engagement by Division chart
                          ├──→ Status Breakdown chart
                          └──→ Division detail cards
```

## Data Flow

```
Excel Cell → Python Reads → Flask API → JavaScript → Chart.js → Your Screen

Example:
MonthlyData!B5 (680) → pandas.read_excel() → /api/data endpoint 
→ fetch('/api/data') → dashboardData.totalEngagement[3] 
→ Chart.js renders → You see "680" on the dashboard
```

## What Happens When You Edit Excel

```
Old Data                    New Data
--------                    --------
Jan | 680                   Jan | 680
                           Feb | 725  ← You add this

                           ↓

Dashboard Before            Dashboard After
-----------------          -----------------
[Chart shows Jan: 680]     [Chart shows Jan: 680, Feb: 725]
Total: 680                 Total: 725
↑ 7.9% from last month     ↑ 6.6% from last month
```

## Safety Features

✅ If Excel file is missing → Dashboard uses default demo data
✅ If Excel has errors → Python catches them and logs errors  
✅ Original mockup HTML → Saved as backup reference
✅ Git history → Can revert to any previous version

## Best Practices

1. **Always download** the current Excel file before editing
2. **Save a backup** before making major changes
3. **Test in Excel** before uploading (check for formula errors)
4. **One change at a time** - easier to debug if something goes wrong
5. **Use commit messages** like "Add February 2026 data" to track changes

---

Remember: Your Excel file is the single source of truth. 
Change Excel → Dashboard updates automatically! 🎉

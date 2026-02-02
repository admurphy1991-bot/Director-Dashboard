# QA Director Dashboard - Deployment & Update Guide

## Overview
This QA Director Dashboard displays engagement metrics across your divisions. The dashboard is powered by data from an Excel file that you can easily update whenever you need to refresh the metrics.

---

## 🚀 PART 1: Deploy to Render (One-Time Setup)

### Prerequisites
- A GitHub account (free)
- A Render account (free tier available at https://render.com)

### Step 1: Upload to GitHub

1. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Repository name: `qa-dashboard` (or any name you prefer)
   - Set to Public or Private (your choice)
   - Do NOT initialize with README, .gitignore, or license
   - Click "Create repository"

2. **Upload your dashboard files:**
   
   **Option A - Using GitHub's web interface (Easiest):**
   - On your new repository page, click "uploading an existing file"
   - Drag and drop ALL the files from your `qa-dashboard` folder
   - Important files to include:
     - `app.py`
     - `requirements.txt`
     - `Procfile`
     - `runtime.txt`
     - `.gitignore`
     - `templates/` folder (with index.html inside)
     - `data/` folder (with qa_dashboard_data.xlsx inside)
   - Click "Commit changes"

   **Option B - Using Git command line:**
   ```bash
   cd qa-dashboard
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/qa-dashboard.git
   git push -u origin main
   ```

### Step 2: Deploy on Render

1. **Sign up/Login to Render:**
   - Go to https://render.com
   - Sign up with your GitHub account (recommended)

2. **Create a new Web Service:**
   - Click "New +" button in top right
   - Select "Web Service"
   - Connect your GitHub account if prompted
   - Select your `qa-dashboard` repository

3. **Configure the Web Service:**
   - **Name:** `qa-dashboard` (or your preferred name)
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Instance Type:** Free (or paid if you prefer)

4. **Deploy:**
   - Click "Create Web Service"
   - Wait 2-5 minutes for deployment
   - Once complete, you'll see a URL like: `https://qa-dashboard-xxxx.onrender.com`

5. **Access your dashboard:**
   - Click the URL to view your live dashboard!
   - Bookmark this URL for easy access

---

## 📊 PART 2: Update Dashboard Data (Anytime)

### Quick Update Process

Whenever you need to update the dashboard with new metrics:

#### Step 1: Download the Current Excel Template

**Option A - From your computer:**
- If you have the original `qa_dashboard_data.xlsx` file, use that

**Option B - From GitHub:**
- Go to your GitHub repository
- Navigate to `data/qa_dashboard_data.xlsx`
- Click "Download" or "Raw" and save the file

#### Step 2: Edit the Excel File

Open `qa_dashboard_data.xlsx` in Excel and update the data:

**Sheet 1 - MonthlyData:** Overall trends across months
```
Month | TotalEngagement | ReportsGenerated | IssuesRaised
Oct   | 520            | 110              | 8
Nov   | 580            | 125              | 10
Dec   | 630            | 136              | 11
Jan   | 680            | 152              | 14
```
- Add/update rows for each month
- Keep months in chronological order

**Sheet 2 - DivisionData:** Engagement trends per division
```
ConcreteRepairs | MembraneRoofing | Facade | Tanking | OldSansom
95              | 70              | 78     | 45      | 232
100             | 75              | 85     | 48      | 272
108             | 83              | 89     | 55      | 295
124             | 87              | 82     | 67      | 320
```
- Each row = one month (matches MonthlyData)
- Each column = one division
- DO NOT change column headers

**Sheet 3 - CurrentMonth:** Current month breakdown by division
```
Division         | TotalEngagement | Pass | Fail | NA | Reports | Issues
Concrete Repairs | 124            | 83   | 2    | 4  | 28      | 2
Membrane Roofing | 87             | 50   | 2    | 11 | 19      | 3
Facade           | 82             | 70   | 1    | 9  | 18      | 2
Tanking          | 67             | 26   | 0    | 1  | 15      | 0
Old Sansom       | 320            | 241  | 10   | 18 | 72      | 7
```
- Update the latest month's detailed metrics
- Division names MUST match DivisionData columns
- TotalEngagement should match the last row in DivisionData

**IMPORTANT:**
- ✅ DO: Change the numbers
- ✅ DO: Add more months (add rows to MonthlyData and DivisionData together)
- ❌ DON'T: Change column headers
- ❌ DON'T: Change sheet names
- ❌ DON'T: Change division names

#### Step 3: Upload Updated File to GitHub

**Option A - GitHub Web Interface (Easiest):**
1. Go to your repository on GitHub
2. Navigate to the `data` folder
3. Click on `qa_dashboard_data.xlsx`
4. Click the trash icon to delete it
5. Commit the deletion
6. Go back to the `data` folder
7. Click "Add file" > "Upload files"
8. Upload your updated `qa_dashboard_data.xlsx`
9. Click "Commit changes"

**Option B - Git Command Line:**
```bash
cd qa-dashboard
# Replace the old file with your updated one
git add data/qa_dashboard_data.xlsx
git commit -m "Update dashboard data for [Month Year]"
git push
```

#### Step 4: Dashboard Auto-Updates

- Render automatically detects the changes to your GitHub repository
- It will rebuild and redeploy (takes 2-5 minutes)
- Go to your Render dashboard to watch the deployment
- Once complete, refresh your dashboard URL
- Your new data will be live! 🎉

---

## 🔧 Troubleshooting

### Dashboard shows old data
- Wait 2-5 minutes after pushing changes to GitHub
- Check Render dashboard to ensure deployment completed
- Hard refresh your browser (Ctrl+F5 or Cmd+Shift+R)

### Deployment failed
- Check Render logs for error messages
- Verify your Excel file format is correct (.xlsx)
- Ensure all sheet names and headers match exactly
- Make sure requirements.txt and other files weren't modified

### Excel file won't upload to GitHub
- File must be named exactly: `qa_dashboard_data.xlsx`
- Must be in the `data/` folder
- File size should be under 100MB

### Data looks wrong on dashboard
- Open Excel file and verify data is correct
- Check that division names match exactly
- Ensure months in MonthlyData match rows in DivisionData
- Verify no formula errors in Excel (#REF!, #VALUE!, etc.)

---

## 📝 Tips for Success

1. **Keep a backup:** Always save a copy of your Excel file before editing

2. **Test locally first:** Open the Excel file and double-check all numbers before uploading

3. **Consistent timing:** Update data on a regular schedule (e.g., first Monday of each month)

4. **Version control:** In your commit messages, note what you changed (e.g., "Added February 2026 data")

5. **Division names:** Keep division names consistent - changing them requires updating both DivisionData headers AND CurrentMonth division column

---

## 🎨 Customization Options

Want to customize your dashboard?

### Change Division Names
1. Edit `CurrentMonth` sheet - Division column
2. Edit `DivisionData` sheet - Column headers
3. Both must match exactly

### Add More Months
1. Add new row to `MonthlyData`
2. Add new row to `DivisionData` (same month)
3. Update `CurrentMonth` with latest month data

### Change Colors
- Edit `templates/index.html`
- Look for division colors in the JavaScript section
- Use hex color codes (e.g., #f87171 for red)

---

## 📞 Support

If you need help:
1. Check the "Instructions" sheet in the Excel file
2. Review this guide
3. Check Render deployment logs for errors
4. Verify your Excel data format matches the template

---

## 🔄 Quick Reference: Update Workflow

```
1. Download qa_dashboard_data.xlsx
2. Update the numbers in Excel
3. Save the file
4. Upload to GitHub (data folder)
5. Wait 2-5 minutes
6. Refresh dashboard URL
7. Done! ✅
```

---

Remember: The Excel file is the single source of truth for your dashboard. Update it, upload it, and your dashboard refreshes automatically!

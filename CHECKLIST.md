# ✅ DEPLOYMENT CHECKLIST

Print this out and check off each step as you complete it!

---

## 📦 INITIAL DEPLOYMENT

### Before You Start
- [ ] You have a GitHub account (sign up at github.com)
- [ ] You have a Render account (sign up at render.com)
- [ ] You have downloaded the qa-dashboard folder
- [ ] You have reviewed the Excel template structure

### Step 1: GitHub Setup
- [ ] Created new repository named "qa-dashboard"
- [ ] Repository is created (can be public or private)
- [ ] Uploaded all project files to GitHub:
  - [ ] app.py
  - [ ] requirements.txt
  - [ ] Procfile
  - [ ] runtime.txt
  - [ ] .gitignore
  - [ ] templates/index.html
  - [ ] data/qa_dashboard_data.xlsx
  - [ ] README.md
  - [ ] DEPLOYMENT_INSTRUCTIONS.md
- [ ] Files are visible in repository on GitHub
- [ ] Verified Excel file is in data/ folder

### Step 2: Render Setup
- [ ] Signed up for Render account
- [ ] Connected GitHub account to Render
- [ ] Created new Web Service
- [ ] Selected correct GitHub repository
- [ ] Configured build settings:
  - [ ] Build Command: `pip install -r requirements.txt`
  - [ ] Start Command: `gunicorn app:app`
- [ ] Selected Free tier (or paid if preferred)
- [ ] Clicked "Create Web Service"

### Step 3: Deployment Verification
- [ ] Deployment started (check Render dashboard)
- [ ] Build completed successfully (no errors in logs)
- [ ] Service is "Live" status
- [ ] Received deployment URL (e.g., https://qa-dashboard-xxxx.onrender.com)
- [ ] Clicked URL and dashboard loads
- [ ] All charts are visible
- [ ] Data matches your Excel file
- [ ] Tested print functionality
- [ ] Tested on mobile/tablet (optional)

### Step 4: Bookmark & Share
- [ ] Bookmarked dashboard URL
- [ ] Shared URL with team (if applicable)
- [ ] Noted URL for future reference
- [ ] Saved Excel template location

---

## 🔄 REGULAR DATA UPDATES

### Each Time You Update Data

#### Preparation
- [ ] Downloaded current qa_dashboard_data.xlsx from GitHub
- [ ] Created backup copy (save as qa_dashboard_data_BACKUP_[DATE].xlsx)
- [ ] Opened Excel file

#### Edit Data
- [ ] Updated MonthlyData sheet
  - [ ] Added/updated month rows
  - [ ] Verified TotalEngagement numbers
  - [ ] Verified ReportsGenerated numbers
  - [ ] Verified IssuesRaised numbers
  
- [ ] Updated DivisionData sheet
  - [ ] Added/updated rows (matching MonthlyData months)
  - [ ] Verified each division column has data
  - [ ] Numbers match expected trends

- [ ] Updated CurrentMonth sheet
  - [ ] Updated all division rows
  - [ ] Verified TotalEngagement matches last DivisionData row
  - [ ] Updated Pass/Fail/NA counts
  - [ ] Updated Reports and Issues counts

#### Quality Checks
- [ ] All numbers are whole numbers (no decimals)
- [ ] No formula errors (#REF!, #VALUE!, etc.)
- [ ] Division names match between sheets
- [ ] Month count matches between MonthlyData and DivisionData
- [ ] Totals add up correctly
- [ ] Saved Excel file

#### Upload to GitHub
- [ ] Logged into GitHub
- [ ] Navigated to qa-dashboard repository
- [ ] Went to data/ folder
- [ ] Deleted old qa_dashboard_data.xlsx
- [ ] Uploaded new qa_dashboard_data.xlsx
- [ ] Added commit message (e.g., "Update Feb 2026 data")
- [ ] Clicked "Commit changes"

#### Verify Deployment
- [ ] Went to Render dashboard
- [ ] Saw automatic deployment trigger
- [ ] Waited for deployment to complete (2-5 minutes)
- [ ] Deployment status shows "Live"
- [ ] No errors in deployment logs

#### Test Dashboard
- [ ] Opened dashboard URL
- [ ] Hard refreshed browser (Ctrl+F5 or Cmd+Shift+R)
- [ ] New data is visible
- [ ] All charts updated correctly
- [ ] Total engagement matches
- [ ] Reports/Issues counts match
- [ ] Division cards show correct data
- [ ] Printed test page (optional)

---

## 🆘 TROUBLESHOOTING CHECKLIST

### Dashboard Not Updating
- [ ] Waited at least 5 minutes after upload
- [ ] Checked Render deployment completed
- [ ] Hard refreshed browser (Ctrl+F5)
- [ ] Cleared browser cache
- [ ] Tried different browser
- [ ] Checked Render logs for errors

### Deployment Failed
- [ ] Checked Render logs for error message
- [ ] Verified all files uploaded to GitHub
- [ ] Confirmed Excel file is .xlsx format
- [ ] Checked Excel file for errors
- [ ] Verified requirements.txt is present
- [ ] Verified Procfile is present

### Data Looks Wrong
- [ ] Opened Excel file to verify data
- [ ] Checked division names match exactly
- [ ] Verified months align across sheets
- [ ] Checked for formula errors in Excel
- [ ] Verified numbers are not formulas in Excel
- [ ] Re-uploaded Excel file

### Excel Upload Failed
- [ ] Confirmed file name is exactly: qa_dashboard_data.xlsx
- [ ] Confirmed file is in data/ folder
- [ ] Verified file size is under 100MB
- [ ] Tried uploading again
- [ ] Checked internet connection

---

## 📅 MONTHLY MAINTENANCE CHECKLIST

### First of Each Month
- [ ] Prepare new month's data
- [ ] Update Excel file (all three sheets)
- [ ] Upload to GitHub
- [ ] Verify dashboard updates
- [ ] Share updated dashboard link with stakeholders
- [ ] Archive previous month's data (optional)

### Quarterly Review
- [ ] Review dashboard performance
- [ ] Check if divisions need updating
- [ ] Verify all metrics are still relevant
- [ ] Consider adding new months
- [ ] Review and update documentation

---

## 📝 NOTES SECTION

**Dashboard URL:**
_________________________________

**GitHub Repository:**
_________________________________

**Last Updated:**
_________________________________

**Next Update Due:**
_________________________________

**Issues/Questions:**
_________________________________
_________________________________
_________________________________

---

## Quick Reference

**Upload Data:** GitHub → data/ → Replace Excel file → Commit
**Check Status:** Render dashboard → Deployments tab
**View Dashboard:** [Your URL here]
**Get Help:** See DEPLOYMENT_INSTRUCTIONS.md

---

**Remember:** The process gets faster each time. After the first update, it typically takes just 5 minutes!

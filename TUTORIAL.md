# 📺 STEP-BY-STEP TUTORIAL: QA Dashboard Setup & Updates

This document walks you through every click and keystroke. Perfect for first-time users!

---

## 🎬 PART 1: FIRST-TIME DEPLOYMENT (10 minutes)

### Scene 1: Upload to GitHub (3 minutes)

**What you'll do:** Put your dashboard code on GitHub so Render can access it.

1. **Open your web browser**
   - Go to: https://github.com

2. **Sign in or create account**
   - If new: Click "Sign up" → Follow prompts
   - If existing: Click "Sign in" → Enter credentials

3. **Create new repository**
   - Click the "+" icon (top right corner)
   - Select "New repository"
   - You'll see a form

4. **Fill out the form**
   - Repository name: Type `qa-dashboard`
   - Description (optional): Type "QA Director Dashboard"
   - Select "Public" or "Private" (your choice)
   - Leave checkboxes UNCHECKED (no README, no .gitignore, no license)
   - Click green "Create repository" button

5. **Upload files**
   - You'll see "Quick setup" page
   - Look for blue link "uploading an existing file"
   - Click it
   - You'll see "Drag files here" area

6. **Drag your files**
   - Open the qa-dashboard folder on your computer
   - Select ALL files and folders
   - Drag them into the browser window
   - Wait for upload (progress bar appears)

7. **Commit the files**
   - Scroll down to bottom of page
   - In "Commit changes" box, type: "Initial dashboard setup"
   - Click green "Commit changes" button
   - Page refreshes → You'll see all your files listed!

✅ **Success check:** You should see folders (templates, data) and files (app.py, README.md, etc.)

---

### Scene 2: Deploy on Render (5 minutes)

**What you'll do:** Tell Render to host your dashboard online.

1. **Open new tab**
   - Go to: https://render.com

2. **Create Render account**
   - Click "Get Started" or "Sign Up"
   - RECOMMENDED: Click "Continue with GitHub"
   - Authorize Render to access GitHub
   - OR: Use email signup if preferred

3. **Create new Web Service**
   - You'll see Render Dashboard
   - Click blue "New +" button (top right)
   - Select "Web Service" from dropdown
   - You'll see "Connect a repository" page

4. **Connect your repository**
   - Look for your "qa-dashboard" repository
   - If you don't see it, click "Configure account"
   - Grant access to repositories
   - Click "Connect" next to qa-dashboard

5. **Configure deployment settings**
   - You'll see configuration form
   
   **Fill in these fields EXACTLY:**
   - Name: `qa-dashboard` (or choose your own)
   - Region: Select closest to you (e.g., Oregon, Frankfurt)
   - Branch: `main` (should auto-fill)
   - Runtime: Select "Python 3"
   - Build Command: Type `pip install -r requirements.txt`
   - Start Command: Type `gunicorn app:app`
   
   **Scroll down:**
   - Instance Type: Select "Free" (or paid if you prefer)
   - Leave other settings as default

6. **Create the service**
   - Click blue "Create Web Service" button at bottom
   - You'll see "Deploying..." page
   - Build logs start appearing (green text)

7. **Wait for deployment**
   - Watch the logs scroll by (interesting to watch!)
   - Status changes: "In progress" → "Live"
   - Takes about 2-5 minutes
   - Don't close the page!

8. **Get your URL**
   - When status shows "Live" (green dot)
   - Look at top of page for your URL
   - Format: `https://qa-dashboard-xxxx.onrender.com`
   - Copy this URL!

9. **Test your dashboard**
   - Click the URL
   - New tab opens
   - Dashboard appears with charts! 🎉

✅ **Success check:** You see the QA Director Dashboard with colorful charts showing data

---

## 🎬 PART 2: UPDATE DATA (5 minutes)

### Scene 3: Edit Excel File (2 minutes)

**What you'll do:** Change the numbers in your data file.

1. **Find your Excel file**
   - On your computer, go to qa-dashboard folder
   - Open "data" folder
   - Find: qa_dashboard_data.xlsx
   - FIRST: Make a copy! (Right-click → Copy → Paste)
   - Rename copy to: qa_dashboard_data_BACKUP.xlsx

2. **Open Excel file**
   - Double-click qa_dashboard_data.xlsx
   - Opens in Excel (or Google Sheets)
   - You'll see tabs at bottom: Instructions, MonthlyData, DivisionData, CurrentMonth

3. **Read Instructions tab (first time only)**
   - Click "Instructions" tab
   - Read the overview
   - Understand what each sheet does

4. **Update MonthlyData**
   - Click "MonthlyData" tab
   - You'll see columns: Month, TotalEngagement, ReportsGenerated, IssuesRaised
   - Example: To add February:
     - Click cell A6 (next empty row)
     - Type: Feb
     - Press Tab
     - Type the total engagement number
     - Press Tab
     - Type reports number
     - Press Tab
     - Type issues number
     - Press Enter

5. **Update DivisionData**
   - Click "DivisionData" tab
   - Add a new row (same month as above)
   - Fill in numbers for each division column
   - Example: Row 5 should have Feb data for all 5 divisions

6. **Update CurrentMonth**
   - Click "CurrentMonth" tab
   - Update the numbers for each division
   - These should match your latest month
   - Update: TotalEngagement, Pass, Fail, NA, Reports, Issues

7. **Save the file**
   - Press Ctrl+S (Windows) or Cmd+S (Mac)
   - Or: File → Save
   - Close Excel

✅ **Success check:** File saved, no error messages

---

### Scene 4: Upload to GitHub (2 minutes)

**What you'll do:** Replace the old Excel file with your new one.

1. **Go to GitHub**
   - Open browser
   - Go to github.com
   - Sign in if needed
   - Click on your "qa-dashboard" repository

2. **Navigate to data folder**
   - You'll see list of files
   - Click on "data" folder
   - You'll see qa_dashboard_data.xlsx

3. **Delete old file**
   - Click on "qa_dashboard_data.xlsx"
   - You'll see the file page
   - Click trash can icon (top right, near "Edit")
   - Scroll down
   - In commit message, type: "Remove old data"
   - Click "Commit changes"

4. **Upload new file**
   - You're back in data folder
   - Click "Add file" button
   - Select "Upload files"
   - Drag your updated qa_dashboard_data.xlsx file
   - OR: Click "choose your files" and select it

5. **Commit the upload**
   - Scroll down to commit box
   - Type message: "Update data for [Month Year]"
   - Example: "Update data for February 2026"
   - Click "Commit changes"

✅ **Success check:** You see qa_dashboard_data.xlsx in the data folder with recent timestamp

---

### Scene 5: Watch Deployment (1 minute)

**What you'll do:** Verify Render picks up your changes.

1. **Go to Render**
   - Open new tab
   - Go to: render.com
   - Click "Dashboard" (if not already there)

2. **View your service**
   - Click on "qa-dashboard" service
   - You'll see deployment page

3. **Watch the deployment**
   - Look for "Events" section
   - You should see: "Deploy triggered by update"
   - Status changes to "In progress"
   - Build logs appear
   - Wait 2-5 minutes
   - Status changes to "Live"

✅ **Success check:** Status shows green "Live" dot

---

### Scene 6: Verify Dashboard (1 minute)

**What you'll do:** Check that your new data appears.

1. **Open dashboard**
   - Click your dashboard URL
   - Or: Go to bookmarked URL

2. **Hard refresh**
   - Windows: Press Ctrl+F5
   - Mac: Press Cmd+Shift+R
   - This clears cache

3. **Check the data**
   - Look at "Total QA Engagement" number
   - Should match your latest Excel data
   - Look at charts
   - Should show your new month
   - Check division cards
   - Numbers should match CurrentMonth sheet

✅ **Success check:** New data is visible, charts updated

---

## 🎬 TROUBLESHOOTING SCENES

### Problem: "I don't see my new data"

**Action:**
1. Wait 5 full minutes after uploading
2. Hard refresh browser (Ctrl+F5)
3. Check Render → Make sure status is "Live"
4. Check Render logs for errors
5. Try different browser
6. Check GitHub → Make sure file uploaded

### Problem: "Render deployment failed"

**Action:**
1. Go to Render → Click your service
2. Click "Logs" tab
3. Scroll to red error message
4. Common fixes:
   - If "Excel file not found": Re-upload Excel to correct folder
   - If "pandas error": Excel format might be wrong
   - If "build failed": Check requirements.txt exists

### Problem: "Excel won't upload to GitHub"

**Action:**
1. Check file name: Must be exactly `qa_dashboard_data.xlsx`
2. Check file size: Should be under 100MB
3. Check format: Must be .xlsx (not .xls or .csv)
4. Try uploading again
5. Check internet connection

### Problem: "Numbers look wrong on dashboard"

**Action:**
1. Download Excel file from GitHub
2. Open it and verify numbers
3. Check that division names match exactly
4. Verify last row of DivisionData = CurrentMonth totals
5. Look for formula errors in Excel
6. Re-save and re-upload

---

## 🎓 TIPS FOR SUCCESS

### First-Time Users

1. **Don't rush:** Take your time with each step
2. **Read messages:** Error messages tell you what's wrong
3. **Use checkboxes:** Print CHECKLIST.md and check off steps
4. **Ask for help:** It's okay to need assistance
5. **Keep files organized:** Know where your Excel file is

### Regular Users

1. **Create a routine:** Update on same day each month
2. **Double-check data:** Preview in Excel before uploading
3. **Use commit messages:** Note what you changed
4. **Keep backups:** Save copies with dates
5. **Monitor trends:** Watch for unexpected jumps in data

### Power Users

1. **Learn Git:** Use command line for faster updates
2. **Set up alerts:** Render can email you about deployments
3. **Customize colors:** Edit templates/index.html
4. **Add divisions:** Expand the Excel template
5. **Automate:** Script Excel generation if you have data sources

---

## ⏱️ TIME ESTIMATES

**First-time complete setup:** 15-20 minutes
**Second time (with practice):** 10-12 minutes
**Regular monthly updates:** 5-7 minutes
**Just uploading Excel (no editing):** 2-3 minutes

---

## 📋 BEFORE YOU START CHECKLIST

Print this and check before beginning:

- [ ] I have a GitHub account
- [ ] I have a Render account  
- [ ] I have downloaded qa-dashboard folder
- [ ] I have Excel or Google Sheets
- [ ] I have a stable internet connection
- [ ] I have 15-20 minutes of uninterrupted time
- [ ] I have read QUICK_START.md
- [ ] I'm ready to follow along step-by-step

---

## 🎉 AFTER DEPLOYMENT CHECKLIST

Celebrate your success!

- [ ] Dashboard is live and accessible
- [ ] URL is bookmarked
- [ ] Team knows the URL
- [ ] Excel template is saved
- [ ] I know how to update data
- [ ] I've tested print function
- [ ] I've set calendar reminder for next update

---

**Remember:** The first time is the hardest. After that, it's quick and easy!

If you get stuck at any point, refer to:
- QUICK_START.md (overview)
- DEPLOYMENT_INSTRUCTIONS.md (detailed guide)
- CHECKLIST.md (printable checklist)
- UPDATE_WORKFLOW.md (visual diagrams)

You've got this! 🚀

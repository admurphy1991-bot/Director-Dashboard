# 🚀 QUICK START GUIDE - Get Your Dashboard Live in 10 Minutes!

## What You're Getting

A live, professional QA dashboard that you can update anytime by editing an Excel file. No coding required!

---

## ⚡ Super Quick Deployment (Follow These Steps)

### 1️⃣ Upload to GitHub (2 minutes)

1. Go to https://github.com/new
2. Name it: `qa-dashboard`
3. Click "Create repository"
4. On the next page, click "uploading an existing file"
5. Drag ALL files from your `qa-dashboard` folder into the browser
6. Click "Commit changes"

✅ Done! Your code is on GitHub.

---

### 2️⃣ Deploy on Render (5 minutes)

1. Go to https://render.com and sign up (use your GitHub account)
2. Click "New +" → "Web Service"
3. Click "Connect" next to your `qa-dashboard` repository
4. Fill in:
   - **Name:** qa-dashboard
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click "Create Web Service"
6. Wait 3-5 minutes...

✅ Done! You'll get a URL like: `https://qa-dashboard-xxxx.onrender.com`

---

### 3️⃣ View Your Dashboard

Click your Render URL → Your dashboard is live! 🎉

---

## 📊 Update Your Data (2 minutes)

Whenever you need to update metrics:

1. Edit `qa_dashboard_data.xlsx` with your new numbers
2. Go to your GitHub repository
3. Navigate to `data` folder → Click on `qa_dashboard_data.xlsx`
4. Click trash icon to delete → Commit
5. Click "Add file" → Upload your updated Excel file → Commit
6. Wait 3-5 minutes for Render to redeploy
7. Refresh your dashboard URL

✅ New data is live!

---

## 📝 What to Update in Excel

Three sheets:

1. **MonthlyData** - Add your monthly totals (engagement, reports, issues)
2. **DivisionData** - Add monthly numbers for each division  
3. **CurrentMonth** - Update current month's detailed breakdown

**Rule:** Keep column headers and sheet names exactly as they are!

---

## 🆘 Need Help?

- Dashboard not updating? Wait 5 minutes and hard-refresh (Ctrl+F5)
- Deployment failed? Check Render logs for error messages
- Excel errors? See the "Instructions" sheet in the Excel file

**For detailed help:** See `DEPLOYMENT_INSTRUCTIONS.md`

---

## That's It!

You now have:
✅ A live dashboard URL you can share
✅ The ability to update data via Excel
✅ Automatic deployment when you update

**Bookmark your dashboard URL and you're all set!**

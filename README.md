# TechStax Assessment - Action Repository

This repository is designed to trigger GitHub webhook events for the TechStax assessment. It serves as the source repository that will send webhook notifications to our webhook receiver application.

## 🎯 Purpose

This repository is part of a GitHub webhook integration assessment. When you perform actions like:

- **Push commits** to this repository
- **Create pull requests** 
- **Merge pull requests**

These actions will automatically trigger webhook events that are captured by our webhook receiver application.

## 🚀 How to Test

### 1. Setup Webhook
Make sure you have configured a webhook in this repository's settings pointing to your webhook receiver endpoint.

### 2. Test Push Events
```bash
# Clone this repository
git clone https://github.com/sharmaasahill/action-repo.git
cd action-repo

# Make a simple change
echo "Test change $(date)" >> test-file.txt

# Commit and push
git add .
git commit -m "Test push event for webhook"
git push origin main
```

### 3. Test Pull Request Events
```bash
# Create a new branch
git checkout -b feature/test-pr

# Make changes
echo "Feature branch change $(date)" >> feature.txt
git add .
git commit -m "Add feature for PR test"

# Push branch
git push origin feature/test-pr

# Then create a Pull Request on GitHub from feature/test-pr to main
```

### 4. Test Merge Events (Brownie Points!)
- After creating the pull request above, merge it through GitHub interface
- This will trigger a merge webhook event

## 📊 Expected Webhook Events

When you perform these actions, the webhook receiver should capture:

1. **Push Event**: Shows commit author, target branch, and timestamp
2. **Pull Request Event**: Shows PR author, source/target branches, and timestamp  
3. **Merge Event**: Shows merger, source/target branches, and timestamp

## 🔍 Monitoring

You can monitor these events in real-time by visiting your webhook receiver application's web interface, which refreshes every 15 seconds.

## 📁 Repository Contents

- `README.md` - This file explaining the repository purpose
- `test-file.txt` - A simple file for testing push events
- `feature.txt` - A file for testing feature branch workflows
- `sample-code.py` - Sample Python code for demonstration
- `.github/` - GitHub workflows (if needed)

---

**Note**: This repository is created specifically for the TechStax technical assessment to demonstrate GitHub webhook integration capabilities. 
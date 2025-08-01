#!/bin/bash
echo "🚀 Auto Git Push Starting..."

REPO_DIR="/home/pi/AI-trading"
LOG_FILE="$REPO_DIR/sym/logs/git_push.log"
cd "$REPO_DIR" || { echo "❌ Failed to enter $REPO_DIR"; exit 1; }

# Set default commit message with timestamp
COMMIT_MSG="Auto push on $(date +'%Y-%m-%d %H:%M:%S')"

{
    echo "🔁 Running at $(date)"
    git add -A
    git commit -m "$COMMIT_MSG" 2>/dev/null || echo "⚠️ Nothing to commit"
    git push origin main && echo "✅ Pushed to GitHub"
    echo "-----------------------------------------"
} >> "$LOG_FILE" 2>&1

echo "📦 Push attempt logged to $LOG_FILE"

#!/bin/bash
echo "🔄 Pulling latest changes from GitHub..."
cd /home/pi/AI-trading || exit 1

# Optional: stash changes to avoid merge conflicts
git stash save "Auto-stash before pull"

# Pull latest changes from main
git pull origin main

# Optional: try to reapply changes
git stash pop || echo "ℹ️ No stashed changes to reapply."

echo "✅ Sync completed at $(date)"

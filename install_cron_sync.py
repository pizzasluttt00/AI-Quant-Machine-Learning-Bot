#!/bin/bash
echo "🛠️  Installing cron job for AI QuantBot sanity checks..."

# Define the absolute path to your sanity check runner
SANITY_SCRIPT="/home/pi/AI-trading/sym/sanity/run_sanity_checks.py"
LOG_FILE="/home/pi/AI-trading/sanity_checks/cron_sanity.log"

# Build the cron job string
CRON_JOB="*/30 * * * * python3 $SANITY_SCRIPT >> $LOG_FILE 2>&1"

# Check if the job already exists
(crontab -l 2>/dev/null | grep -F "$SANITY_SCRIPT") && {
    echo "⚠️  Cron job already installed."
} || {
    # Add the new cron job
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "✅ Cron job added successfully."
}

# Confirm by printing the new crontab
echo "📋 Current crontab:"
crontab -l

#!/bin/bash

echo "🛠️ Rebuilding social_campaign..."

cd ~/AI-trading || exit 1
rm -rf social_campaign
mkdir -p social_campaign/{apis,config,campaign,logs,templates,cron}

# ----- Config: API Keys -----
cat > social_campaign/config/api_keys.json << 'EOF'
{
  "reddit": {
    "client_id": "REPLACE_ME",
    "client_secret": "REPLACE_ME",
    "user_agent": "wishlistbot by /u/yourusername",
    "username": "yourusername",
    "password": "yourpassword"
  },
  "telegram": {
    "bot_token": "REPLACE_ME",
    "chat_id": "REPLACE_ME"
  },
  "discord": {
    "webhook_url": "REPLACE_ME"
  }
}
EOF

# ----- Template: Post Message -----
cat > social_campaign/templates/post_message.txt << 'EOF'
🎓 Help support my college essentials journey!

I've created a small Amazon Wish List of the drinks and supplies I could really use this semester. Anything helps, and I'd love the support!

👉 [Amazon Wishlist]({wishlist_url})

Thanks for taking a look 💙
EOF

# ----- Campaign Logic -----
cat > social_campaign/campaign/wishlist_poster.py << 'EOF'
import json, os
from datetime import datetime

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'api_keys.json')
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), '..', 'templates', 'post_message.txt')
LOG_PATH = os.path.join(os.path.dirname(__file__), '..', 'logs', 'post_log.txt')

WISHLIST_URL = "https://www.amazon.com/registries/gl/guest-view/1PHHWF2FK0MDM"

def load_keys():
    with open(CONFIG_PATH) as f:
        return json.load(f)

def generate_post_message():
    with open(TEMPLATE_PATH) as f:
        return f.read().replace("{wishlist_url}", WISHLIST_URL)

def main():
    creds = load_keys()
    message = generate_post_message()

    # Future: call reddit_api.post_to_subreddit(), etc.
    print("📬 Prepared message:\n")
    print(message)
    with open(LOG_PATH, "a") as log:
        log.write(f"[{datetime.now()}] Dry run: Message ready.\n")

if __name__ == "__main__":
    main()
EOF

# ----- Cron Wrapper -----
cat > social_campaign/cron/run_campaign.sh << 'EOF'
#!/bin/bash
source ~/AI-trading/venv/bin/activate
python3 ~/AI-trading/social_campaign/campaign/wishlist_poster.py
EOF
chmod +x social_campaign/cron/run_campaign.sh

# ----- README -----
cat > social_campaign/README.md << 'EOF'
# Social Campaign for Wishlist Support

This directory contains all logic, config, and automation for pushing your wishlist link to social platforms via APIs.

## Structure

- apis/       → Individual platform integrations (Reddit, Telegram, etc.)
- config/     → `api_keys.json` with all credentials in one place
- campaign/   → Main posting script: `wishlist_poster.py`
- templates/  → Message text with `{wishlist_url}` placeholder
- logs/       → Posting logs
- cron/       → Script to call via crontab

## Usage

Run once:
```bash
python3 social_campaign/campaign/wishlist_poster.py

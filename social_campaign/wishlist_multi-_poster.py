#!/usr/bin/env python3

import json
import requests
import time
import os
import praw
import discord
from discord.ext import commands

# Load credentials
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/wishlist_api_keys.json")
with open(CONFIG_PATH, "r") as f:
    keys = json.load(f)

# Shared message
wishlist_url = "https://www.amazon.com/registries/gl/guest-view/1PHHWF2FK0MDM?ref_=cm_sw_r_apann_ggr-subnav-share_JZ4F4P0TF2EZT7EEGQH1"
message = f"I'm experimenting — would anyone help get drinks from my college Amazon wish list? ?? {wishlist_url}"

### ─────────────────────────────
### 1. REDDIT POSTING
### ─────────────────────────────
def post_to_reddit():
    try:
        reddit = praw.Reddit(
            client_id=keys["reddit"]["client_id"],
            client_secret=keys["reddit"]["client_secret"],
            user_agent="wishlist-bot",
            username=keys["reddit"]["username"],
            password=keys["reddit"]["password"]
        )
        subreddit = reddit.subreddit(keys["reddit"]["subreddit"])
        subreddit.submit(title="?? Help a college student experiment with kindness", selftext=message)
        print("✅ Reddit post succeeded")
    except Exception as e:
        print(f"❌ Reddit post failed: {e}")

### ─────────────────────────────
### 2. TELEGRAM POSTING
### ─────────────────────────────
def post_to_telegram():
    try:
        bot_token = keys["telegram"]["bot_token"]
        chat_id = keys["telegram"]["chat_id"]
        telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message
        }
        response = requests.post(telegram_url, json=payload)
        if response.ok:
            print("✅ Telegram post succeeded")
        else:
            print(f"❌ Telegram post failed: {response.text}")
    except Exception as e:
        print(f"❌ Telegram error: {e}")

### ─────────────────────────────
### 3. DISCORD POSTING
### ─────────────────────────────
class DiscordPoster(commands.Bot):
    def __init__(self, channel_id, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_id = channel_id
        self.message = message

    async def on_ready(self):
        channel = self.get_channel(self.channel_id)
        if channel:
            await channel.send(self.message)
            print("✅ Discord post succeeded")
        else:
            print("❌ Discord channel not found")
        await self.close()

def post_to_discord():
    try:
        token = keys["discord"]["bot_token"]
        channel_id = int(keys["discord"]["channel_id"])
        bot = DiscordPoster(
            command_prefix="!",
            channel_id=channel_id,
            message=message,
            intents=discord.Intents.default()
        )
        bot.run(token)
    except Exception as e:
        print(f"❌ Discord error: {e}")

# Run all
if __name__ == "__main__":
    print("?? Starting multi-platform post...")
    post_to_reddit()
    time.sleep(2)
    post_to_telegram()
    time.sleep(2)
    post_to_discord()

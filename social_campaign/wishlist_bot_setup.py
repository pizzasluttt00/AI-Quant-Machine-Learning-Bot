#!/usr/bin/env python3

import os
import time
from datetime import datetime
import random

# DRY RUN MODE
dry_run = False

# Example messages (can be expanded)
messages = [
    "Help me stock up for college 🎓🍹 Check my wishlist: {url}",
    "Not asking for much... just drinks for studying 🍻🧃 {url}",
    "If you're feeling generous today... my Amazon wishlist needs love ❤️ {url}",
    "Experimental generosity: be the first to grant a stranger's college wish 🍺 {url}"
]

# Wishlist link
wishlist_url = "https://www.amazon.com/registries/gl/guest-view/1PHHWF2FK0MDM?ref_=cm_sw_r_apann_ggr-subnav-share_JZ4F4P0TF2EZT7EEGQH1"

# Simulated social platforms
platforms = ["Twitter", "Reddit", "Threads", "Bluesky", "Facebook"]
def post_to_social(platform, message):
    if dry_run:
        print(f"[DRY RUN] Would post to {platform}: {message}")
    else:
        print(f"[POSTED] {platform}: {message}")
        # Place actual API call here

def run_campaign():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"📣 Running wishlist bot at {timestamp}")

    for platform in platforms:
        msg = random.choice(messages).format(url=wishlist_url)
        post_to_social(platform, msg)
        time.sleep(1)

if __name__ == "__main__":
    run_campaign()

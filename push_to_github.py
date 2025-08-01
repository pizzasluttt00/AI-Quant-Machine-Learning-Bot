#!/bin/bash

# CONFIGURE THESE
GITHUB_USERNAME="tacosluttt00"
REPO_NAME="AI-Quant-Machine-Learning-Bot"
REMOTE_URL="https://github.com/pizzasluttt00/AI-Quant-Machine-Learning-Bot"

# Use current folder or set your project path
PROJECT_DIR="$(pwd)"

cd "$PROJECT_DIR"

# Initialize Git if not already a repo
if [ ! -d ".git" ]; then
    git init
fi

# Add GitHub remote (overwrite if needed)
git remote remove origin 2> /dev/null
git remote add origin "$REMOTE_URL"

# Add and commit all files
git add .
git commit -m "Pushing project to GitHub"

# Push to GitHub
git branch -M main
git push -u origin main

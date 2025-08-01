#!/bin/bash

echo "🔗 Creating symbolic links under ./sym..."

# Define project root (assumes script is run from ~/AI-trading or similar project root)
PROJECT_ROOT="$(pwd)"
SYM_DIR="$PROJECT_ROOT/sym"

# Create /sym if it doesn't exist
mkdir -p "$SYM_DIR"

# Map of symlink name => actual path
declare -A LINKS=(
  ["config"]="$PROJECT_ROOT/config"
  ["utils"]="$PROJECT_ROOT/utils"
  ["agents"]="$PROJECT_ROOT/agents"
  ["sanity"]="$PROJECT_ROOT/sanity_checks"
  ["templates"]="$PROJECT_ROOT/templates"
  ["logs"]="$PROJECT_ROOT/logs"
  ["ai_env"]="$PROJECT_ROOT/ai-trading-env"
)

# Loop through each and create symlink
for name in "${!LINKS[@]}"; do
  target="${LINKS[$name]}"
  link_path="$SYM_DIR/$name"

  # Remove existing link or file
  if [ -L "$link_path" ] || [ -e "$link_path" ]; then
    echo "⚠️  Removing existing: $link_path"
    rm -rf "$link_path"
  fi

  # Create symbolic link
  ln -s "$target" "$link_path"
  echo "✅ Created symlink: $link_path → $target"
done

echo "🎉 All symbolic links created in $SYM_DIR"

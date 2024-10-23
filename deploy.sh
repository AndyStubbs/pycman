#!/bin/bash

SOURCE_DIR="/home/andy/workspace/github.com/andy/pacman/"
TARGET_DIR="/mnt/c/docs/src/pacman/"

mkdir -p "$TARGET_DIR"

echo "Copying files from $SOURCE_DIR to $TARGET_DIR..."
rsync -av --delete --exclude 'venv/' --exclude '__pycache__/' --exclude '.git/' "$SOURCE_DIR" "$TARGET_DIR"

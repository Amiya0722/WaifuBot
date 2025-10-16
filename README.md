# Discord Bot with Pixiv Integration

## Overview
This is a Discord bot that provides anime/waifu image functionality using the Waifu.im API and Pixiv API integration. The bot responds to various commands for fetching and displaying images.

## Project Type
- **Language**: Python 3.12
- **Main Application**: Discord Bot (Console Application)
- **APIs Used**: Discord API, Waifu.im API, Pixiv API

## Recent Changes (October 16, 2025)
- Imported from GitHub repository
- Installed Python 3.12 and all required dependencies (discord.py, requests, python-dotenv, pixivpy3)
- Fixed type safety issues in index.py:
  - Added null check for bot.user.name
  - Added validation for TOKEN environment variable
- Fixed critical bug in pixiv_auth.py:
  - Removed trailing space from Pixiv download filename (was causing FileNotFoundError)
  - Added validation for PIXIV_REFRESH_TOKEN environment variable
- Converted Windows line endings to Unix format
- Created img/ directory for Pixiv image downloads
- Updated .gitignore to exclude img/, discord.log, and Python cache files
- Configured Discord Bot workflow to run the bot
- Set up environment secrets: TOKEN (Discord bot token) and PIXIV_REFRESH_TOKEN (Pixiv API token)

## Project Architecture
### File Structure
- `index.py`: Main Discord bot application with command handlers
- `pixiv_auth.py`: Pixiv API authentication and image fetching functionality
- `requirements.txt`: Python dependencies
- `img/`: Directory for temporary Pixiv image storage
- `discord.log`: Bot logging output

### Bot Commands
- `/hello`: Greets the user
- `/waifu [tag1] [tag2] ...`: Sends a random waifu image based on specified tags
- `/tag`: Displays available tags for the waifu command
- `/helpbot`: Displays list of available commands
- `/pixiv [search_term]`: Sends a random Pixiv illustration based on search term

## Environment Variables
The following secrets are configured in Replit Secrets:
- `TOKEN`: Discord bot token (required)
- `PIXIV_REFRESH_TOKEN`: Pixiv refresh token for API access (required)

## Workflow Configuration
- **Workflow Name**: Discord Bot
- **Command**: `python3 index.py`
- **Output Type**: Console
- **Status**: Running

## Dependencies
- discord.py: Discord API wrapper
- requests: HTTP library for API calls
- python-dotenv: Environment variable management
- pixivpy3: Pixiv API wrapper

## Notes
- Bot uses @ as command prefix
- Images from Pixiv are temporarily downloaded to img/ directory and deleted after sending
- Bot includes content moderation (filters certain words)
- Logging is configured to write to discord.log file

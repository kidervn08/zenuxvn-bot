# ZenuxVN Bot

## Overview
The ZenuxVN Bot is a Telegram bot designed to enhance user engagement and automate various tasks within the Telegram platform.

## Features
- Automated responses to user queries
- Customizable commands for user interaction
- Integration with external APIs for extended functionality
- Support for multiple languages
- Rich media support (images, videos, files)

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/kidervn08/zenuxvn-bot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd zenuxvn-bot
   ```
3. Install the required dependencies:
   ```bash
   npm install
   ```
4. Set up the environment variables:
   - Create a `.env` file in the root directory and add your configurations.

## Commands
- `/start` - Initiates interaction with the bot.
- `/help` - Provides a list of available commands.
- `/settings` - Allows users to adjust their preferences.
- `/info` - Retrieves information about the bot and its capabilities.

## Project Structure
```
zenuxvn-bot/
├── src/
│   ├── commands/       # Contains command handlers
│   ├── config/         # Configuration files
│   ├── models/         # Database models
│   └── services/       # External API services
├── tests/              # Unit and integration tests
├── .env                # Environment configuration
├── package.json        # Node.js dependencies
└── README.md           # Project documentation
```

## Configuration
- **TELEGRAM_TOKEN**: Your bot's API token from BotFather.
- **DATABASE_URL**: Connection string to your database.
- **LANGUAGE**: Default language for the bot responses.

## Database Schema
- **users**  
  - `id` (Primary Key)  
  - `username`  
  - `language`  

- **commands**  
  - `id` (Primary Key)  
  - `command_name`  
  - `description`  

## Support Information
For any issues or feature requests, please open an issue in the repository or contact the maintainer directly.  
You can also contribute by submitting pull requests with improvements or new features.
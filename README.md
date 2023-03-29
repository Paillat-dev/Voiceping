# Voiceping
This bot allows you to ping all users connected to a voice channel in your Discord server. It provides the following features:
- Automatically adds roles to members when they join a voice channel and removes them when they leave.
- Allows you to ping all members connected to a specific voice channel with a single command.

## Installation
There are two options to add this bot to your Discord server:

### Option 1: Adding the bot directly
You can add the bot to your Discord server by clicking on the following link:

https://discord.com/api/oauth2/authorize?client_id=1090325955484070068&permissions=277831830592&scope=bot

**Make sure to grant the bot permissions to view voice channels in your server.**

### Option 2: Self-hosting
1. Clone this repository to your local machine.

2. Install the required dependencies by running pip install -r requirements.txt.

3. Create a .env file with your Discord bot token:
```
TOKEN=your_discord_bot_token
```
4. Run the main.py file with python main.py command.

## Usage
```css
@voice_channel_name
```
**Note:** The bot requires permissions to view the voice channels in your server. If you don't want it to work in a specific channel, simply remove the "View Channel" permission for the bot in that channel.
from os import environ
class Config(object):
    API_ID = int(environ.get("API_ID", '7767744')) 
    API_HASH = environ.get("API_HASH", '7e5504b4fcaa6ad4515b52a66c09ceb1')
    BOT_TOKEN = environ.get("BOT_TOKEN", "1948692090:AAFwNBZnXEnywIvSOyNJQQ6QbANPl5PDcQA")
    STRING_SESSION = environ.get("STRING", "AQBxFKvq73hcY5z2SmnLpyLq3CP2RmFoqOrxKjwBtq4VxeJwdtuJ5hhZECwi3zJBeTRfrxdEwgfJUZVYul0DvNYAlmp9ZD7vD94WkHlR57gX6KXbJ06EfeEEC3OiB7k6jRcEHz2Zdw5JOx0hQV6VjVLVnv1S0qgOvuvz8wnsHwEToWzVoaFUbJvksPrl21R2EXDUcj4-jEWHmRkwq3lKEm3o7fpvixcNqMvlWt3JovECcLm9c6BE5S4BhjPx89NOyt0DQpSJli8V94e8qQsM6Ko8infCM7OXIcRpewDM-ZaCSTG9YpFAKTTTG5MMU3baTWEy-7q8hKb_MiqykzIwGTZ3aY7eSgA")
    SUDO_USERS = int(environ.get("SUDO_USERS", '1770970698')) 
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """

from twitchio.ext import commands
from commands.score import Score
from commands.misc import MiscCommands
import yaml
from typing import Dict

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

CONFIG_FILE_PATH = "config.yaml"


class BotConfig:
    def __init__(self, config_path: str):
        self.data = {}
        # Open the config file and parse the yaml contents
        try:
            with open(config_path) as config_file:
                try:
                    self.data = yaml.load(config_file, Loader=Loader)
                except Exception as E:
                    print(f"Error: Failed to parse config file {config_path}")
                    print(E)
        except Exception:
            print(f"Can't find config at {config_path}, using default values instead.")


# Define the bot
class Bot(commands.Bot):
    def __init__(self, config: Dict):
        token: str = config.get("token", "YOUR_TOKEN_HERE")
        channels: str = config.get("channels", ["YOUR_CHANNEL_NAME"])
        # Define the users who are NOT allowed to send commands
        self.banned_users = config.get("banned_users", ["YOUR_CHANNEL_NAME"])
        super().__init__(
            token=token,
            prefix=["!", "?"],
            initial_channels=channels,
        )
        self.process = None

    async def event_ready(self):
        # Notify when we are logged in and ready to use commands
        print(f"Logged in | {self.nick} | {self.user_id}")

    @commands.command(aliases=("commandos", "commands"))
    async def bot_commands(self, ctx: commands.Context):
        commands = [
            "commands",
            "score",
            "explain_score",
            "boktai",
            "discord",
            "solutions",
            "leaderboard",
            "website",
            "pizza",
            "splits",
        ]
        await ctx.send(", ".join(commands))

    @commands.command()
    async def banned(self, ctx: commands.Context):
        if ctx.prefix == "?":
            await ctx.send(self.banned_users)
        elif ctx.author.name in self.banned_users:
            await ctx.send("yes")
        else:
            await ctx.send("nope")


# Main entry point of script
if __name__ == "__main__":
    conf = BotConfig(CONFIG_FILE_PATH)
    bot = Bot(conf.data)

    bot.add_cog(MiscCommands(bot))
    bot.add_cog(Score(bot))

    bot.run()

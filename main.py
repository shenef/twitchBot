from twitchio.ext import commands

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
            print(f"Didn't find config file {config_path}, using default values.")


# Define the bot
class Bot(commands.Bot):
    def __init__(self, config: Dict):
        token: str = config.get("token", "YOUR_TOKEN_HERE")
        channels: str = config.get("channels", ["YOUR_CHANNEL_NAME"])
        # Define the users who are NOT allowed to send commands
        self.blocked_users = config.get("blocked_users", ["YOUR_CHANNEL_NAME"])
        super().__init__(token=token, prefix="!", initial_channels=channels)
        self.process = None

    async def event_ready(self):
        # Notify when we are logged in and ready to use commands
        print(f"Logged in as {self.nick}")
        print(f"User id is {self.user_id}")

    @commands.command()
    async def boktai(self, ctx: commands.Context):
        await ctx.send("")

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("My Discord: https://discord.gg/ebmfGDP")
        await ctx.send("TaiyohNetwork: https://discord.gg/hdJsvEJP3p")

    @commands.command()
    async def solutions(self, ctx: commands.Context):
        await ctx.send("7 9 10 1 3 5 8, = + /, 53, 254")

    @commands.command()
    async def leaderboard(self, ctx: commands.Context):
        await ctx.send("https://speedrun.com/tsiiyh")

    @commands.command()
    async def website(self, ctx: commands.Context):
        await ctx.send(
            "Collection of information about Boktai mechanics: https://boktai.shenef.one"
        )
        await ctx.send("WIP update: https://beta.shenef.one")

    @commands.command()
    async def pizza(self, ctx: commands.Context):
        await ctx.send("Calculate and compare price/cm²: https://pizza.shenef.one")

    @commands.command()
    async def splits(self, ctx: commands.Context):
        await ctx.send(
            "Create split files from plain text: https://splitify.shenef.one"
        )

    @commands.command(aliases=("commandos", "commands"))
    async def options(self, ctx: commands.Context):
        commands = [
            "commands",
            "boktai",
            "discord",
            "solutions",
            "leaderboard",
            "website",
            "pizza",
            "splits",
        ]
        await ctx.send(", ".join(commands))

    # Define some command
    # @commands.command()
    # async def something(self, ctx: commands.Context):
    #     if ctx.author.name not in self.banned_users:
    #         await ctx.send("yes")
    #     else:
    #         await ctx.send("nope")


# Main entry point of script
if __name__ == "__main__":
    conf = BotConfig(CONFIG_FILE_PATH)

    bot = Bot(conf.data)
    bot.run()

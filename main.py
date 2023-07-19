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
            print(f"Can't find config at {config_path}, using default values instead.")


# Define the bot
class Bot(commands.Bot):
    def __init__(self, config: Dict):
        token: str = config.get("token", "YOUR_TOKEN_HERE")
        channels: str = config.get("channels", ["YOUR_CHANNEL_NAME"])
        # Define the users who are NOT allowed to send commands
        self.banned_users = config.get("banned_users", ["YOUR_CHANNEL_NAME"])
        super().__init__(token=token, prefix="!", initial_channels=channels)
        self.process = None

    async def event_ready(self):
        # Notify when we are logged in and ready to use commands
        print(f"Logged in | {self.nick} | {self.user_id}")

    @commands.command()
    async def boktai(self, ctx: commands.Context):
        await ctx.send(
            "Boktai: The Sun is in Your Hand is an action-adventure RPG where you play "
            + "as Django, a vampire hunter who uses a solar-powered gun to fight "
            + "against the forces of darkness. The game's unique light sensor tracks "
            + "the amount of sunlight in your environment, which affects the gameplay."
        )

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send("My Discord: https://discord.gg/ebmfGDP")
        await ctx.send("Taiyoh Network: https://discord.gg/hdJsvEJP3p")

    @commands.command()
    async def solutions(self, ctx: commands.Context):
        await ctx.send("7 9 10 1 3 5 8, 4x straight, 2x left, = + /, 53, 254")

    @commands.command()
    async def leaderboard(self, ctx: commands.Context):
        await ctx.send("Boktai 1 Leaderboard: https://speedrun.com/tsiiyh")

    @commands.command()
    async def website(self, ctx: commands.Context):
        await ctx.send(
            "Collection of information about Boktai mechanics: https://boktai.shenef.one"
        )
        await ctx.send("WIP update: https://beta.shenef.one/boktai1")

    @commands.command()
    async def pizza(self, ctx: commands.Context):
        await ctx.send("Calculate and compare price/cm²: https://pizza.shenef.one")

    @commands.command()
    async def splits(self, ctx: commands.Context):
        await ctx.send(
            "Generate split files from plain text: https://splitify.shenef.one"
        )

    @commands.command()
    async def score(
        self,
        ctx: commands.Context,
        dungeon_name: str,
        time: int,
        found: int,
        continues: int,
        charged: int,
    ):
        base_scores = {
            "Crumbling Mine": 45,
            "Deserted Arsenal": 50,
            "Gate of the Dead": 50,
            "Ruined Cemetery": 50,
            "Stench Forest": 50,
            "Noname Fortress": 55,
            "Small Cave": 70,
            "Death Cliff": 80,
            "Forgotten Tomb": 90,
            "Suffering House": 90,
            "Fire Dragon's Grave": 100,
            "Remaining Tower": 105,
            "Ancient Forest": 120,
            "Catacomb": 120,
            "Scar of the Land": 120,
            "Water Demon's Cage": 125,
            "Stairs of Trial": 130,
            "Valley of Ice": 130,
            "Abyss": 135,
            "Delusion Forest": 180,
            "Fallen Devil Castle": 190,
            "House of Darkness": 210,
            "Permafrost": 600,
            "Fog Castle": 720,
            "Bloodrust Mansion": 1200,
            "Sol City": 1200,
            "Firetop Mountain": 1500,
        }

        base_score = base_scores[dungeon_name]
        score = 1000 + base_score - time
        if score > 1000:
            score = 1000

        dungeon_score = score - (found * 30) - (continues * 100) + (charged * 10)

        def get_dungeon_rank(dungeon_score):
            if dungeon_score < 100:
                dungeon_rank = "C-"
            elif dungeon_score < 300:
                dungeon_rank = "C"
            elif dungeon_score < 500:
                dungeon_rank = "C+"
            elif dungeon_score < 600:
                dungeon_rank = "B-"
            elif dungeon_score < 700:
                dungeon_rank = "B"
            elif dungeon_score < 800:
                dungeon_rank = "B+"
            elif dungeon_score < 900:
                dungeon_rank = "A-"
            elif dungeon_score < 950:
                dungeon_rank = "A"
            elif dungeon_score < 1000:
                dungeon_rank = "A+"
            else:
                dungeon_rank = "S"
            return dungeon_rank

        dungeon_rank = get_dungeon_rank(dungeon_score)

        await ctx.send(f"Score: {dungeon_score} | Rank: {dungeon_rank}")

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

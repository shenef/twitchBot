from twitchio.ext import commands


class MiscCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def boktai(self, ctx: commands.Context):
        await ctx.send(
            "Boktai is a series of portable action RPGs by Konami and Hideo Kojima. "
            + "The games feature a solar sensor that affects gameplay. The protagonist,"
            + " Django, is a vampire hunter who uses a solar-powered gun to fight "
            + "the undead."
        )

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(
            "My Discord: https://discord.gg/ebmfGDP | "
            + "Taiyoh Network: https://discord.gg/hdJsvEJP3p"
        )

    @commands.command()
    async def solutions(self, ctx: commands.Context):
        await ctx.send("7 9 10 1 3 5 8, 4x straight, 2x left, = + /, 53, 254")

    @commands.command()
    async def leaderboard(self, ctx: commands.Context):
        await ctx.send("Boktai 1 Leaderboard: https://speedrun.com/tsiiyh")

    @commands.command()
    async def website(self, ctx: commands.Context):
        await ctx.send(
            "Collection of information about Boktai mechanics: "
            + "https://boktai.shenef.one | WIP update: https://beta.shenef.one/boktai1"
        )

    @commands.command()
    async def pizza(self, ctx: commands.Context):
        await ctx.send("Calculate and compare price/cm²: https://pizza.shenef.one")

    @commands.command()
    async def splits(self, ctx: commands.Context):
        await ctx.send(
            "Generate split files from plain text: https://splitify.shenef.one"
        )

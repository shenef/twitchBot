from twitchio.ext import commands


class Score(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def explain_score(self, ctx: commands.Context):
        await ctx.send('Example: !score "Water Demon\'s Cage" 330 4 0 11')
        await ctx.send("Format: DungeonName TimeInSeconds Found Continues Charged")
        await ctx.send(
            "The dungeon name only needs quotes when there is a space in "
            + "between. The dungeon name must be exactly as in Game "
            + "(case, special characters, spaces). All arguments must be present."
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

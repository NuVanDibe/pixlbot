import random

from discord.ext import commands


class DiceRoll(commands.Cog):

    def __init__(self, bot):
        self.bot = bot  # why

    @commands.command()
    async def roll(self, ctx, *args):
        st = ''.join(args)
        total = 'Rolling ' + st + ": **"
        mod = 0
        if st.find('+', 0, -1) != -1:
            mod = int(st.split('+')[1])
            st = st.split('+')[0]
        if st.find('d', 0, -1) != -1:
            rolls = int(st.split('d')[0])
            die = range(1, int(st.split('d')[1]) + 1)
            dice = random.choices(die, k=rolls)
            total = total + str(sum(dice) + mod) + "** "
            if dice.__len__() > 1:
                total = total + str(dice)
            if mod > 0:
                total = total + " + " + str(mod)
        else:
            total = st + " and also maybe specify some dice next time"
        await ctx.send(total)


def setup(bot):
    bot.add_cog(DiceRoll(bot))

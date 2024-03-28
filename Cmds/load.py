from discord.ext import commands
import discord
from discord.ext.commands.core import command
from Core.classes import Bot_Cog

class Load(Bot_Cog):
    @commands.command()    #載入
    async def load(self,ctx,extension)-> None:
        self.bot.load_extension(f'Cmds.{extension}')
        await ctx.send(f'Loaded {extension} done.')
    
    @commands.command()    #重新載入
    async def reload(self,ctx,extension)-> None:
        self.bot.reload_extension(f'Cmds.{extension}')
        await ctx.send(f'Reloaded {extension} done.')
    @commands.command()    #卸載
    async def unload(self,ctx,extension)-> None:
        self.bot.unload_extension(f'Cmds.{extension}')
        await ctx.send(f'Unloaded {extension} done.')
async def setup(bot):
    await bot.add_cog(Load(bot))
import discord
from discord.ext import commands

class test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def test(self, ctx):

		embed=discord.Embed(color=discord.Colour(0xb3d4fc))
		embed.set_image(url="https://media.discordapp.net/attachments/715525927496581192/756609499959394394/IMG_20200916_223012_893.jpg")
		await ctx.send(embed=embed)

def setup(bot):
	c = test(bot) 
	bot.add_cog(c)
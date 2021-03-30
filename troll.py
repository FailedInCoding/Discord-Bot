import discord
from discord.ext import commands

class troll(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def secret(self, ctx):

		embed=discord.Embed(color=discord.Colour(0xb3d4fc))
		embed.set_image(url="<div class="tenor-gif-embed" data-postid="17299838" data-share-method="host" data-width="100%" data-aspect-ratio="2.1842105263157894"><a href="https://tenor.com/view/spinning-gorilla-animal-gorilla-spinning-gif-17299838">Spinning Gorilla GIF</a> from <a href="https://tenor.com/search/spinning-gifs">Spinning GIFs</a></div><script type="text/javascript" async src="https://tenor.com/embed.js"></script>")
		await ctx.send(embed=embed)

def setup(bot):
	c = troll(bot) 
	bot.add_cog(c)
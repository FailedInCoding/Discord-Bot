from ducky import DuckyClient
import asyncio

if __name__ == '__main__':
	TOKEN = 'NzU1MDg5NzI2MjA5MzkyNzIx.X1-OGw.IJM9wlYBWgRXo-SBxL9-lmyMfFQ'
	PREFIXES = ['!']
	COGS = ['general', 'troll', 'test']      # Default cogs o_O on startup
	bot = DuckyClient(default_prefixes = PREFIXES, default_cogs = COGS)


	loop = asyncio.get_event_loop()
	loop.run_until_complete(bot.launch(TOKEN))
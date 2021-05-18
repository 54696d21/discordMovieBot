import discord
import rottentomatoesHelper
from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists


class MovieBot(discord.Client):
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith("!movie"):

            reqMovie = str(message.content).strip("!movie").lstrip()
            print(f"requested movie was '{reqMovie}'")
            retMovie = rottentomatoesHelper.evalMovie(reqMovie)
            await message.channel.send(retMovie)


client = MovieBot()
client.run(env("BOT_TOKEN"))

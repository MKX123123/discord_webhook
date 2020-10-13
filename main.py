from discord_webhook import DiscordWebhook, DiscordEmbed
import os


from dotenv import load_dotenv
load_dotenv()
webhook_urls = os.getenv('webhook')


webhook = DiscordWebhook(url=webhook_urls)

embed = DiscordEmbed(title='Embed Title', description='Your Embed Description', color=242424)
embed.set_author(name='Author Name', url='https://github.com/HazemMeqdad')
embed.set_footer(text='Embed Footer Text')
embed.set_timestamp()
embed.add_embed_field(name='Field 1', value='Lorem ipsum')
embed.add_embed_field(name='Field 2', value='dolor sit')
embed.add_embed_field(name='Field 3', value='amet consetetur')
embed.add_embed_field(name='Field 4', value='sadipscing elitr')


webhook.add_embed(embed)

response = webhook.execute()

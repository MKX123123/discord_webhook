from discord_webhook import DiscordWebhook
import os
data = '''```yor masseg`'''

webhook_urls = ''

from dotenv import load_dotenv
load_dotenv()
webhook_urls = os.getenv('webhook')


webhook = DiscordWebhook(url=webhook_urls, content=data)

response = webhook.execute()

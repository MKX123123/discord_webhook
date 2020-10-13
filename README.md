# discord webhook
execute discord webhooks

## Installation
Use the package manager [pip](https://pypi.org/project/discord-webhook/) to install discord webhook.

```bash
pip install discord-webhook
```

## Usage
```python
from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='your webhook url', content='Webhook Message')
response = webhook.execute()
```
or

### Pre-Setup

![Left panel](https://media.discordapp.net/attachments/741732875262623748/765623751554891786/unknown.png)

![Left panel](https://media.discordapp.net/attachments/741732875262623748/765624777733439538/unknown.png?width=960&height=386)

![Left panel](https://cdn.discordapp.com/attachments/741732875262623748/765625695527108668/unknown.png)

### Setup

Create a file named `.env`

Add `webhook=<your link webhook>`

Your .env file should look something like this:

```
webhook=<your link webhook>
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Through
By: !  HåźěmMěqďađᵒᵗ#0090



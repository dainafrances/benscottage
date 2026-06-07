# Ben's Cottage Bot

## Discord setup: let Ben see the whole channel

Ben can only remember messages Discord actually delivers to him. To receive ordinary
channel messages—not only direct mentions and `@everyone` messages—the bot application
must have the privileged **Message Content Intent** enabled:

1. Open the Discord Developer Portal and select Ben's application.
2. Open **Bot** in the left sidebar.
3. Under **Privileged Gateway Intents**, enable **Message Content Intent**.
4. Save the change, then restart/redeploy Ben.

Ben's Discord role also needs **View Channel** and **Read Message History** in every
channel he should observe. The code requests the Message Content Intent and stores
unaddressed human and companion-bot messages as context, but it stays silent unless its
normal response-routing rules accept the message.

## Bot-to-bot exchange safety

A companion bot may trigger Ben by directly mentioning him or replying to one of his
messages. Ben replies directly to that companion once, then will not answer that same
bot again until a human addresses Ben. The per-channel time cooldown remains as an
additional anti-loop safety layer.

Ben may independently invite Colin by emitting the private control tag
`[PING: Colin]`; he does not need a human to instruct him first. The send layer replaces
that tag with Colin's real numeric Discord mention. `@Colin#2237` is only a username
label, not the wire format Discord requires for a live ping.

Set `COLIN_DISCORD_USER_ID` to Colin's numeric Discord user ID for reliable pings after
every restart. Ben also learns the ID when he observes Colin/Moose, but the environment
value removes that timing dependency. Only that known companion ID is permitted;
human, role, `@everyone`, and `@here` pings remain blocked. The existing one-exchange
latch prevents the ping from becoming an endless bot conversation.

This repository controls Ben only. Colin needs the same Message Content Intent and
equivalent observe/respond routing in his own bot deployment for the behavior to work
in both directions.

## Environment variables

- `DISCORD_RESPONSE_CHAR_LIMIT` (default: `2000`): legacy single-message limit setting. Long AI replies are currently sent as ordered chunks of at most 1800 characters.
- `BOT_REPLY_COOLDOWN_SECONDS` (default: `12`): cooldown in seconds for **bot-origin triggers per channel** after Ben sends a bot-origin reply.
- `COLIN_DISCORD_USER_ID`: Colin/Moose's numeric Discord user ID, used to render Ben's `[PING: Colin]` control tag as a real mention.
- `DEDUPLICATION_WINDOW_SECONDS` (default: `300`): message-ID dedupe window.
- `DUPLICATE_CONTENT_WINDOW_SECONDS` (default: `20`): content-signature dedupe window.
- `DEDUPE_LOGGING_ENABLED` (default: `true`): enables lightweight dedupe/cooldown debug logging.

Copy `.env.example` into your deployment environment and set values as needed.

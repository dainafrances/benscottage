# Ben's Cottage Bot

## Environment variables

- `DISCORD_RESPONSE_CHAR_LIMIT` (default: `2000`): maximum size of a single Discord reply before Ben truncates with an ellipsis.
- `BOT_REPLY_COOLDOWN_SECONDS` (default: `12`): cooldown in seconds for **bot-origin triggers per channel**. After Ben sends a bot-origin reply in a channel, new bot-origin triggers in that same channel are ignored until this cooldown expires.
- `DEDUPLICATION_WINDOW_SECONDS` (default: `300`): message-ID dedupe window.
- `DUPLICATE_CONTENT_WINDOW_SECONDS` (default: `20`): content-signature dedupe window.
- `DEDUPE_LOGGING_ENABLED` (default: `true`): enables lightweight dedupe/cooldown debug logging.

Copy `.env.example` into your deployment environment and set values as needed.

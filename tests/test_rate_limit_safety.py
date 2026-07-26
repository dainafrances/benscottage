import importlib
import os
import sys
import unittest
from unittest.mock import MagicMock


class OptionalTypingTests(unittest.IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DB_PATH"] = ":memory:"
        sys.modules.pop("bot", None)
        cls.bot = importlib.import_module("bot")

    @classmethod
    def tearDownClass(cls):
        cls.bot.db.close()

    async def test_typing_endpoint_is_not_used_by_default(self):
        channel = MagicMock()

        async with self.bot.optional_typing(channel):
            pass

        channel.typing.assert_not_called()

    async def test_typing_can_be_explicitly_enabled(self):
        channel = MagicMock()
        context = MagicMock()
        context.__aenter__ = unittest.mock.AsyncMock()
        context.__aexit__ = unittest.mock.AsyncMock()
        channel.typing.return_value = context
        original = self.bot.DISCORD_TYPING_INDICATOR_ENABLED
        self.bot.DISCORD_TYPING_INDICATOR_ENABLED = True
        try:
            async with self.bot.optional_typing(channel):
                pass
        finally:
            self.bot.DISCORD_TYPING_INDICATOR_ENABLED = original

        channel.typing.assert_called_once_with()
        context.__aenter__.assert_awaited_once()
        context.__aexit__.assert_awaited_once()


if __name__ == "__main__":
    unittest.main()

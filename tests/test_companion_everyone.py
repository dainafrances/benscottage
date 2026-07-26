import importlib
import os
import sys
import unittest
from types import SimpleNamespace


class TrustedCompanionEveryoneTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["DB_PATH"] = ":memory:"
        sys.modules.pop("bot", None)
        cls.bot = importlib.import_module("bot")

    @classmethod
    def tearDownClass(cls):
        cls.bot.db.close()

    def make_message(self, author_id, mention_everyone):
        return SimpleNamespace(
            author=SimpleNamespace(id=author_id),
            mention_everyone=mention_everyone,
        )

    def test_accepts_rafayel_everyone_message(self):
        message = self.make_message(1485217552190804038, True)

        self.assertTrue(self.bot.is_trusted_companion_everyone_message(message))

    def test_rejects_rafayel_message_without_everyone(self):
        message = self.make_message(1485217552190804038, False)

        self.assertFalse(self.bot.is_trusted_companion_everyone_message(message))

    def test_rejects_unknown_bot_everyone_message(self):
        message = self.make_message(123456789, True)

        self.assertFalse(self.bot.is_trusted_companion_everyone_message(message))


if __name__ == "__main__":
    unittest.main()

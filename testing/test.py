# Automated testing
# Tests for InputParser and Save modules

import unittest
import sys
import os
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from modules.parser.InputParser import parse_game
from modules.save import Save
from modules.Backlog import Backlog
from structs.VideoGame import VideoGame

class TestParser(unittest.TestCase):

    def test_parse_all_fields(self):
        game = parse_game("Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD")
        self.assertEqual(game.get_title(), "Minecraft")
        self.assertEqual(game.get_time_spent(), 3000.0)
        self.assertEqual(game.get_priority(), 1)
        self.assertEqual(game.get_status_text(), "STARTED")
        self.assertEqual(game.get_tags_text(), ["ADVENTURE", "OPENWORLD"])

    def test_parse_no_tags(self):
        game = parse_game("Cyberpunk, 100.5, 2, INTERESTED")
        self.assertEqual(game.get_title(), "Cyberpunk")
        self.assertEqual(game.get_tags_text(), [])

    def test_parse_wrong_tags(self):
        game = parse_game("TestGame, -5.0, 1, INTERESTED, WRONGTAG")
        self.assertEqual(game.get_tags(), [])


if __name__ == '__main__':
    unittest.main()

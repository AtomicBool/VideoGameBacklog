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


class TestInputParser(unittest.TestCase):

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

    def test_parse_invalid_status_falls_back_to_interested(self):
        game = parse_game("TestGame, 0.0, 1, BADSTATUS")
        self.assertEqual(game.get_status_text(), "INTERESTED")

    def test_parse_negative_time_falls_back_to_zero(self):
        game = parse_game("TestGame, -5.0, 1, STARTED")
        self.assertEqual(game.get_time_spent(), 0.0)

    def test_parse_single_tag(self):
        game = parse_game("Balatro, 50.0, 3, FINISHED, ARCADE")
        self.assertEqual(game.get_tags_text(), ["ARCADE"])


class TestSave(unittest.TestCase):

    def setUp(self):
        tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        tmp.close()
        self.save_path = tmp.name

    def tearDown(self):
        if os.path.exists(self.save_path):
            os.remove(self.save_path)

    def test_save_and_load_roundtrip(self):
        games = [
            VideoGame("Minecraft", 3000.0, 1, "STARTED", ["ADVENTURE", "OPENWORLD"]),
            VideoGame("Balatro", 50.0, 2, "INTERESTED", ["ARCADE"]),
        ]
        Save.save(games, self.save_path)
        loaded = Save.load(self.save_path)

        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].get_title(), "Minecraft")
        self.assertEqual(loaded[0].get_time_spent(), 3000.0)
        self.assertEqual(loaded[0].get_priority(), 1)
        self.assertEqual(loaded[0].get_status_text(), "STARTED")
        self.assertEqual(loaded[0].get_tags_text(), ["ADVENTURE", "OPENWORLD"])
        self.assertEqual(loaded[1].get_title(), "Balatro")
        self.assertEqual(loaded[1].get_status_text(), "INTERESTED")

    def test_load_nonexistent_file_returns_empty_list(self):
        result = Save.load("/nonexistent/path/backlog.json")
        self.assertEqual(result, [])

    def test_save_empty_list_loads_empty_list(self):
        Save.save([], self.save_path)
        loaded = Save.load(self.save_path)
        self.assertEqual(loaded, [])

    def test_save_load_into_backlog(self):
        games = [
            VideoGame("Minecraft", 3000.0, 1, "STARTED", ["OPENWORLD"]),
            VideoGame("Dead Cells", 200.0, 2, "FINISHED", ["ROGUELIKE", "COMBAT"]),
        ]
        Save.save(games, self.save_path)

        backlog = Backlog()
        backlog.load_games(Save.load(self.save_path))

        self.assertEqual(len(backlog.get_list()), 2)
        self.assertEqual(backlog.get_list()[0].get_title(), "Minecraft")
        self.assertEqual(backlog.get_list()[1].get_title(), "Dead Cells")
        self.assertEqual(backlog.get_list()[1].get_tags_text(), ["ROGUELIKE", "COMBAT"])

    def test_parser_then_save_then_load_into_backlog(self):
        raw_inputs = [
            "Minecraft, 3000.0, 1, STARTED, ADVENTURE, OPENWORLD",
            "Balatro, 50.0, 2, INTERESTED, ARCADE",
            "CS2, 500.0, 3, FINISHED, COMBAT",
        ]
        games = [parse_game(r) for r in raw_inputs]

        Save.save(games, self.save_path)

        backlog = Backlog()
        backlog.load_games(Save.load(self.save_path))

        self.assertEqual(len(backlog.get_list()), 3)
        self.assertEqual(backlog.get_list()[0].get_title(), "Minecraft")
        self.assertEqual(backlog.get_list()[1].get_title(), "Balatro")
        self.assertEqual(backlog.get_list()[2].get_title(), "CS2")
        self.assertEqual(backlog.get_list()[2].get_status_text(), "FINISHED")


if __name__ == '__main__':
    unittest.main()

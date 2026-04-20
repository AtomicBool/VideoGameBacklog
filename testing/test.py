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

class TestSave(unittest.TestCase):

    def setUp(self):
        tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        tmp.close()
        self.save_path = tmp.name

    def tearDown(self):
        if os.path.exists(self.save_path):
            os.remove(self.save_path)

    def test_save_load(self):
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

    def test_parser_save(self):
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

class TestBacklog(unittest.TestCase):

    def test_add_new_game(self):
        backlog = Backlog()
        backlog.add_game(VideoGame("Minecraft", 10.0, 1, "STARTED", []))
        self.assertEqual(len(backlog.get_list()), 1)
        self.assertEqual(backlog.get_list()[0].get_title(), "Minecraft")

    def test_add_game_updates_duplicate_title(self):
        backlog = Backlog()
        backlog.add_game(VideoGame("Minecraft", 10.0, 1, "STARTED", []))
        backlog.add_game(VideoGame("Minecraft", 500.0, 1, "FINISHED", []))
        self.assertEqual(len(backlog.get_list()), 1)
        self.assertEqual(backlog.get_list()[0].get_status_text(), "FINISHED")

    def test_remove_existing_game(self):
        backlog = Backlog()
        backlog.add_game(VideoGame("Minecraft", 10.0, 1, "STARTED", []))
        backlog.remove_game("Minecraft")
        self.assertEqual(len(backlog.get_list()), 0)

    def test_remove_nonexistent_game_no_crash(self):
        backlog = Backlog()
        backlog.add_game(VideoGame("Minecraft", 10.0, 1, "STARTED", []))
        backlog.remove_game("DoesNotExist")
        self.assertEqual(len(backlog.get_list()), 1)


if __name__ == '__main__':
    unittest.main()

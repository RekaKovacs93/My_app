import unittest
from models.game import Game

class TestGame(unittest.TestCase):
    
    def setUp(self):
        self.game = Game("Reka", "computer", "Reka")
    
    
    def test_game_has_winner(self):
        self.assertEqual("computer", self.game.winner)
        
        
    # def test_task_has_assignee(self):
    #     self.assertEqual("Ada Lovelace", self.task.assignee)
       
        
    # def test_task_has_duration(self):
    #     self.assertEqual(60, self.task.duration)
    
    
    # def test_task_completed_starts_false(self):
    #     self.assertEqual(False, self.task.completed)
        
    
    # def test_can_mark_test_complete(self):
    #     self.task.mark_complete()
    #     self.assertEqual(True, self.task.completed)
    
    
   
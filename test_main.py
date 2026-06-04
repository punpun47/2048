import unittest
import main

class TestSlideLeft(unittest.TestCase):
    def test_normal_case(self):
        test_board = [
            [8,4,0,2],
            [4,0,0,0],
            [2,0,2,4],
            [16,8,4,4]
        ]
        expected_outcome = [
            [8,4,2,0],
            [4,0,0,0],
            [4,4,0,0],
            [16,8,8,0]
        ]
        main.slide_left(test_board)
        self.assertEqual(test_board, expected_outcome)
        
class TestSlideUp(unittest.TestCase):
    def test_normal_case(self):
        test_board = [
            [8,4,0,2],
            [4,0,0,0],
            [2,0,2,4],
            [16,8,4,4]
        ]
        expected_outcome = [
            [8,4,2,2],
            [4,8,4,8],
            [2,0,0,0],
            [16,0,0,0]
        ]
        main.slide_up(test_board)
        self.assertEqual(test_board, expected_outcome)



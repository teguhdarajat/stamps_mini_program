import unittest
from mini_program import MiniProgram

class TestMiniProgram(unittest.TestCase):
        
    def test_is_prime(self):
        mini_program = MiniProgram(100)
        self.assertTrue(mini_program.is_prime(7))
        self.assertTrue(mini_program.is_prime(13))
        self.assertTrue(mini_program.is_prime(89))
    
    def test_is_prime_with_non_prime_number(self):
        mini_program = MiniProgram(100)
        self.assertFalse(mini_program.is_prime(100))
        self.assertFalse(mini_program.is_prime(21))
        self.assertFalse(mini_program.is_prime(15))
        
    def test_is_prime_with_edge_cases(self):
        mini_program = MiniProgram(100)
        self.assertFalse(mini_program.is_prime(1))
        self.assertFalse(mini_program.is_prime(0))
        self.assertTrue(mini_program.is_prime(2))
        
    def test_get_numbers(self):
        expected_result = ['Bar', 'Foo', 8, 'Foo', 4, 1]
        mini_program = MiniProgram(10)
        actual_result = mini_program.get_numbers()
        self.assertEqual(expected_result, actual_result)
        
        expected_result = ['Bar', 'Foo', 16, 'FooBar', 14, 'Foo', 'Bar', 'Foo', 8, 'Foo', 4, 1]
        mini_program = MiniProgram(20)
        actual_result = mini_program.get_numbers()
        self.assertEqual(expected_result, actual_result)
        
if __name__ == "__name__":
    unittest.main()
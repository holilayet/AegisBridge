# test_aegisbridge.py
"""
Tests for AegisBridge module.
"""

import unittest
from aegisbridge import AegisBridge

class TestAegisBridge(unittest.TestCase):
    """Test cases for AegisBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AegisBridge()
        self.assertIsInstance(instance, AegisBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AegisBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

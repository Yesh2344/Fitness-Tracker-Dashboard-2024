import unittest
from unittest.mock import patch
from utils.data_loader import load_data

class TestDataLoader(unittest.TestCase):
    @patch("pandas.read_csv")
    def test_load_data(self, mock_read_csv):
        mock_read_csv.side_effect = [pd.DataFrame(), pd.DataFrame(), pd.DataFrame()]
        data = load_data()
        self.assertIsInstance(data, tuple)
        self.assertEqual(len(data), 3)

if __name__ == "__main__":
    unittest.main()
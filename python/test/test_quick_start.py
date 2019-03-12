import unittest2 as unittest
import pandas as pd

import python.quick_start as qs

class TestQuickStart(unittest.TestCase):
    """
    Test code from 'Quick Start' section exercises.
    """
    @classmethod
    def setUpClass(cls):
        """
        Read README.md file.
        """
        cls.text_file = qs.read_readme_file()

    def test_count(self):
        """
        Test row count.
        """
        self.assertEqual(self.text_file.count(), 105)
    
    def test_lines_with_spark(self):
        """
        Check how many lines contain 'Spark'.
        """
        lines_with_spark = self.text_file.filter(self.text_file.value.contains("Spark")) 
        self.assertEqual(lines_with_spark.count(), 20)

    def test_to_pandas(self):
        """
        Test toPandas() function.
        """
        df = self.text_file.toPandas()
        self.assertIsInstance(df, pd.DataFrame)
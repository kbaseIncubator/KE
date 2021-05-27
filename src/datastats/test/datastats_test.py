import unittest
import shutil
import datastats
import os


class TestDataStats(unittest.TestCase):

    temp_dir = 'test/data/temp'
    test_data = 'test/data'
    test_file = 'test/data/test.tsv'

    @classmethod
    def setUpClass(cls) -> None:
        os.makedirs(cls.temp_dir, exist_ok=True)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.temp_dir):
            shutil.rmtree(cls.temp_dir)

    def test_row(self):
        output_file = os.path.join(self.temp_dir, 'row_stats.tsv')
        target_file = os.path.join(self.test_data, 'row_stats.tsv')
        datastats.row_stats(self.test_file, output_file, start_index=2)
        f1 = open(target_file)
        s1 = f1.read()
        f2 = open(output_file)
        s2 = f2.read()
        self.assertEqual(s1, s2)
        f1.close()
        f2.close()

    def test_col(self):
        output_file = os.path.join(self.temp_dir, 'col_stats.tsv')
        target_file = os.path.join(self.test_data, 'col_stats.tsv')
        datastats.col_sum(self.test_file, output_file, start_index=2)
        f1 = open(target_file)
        s1 = f1.read()
        f2 = open(output_file)
        s2 = f2.read()
        self.assertEqual(s1, s2)
        f1.close()
        f2.close()


if __name__ == '__main__':
    unittest.main()
import unittest
from core.core import *


class CoreTestCase(unittest.TestCase):

    def test_Notebook_cp_dp(self):
        """TODO"""
        test_dict = {'file1': 'value1', 'file2': 'value2',
                     'list1': ['file1.1', 'file2.2']}
        nb = Notebook(test_dict)

        c = nb.comp_self()
        d = Notebook.decompress(c)
        self.assertEqual(nb.note_dict, d)



if __name__ == '__main__':
    unittest.main()

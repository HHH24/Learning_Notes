import unittest
from core.core import *

test_dict = {
    'format': (('name', 1), (':', 0), ('sex', 1)),
    'content': [{'name': 'Crow', 'sex': 'man'},
                {'name': 'Bibi', 'sex': 'woman'}]
    }
nb = Notebook(test_dict)
expected_analysis = [
    'Crow : man',
    'Bibi : woman'
    ]
nd = nb.note_dict

class NotebookTestCase(unittest.TestCase):

    def test_cp_dp(self):
        c = nb.compress_self()
        d = Notebook.decompress(c)
        self.assertEqual(d, nd)

    def test_analysis(self):
        aa = nb.analize(nd)
        self.assertEqual(aa, expected_analysis)


if __name__ == '__main__':
    unittest.main()

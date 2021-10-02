"""Author:Yiyang Shi
   Program content:HW04: Develop with the Perspective of the Tester in mind
"""

import unittest

from HW04_Yiyang_Shi import Findgit


class TriangleTest(unittest.TestCase):
    """Test the class and functions"""

    def test_repo(self):
        """Test the repos"""
        User = Findgit("zk3304439")

        self.assertTrue('SSW-567' in User.get_repo_list())
        self.assertTrue('567Tri' in User.get_repo_list())
        self.assertFalse('Student-Repository' not in User.get_repo_list())
        self.assertTrue('hello-world' in User.get_repo_list())
        self.assertTrue('tinyobjloader' in User.get_repo_list())

    def test_commits(self):
        """Test the commits"""
        User = Findgit("zk3304439")
        self.assertGreaterEqual(User.get_commits('SSW-567'), 1)
        self.assertGreaterEqual(User.get_commits('567Tri'), 15)
        self.assertGreaterEqual(User.get_commits('Student-Repository'), 9)
        self.assertGreaterEqual(User.get_commits('hello-world'), 1)
        self.assertGreaterEqual(User.get_commits('tinyobjloader'), 30)
        self.assertGreaterEqual(User.get_commits('nothing else'), -1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

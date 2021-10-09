"""Author:Yiyang Shi
   Program content:HW05: Mock test
"""

import unittest
from unittest import mock
from unittest.mock import Mock

from HW04_Yiyang_Shi import Findgit


class GitTest(unittest.TestCase):
    """Test the class and functions"""

    @mock.patch('requests.get')
    def test_getting_todos_when_response_is_ok(self, mock_get):
        """Test the repos"""
        todos = 'zk3304439'
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = todos
        User = Findgit(todos)

        self.assertTrue('567Tri' in User.get_repo_list())
        self.assertFalse('Student-Repository' not in User.get_repo_list())
        self.assertTrue('hello-world' in User.get_repo_list())
        self.assertTrue('tinyobjloader' in User.get_repo_list())

    @mock.patch('requests.get')
    def test_getting_todos_when_commit_is_ok(self, mock_get):
        """Test the commits"""
        todos = 'zk3304439'
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.json.return_value = todos
        User = Findgit(todos)

        self.assertGreaterEqual(User.get_commits('SSW-567'), 1)
        self.assertGreaterEqual(User.get_commits('567Tri'), 15)
        self.assertGreaterEqual(User.get_commits('Student-Repository'), 9)
        self.assertGreaterEqual(User.get_commits('hello-world'), 1)
        self.assertGreaterEqual(User.get_commits('tinyobjloader'), 30)
        self.assertGreaterEqual(User.get_commits('nothing else'), -1)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

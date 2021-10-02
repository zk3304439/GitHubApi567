"""Author:Yiyang Shi
   Program content:HW04: Develop with the Perspective of the Tester in mind
"""

import sys, json, requests


class Findgit:
    """Use this class to get information of github"""

    def __init__(self, userid):
        """the init in class"""
        self.userid = userid
        self._repo = dict()
        self._url = 'https://api.github.com/users/' + self.userid + '/repos'
        self.get_repo()

    def get_repo(self):
        """get repos in github"""
        time = json.loads(requests.get(self._url).text)
        for i in time:
            try:
                self._repo.setdefault(i['name'], 0)
                url = "https://api.github.com/repos/" + self.userid + "/" + i["name"] + "/commits"
                self._repo[i['name']] = len(json.loads(requests.get(url).text))
            except Exception as e:
                print(e)
                sys.exit()

    def get_info(self):
        """prepare to print the info"""
        for i, j in self._repo.items():
            print(f"Repo: {i} Number of commits: {j}")

    def get_repo_list(self):
        """get the repo list"""
        return self._repo.keys()

    def get_commits(self, name: str):
        """get the commits"""
        if name in self._repo.keys():
            return self._repo[name]
        else:
            return -1


if __name__ == '__main__':
    """Enter user id and print info"""
    User = Findgit('zk3304439')
    User.get_info()

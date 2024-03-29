import re
import requests
import json
import utils


class urlService:
    # TODO missing validations
    @classmethod
    def get_identifier(self, url):
        try:
            # TODO Add validations
            r = re.search(r"(watch\?v=|\.be\/)([\-A-z\d]+)", url)
            result = r.group(2)
            if result is None:
                return None
            return result
        except Exception as ex:
            utils.log(
                "Error", "Somethig went wrong trying to ge the identifier", ex)
            return None


class GithubGistService():
    def __init__(self, githubGist_url, githubAPI_token):
        self.url = githubGist_url
        self.headers = {
            'Authorization': "Token " + githubAPI_token,
            'Content-Type': 'application/json'
        }

    def __get_request(self):
        response = requests.request(
            "GET", url=self.url, headers=self.headers)
        return json.loads(response.text)

    def __patch_request(self, body):
        response = requests.request(
            "PATCH", url=self.url, headers=self.headers, data=body)
        return json.loads(response.text)

    def get_all_files(self):
        response = self.__get_request()
        return response["files"]

    def get_url(self):
        response = self.__get_request()
        return response["files"]["PlayerURL"]["content"]

    def update_url(self, content):
        body = json.dumps({"files": {"PlayerURL": {"content": content}}})
        self.__patch_request(body)


if __name__ == '__main__':
    pass

import requests

class HttpRequest():

    def __init__(self,url,data):
        self.url=url
        self.data=data
        self.header={
          "content-type":"application/json; charset=UTF-8",
          "token":"eyJjIjoidFVEWlp5N25kM21sUlVEaDlXV21mM2NxTlJTZlVWRW16Z1J1VE8wYjYxNVIwdHRpQWdlVVFPM21LM3o2d290NGhUcWptUjEzeFp0cng3R1lwcDdEQk1veDVBIiwiciI6MCwicyI6IkdUeTNxYmJKSDVaT0hPeXZIRnVVZDZTZEZwOU9SZzFWTCtYUGNtNHRKNlE9IiwidCI6MTY4NjIxNDE5MywidiI6ImZhdC1kMSJ9",
          "user-agent":"Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"
        }

    def http_request(self):
        res=requests.post(self.url,headers=self.header,json=self.data)
        return res.json()

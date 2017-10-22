# !/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import get_timeline
import index

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    user_name = ""
    tweets = ""
    if request.method == "POST" :
        # リクエストの取得
        user_name = request.form["username"]
        count = request.form["count"]

        # ツィートの取得
        tweets = get_timeline.getUserTimeLine(user_name, count)

    return index.index(user_name, tweets)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
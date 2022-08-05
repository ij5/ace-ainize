from datetime import datetime
import glob
import os
import time
import anim
import threading

print(datetime.timestamp(datetime.now()))

class User:
    def __init__(self, name: str):
        self.name = name

class Chat:
    def __init__(self, username: str, text: str, score: int = 0):
        self.author = User(username)
        self.body = text
        self.score = score

# most_common = ['a', 'b', 'c']
# characters = anim.get_characters(most_common)
# chats = [
#     Chat('a', '안녕'),
#     Chat('b', '반가워'),
#     Chat('c', '안녕하세요.', score=-1)
# ]

# anim.comments_to_scene(chats, characters, output_filename="hello.mp4")

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.post('/generate')
def generate():
    chats = []
    most_common = []
    print(request.json)
    for c in request.json:
        chats.append(Chat(c['nickname'], c['content']))
        # if not c['nickname'] in most_common:
        most_common.append(c['nickname'])
    characters = anim.get_characters(most_common)
    filename = f"outputs/{datetime.timestamp(datetime.now())}.mp4"
    anim.comments_to_scene(chats, characters, output_filename=filename)
    print("success")
    return send_file(filename, mimetype='video/mp4')

def delete_every_10_min():
    for f in glob.glob("outputs/*.mp4"):
        os.remove(f)
    time.sleep(600)
    delete_every_10_min()
    

threading.Thread(target=delete_every_10_min)

app.run('0.0.0.0', 5050)
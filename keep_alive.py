from flask import Flask
from threading import Thread

app = Flask("app")

@app.route("/")
def keep():
  return "hello, <marquee><iframe src='https://infinityiron.xyz' height='500' width='500'></marquee>"

def run():
  app.run(host='0.0.0.0',port=8042)

def keep_alive():
    t = Thread(target=run)
    t.start()
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
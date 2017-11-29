from flask import Flask

app=Flask(__name__)

@app.route("/yes/<name>")
def yes(name):
	return "hello"+" "+name

if __name__=="__main__":
	app.run()
from flask import Flask
app=Flask("__name__")

@app.route("/Home/<name>/<man>")
def Home(name,man):
	return "Hey"+" "+name+man

if __name__=="__main__":
	app.run()
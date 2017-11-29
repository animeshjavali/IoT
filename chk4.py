from flask import Flask
app=Flask("__name__")

@app.route("/home/LED test/<variable>")
def home(variable):
	if(variable==0):
		return "LED is OFF"
	else:
		return "LED is ON"

if "__name__"=="__main__":
	app.run()

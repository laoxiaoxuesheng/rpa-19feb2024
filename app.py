from flask import Flask,request,render_template

app = Flask(_name_)

@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

if __name__ == "__main__":
  app.run()

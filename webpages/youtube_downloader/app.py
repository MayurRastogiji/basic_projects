from flask import Flask, render_template, request
import yt_dlp
import os


# folder of the downloaded files 
folder_path = './static'

# Get the list of files in the folder
file_names = os.listdir(folder_path)

# Filter the list to only include files (and not directories)
file_names = [f for f in file_names if os.path.isfile(os.path.join(folder_path, f))]

app = Flask(__name__)
else_conditon="Page Not Found"

# name = "/static/"+file_names[-1]

@app.route("/", methods =["GET", "POST"])
def index():
  if request.method == "POST":
    link = request.form["link"]
    name = request.form["name"]
    print(link)
    yt_dlp.YoutubeDL({'format': 'best', 'outtmpl' : f'static/{name}.%(ext)s'}).download([link])
  return render_template("index.html", file_names=file_names)

@app.route("/about.html")
def about():
  return render_template("about.html")

@app.route("/contactus.html")
def contact():
  return render_template("contactus.html")

@app.route(f"/static/{file_names[-1]}")
def view():
  return render_template(f"/static/{file_names[-1]}")

if __name__ == "__main__":
    app.run(debug=True)


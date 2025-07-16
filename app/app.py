from flask import Flask, render_template, request
from app.model import auto_clusterer


app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        df_x = request.form["x_df"]
        df_main = request.form["main_df"]
        try:
            pca = request.form["pca"]
        except:
            pca = False

        model_score = auto_clusterer(df_main, df_x, pca)
    else:
        model_score = None

    if model_score:
        return render_template("main_withscore.html", results=f"{round(model_score *100, 3)}%")
    else:
        return render_template("main_withoutscore.html")




if __name__ == "__main__":
    app.run(debug=True)
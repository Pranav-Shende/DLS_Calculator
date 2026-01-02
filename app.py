from flask import Flask, render_template, request
from dls import (
    dls_pre_first_innings,
    dls_mid_first_innings,
    dls_pre_second_innings,
    dls_mid_second_innings
)

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        scenario = request.form.get("scenario")
        fmt = request.form.get("format")

        try:
            if scenario == "pre1":
                delay = int(request.form.get("delay", 0))
                result = dls_pre_first_innings(fmt, delay)
                return render_template("result.html", result=result, scenario=scenario)

            elif scenario == "mid1":
                overs = float(request.form.get("overs", 0))
                wickets = int(request.form.get("wickets", 0))
                delay = int(request.form.get("delay", 0))
                result = dls_mid_first_innings(fmt, overs, wickets, delay)
                return render_template("result.html", result=result, scenario=scenario)

            elif scenario == "pre2":
                score = int(request.form.get("team1", 0))
                delay = int(request.form.get("delay", 0))
                result = dls_pre_second_innings(fmt, score, delay)
                return render_template("result.html", result=result, scenario=scenario)

            elif scenario == "mid2":
                t1 = int(request.form.get("team1", 0))
                t2 = int(request.form.get("team2", 0))
                overs = float(request.form.get("overs", 0))
                wickets = int(request.form.get("wickets", 0))
                delay = int(request.form.get("delay", 0))
                
                result = dls_mid_second_innings(fmt, t1, t2, overs, wickets, delay)
                result["team2_score"] = t2
                return render_template("result.html", result=result, scenario=scenario)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
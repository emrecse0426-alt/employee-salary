from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        emp_id = request.form["emp_id"]
        emp_name = request.form["emp_name"]
        basic_salary = float(request.form["basic_salary"])

        # Salary calculations (same as your code)
        hra = basic_salary * 0.20
        da = basic_salary * 0.10
        pf = basic_salary * 0.12

        gross_salary = basic_salary + hra + da
        net_salary = gross_salary - pf

        result = {
            "emp_id": emp_id,
            "emp_name": emp_name,
            "basic_salary": basic_salary,
            "hra": hra,
            "da": da,
            "pf": pf,
            "gross_salary": gross_salary,
            "net_salary": net_salary
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

# python 3

from flask import Flask, render_template, request

app = Flask (__name__)

@app.route('/', methods=['GET', 'POST'])
def root_page():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight,height)
    return render_template("bmi_cal.html",
                            bmi=bmi)

def calc_bmi(weight,height):
    return round((weight/((height/100)**2)), 2 )


app.run(debug=True)
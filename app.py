# ---------------------------------------------------------------------------- #
# -- Imports ----------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from flask import Flask, render_template, request
import budget


# ---------------------------------------------------------------------------- #
# -- App Routes -------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #

app = Flask(__name__)
income = []
expenses = []
i_total = 0
e_total = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item_name = request.form['item_name']
        amount = float(request.form['amount'])
        if request.form['type'] == 'income':
            budget.add_item(income, item_name, amount)
        else:
            budget.add_item(expenses, item_name, amount)

        budget.calculate_weights(income) 
        budget.calculate_weights(expenses) 

        i_total = budget.calculate_total(income)
        e_total = budget.calculate_total(expenses)

        return render_template('index.html', income=income, expenses=expenses, i_total=i_total, e_total=e_total)
    else:
        return render_template('index.html', income=income, expenses=expenses, i_total=0, e_total=0)


# ---------------------------------------------------------------------------- #
# -- Main -------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


if __name__ == 'main':
    app.run(debug=True)

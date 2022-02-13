# ---------------------------------------------------------------------------- #
# -- Imports ----------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from flask import Flask, render_template, request
from budget import Budget

# ---------------------------------------------------------------------------- #
# -- App Routes -------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


app = Flask(__name__)
global user_budget
user_budget = Budget([], [], [], 0, 0)

@app.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        if request.form['action'] == 'Undo':
            user_budget.undo()
        else:
            item_name = request.form['item_name']
            amount = request.form['amount']
            if item_name == '' or amount == '':
                balance = user_budget.i_total - user_budget.e_total
                return render_template('index.html', income=user_budget.income, expenses=user_budget.expenses, i_total=user_budget.i_total, e_total=user_budget.e_total, balance=balance)
            amount = float(amount)
            if request.form['type'] == 'income':
                user_budget.add_item('income', item_name, amount)
            else:
                user_budget.add_item('expenses', item_name, amount)

        user_budget.calculate_weights('income') 
        user_budget.calculate_weights('expenses') 

        balance = user_budget.i_total - user_budget.e_total

        return render_template('index.html', income=user_budget.income, expenses=user_budget.expenses, i_total=user_budget.i_total, e_total=user_budget.e_total, balance=balance)
    else:
        return render_template('index.html', income=[], expenses=[], i_total=0, e_total=0, balance=0)


# ---------------------------------------------------------------------------- #
# -- Main -------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


if __name__ == 'main':
    app.run(debug=True)

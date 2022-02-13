# ---------------------------------------------------------------------------- #
# -- Imports ----------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


from dataclasses import dataclass, field, asdict


# ---------------------------------------------------------------------------- #
# -- Class ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


@dataclass
class Budget:
    income: list = field(default_factory=list())
    expenses: list = field(default_factory=list())
    last_added: list = field(default_factory=list())
    i_total: int = 0
    e_total: int = 0
    balance: int = 0


    # ---------------------------------------------------------------------------- #
    # -- Functions --------------------------------------------------------------- #
    # ---------------------------------------------------------------------------- #


    def add_item(self, category: str, name: str, amount: float):
        item = {
            'name': name,
            'percent': '',
            'amount': round(amount, 2)
        }
        if category == 'income':
            self.income.append(item)
            self.last_added.append('income')
        else:
            self.expenses.append(item)
            self.last_added.append('expenses')


    def calculate_weights(self, category: str):
        if category == 'income':
            self.calculate_total('income')
            total = self.i_total
            for item in self.income:
                item['percent'] = round(((item['amount'] / total) * 100), 2)
        else:
            self.calculate_total('expenses')
            total = self.e_total
            for item in self.expenses:
                item['percent'] = round(((item['amount'] / total) * 100), 2)

        
    def calculate_total(self, category: str):
        if category == 'income':
            total = 0
            for item in self.income:
                total += item['amount']
            self.i_total = total
        else:
            total = 0
            for item in self.expenses:
                total += item['amount']
            self.e_total = total
    
    def get_balance(self):
        self.balance = self.i_total - self.e_total

    def undo(self):
        if len(self.last_added) > 0:
            if self.last_added[-1] == 'income':
                if len(self.income) > 0:
                    self.income.pop(-1)
                    self.last_added.pop(-1)
                    self.calculate_weights('income')
            else:
                if len(self.expenses) > 0:
                    self.expenses.pop(-1)
                    self.last_added.pop(-1)
                    self.calculate_weights('expenses')



# ---------------------------------------------------------------------------- #
# -- Main -------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def main():
    budget = Budget([], [], [], 0, 0)
    budget.add_item('income', 'Allowance', 5049)
    budget.add_item('expenses', 'Virgin Active', 510)
    budget.calculate_weights('income')
    budget.calculate_weights('expenses')
    print(budget.income)
    print(budget.expenses)

    print(f'Income total: {budget.i_total}')
    print(f'Expenses total: {budget.e_total}')
    budget.undo()
    budget.undo()
    print(budget.income)
    print(budget.expenses)

    print(f'Income total: {budget.i_total}')
    print(f'Expenses total: {budget.e_total}')

if __name__ == '__main__':
    main()
class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})
    
    def whithdraw(self, amount, description):
        print(sum(map(lambda total: total['amount'],self.ledger)))
        #    self.ledger.append({'amount':-amount, 'description':description})

def create_spend_chart(categories):
    pass

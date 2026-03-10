class Commissions:
    def __init__(self):
        self.fixed_commissions = {
            'USD': 5.00,
            'EUR': 4.50,
            'GBP': 4.00
        }
    
    def process(self, data):
        if 'error' in data:
            return data
        if 'converted_amount' not in data:
            print("Commission failed: No converted amount")
            return {'error': 'No converted amount to calculate commission'}
            
        commission = self.fixed_commissions.get(data['currency'], 5.00)
        data['commission'] = commission
        data['total'] = data['converted_amount'] + commission
        
        print(f"Commission: {commission:.2f} {data['currency']}")
        print(f"Total: {data['total']:.2f} {data['currency']}")
        
        return data
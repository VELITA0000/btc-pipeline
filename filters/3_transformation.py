class Transformation:
    def __init__(self):
        self.exchange_rates = {
            'USD': 65000.00,
            'EUR': 60000.00,
            'GBP': 52000.00
        }
    
    def process(self, data):
        if 'error' in data:
            return data
        
        rate = self.exchange_rates.get(data['currency'])
        if not rate:
            print(f"Transformation failed: No rate for {data['currency']}")
            return {'error': 'Could not get exchange rate'}
        
        data['converted_amount'] = data['btc_amount'] * rate
        print(f"Converted: {data['btc_amount']} BTC = {data['converted_amount']:.2f} {data['currency']}")
        
        return data
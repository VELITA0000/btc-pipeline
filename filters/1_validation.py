class Validation:
    def process(self, data):
        if not data.get('user_id'):
            print("Validation failed: Missing user ID")
            return {'error': 'Missing user ID'}
        if not data.get('btc_amount') or data['btc_amount'] <= 0:
            print("Invalid BTC amount")
            return {'error': 'Invalid BTC amount'}
        if data.get('currency') not in ['USD', 'EUR', 'GBP']:
            print("Invalid currency (USD/EUR/GBP)")
            return {'error': 'Invalid currency (USD/EUR/GBP)'}
        
        print("Validation passed")
        return data
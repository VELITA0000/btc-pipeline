import json
import os
from datetime import datetime

class Storage:
    def __init__(self, file='transactions_result.json'):
        self.file = file
        
    def process(self, data):
        data['processed_at'] = datetime.now().isoformat()
        data['status'] = 'completed' if 'error' not in data else 'failed'
        
        transactions = []
        if os.path.exists(self.file):
            try:
                with open(self.file, 'r') as f:
                    transactions = json.load(f)
            except:
                transactions = []
        
        transactions.append(data)
        
        with open(self.file, 'w') as f:
            json.dump(transactions, f, indent=2)
        
        if 'error' in data:
            print(f"Transaction saved with error: {data['error']}")
        else:
            print("Transaction saved")
        
        return data
import json
import os
import importlib

class Pipeline:
    def __init__(self):
        filter_modules = [
            '1_validation',
            '2_authentication', 
            '3_transformation',
            '4_commissions',
            '5_storage'
        ]
        
        self.filters = []
        for module_name in filter_modules:
            module = importlib.import_module(f'filters.{module_name}')
            filter_class = getattr(module, module_name.split('_')[1].capitalize())
            self.filters.append(filter_class())
    
    def process(self, transactions):
        results = []
        for i, t in enumerate(transactions):
            print(f"\n--- Transaction {i+1} ---")
            data = t.copy()
            for f in self.filters:
                data = f.process(data)
                if 'error' in data:
                    break
            results.append(data)
        return results
    
    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            return json.load(f)

if __name__ == "__main__":
    pipeline = Pipeline()
    transactions = pipeline.load('transactions.json')
    if transactions:
        results = pipeline.process(transactions)
        print(f"\nProcessed {len(results)} transactions")
import json
import os

class Authentication:
    def __init__(self, db_file='database/users.json'):
        self.db_file = db_file
        self.users = self._load_users()
    
    def _load_users(self):
        if not os.path.exists(self.db_file):
            print(f"Database file {self.db_file} not found")
            return []
        
        try:
            with open(self.db_file, 'r') as f:
                data = json.load(f)
                return data.get('users', [])
        except:
            print("Error loading database")
            return []
    
    def _verify_user(self, user_id):
        for user in self.users:
            if user['user_id'] == user_id:
                return True
        return False
    
    def process(self, data):
        if 'error' in data:
            return data
        
        if not self._verify_user(data['user_id']):
            print(f"Authentication failed: User {data['user_id']} not found")
            return {'error': f"User {data['user_id']} not found in database"}
        
        print("Authentication passed")
        return data
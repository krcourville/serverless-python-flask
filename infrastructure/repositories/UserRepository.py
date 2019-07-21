from injector import inject

db = {
    'keys': [],
    'items': {}
}


class UserRepository:
    def get(self, user_id: str):
        return db['items'].get(user_id, None)

    def add(self, data: dict):
        user_id = data['user_id']
        db['keys'].append(user_id)
        db['items'][user_id] = data


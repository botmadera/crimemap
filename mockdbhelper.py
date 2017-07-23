class MockDBHelper:
    def connect(self, database="crimemap"):
        pass

    def get_all_inputs(self):
        return []

    def add_input(self, data):
        pass

    def clear_all(self):
        pass

    def add_crime(self, category, date, latitude, longitude, description):
        pass

    def get_all_crimes(self):
        crime =[{'latitude': -25.297651,
                 'longitude': -57.593593,
                'date': '2000-01-01',
                'category': 'muggin',
                'description': 'mock description'},{'latitude': -25.297433801640814,
                 'longitude': -57.59552478790283,
                'date': '2000-01-01',
                'category': 'muggin',
                'description': 'mock description'},
                {'latitude': -25.30243629054295,
                 'longitude': -57.583208084106445,
                'date': '2000-01-01',
                'category': 'muggin',
                'description': 'mock description'},
                {'latitude': -25.30220350091566,
                 'longitude': -57.597198486328125,
                'date': '2000-01-01',
                'category': 'muggin',
                'description': 'mock description'}]
        return crime

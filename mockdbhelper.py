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
        crime =[{'latitude': -33.301304,
                 'longitude': 26.523355,
                'date': "2000-01-01",
                'category': "muggin",
                'description': "mock description"}]
        return crime[0]

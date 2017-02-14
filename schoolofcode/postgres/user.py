import psycopg2

class User:
    def __init__(self, id, email, firstName, lastName):
        self.id = id
        self.email = email
        self.firstName = firstName
        self.lastName = lastName

    def __repr__(self):
        return "<User {}".format(self.email)

    def save_to_db(self):
        with psycopg2.connect(dsn=None, database='test', user='test', password='test', host='localhost') as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    'insert into users(email, firstName, lastName) values (%s, %s, %s)',
                    (self.email, self.firstName, self.lastName))


import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'israel'
DATABASE = 'users'


def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
        connection.close()
        return results
    except:
        connection.close()


def create_table_query(name, **kwargs):
    q = f'Create table {name} ('
    for field_name, field_type in kwargs.items():
        q += f'{field_name} {field_type},'
    return q[:-1] + ')'


def add_user_query(user_name, password):
    q = f"INSERT INTO user_passwords (user_name, user_password) VALUES ('{user_name}', '{password}') RETURNING id, user_name, user_password;"
    return run_query(q)

#def add_constraint_query(constraint_name, constraint):
   # q = 'CONSTRAINT'





q = create_table_query('logins', id='serial primary key', user_id='int')
run_query(q)
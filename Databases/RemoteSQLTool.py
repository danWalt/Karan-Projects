# A utility that can execute queries on remote servers from your local
# computer across the Internet. It should take in a remote host, user name
# and password, run the query and return the results.

import pymysql.cursors

# get remote host connection from user:
print('host name: ')
host = input()
print('user name: ')
user = input()
print('password: ')
password = input()
print('db name: ')
db_name = input()

connection = pymysql.connect(host=host,
                             user=user,
                             port=3306,
                             password=password,
                             db=db_name,
                             autocommit=True)
try:
    with connection.cursor() as cursor:
        print('sql query: ')
        query = input()
        # execute the requested sql query
        cursor.execute(query)

finally:
    connection.close()
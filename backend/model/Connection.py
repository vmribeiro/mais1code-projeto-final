import json
import psycopg2

class Connection():

    def __init__(self):
        credentials = json.load(open('database/assets/configs.json'))

        try:
            self.conn = psycopg2.connect( user     = credentials['username']
                                        , password = credentials['password']
                                        , host     = credentials['host'    ]
                                        , port     = credentials['port'    ]
                                        , database = credentials['database'])
        except Exception as ex: 
            print("Error during DB connection. Error: {}".format(str(ex)))


    def close_connection(self, cursor, connection):
        cursor.close()
        connection.close()
        print("Connection with database is now closed.")
        return True;


from model.Connection import Connection

class ControllerUsuario():

    def __init__(self):
        self.status = 1

    def insertUser(self, user_name):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            insert_query = """ INSERT INTO "MAIS1CODE_PROJETOFINAL".USERS (  USER_NAME     ) 
                                              VALUES                    (           %s   )
                    """

            record_to_insert = ( user_name , )

            cursor.execute(insert_query, record_to_insert)
            conn_obj.commit()
            count = cursor.rowcount
            
            print(count, "Record inserted successfully into user table.")

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during user insertion. Error: {}".format(str(ex)))
            return False


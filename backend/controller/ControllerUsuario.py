
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


    def select_all_users(self):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM "MAIS1CODE_PROJETOFINAL".USERS """
    
            cursor.execute(sql_select_query)
            rows = cursor.fetchall()

            list_users = []
            for row in rows:
                list_users.append({
                          'id':                 row[0]
                        , 'name':               row[1]})

            connection.close_connection(cursor = cursor, connection = conn_obj)

            return list_users

        except Exception as ex:

            print("Error during users selection. Error: {}".format(str(ex)))
            return False

    def select_user_by_id(self, user_id):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM "MAIS1CODE_PROJETOFINAL".USERS WHERE USER_ID=%s"""
    
            fields_to_select = (user_id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("User {} not found!".format(user_id))
                return False

            user = {
                      'id': record[0]
                    , 'name': record[1]}


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return user

        except Exception as ex:

            print("Error during user selection. Error: {}".format(str(ex)))
            return False


    def update_user(self, user_name, user_id):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM "MAIS1CODE_PROJETOFINAL".USERS WHERE USER_ID=%s"""
    
            fields_to_select = (user_id)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("User {} not found!".format(user_id))
                return False

            print("Updating user: \n\n" + str(record) + "\n\n") # Use it as a backup in case of issues

            update_query = """ UPDATE "MAIS1CODE_PROJETOFINAL".USERS 
                               SET                                USER_NAME         = %s
                                WHERE USER_ID = %s
                            """

            if user_name != "nan": 
                treated_user_name = user_name
            else: 
                treated_user_name = record[1]

           

            fields_to_update = (                                  treated_user_name
                                                                , user_id )
            
            cursor.execute(update_query, fields_to_update)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record updated successfully into user table.")


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during user update. Error: {}".format(str(ex)))
            return False

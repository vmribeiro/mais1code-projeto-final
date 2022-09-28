
from model.Connection import Connection

class ControllerUsuario():

    def __init__(self):
        self.status = 1


    def insertUser(self, user_name , name, data_de_nascimento, telefone, is_professional, formacao, especializacao, senha, email):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            insert_query = """ INSERT INTO "MAIS1CODE_PROJETOFINAL".USERS (  USER_NAME, NAME, DATA_DE_NASCIMENTO, TELEFONE, IS_PROFESSIONAL, FORMACAO, ESPECIALIZACAO, SENHA, EMAIL     ) 
                                              VALUES                    (           %s,   %s,                 %s,       %s,              %s,       %s,             %s,    %s,    %s   )
                    """

            record_to_insert = ( user_name , name, data_de_nascimento, telefone, is_professional, formacao, especializacao, senha, email, )

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
                        , 'name':               row[2]
                        , 'data_de_nascimento': row[3]
                        , 'telefone':           row[4]
                        , 'profssional':        row[5]
                        , 'formacao':           row[6]
                        , 'especializacao':     row[7]
                })

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
                    , 'name': record[2]
                    , 'data_de_nascimento': record[3]
                    , 'telefone': record[4]
                    , 'profissional': record[5]
                    , 'fomacao': record[6]
                    , 'especializacao': record[7]
            }


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return user

        except Exception as ex:

            print("Error during user selection. Error: {}".format(str(ex)))
            return False


    def login(self, username, password):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            sql_select_query = """SELECT * FROM "MAIS1CODE_PROJETOFINAL".USERS WHERE USER_NAME=%s AND SENHA=%s"""
    
            fields_to_select = (username, password)
            cursor.execute(sql_select_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("User {} not found!".format(username))
                return False

            user = {
                      'id': record[0]
                    , 'name': record[2]
                    , 'data_de_nascimento': record[3]
                    , 'telefone': record[4]
                    , 'profissional': record[5]
                    , 'fomacao': record[6]
                    , 'especializacao': record[7]
            }


            connection.close_connection(cursor = cursor, connection = conn_obj)

            return user

        except Exception as ex:

            print("Error during user selection. Error: {}".format(str(ex)))
            return False


    def update_user(self,  user_id, user_name = "nan", name = "nan", data_de_nascimento = "nan", telefone = "nan", is_professional = "nan", formacao = "nan", especializacao = "nan", senha = "nan", email = "nan"):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            update_query = """SELECT * FROM "MAIS1CODE_PROJETOFINAL".USERS WHERE USER_ID = %s"""
    
            fields_to_select = (user_id ,)
            cursor.execute(update_query, fields_to_select)
            record = cursor.fetchone()

            if record is None:
                print("User {} not found!".format(user_id))
                return False

            print("Updating user: \n\n" + str(record) + "\n\n") # Use it as a backup in case of issues

            update_query = """ UPDATE "MAIS1CODE_PROJETOFINAL".USERS 
                               SET                                USER_NAME             = %s
                                                                , NAME                  = %s
                                                                , DATA_DE_NASCIMENTO    = %s
                                                                , TELEFONE              = %s
                                                                , IS_PROFESSIONAL       = %s
                                                                , FORMACAO              = %s
                                                                , ESPECIALIZACAO        = %s
                                                                , SENHA                 = %s
                                                                ,EMAIL                  = %s
                                WHERE USER_ID = %s
                            """

            if user_name != "nan": 
                treated_user_name = user_name
            else: 
                treated_user_name = record[1]

            if name != "nan": 
                treated_name = name
            else: 
                treated_name = record[2]

            if data_de_nascimento != "nan": 
                treated_data_de_nascimento = data_de_nascimento
            else: 
                treated_data_de_nascimento = record[3]

            if telefone != "nan":
                treated_telefone = telefone
            else:
                treated_telefone = record[4]

            if is_professional != "nan":
                treated_is_professional = is_professional
            else:
                treated_is_professional = record[5]

            if formacao != "nan":
                treated_formacao = formacao
            else:
                treated_formacao = record[6]

            if especializacao != "nan":
                treated_especializacao = especializacao
            else: treated_especializacao = record[7]

            if senha != "nan":
                treated_senha = senha
            else: treated_senha = record[8]

            if email != "nan":
                treated_email = email
            else: treated_email = record[9]



            fields_to_update = (                                  treated_user_name
                                                                , treated_name
                                                                , treated_data_de_nascimento
                                                                , treated_telefone
                                                                , treated_is_professional
                                                                , treated_formacao
                                                                , treated_especializacao
                                                                , treated_senha
                                                                , treated_email
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


    def delete_user(self, user_id):
        try:
            
            connection = Connection()
            conn_obj = connection.conn
            cursor = conn_obj.cursor()

            delete_query = """ DELETE FROM "MAIS1CODE_PROJETOFINAL".USERS 
                               WHERE USER_ID = %s
                           """ 

            fields_to_select = (user_id)

            cursor.execute(delete_query, fields_to_select)
            conn_obj.commit()
            count = cursor.rowcount
            print(count, "Record deleted successfully from user table.")
            
            connection.close_connection(cursor = cursor, connection = conn_obj)

            return True

        except Exception as ex:

            print("Error during deleted user. Error: {}".format(str(ex)))
            return False


 
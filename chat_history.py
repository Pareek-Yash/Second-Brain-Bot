def insert_data(mydb, vec_class, uuid, question, chat_conv):
    # Check if UUID already exists in the database
    mycursor = mydb.cursor()
    sql_select_query = "SELECT * FROM chat_history WHERE uuid = %s AND vec_class = %s"
    mycursor.execute(sql_select_query, (uuid, vec_class))
    result = mycursor.fetchone()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    if result: # UUID already exists, update the existing row
        sql_update_query = "UPDATE chat_history SET prev_queries = CONCAT(prev_queries, CONCAT('###', %s)), chat_history = CONCAT(chat_history, CONCAT('###', %s)), logged_at = NOW() WHERE uuid = %s AND vec_class = %s"
        mycursor.execute(sql_update_query, (question, chat_conv, uuid, vec_class))
        mydb.commit()
    else: # UUID does not exist, insert a new row
        sql_insert_query = "INSERT INTO chat_history (vec_class, uuid, prev_queries, chat_history, logged_at) VALUES (%s, %s, %s, %s, %s)"
        mycursor.execute(sql_insert_query, (vec_class, uuid, question, chat_conv, timestamp))
        mydb.commit()
    

# Define function for retrieving the last conversation for a given vec_class
def get_last_conversation(mydb, uuid, vec_class):
    
    mycursor = mydb.cursor()
    sql = "SELECT chat_history FROM chat_history WHERE uuid = %s AND vec_class = %s"
    val = (uuid, vec_class)
    mycursor.execute(sql, val)
    result = mycursor.fetchone() #result[0] stores the last conversations ; if result is not none: return result[0]; similar in get_prev_queries
    
    
    if result is not None:
        conversations = result[0].split("###")
        context = "###".join(conversations[-5:])  # Keep only the most recent 3 conversations
        prev_responses = "###".join([context] + conversations[:-3]) 
        return context
    else:
        return None

# Define function for retrieving the last conversation for a given vec_class
def get_prev_queries(mydb, uuid, vec_class):
    
    mycursor = mydb.cursor()
    sql = "SELECT prev_queries FROM chat_history WHERE uuid = %s AND vec_class = %s"
    val = (uuid, vec_class)
    mycursor.execute(sql, val)
    result = mycursor.fetchone()
     
    
    if result is not None:
        conversations = result[0].split("###")
        context = "###".join(conversations[-5:])  # Keep only the most recent 3 conversations
        prev_queries = "###".join([context] + conversations[:-3])  
        return context
    else:
        return None
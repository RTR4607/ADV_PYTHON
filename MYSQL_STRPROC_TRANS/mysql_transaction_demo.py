from database_connection import database
class HclPythonTransaction(database):
    def execute_transaction_query(self):
        custid=2
        sql="delete from hcl_customer where cust_id=%s"
        try:
            self.cursor.execute(sql,(custid,))
            self.connection.commit()
        except:
            self.connection.roolback()
            print("Something goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
obj=HclPythonTransaction()
obj.connect('localhost','root','root','student_db')
obj.execute_transaction_query()

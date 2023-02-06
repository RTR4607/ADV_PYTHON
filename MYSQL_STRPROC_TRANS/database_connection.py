from stored_proc_demo import HclStoreProducre
class database(HclStoreProducre):
    def execute_str_procedure(self):
        try:
            mydata=('phone',)
            self.cursor.callproc('get_one',args=mydata)
            for i in self.cursor.stored_results():
                print(i.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
obj=database()

obj.connect('localhost','root','root','student_db')
obj.execute_str_procedure()
print(obj)

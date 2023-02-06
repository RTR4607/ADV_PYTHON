from stored_proc_demo import HclStoreProducre
class Booking(HclStoreProducre):
    def available_seats(self):
        try:
            myd=('12748',)
            self.cursor.callproc('get_trainss',args=myd)
            for i in self.cursor.stored_results():
                print(i.fetchall())
        except Exception as e:
            print(e)
        finally:
            if (self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
    def no_of_tickets(self):
        pass
obj=Booking()
obj.connect('localhost','root','root','student_db')
obj.available_seats()
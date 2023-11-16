
_instance = None

#Implementing Singleton Pattern Desgin 

class DataDB:
   
   host = 'localhost'
   user = 'root'
   password = ''
   db_name = 'arquisw' 

   @staticmethod
   def get_instance():
      
      global _instance
      if _instance is None:
         _instance = DataDB()
      return _instance

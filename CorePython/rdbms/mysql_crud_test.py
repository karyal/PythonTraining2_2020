# import library
from rdbms.mysql_crud import connect_server
from rdbms.mysql_crud import connect_dbms
from rdbms.mysql_crud import *

# Call connect function
# connect_dbms()
values= ('Raj Thapa','Bhaktapur','raj@gmail.com')
insert_record(values)
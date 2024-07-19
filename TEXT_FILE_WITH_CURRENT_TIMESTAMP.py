#CREATE TEXT FILE WITH CURRENT TIMESTAMP FILE NAME.
from datetime import datetime
def create_text_file_with_timestamp():
        # TO GET CURRENT TIME DATE WITH FORMAT
        timestr = datetime.now().strftime("%Y%m%d - %H%M%S")
        # CREATE FILE
        filename = f"file_{timestr}.txt"
        # CREATE AND WRITE THE CONTENT ON FILE
        with open(filename, 'w') as file:
           file.write("")
        print(f"TEXT FILE  '{filename}' CREATED.")

create_text_file_with_timestamp()


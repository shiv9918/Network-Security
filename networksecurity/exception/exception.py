import sys
from networksecurity.logging.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        # Provide clear context on where the error originated
        return (
            f"Error occured in python script name [{self.file_name}] "
            f"line number [{self.lineno}] error message [{self.error_message}]"
        )

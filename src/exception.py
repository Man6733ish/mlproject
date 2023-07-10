# this will keep information of exception that occured
import sys
from src.logger import logging
# error_detail:sys =error details will be present in sys
def error_message_details(error,error_detail:sys):
    # this will tell us where error has occured or in which line or module
    _,_,exc_tb=error_detail.exc_info()
    # in the exception handing documentation this is how we find file name
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))

    return error_message

class CustomException(Exception):
    # this is a cosntuctor which is used to call an object
    # we are inheriting from exception
    def __init__(self,error_message,error_detail:sys):
        # inheriting
        super().__init__(error_message)
        # we will initialise in the custom class variable
        self.error_message=error_message_details(error_message,error_detail=error_detail)

    # we will inherit one functionality of the class, WE WILL PRINT THE ERROR MESSAGE FROM HERE
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)

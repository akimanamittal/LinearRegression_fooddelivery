import sys
import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()          #gives the information about the error(type and line of error)
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

if __name__=='main':

    try:
        a=1/10
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)
    
    
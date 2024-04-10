import sys

def error_message_detail(error):
    _, _, exec_tb = sys.exc_info()
    file_name = exec_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script file name [{0}], line number [{1}], error message [{2}]".format(file_name, exec_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message)
    
    def __str__(self):
        return self.error_message

# Example of raising the custom exception
try:
    raise ValueError("An example error.")
except ValueError as e:
    raise CustomException(e) from None
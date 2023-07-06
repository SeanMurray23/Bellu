class LoggingContextManager:
    def __enter__(self):
        print("LogginContextManager.__enter__()")
        return "Your in a with block!"
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        if exc_type is None:
            print('LogginContextManager.__exit__: Normal Exit detected')
        else:
            print('LoggingContextManager.__exit__:'
                  'Exception Detected '
                  'type={}, Value={}, traceback={}'.format(exc_type,exc_val,exc_tb))
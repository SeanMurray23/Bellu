class LoggingContextManager:
    def __enter__(self):
        print("LogginContextManager.__enter__()")
        return "Your in a with block!"
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('LoggingContxtManager.__exit__({},{},{})'.format(exc_type,exc_val,exc_tb))
        return
    
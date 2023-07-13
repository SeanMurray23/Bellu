import contextlib
import sys



@contextlib.contextmanager
def propagater(name,propagate):
    try:
        yield
        print(name, 'exited normally')
    except Exception:
        print(name, "exited poorly")
        if propagate:
            raise

@contextlib.contextmanager
def nest_test(name):
    print('Entering:', name)
    yield name
    print('Exiting:', name)

@contextlib.contextmanager
def logging_context_manager():  #generator
    print('logging_context_manager:Enter')
    try:
        yield " You're in a With block"
        print("logging_context_manager: normal exit")
    except Exception:
        print('logging contenxt manager :exception exit', sys.exc_info())
    raise # this will push exception to repl



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
            
            
            
            

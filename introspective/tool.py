import inspect
import reprlib
import itertools

def dump(obj):
    print("Type")
    print("===")
    print(type(obj))
    print()
    
    print("Documentation")
    print('==============')
    print(inspect.getdoc(obj.__doc__))
    print()
    
    all_attr_names = set(dir(obj))
    method_names = set(
        filter(lambda attr_name: callable(getattr(obj,attr_name)),
               all_attr_names))
    assert method_names <= all_attr_names
    attr_names = all_attr_names - method_names
    print("Attributes")
    print("=========")
    attr_names_and_values = [(name, reprlib.repr(getattr(obj, name)))
                             for name in attr_names] 
    print_table(attr_names_and_values, "Name", "Value")
    print()
    
    
    print("Methods")
    print("========")
    methods = (getattr(obj,method_name) for method_name in method_names)
    method_names_and_doc = sorted((full_sig(method), brief_doc(method))
                                  for method in methods)
    print_table(method_names_and_doc, "Name", "Description")
    print()
 
def print_table(rows_of_columns, *headers):
        num_col = len(rows_of_columns[0])
        num_header = len(headers)
        if len(headers) != num_col:
            raise TypeError("Expceted {} header arguements,"
                            "got {}".format(num_col, num_header))
        rows_of_columns_with_headers = itertools.chain([headers], rows_of_columns)
        col_of_rows = list(zip(*rows_of_columns))
        column_widths = [max(map(len, column)) for column in col_of_rows]
        col_specs = ('{{:{w}}}'.format(w=width) for width in column_widths)
        format_spec = ''.join(col_specs)
        print(format_spec.format(*headers))
        rules = ('-' * width for width in column_widths)
        print(format_spec.format(*rules))
        for row in rows_of_columns:
            print(format_spec.format(*row))
        
         
    
    
def full_sig(method):
    try:
        return method.__name__ + str(inspect.signature(method))
    except ValueError:
        return method.__name__ + '(...)'
        
def brief_doc(obj):
    doc = obj.__doc__
    if doc is not None:
        lines = doc.splitlines()
        if len(lines) >0:
            return lines[0]
        return ""
    
    
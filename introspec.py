import pprint


def introspection_info(obj):
    attributes = dir(obj)
    obj_type = type(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    
    result = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
    return result


number_info = introspection_info(5)
pprint.pprint(number_info)

str_info = introspection_info('f')
pprint.pprint(str_info)

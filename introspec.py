import pprint


def introspection_info(obj):
    result = {
        'Тип объекта': type(obj),
        'Атрибуты объекта': obj.__dict__,
        'Методы': getattr(obj, '__methods__', []),
        'Модуль': obj.__mod__,
    }
    return result


number_info = introspection_info('f')
pprint.pprint(number_info)

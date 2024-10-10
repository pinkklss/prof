import pprint


def introspection_info(obj):
    result = {
        'Атрибуты объекта': __dict__(obj, '__methods__', []),
        'Тип объекта': type(obj),
        'Методы': dir(obj),
        'Модуль': obj.__mod__,
    }
    return result


number_info = introspection_info('f')
pprint.pprint(number_info)

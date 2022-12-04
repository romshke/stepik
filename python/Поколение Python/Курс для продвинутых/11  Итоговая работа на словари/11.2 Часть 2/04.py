def build_query_string(params):
    result = str()
    
    for _ in sorted(params.items()):
        if result == '':
            result += f'{_[0]}={_[1]}'
        else:
            result += f'&{_[0]}={_[1]}'
    
    return result
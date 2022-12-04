def merge(values):      # values - это список словарей
    result = {}

    for dicts in values:
        for item in dicts.items():
            if item[0] not in result:
                result.setdefault(item[0], set([item[1],]))
            else:
                result[item[0]].add(item[1])
                
    return result
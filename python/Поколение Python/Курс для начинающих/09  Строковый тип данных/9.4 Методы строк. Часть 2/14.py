s = input()

print(f"{s.find('f')} {s.rfind('f')}" if s.count('f') > 1 else (s.find('f') if s.count('f') == 1 else 'NO')) 
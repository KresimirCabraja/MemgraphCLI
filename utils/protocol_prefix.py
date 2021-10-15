def check_protocol(item: str) -> bool:
    if item is None:
        return False
    if item.startswith(('http', 'https')):
        return True
    return False


def add_https(argument: str) -> str:
    if not argument.startswith('https://'):
        return 'https://' + argument
    return argument

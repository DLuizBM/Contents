def eat(food, is_healhy):
    if is_healhy:
        return f"Estou comendo {food} porque é saudável."
    else:
        return f"Estou comendo {food}, pois só se vive uma vez."

def sleep(hours):
    if hours > 8:
        return f"Dormi demais."
    else:
        return f"Dormi muito pouco."


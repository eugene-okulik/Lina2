def repeat_me(func=None, *, count=None):
    def decorator(f):
        def wrapper(text, **kwargs):
            local_count = count or kwargs.pop("count", 1)
            for _ in range(local_count):
                f(text, **kwargs)

        return wrapper

    if func is not None and callable(func):
        return decorator(func)
    return decorator


@repeat_me
def example(text):
    print(text)


example("print me", count=2)

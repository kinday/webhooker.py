from operator import or_


# any_pass :: (fn -> [*]) -> boolean
# Returns True if any iterable item returns true when passed to fn
def any_pass(fn, iterable):
    return reduce(lambda passed, a: or_(passed, fn(a)), iterable, False)


# path :: ([string] -> dict) -> *
# Gets deep value from dict
def path(keys, dict_):
    return reduce(
        lambda v, k: v and isinstance(v, dict) and v.get(k) or None,
        keys,
        dict_
    )

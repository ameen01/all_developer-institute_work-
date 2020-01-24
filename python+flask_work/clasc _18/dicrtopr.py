import time as t


def long_with(secend):
    def timeer(f):
        def new_f(*args, **kwargs):
            t.sleep(secend)
            rus = f(*args, **kwargs)
            return rus
        return new_f
    return timeer


@long_with(1)
def halo_world():
    print('haloo ameen')


long_with(2)
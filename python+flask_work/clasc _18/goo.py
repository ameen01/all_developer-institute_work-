

def hallo_wolrd(f):
    def new_hallo():
        print("the fuction", f.__name__)
        f()
    return new_hallo


@hallo_wolrd
def hallo():
    print('halowol ameen')


hallo()

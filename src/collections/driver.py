from . import Collection

def main():
    # instantiate calculators
    c1 = Collection([1, 2, 3])
    c2 = Collection(["a", "b", "c"])
    # 
    if (id(c1) == id(c2)):
        print("same Collections instance: c1==c2")
    else:
        print("different Collections instances: c1 != c2")
    # 
    # print(f'{next()}: c1.add(1, 2)\t-> {c1.add(1, 2)}')
    # print(f'{next()}: c2.add(8, 3)\t-> {c2.add(8, 3)}')

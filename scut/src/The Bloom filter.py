class B:
    def __init__(s, n, h):
        s.s = n
        s.b = [0] * n
        s.h = h

    def a(s, x):
        for f in s.h:
            i = f(x) % s.s
            s.b[i] = 1

    def __contains__(s, x):
        for f in s.h:
            i = f(x) % s.s
            if s.b[i] == 0:
                return False
        return True

# create a Bloom filter of 
# size 100 with two hash functions.

b = B(100, [hash, hash])

# add items
b.a("s1")
b.a("s2")

# check membership
print("Is 's1' in the filter?", "s1" in b)
print("Is 's3' in the filter?", "s3" in b)

# Output:
# Is 's1' in the filter? True
# Is 's3' in the filter? False

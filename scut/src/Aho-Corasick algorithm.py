class T:
    def __init__(s):
        s.c = {}
        s.o = []

def b(p):
    r = T()
    for x in p:
        n = r
        for y in x:
            if y not in n.c:
                n.c[y] = T()
            n = n.c[y]
        n.o.append(x)
    return r

def a(t, r):
    z = []
    n = r
    for i, y in enumerate(t):
        while y not in n.c and n != r:
            n = n.f
        if y in n.c:
            n = n.c[y]
            for x in n.o:
                z.append((i - len(x) + 1, x))
    return z

def f(r):
    q = []
    for n in r.c.values():
        n.f = r
        q.append(n)
    while q:
        m = q.pop(0)
        for y, k in m.c.items():
            q.append(k)
            s = m.f
            while y not in s.c and s != r:
                s = s.f
            k.f = s.c.get(y, r)

if __name__ == "__main__":
    p = ["s1", "s2", "s3", "s4"]
    t = "IAs3mAfile"

    r = b(p)
    f(r)
    z = a(t, r)

    if z:
        print("Found patterns:")
        for i, x in z:
            print(f"Pattern '{x}' found at position {i}")
    else:
        print("No patterns found.")

# Output:
# Found patterns:
# Pattern 's3' found at position 2
#
# References
# Paul A. Gagniuc. Antivirus Engines: From Methods to Innovations, Design, and Applications. Cambridge, MA: Elsevier Syngress, 2024. pp. 1-656.

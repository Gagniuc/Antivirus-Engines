class H:
    def __init__(s, n):
        s.n = n
        s.t = [[] for _ in range(n)]

    def _h(s, k):
        return hash(k) % s.n

    def i(s, k, v):
        idx = s._h(k)
        s.t[idx].append((k, v))

    def f(s, k):
        idx = s._h(k)
        for x, y in s.t[idx]:
            if x == k:
                return y
        return None

# create a hash table and insert some key-value pairs:
h = H(n=10)
h.i("d41d8cd98f00b204e9800998ecf8427e", "Trojan")
h.i("098f6bcd4621d373cade4e832627b4f6", "Rootkit")
h.i("1f0e3dad99908345f7439f8ffabdffc4", "Bootkit")

# search for values using keys:
print(h.f("d41d8cd98f00b204e9800998ecf8427e"))
print(h.f("098f6bcd4621d373cade4e832627b4f6"))
print(h.f("1f0e3dad99908345f7439f8ffabdffc4"))
print(h.f("c4ca4238a0b923820dcc509a6f75849b"))


# Output:
#
# Trojan
# Rootkit
# Bootkit
# None
#
# References
# Paul A. Gagniuc. Antivirus Engines: From Methods to Innovations, Design, and Applications. Cambridge, MA: Elsevier Syngress, 2024. pp. 1-656.

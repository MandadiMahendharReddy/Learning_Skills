import time

# Create big list and set
big_list = list(range(1_000_000))
big_set = set(big_list)

# Lookup value not present (worst case)
start = time.time()
9999999 in big_list
print("List lookup time:", time.time() - start)

start = time.time()
9999999 in big_set
print("Set lookup time:", time.time() - start)

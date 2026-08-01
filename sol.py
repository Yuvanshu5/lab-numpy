import numpy as np

# 1. Import NumPy under the name np.

# 2. Print your NumPy version.
print("NumPy version:", np.__version__)

# 3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable a.
method1 = np.random.rand(2, 3, 5)
method2 = np.random.random((2, 3, 5))
method3 = np.random.uniform(0, 1, (2, 3, 5))
a = method1

# 4. Print a.
print("\na:")
print(a)

# 5. Create a 5x2x3 3-dimensional array with all values equaling 1. Assign the array to variable b.
b = np.ones((5, 2, 3))

# 6. Print b.
print("\nb:")
print(b)

# 7. Do a and b have the same size? How do you prove that in Python code?
print("\nSame size?", a.size == b.size)
print("a.size:", a.size, "b.size:", b.size)

# 8. Are you able to add a and b? Why or why not?
try:
    _ = a + b
    add_possible = True
except ValueError as err:
    add_possible = False
    add_error = err

print("\nCan add a and b?", add_possible)
if not add_possible:
    print("Reason:", add_error)

# 9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to variable c.
c = np.transpose(b, (1, 2, 0))
print("\nc.shape:", c.shape)

# 10. Try to add a and c. Now it should work. Assign the sum to variable d. But why does it work now?
d = a + c
print("\nd:")
print(d)
print("\nWhy it works: a and c now have the same shape, so elementwise addition is valid.")

# 11. Print a and d. Notice the difference and relation of the two arrays in terms of the values? Explain.
print("\na:")
print(a)
print("\nd:")
print(d)
print("\nExplanation: d equals a plus 1 everywhere because c is an array of ones.")

# 12. Multiply a and c. Assign the result to e.
e = a * c
print("\ne equals a?", np.allclose(e, a))

# 13. Does e equal to a? Why or why not?
print("\nExplanation: e equals a because multiplying by an array of ones leaves the values unchanged.")

# 14. Identify the max, min, and mean values in d. Assign those values to variables d_max, d_min and d_mean.
d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print("\nd_max:", d_max)
print("d_min:", d_min)
print("d_mean:", d_mean)

# 15. Now we want to label the values in d. First create an empty array f with the same shape as d using np.empty.
f = np.empty(d.shape)

# 16. Populate the values in f.
mask_min = d == d_min
mask_max = d == d_max
mask_mean = d == d_mean
mask_between_min_mean = (d > d_min) & (d < d_mean)
mask_between_mean_max = (d > d_mean) & (d < d_max)

f[mask_between_min_mean] = 25
f[mask_between_mean_max] = 75
f[mask_mean] = 50
f[mask_min] = 0
f[mask_max] = 100

# 17. Print d and f. Do you have your expected f?
print("\nd:")
print(d)
print("\nf:")
print(f)

# 18. Bonus question: instead of using numbers, use string values (A,B,C,D,E) to label the array elements.
g = np.empty(d.shape, dtype='<U1')
g[mask_between_min_mean] = 'B'
g[mask_between_mean_max] = 'D'
g[mask_mean] = 'C'
g[mask_min] = 'A'
g[mask_max] = 'E'

print("\ng:")
print(g)

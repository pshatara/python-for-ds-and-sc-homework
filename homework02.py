import numpy as np

# 1. Include	a	section	with	your	name	
# Peter Shatara

# 2. Create	matrix	A	with	size	(3,5)	containing	random	numbers	A	=	np.random.random(15)
A = np.array([np.random.random(5), np.random.random(5), np.random.random(5)])
print("3x5 Numpy Array:\n", A)

# 3. Find	the	size	and	length	of	matrix	A	
print("Size: ", A.size)
print("Length: ", A.shape)

# 4. Resize	(crop/slice)	matrix	A	to	size	(3,4)	
A = np.resize(A, (3, 4))
print("3x4 Numpy Array:\n", A)

# 5. Find	the	transpose	of	matrix	A	and	assign	it	to	B	
B = np.transpose(A)
print("B (A Transpose):\n", B)

# 6. Find	the	minimum	value	in	column	1	of	matrix	B	(check	the	properties	of	a	matrix	–	‘B.min()’)	
# Unclear if column 1 refers to first column (index 0), or second (index 1)
print("Minimum Value in Frist Column of B: ", np.amin(B, 0)[0])


# 7. Find	the	minimum	and	maximum	values	for	the	entire	matrix	A	
print("Minimum Value of Matrix A: ", A.min())
print("Maximum Value of Matrix A: ", A.max())

# 8. Create	vector	X	(an	array)	with	4	random	numbers	
X = np.random.random(4)
print("Vector X: ", X)

# 9. Create	a	function	and	pass	vector	X	and	matrix	A	in	it	
# 10. In	the	new	function	multiply	vector	X	with	matrix	A	and	assign	the	result	to	D	
def matrix_multiply(a, b):
    return np.multiply(X, A)

D = matrix_multiply(X, A)
print("Product of X and A:\n", D)

# 11. Create	a	complex	number	Z	with	absolute	and	real	parts	!=	0	
Z = np.complex(1, 2)
print("Complex Number Z: ", Z)

# 12. Show	its	real	and	imaginary	parts	as	well	as	it’s	absolute	value	
print("Z Real Part: ", np.real(Z))
print("Z Imaginary Part: ", np.imag(Z))
print("Z Absolute Value: ", np.abs(Z))

# 13. Multiply	result	D	with	the	absolute	value	of	Z	and	record	it	to	C	
C = matrix_multiply(D, Z)
print("Product of D and Z (C):\n", C)

# 14. Convert	matrix	B	from	a	matrix	to	a	string	and	overwrite	B	
B = np.array_str(B)
print("B String:\n", B)

# 15. Display	a	text	on	the	screen:	‘Your Name	is	done	with	HW2‘	
print("Peter Shatara is done with HW2")

# 16. Organize	your	code:	use	each	line	from	this	assignment	as	a	comment	line	before	each	step	
# Done

# 17. Save	all	steps	as	a	script	in	a	.py	file	
# Done

# 18. Email	your	Github	link	to	me	including	your	.py	file	+	screenshots	of	your running code no	later than	midnight	on	Saturday	Jun.09.
# Done
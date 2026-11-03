import numpy as np
import math
def compute_partial_derivatives(func_name: str, point: tuple[float, ...]) -> tuple[float, ...]:
	"""
	Compute partial derivatives of multivariable functions.
	
	Args:
		func_name: Function identifier
			'poly2d': f(x,y) = x²y + xy²
			'exp_sum': f(x,y) = e^(x+y)
			'product_sin': f(x,y) = x·sin(y)
			'poly3d': f(x,y,z) = x²y + yz²
			'squared_error': f(x,y) = (x-y)²
		point: Point (x, y) or (x, y, z) at which to evaluate
	
	Returns:
		Tuple of partial derivatives (∂f/∂x, ∂f/∂y, ...) at point
	"""
	# Your code here
	
	if func_name == 'poly2d':
		x, y = point
		d_x = 2* x *y + y**2
		d_y = x ** 2 + 2*y*x
		return (float(d_x), float(d_y))
	elif func_name == "exp_sum":
		x, y = point
		d_ = np.exp(x + y)
		return (float(d_), float(d_))
	elif func_name == "product_sin":
		x, y = point
		d_x = math.sin(y)
		d_y = x * math.cos(y)
		return (float(d_x), float(d_y))
	elif func_name == 'poly3d':
		x, y, z = point
		d_x = 2 * x * y
		d_y = x**2 + z**2
		d_z = 2 * y * z
		return (float(d_x), float(d_y), float(d_z))
	else:
		x, y = point

		d_x = 2 * (x - y)
		d_y = -2 * (x - y)

		return (float(d_x), float(d_y))
		


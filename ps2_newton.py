# Problem set 2
# Name: Vaishnavi Mittal
# Time spent:1:30:00

def evaluate_poly(poly,x):
    answer=0
    for i in range(0,len(poly)):
        answer+= poly[i] *x**i
    return answer

poly=(0.0, 0.0, 5.0, 9.3, 7.0)
x=-13
print(evaluate_poly(poly,x)) 


def compute_deriv(poly):
    answer=()
    for i in range(1,len(poly)):
        answer+=(poly[i]*(i),)
    return answer

poly=(-13.39, 0.0, 17.5, 3.0, 1.0)
print(compute_deriv(poly))


def compute_root(poly, x_0, epsilon):
    c= x_0
    iterations=1
    while(abs(evaluate_poly(poly,c))>epsilon):
        a=evaluate_poly(poly,c)
        b=evaluate_poly(compute_deriv(poly), c)
        c=(c- a/b)
        iterations=iterations + 1
    return(c,iterations)

poly=(-13.39, 0.0, 17.5, 3.0, 1.0)
x_0=0.1
epsilon=.0001
print(compute_root(poly, x_0, epsilon))
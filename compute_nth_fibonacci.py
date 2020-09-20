
def power(M, p):

    if p == 1:
        return M

    half = power(M, p//2)

    if p % 2:
        return mat_mat_mul(mat_mat_mul(half, half), M)
    else:
        return mat_mat_mul(half, half)


def mat_mat_mul(M1, M2):
    m11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
    m12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
    m21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
    m22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
    return [[m11, m12], [m21, m22]]


def mat_vec_mul(M, v):
    v1 = M[0][0]*v[0] + M[0][1]*v[1]
    v2 = M[1][0]*v[0] + M[1][1]*v[1]
    return [v1, v2]


def fib(n):

    if n < 0:
        raise ValueError('Index must be positive')

    if n == 0:
        return 0

    if n == 1:
        return 1

    M = [[1, 1], [1, 0]]

    vec = mat_vec_mul(power(M, n - 1), [1, 0])

    # Compute the nth Fibonacci number

    return vec[0]

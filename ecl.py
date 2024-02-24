def euclidian(m, b):
    A1, A2, A3 = 1, 0, m
    B1, B2, B3 = 0, 1, b
    while True:
        if B3 == 0:
            A3 = PGCD(m,b)
            print("pas divisible")
            return A1, A2, A3 
        elif B3 == 1:
            B3 = PGCD(m,b)
            return  B2   
        Q = A3 // B3
        T1, T2, T3 = (A1 - Q * B1), (A2 - Q * B2), (A3 - Q * B3)
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3

def PGCD(a, b):
    while b:
        a, b = b, a % b
    return a

b = euclidian(26, 7)
try:
    print("Result: ", b % 26)
except Exception as Err:
    pass
def binomial_coefficient(n, k):
    bc = [[0] * 100 for i in range(100)]
    for i in range(n+1):
        bc[i][0] = 1 #base condition:= choose 0 things out of n things = 1
    for j in range(n+1):
        bc[j][j] = 1 #base condition:= choose k things out of k things = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            bc[i][j] = bc[i-1][j-1] + bc[i-1][j] #nCk = (n-1)C(k-1) + (n-1)Ck

    return bc[n][k] 

def main():
    print("Enter the value of n and k for nCk") 
    n = int(input())
    k = int(input())
    res = binomial_coefficient(n, k) 
    print(res) 

if __name__ == "__main__":
    main()
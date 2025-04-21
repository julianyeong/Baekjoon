# def divisor(n):
#     div = []
#     for i in range(1, n+1):
#         if n%i == 0:
#             div.append(i)
#     return div

# def solution(numer1, denom1, numer2, denom2):
#     numer3 = numer1*denom2 + numer2*denom1
#     denom3 = denom1*denom2
    
#     divi = []
#     divi = divisor(denom3)
    
#     for i in range(len(divi)):
#         if numer3%divi[i] == 0:
#             numer3 = numer3//divi[i]
#             denom3 = denom3//divi[i]
            
#     return [numer3, denom3]

from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numer3 = numer1*denom2 + numer2*denom1
    denom3 = denom1*denom2
    
    gcdd = gcd(numer3, denom3)
    return [numer3//gcdd, denom3//gcdd]
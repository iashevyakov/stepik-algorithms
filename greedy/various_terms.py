"""
https://stepik.org/lesson/13238/step/11?unit=3424
"""
def various_terms(n: int):
    current_term = 1
    terms_sum = current_term
    terms = [current_term]
    while terms_sum <= n:
        current_term += 1
        terms_sum += current_term
        terms.append(current_term)
    terms[-2] += n - (terms_sum - terms[-1])
    terms.pop()
    return terms


if __name__ == "__main__":
    n = int(input())
    terms = various_terms(n)
    print(len(terms))
    print(*terms)
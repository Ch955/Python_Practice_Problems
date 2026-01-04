if __name__ == "__main__":
    n,m = map(int, input().split(" "))
    a, b = [], []
    for _ in range(n): a.append(input())
    for _ in range(m): b.append(input())
    
    for b_word in b:
        indices = [i+1 for i,word in enumerate(a) if word == b_word]
        print(" ".join(map(str, indices))) if indices else print(-1)
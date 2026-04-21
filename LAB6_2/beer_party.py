def solve_beers(n, b, s):
    s = s.replace(" ", "").replace("\n", "")
    
    masks = [0] * b
    for i in range(n):
        for j in range(b):
            if s[i * b + j] == 'Y':
                masks[j] |= (1 << i)

    masks.sort(key=lambda x: bin(x).count('1'), reverse=True)
    target = (1 << n) - 1
    ans = b

    def dfs(idx, mask, count):
        nonlocal ans
        if count >= ans:
            return
        if mask == target:
            ans = count
            return
        if idx == b:
            return

        if (mask | masks[idx]) != mask:
            dfs(idx + 1, mask | masks[idx], count + 1)
        
        dfs(idx + 1, mask, count)

    dfs(0, 0, 0)
    return ans
import sys

def isPalindrome(candidate, s_idx, e_idx, isFirstDepth):
    result = 0
    
    while(s_idx<e_idx):
        if candidate[s_idx] == candidate[e_idx] :
            s_idx += 1
            e_idx -= 1
        elif isFirstDepth:
            result = isPalindrome(candidate, s_idx+1, e_idx, False)
            if result == 2:
                result = isPalindrome(candidate, s_idx, e_idx-1, False)
            
            if result == 0:  
                result = 1
            
            break;
        else:
            result = 2
            break
          
    return result



n = int(input().rstrip())
answer = []

for _ in range(n):
    candidate = list(input().rstrip())
    
    idx = [0, len(candidate)-1];
    result = isPalindrome(candidate, idx[0], idx[1], True);
    answer.append(result)

print("\n".join(map(str,answer)))
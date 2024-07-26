class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False 
        if(x>=0 and x<10):
            return True 
        temp=x
        k=0
        while(temp>0):
            k = (k*10)+temp%10
            temp = temp//10
        
        return (k==x)
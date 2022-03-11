class UserMainCode(object):
    @classmethod
    def palindrome(cls, input1):
        print(1) if input1 == input1[::-1] else print(0)

obj = UserMainCode()
obj.palindrome(input())

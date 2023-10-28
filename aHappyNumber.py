class Solution:
    def sum_of_square(self, n: int) -> int:
        sum = 0
        while n > 0:
            lastDigit = n % 10
            sum += lastDigit ** 2
            n = n // 10

        return sum

    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        slow = n
        fast = n

        while True:
            slow = self.sum_of_square(slow)
            fast = self.sum_of_square(self.sum_of_square(fast))

            if (slow == fast):
                break

        return n == 1
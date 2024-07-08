class Solution:
    @staticmethod
    def num_bottles(num_bottles: int, num_exchange: int) -> int:
        answer = 0
        bottles = num_bottles
        remain = 0
        while bottles:
            answer += bottles
            remain += bottles
            bottles = remain // num_exchange
            remain %= num_exchange
        return answer

class Solution:
    def maximumPopulation(self, logs):
        START = 1950
        END = 2050

        diff = [0] * (END - START + 1)

        for birth, death in logs:
            diff[birth - START] += 1
            diff[death - START] -= 1

        max_population = 0
        curr_population = 0
        answer = START

        # prefix sum
        for i in range(len(diff)):
            curr_population += diff[i]

            if curr_population > max_population:
                max_population = curr_population
                answer = START + i
        
        return answer



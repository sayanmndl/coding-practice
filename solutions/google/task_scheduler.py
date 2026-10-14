from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)

        max_freq = task_counts.most_common(1)[0][1]

        num_max_freq_tasks = sum(
            1
            for count in task_counts.values()
            if count == max_freq
        )

        min_time = max(
            len(tasks),
            (max_freq - 1) * (n + 1) + num_max_freq_tasks
        )

        return min_time
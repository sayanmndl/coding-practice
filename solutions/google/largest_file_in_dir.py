import heapq
import os

def get_top_5_largest_files(path):
    top5 = []

    def dfs(curr_path):
        try:
            entries = list_dir(curr_path)
        except Exception as e:
            size = size_of(curr_path)

            if len(top5) < 5:
                heapq.heappush(top5, (size, curr_path))
            elif size > top5[0][0]:
                heapq.heapreplace(top5, (size, curr_path))
            
            return
        
        if not entries:
            size = size_of(curr_path)

            if size != -1:
                if len(top5) < 5:
                    heapq.heappush(top5, (size, curr_path))
                elif size > top5[0][0]:
                    heapq.heapreplace(top5, (size, curr_path))

            return

        for name in entries:
            child_path = os.path.join(curr_path, name)
            dfs(child_path)

    dfs(path)

    return sorted(top5, reverse=True)
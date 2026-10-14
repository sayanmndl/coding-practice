class UploadTracker:
    def __init__(self):
        self.next_missing = 0
        self.acked = set()

    def init(self, nextChunk):
        self.next_missing = nextChunk
        self.acked.clear()

    def ack(self, chunkNumber):
        if chunkNumber < self.next_missing:
            return
        self.acked.add(chunkNumber)

        while self.next_missing in self.acked:
            self.acked.remove(self.next_missing)
            self.next_missing += 1

    def lastUploadedChunk(self):
        return self.next_missing


tracker = UploadTracker()

tracker.init(5)

tracker.ack(7)
tracker.ack(6)

tracker.lastUploadedChunk()
# 5

tracker.ack(5)

tracker.lastUploadedChunk()
# 8
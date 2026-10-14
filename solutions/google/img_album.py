class Gallery:
    def __init__(self, allImages, markedFavorites):
        self.allImages = allImages
        self.favorites = markedFavorites
        self.favourite_set = set(markedFavorites)
        self.fav_idx = 0
        self.all_idx = 0

    def getNext(self):
        if self.fav_idx < len(self.favorites):
            image = self.favorites[self.fav_idx]
            self.fav_idx+=1
            return image
        
        while self.all_idx < len(self.allImages):
            image = self.allImages[self.all_idx]
            self.all_idx += 1

            if image not in self.favourite_set:
                return image
        return None

gallery = Gallery(
    ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10"],
    ["i2", "i5", "i7"]
)

while True:
    image = gallery.getNext()

    if image is None:
        break

    print(image)
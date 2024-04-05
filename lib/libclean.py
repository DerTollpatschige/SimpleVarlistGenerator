class LibClean:
    _collection = set()

    def collector(self, val):
        self._collection.add(val)

    def removeduplicates(self, collection):
        cleanedcollection = list(set(collection))

        return cleanedcollection

    def getcollection(self):
        return list(self._collection)

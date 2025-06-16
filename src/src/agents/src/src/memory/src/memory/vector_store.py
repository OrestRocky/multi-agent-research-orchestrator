class VectorMemory:
    def __init__(self):
        self.storage = {}

    def store(self, key: str, value: str):
        print(f"[MEMORY] Storing data under key: {key}")
        self.storage[key] = value

    def retrieve(self, key: str):
        print(f"[MEMORY] Retrieving data for key: {key}")
        return self.storage.get(key, None)

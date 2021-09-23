class DUID:
    """Deterministic Unique IDentifier"""
    __next_uid = 0
    def __init__(self):
        self.duid = DUID.__next_uid
        DUID.__next_uid += 1

import uuid


class UUIDManager():
    def get_new():
        return str(uuid.uuid4())[:8]

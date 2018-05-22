import uuid

class Identifier():
    def get_new():
        return str(uuid.uuid4())[:8]
        # return 1
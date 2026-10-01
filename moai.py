class Moai:
    def __init__(self, moai_id):
        self.id = moai_id
        self.alive = True

    def destroy(self):
        self.alive = False

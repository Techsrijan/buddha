class Sabkabap:
    def __init__(self):
        print("Sabka constructor")
class Room(Sabkabap):
    def __init__(self):
        super().__init__()
        print("Room constructor")

class GustRoom(Room):

    def __init__(self):
        super().__init__()
        print("GuestRoom coonstructor")

g=GustRoom()
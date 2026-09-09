class Event:
    def __init__(self, event_name):
        self.event_name = event_name
        self.participants = []

    def register_new_member(self, member_name, ms):
        self.participants.append(member_name)
        ms.add_member(member_name)

    def sign_up(self, member_name, ms):
        if ms.has_member(member_name):
            self.participants.append(member_name)

        #if member_name in ms.get_members():    #Varför fungerar inte detta? TypeError: argument of type 'Mock' is not a container or iterable
            #self.participants.append(member_name)

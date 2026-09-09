class MemberService:
    def __init__(self):
        self.member_list = []

    def add_member(self, member_name):
        self.member_list.append(member_name)

    def get_members(self):
        return self.member_list

    def has_member(self, member_name):
        if member_name in self.member_list:
            return True
        else:
            return False

import re


class Sender:
    # prefix     =  servername / ( nickname [ [ "!" user ] "@" host ] )
    def __init__(self, sender: str):
        self.full = sender
        self.nick = ""
        self.ident = ""
        self.host = ""
        end = sender.find("!")
        if end == -1:
            end = len(sender)
        self.nick = sender[0:end]
        sender = sender[len(self.nick):]
        if "!" in sender:
            end = sender.find("@")
            if end == -1:
                end = len(sender)
            self.ident = sender[1:end]
            sender = sender[len(self.ident)+1:]
        if "@" in sender:
            self.host = sender[1:]

    # for now just do a tolower idc about server's casemapping

    def nick_equals(self, nick: str) -> bool:
        return self.nick.lower() == nick.lower()

    def ident_equals(self, ident):
        return self.ident.lower() == ident.lower()

    def __str__(self):
        return self.full

    def hostmask_match(self, mask: str) -> bool:
        maskb = ""
        # this might be silly
        for c in mask:
            if c == "*":
                maskb += ".*"
            elif c == "?":
                maskb += "."
            else:
                if c.isalnum():
                    maskb += c
                else:
                    maskb += "\\" + c
        m = re.fullmatch(maskb, self.full, flags=re.IGNORECASE)
        if m is not None:
            return True
        return False

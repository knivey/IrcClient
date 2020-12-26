from Sender import Sender

class Message:
    def __init__(self, line: str):
        self.line = line
        self.command = ""
        self.sender = None
        self.params = []
        if line == "":
            return
        if line[0] == ':':
            line = line[1:]
            words = line.split(maxsplit=1)
            self.sender = Sender(words.pop(0))
            if len(words) == 0:
                # this is actually a malformed message
                return
            line = words[0]
        words = line.split(maxsplit=1)
        self.command = words.pop(0)
        if len(words) == 0:
            return
        # want to preserve whitespace in :params
        words = words[0].split(" ")
        while len(words) > 0:
            if not words[0]:
                words.pop(0)
                continue
            if words[0][0] == ":":
                self.params.append(" ".join(words)[1:])
                break
            else:
                self.params.append(words.pop(0))


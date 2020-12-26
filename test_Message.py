from Message import Message
# from Sender import Sender


def test_just_cmd():
    m = Message("PING")
    assert m.command == "PING"
    assert m.sender is None
    assert not m.params

def test_just_cmd_with_args():
    m = Message("PING :1234")
    assert m.command == "PING"
    assert m.sender is None
    assert m.params == ['1234']
    m = Message("NOTICE AUTH :*** No ident response")
    assert m.command == "NOTICE"
    assert m.params == ["AUTH", "*** No ident response"]

def test_cmd_withprefix():
    m = Message(":Portlane.SE.EU.GameSurge.net 001 grape :Welcome to the GameSurge IRC Network via portlane.se, grape")
    assert m.command == "001"
    assert str(m.sender) == "Portlane.SE.EU.GameSurge.net"
    assert m.params == ["grape", "Welcome to the GameSurge IRC Network via portlane.se, grape"]
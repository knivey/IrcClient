from Sender import Sender


def test_server():
    # Message class should process leading :
    s = "Prothid.CA.US.GameSurge.net"
    sender = Sender(s)
    assert sender.full == s
    assert sender.host == ""
    assert sender.nick == s
    assert sender.ident == ""

def test_chatter():
    s = "Bruk!~Bruk@Bruk_.user.gamesurge"
    sender = Sender(s)
    assert sender.full == s
    assert sender.nick == "Bruk"
    assert sender.ident == "~Bruk"
    assert sender.host == "Bruk_.user.gamesurge"

    sender = Sender("knivey")
    assert sender.full == "knivey"
    assert sender.nick == "knivey"
    assert sender.ident == ""
    assert sender.host == ""

    sender = Sender("foo!bar")
    assert sender.nick == "foo"
    assert sender.ident == "bar"
    assert sender.host == ""

def test_comparisons():
    s = "Bruk!~Bruk@Bruk_.user.gamesurge"
    sender = Sender(s)
    assert sender.nick_equals("BRUK")
    assert sender.nick_equals("Bruk")
    assert sender.ident_equals("~BRUk")

def test_stringer():
    s = "Bruk!~Bruk@Bruk_.user.gamesurge"
    sender = Sender(s)
    assert str(sender) == s

def test_mask():
    s = "Bruk!~Bruk@Bruk_.user.gamesurge"
    sender = Sender(s)
    assert sender.hostmask_match("*!*@*")
    assert sender.hostmask_match("*!?*@*")
    assert sender.hostmask_match("*")
    assert sender.hostmask_match("*!?bruk@*")
    assert False == sender.hostmask_match("*!?bruk@*k")

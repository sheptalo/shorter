from domain import Link


def test_generate_uid():
    link = Link(link="https://www.google.com")
    link.generate_uid("BBBB")
    assert link.uid == "BBBC"

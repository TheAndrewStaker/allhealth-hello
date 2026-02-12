from core.app.greet import make_greeting
from hypothesis import given, strategies as st

def test_default_is_world():
    assert make_greeting().message == "Hello, world!"

@given(st.text())
def test_never_returns_empty_message(name):
    message = make_greeting(name).message
    assert message.startswith("Hello, ")
    assert message.endswith("!")

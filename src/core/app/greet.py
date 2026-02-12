from core.domain.greeting import Greeting

def make_greeting(name: str | None = None) -> Greeting:
    name = name or "world"
    return Greeting(message=f"Hello, {name}!")

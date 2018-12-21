import behave
from parse_type import TypeBuilder
import parse

class Roles:
    Button = "button"
    Item = "item"
    Page = "page"
    List = "list"

class Actions:
    Press = "press"
    ScrollUp = "scroll up"
    ScrollDown = "scroll down"

class States:
    Visible = "visible"
    Showing = "showing"


def get_property_values(target):
    values = []
    for i in dir(target):
        value = getattr(target, i)
        if isinstance(value, str):
            values.append(value)
    return values

behave.register_type(Role=TypeBuilder.make_choice(get_property_values(Roles)))
behave.register_type(Action=TypeBuilder.make_choice(get_property_values(Actions)))
behave.register_type(State=TypeBuilder.make_choice(get_property_values(States)))

@parse.with_pattern(r"\s*\"[^\"]+\"\s*")
def parse_name(text: str):
    return text.strip(" \t\n\r\"")
behave.register_type(Name=parse_name)
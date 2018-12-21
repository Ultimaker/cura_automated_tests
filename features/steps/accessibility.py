from behave import *
import impl

use_step_matcher("cfparse")

@given("{parent:Name} contains {role:Role?}{child:Name}")
def step_impl(context, parent, role, child):
    parent_obj = impl.find_object(object_name = parent)
    assert parent_obj, "{} not found".format(parent)

    child_obj = impl.find_object(search_in = parent_obj, object_name = child, object_type = role)
    assert child_obj, "{} does not contain {}".format(parent, child)


@when("we {action:Action} the {role:Role?}{name:Name}")
def step_impl(context, action, name, role):
    obj = impl.find_object(object_type = role, object_name = name)
    assert obj, "{} named {} not found".format(role if role else "anything", name)

    assert impl.has_action(obj, action), "{} named {} does not have an action {}".format(role if role else "anything", name, action)
    impl.perform_action(obj, action)

@when("we scroll the {list_role:Role?}{list_name:Name} to the {target_role:Role?}{target:Name}")
def step_impl(context, list_role, list_name, target_role, target):
    list_obj = impl.find_object(object_type = list_role, object_name = list_name)
    assert list_obj, "{} {} not found".format(list_role, list_name)
    assert impl.has_action(list_obj, "scroll down"), "{} {} does not have a scroll down action".format(list_role, list_name)

    attempts = 100
    target_obj = impl.find_object(object_type = target_role, object_name = target)
    while not target_obj and attempts > 0:
        attempts -= 1
        impl.perform_action(list_obj, "scroll down")
        target_obj = impl.find_object(object_type = target_role, object_name = target)

    assert target_obj, "{} {} not found".format(target_role, target)

@then("{parent:Name} should contain {role:Role?}{child:Name}")
def step_impl(context, parent, role, child):
    parent_obj = impl.find_object(object_name = parent)
    assert parent_obj, "{} not found".format(parent)

    child_obj = impl.find_object(search_in = parent_obj, object_name = child, object_type = role)
    assert child_obj, "{} does not contain {}".format(parent, child)

@then("it should be possible to {action:Action} {role:Role?}{name:Name}")
def step_impl(context, action, role, name):
    obj = impl.find_object(object_name = name, object_type = role)
    assert obj, "{} {} not found".format(role, name)

    assert impl.has_action(obj, action), "{} {} does not have an action {}".format(role, name, action)

@then("{role:Role?}{name:Name} should be {state:State}")
def step_impl(context, role, name, state):
    obj = impl.find_object(object_name = name, object_type = role)
    assert obj, "{} {} not found".format(role, name)

    assert impl.has_state(obj, state), "{} {} does not have state {}".format(role, name, state)
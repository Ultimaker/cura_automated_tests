from pywinauto.application import Application
from pywinauto import Desktop

# from .types import Roles, States, Actions

# role_map = {
#     Roles.Button: "push button",
#     Roles.Item: "list item",
#     Roles.Page: "page tab",
#     Roles.List: "list",
# }

# state_map = {
#     States.Showing: pyatspi.STATE_SHOWING,
#     States.Visible: pyatspi.STATE_VISIBLE
# }

# action_map = {
#     Actions.Press: "press",
#     Actions.ScrollUp: "scroll up",
#     Actions.ScrollDown: "scroll down",
# }

def start_application(application_path):
    app = Application(backend = "uia")
    app.start(application_path)

    return app

def stop_application(application):
    application.terminate()
    application.wait(10)

def find_main_window(name, wait = True):
    desktop = Desktop()
    main_window = desktop.window(best_match = name)

    if wait:
        main_window.wait("visible")

    main_window.print_control_identifiers()

    return main_window

def find_object(*, search_in = None, object_type = None, object_name = None):
    retval = None

    obj = search_in
    if not obj:
        obj = find_main_window("Ultimaker Cura")

    if not obj:
        return None

    # for item in obj:
    #     retval = find_object(search_in = item, object_type = object_type, object_name = object_name)
    #     if retval:
    #         return retval
    #
    #     if object_type:
    #         mapped_type = role_map.get(object_type.lower(), "unknown")
    #         if mapped_type != item.getRoleName().lower():
    #             continue
    #
    #     if object_name:
    #         match_name = object_name.lower()
    #         item_name = item.name.lower()
    #         if item_name != match_name:
    #             continue
    #
    #     return item

    return None

def has_action(obj, action):
    actions = obj.queryAction()
    if not actions:
        return False

    for i in range(actions.nActions):
        if actions.getName(i).lower() == action.lower():
            return True

    return False

def perform_action(obj, action):
    actions = obj.queryAction()
    for i in range(actions.nActions):
        if actions.getName(i).lower() == action.lower():
            return actions.doAction(i)

    return False

# def has_state(obj, state):
#     state_set = obj.getState()
#
#     if state_set.isEmpty():
#         return False
#
#     if state not in state_map:
#         return False
#
#     return state_map[state] in state_set.getStates()
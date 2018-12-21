import sys

# This file exposes a minimal abstraction around platform specific accessibility
# APIs.
#
# The following functions are expected to exist:
#
# def start_application(args: list[str], wait_for_message: str): Process
#
# def stop_application(application: Process): None
#
# def find_main_window(name: str): Application object
#
# def find_object(*, search_in: str, object_type: str, object_name: str) : Accessibility object
#
# def has_action(object: Accessibility object, action: str): bool
#
# def perform_action(object: Accessibility object, action: str): bool
#
# def has_state(object: Accessibility object, state: str): bool
#

from . import types

if sys.platform == "win32":
    from .atspi import start_application, stop_application, find_main_window, find_object, has_action, perform_action, has_state
else:
    raise NotImplementedError("Platform {} is not supported yet".format(sys.platform))
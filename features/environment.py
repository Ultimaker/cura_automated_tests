from behave import *

import impl

@fixture
def application(context):
    application_to_test = "python.exe cura_app.py"

    context.process = impl.start_application(application_to_test)

    yield context.process

    impl.stop_application(context.process)

def before_feature(context, feature):
    use_fixture(application, context)
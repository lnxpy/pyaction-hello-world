from pyaction import PyAction


workflow = PyAction()


@workflow.action
def my_action(name: str) -> None:
    workflow.write(
        {
            "phrase": f"Hi {name}!"
        }
    )

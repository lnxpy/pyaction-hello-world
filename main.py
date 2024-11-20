from pyaction import PyAction
from pyaction.workflow.stream import WorkflowContext

workflow = PyAction()


@workflow.action
def my_action(name: str) -> None:
    context = WorkflowContext(
        {
            "phrase": f"Hi {name}!",
        }
    )
    workflow.write(context)

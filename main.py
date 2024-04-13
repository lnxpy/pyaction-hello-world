import sys
from typing import List

from pyaction.auth import Auth
from pyaction.issues import IssueForm

from pyaction import io

import logging


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    token = io.read("github_token")
    auth = Auth(token=token)
    auth.authenticate()

    repo = auth.github.get_repo(io.read("repository"))
    user_input = IssueForm(repo=repo, number=int(io.read("issue_number"))).render()

    logging.error(token, "pyaction")
    logging.error(f"{token} | {len(token)}", "pyaction")
    logging.error(repo, "pyaction")
    logging.error(user_input, "pyaction")


if __name__ == "__main__":
    main(sys.argv[1:])

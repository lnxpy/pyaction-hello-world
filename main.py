import sys
from typing import List

from pyaction import io


def main(args: List[str]) -> None:
    """main function

    Args:
        args: STDIN arguments
    """

    # reading the `name` input parameter
    name = io.read("name")
    repo = io.read("repository")
    token = io.read("github_token")

    # writing the `phrase` greeting message to output
    io.write({"phrase": f"name is {name} and repo is {repo} and token is {token}"})

    # Now, people can $echo `phrase`


if __name__ == "__main__":
    main(sys.argv[1:])

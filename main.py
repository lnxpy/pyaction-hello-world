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
    message = f"Hello {name}!"

    # writing the `phrase` greeting message to output
    io.write({"phrase": message})

    # Now, people can $echo `phrase`


    # debugging locally
    # print(message)



if __name__ == "__main__":
    main(sys.argv[1:])

import re
from argparse import Action, ArgumentError, ArgumentParser
from pathlib import Path
from typing import Self

from pydantic import BaseModel

import ghutter

REGEX_REPOSITORY = re.compile(
    r"^(https?://github.com/)?(?P<owner>[^\/\.]+)\/(?P<repo>[^\/\.]+)(\.git)?$", re.IGNORECASE
)


class Arguments(BaseModel):
    repositoryOwner: str
    repository: str
    token: str
    maxCommits: int | None = None
    svgOutput: Path | None = None
    dotOutput: Path

    class _RepositoryAction(Action):
        def __call__(self, parser, namespace, value, option_string=None):
            match = REGEX_REPOSITORY.match(value)
            if not match:
                raise ArgumentError(self, f"invalid repository {value}")
            setattr(namespace, "repository", match.group("repo"))
            setattr(namespace, "repositoryOwner", match.group("owner"))

    @classmethod
    def parse_arguments(cls) -> Self:
        parser = ArgumentParser(prog=ghutter.__package__, description="GHutter")

        parser.add_argument(
            "repository", help='github repository in format "owner/repository" or url', action=cls._RepositoryAction
        )
        parser.add_argument("--token", help="github personal access token")
        parser.add_argument(
            "--max-commits",
            help="max number or commits to fetch from the history " "(parents will always be shown)",
            type=int,
            dest="maxCommits",
        )
        parser.add_argument("--svg-output", help="svg graph output path", type=Path, dest="svgOutput")
        parser.add_argument(
            "--dot-output", help="graph dot file output path", type=Path, default="result.dot", dest="dotOutput"
        )

        return cls(**parser.parse_args().__dict__)

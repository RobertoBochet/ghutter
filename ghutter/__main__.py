from logging import getLogger

from pydot import graph_from_dot_file

from ghutter.github_api.exceptions import GitHubApiException, UnauthorizedException
from ghutter.github_api.fetch_history_graph import FetchHistoryGraph
from ghutter.utils.arguments import Arguments
from ghutter.utils.helpers import sha_2_short_sha

_LOGGER = getLogger(__package__)

if __name__ == "__main__":
    args = Arguments.parse_arguments()

    try:
        fetch = FetchHistoryGraph(**args.model_dump())
        result = fetch()

        # Write the edge directly in file instead of using pydot to prevent memory issues
        with open(args.dotOutput, "w") as f:
            f.write("digraph G {\n")
            for i, j in result:
                f.write(f"C{sha_2_short_sha(i)} -> C{sha_2_short_sha(j)}\n")
            f.write("}\n")
    except UnauthorizedException:
        _LOGGER.fatal("GitHub api returned 401, please check your token")
        exit(1)
    except GitHubApiException as e:
        _LOGGER.fatal(f"GitHub api error {e}")
        exit(1)

    if args.svgOutput:
        graphs = graph_from_dot_file(args.dotOutput)
        try:
            graphs[0].write_svg(args.svgOutput)
        except FileNotFoundError:
            _LOGGER.error("Unable to find graphviz, please install it and try again.")
            exit(1)

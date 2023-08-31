# GHutter

`GHutter` is a tool to recreate the history graph of a GitHub repository in graphviz dot format

## Usage

```text
usage: python -m ghutter [-h] [-t TOKEN] [--max-commits MAXCOMMITS] [-d DOTOUTPUT] [-o DRAWOUTPUT] repository

'GHutter' is a tool to recreate the history graph of a GitHub repository in graphviz dot format

positional arguments:
  repository            github repository in format "owner/repository" or url

options:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        github personal access token
  --max-commits MAXCOMMITS
                        max number or commits to fetch from the history (parents will always be shown)
  -d DOTOUTPUT, --dot-output DOTOUTPUT
                        graph dot file output path (default 'history.dot')
  -o DRAWOUTPUT, --draw-output DRAWOUTPUT
                        graph render output path (there may be several). Check 'Graphviz' supported formats on your
                        system
```

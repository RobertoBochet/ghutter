class GitHubApiException(Exception):
    """Base exception for all GitHubApi exceptions."""


class UnauthorizedException(GitHubApiException):
    """Raised when the GitHub API returns 401."""

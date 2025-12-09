class ApplicationError(Exception):
    """Base class for all application-specific exceptions."""

    pass


class InvalidFeed(ApplicationError):
    """Exception raised for invalid feed formats or structures."""

    def __init__(self, message: str, feed: str, max_length: int = 500) -> None:
        super().__init__(message)
        self.feed = feed
        self.max_length = max_length

    def __str__(self) -> str:
        msg = [
            super().__str__(),
            "============= Feed Content ==============",
            self.feed[: self.max_length],
            "[... snipped]" if len(self.feed) > self.max_length else "",
            "============= /Feed Content ==============",
        ]
        return "\n".join(m for m in msg if m)

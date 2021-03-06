class HoneybadgerbftError(Exception):
    """Base exception class."""


class BroadcastError(HoneybadgerbftError):
    """Base class for broadcast errors."""


class UnknownTagError(BroadcastError):
    """Raised when an unknown broadcast tag is detected."""


class RedundantMessageError(BroadcastError):
    """Raised when a rdundant message is received."""


class AbandonedNodeError(HoneybadgerbftError):
    """Raised when a node does not have enough peer to carry on a distirbuted task."""

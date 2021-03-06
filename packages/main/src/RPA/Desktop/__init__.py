import logging
from robotlibcore import DynamicCore

from RPA.Desktop.keywords import (
    ApplicationKeywords,
    ClipboardKeywords,
    FinderKeywords,
    KeyboardKeywords,
    MouseKeywords,
    ScreenKeywords,
)


class Desktop(DynamicCore):
    """Cross-platform library for interacting with desktop environments."""

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_DOC_FORMAT = "REST"

    def __init__(self):
        self.logger = logging.getLogger(__name__)

        # Register keyword libraries to LibCore
        libraries = [
            ApplicationKeywords(self),
            ClipboardKeywords(self),
            FinderKeywords(self),
            KeyboardKeywords(self),
            MouseKeywords(self),
            ScreenKeywords(self),
        ]
        super().__init__(libraries)

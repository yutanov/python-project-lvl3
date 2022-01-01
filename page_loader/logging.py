# -*- coding: utf-8 -*-

"""Logging configuration."""

import logging
import sys

LEVELS = (INFO, DEBUG) = ('INFO', 'DEBUG')  # noqa: WPS110


def configure_logger(log_level):
    """Configure app logging.

    Args:
        log_level: string, sets the desired log verbosity
    """
    log_format = '[ %(levelname)-5.5s ] :: %(message)s'  # noqa: WPS323
    logging.basicConfig(
        handlers=[logging.StreamHandler(sys.stdout)],
        format=log_format,
        level=logging.getLevelName(log_level),
    )

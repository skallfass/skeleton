# -*- coding: utf-8 -*-


"""
Copyright (C) {{cookiecutter.year}} {{cookiecutter.company}}

Created on: {{cookiecutter.date}}

Author: {{cookiecutter.username}}

E-mail: <{{cookiecutter.email}}>


Description
-----------


Attributes
----------


"""

# Comments are single ...

# or multiline
# comments.


# standard library imports
import argparse
from datetime import datetime as dt
import logging
import os
import sys

# third-party imports
import attr

# application-specific imports


# Globals are defined as the following
GREEN = '\033[1;92m'
"""str: Color green used for visual output for the user."""
RED = '\033[1;91m'
"""str: Color red used for visual output for the user."""
NCOLOR = '\033[0m'
"""str: Resets the color used for visual output for the user."""


# -----------------------------------------------------------------------------
def build_arguments(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)



# -----------------------------------------------------------------------------
def build_logging():
    """
    Customizes logging for this module.
    """
    # TODO: more detailed docstring
    logger = logging.getLogger(__name__)
    logger.basicConfig(level=logging.DEBUG, stream=sys.stdout,
                        format=' %(levelname)s %(message)s')
    logger.addLevelName(logging.DEBUG, '{}d{}'.format(GREEN, NCOLOR))
    logger.addLevelName(logging.INFO, '{}I{}'.format(GREEN, NCOLOR))
    logger.addLevelName(logging.ERROR, '{}E{}'.format(RED, NCOLOR))
    logger.addLevelName(logging.CRITICAL, '{}C{}'.format(RED, NCOLOR))
    return logger



# =============================================================================
class ExampleClass(object):
    """
    Docstring describing the ExampleClass.

    Attributes
    ----------
    attribute name: datatype of this attribute
        description of the attribute
    another attribute name: datatype of this attribute
        description of the attribute

    Notes
    -----
    General notes to this method. Linkages to other methods, classes or
    functions can be expressed like this: :class:`ExampleClass` or
    :func:`ExampleClass.example_method` or :func:`main` .
    """

    # -------------------------------------------------------------------------
    def example_method(self):
        """
        Docstring describing the example_method.

        Parameters
        ----------
        parameter name: parameter type
            description of the parameter

        Returns
        -------
        variable name: variable type
            description

        Notes
        -----
        General notes to this method. Linkages to other methods, classes or
        functions can be expressed like this: :class:`ExampleClass` or
        :func:`ExampleClass.example_method` or :func:`main` .
        """
        return True


# ------------------------------------------------------------------------------
def main():
    """
    Docstring describing the function.

    Parameters
    ----------
    parameter name: parameter type
        description of the parameter

    Returns
    -------
    variable name: variable type
        description

    Notes
    -----
    General notes to this method. Linkages to other methods, classes or
    functions can be expressed like this: :class:`ExampleClass` or
    :func:`ExampleClass.example_method` or :func:`main` .
    """
    logger = build_logging()
    options = build_arguments(sys.argv[1:])


# ==============================================================================
if __name__ == '__main__':
    main()

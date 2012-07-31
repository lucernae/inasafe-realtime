"""
InaSAFE Disaster risk assessment tool developed by AusAid -
**Realtime Exception Classes.**

Custom exception classes for the IS application.

Contact : ole.moller.nielsen@gmail.com

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'tim@linfiniti.com'
__version__ = '0.5.0'
__revision__ = '$Format:%H$'
__date__ = '31/07/2011'
__copyright__ = ('Copyright 2012, Australia Indonesia Facility for '
                 'Disaster Reduction')

class EventUndefinedError(Exception):
    """Exception for when trying to work with an event that is not defined."""
    pass

class NetworkError(Exception):
    """Exception for when trying to fetch a remote resource and failing."""
    pass

class EventValidationError(Exception):
    """Exception for when an event is deemed to be invalid - typically for
    when no matching event can be located on the server or local filesystem
    cache."""
    pass

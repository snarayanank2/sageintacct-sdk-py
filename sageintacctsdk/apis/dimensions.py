"""
Sage Intacct Expense Custom Fields
"""
from typing import Dict

from .api_base import ApiBase

class GetDimensions(ApiBase):
    """Get all the Dimension from Sage Intact

    Returns:
        List of Dict of dimensions
    """

    def get(self):

        data = {
            'getDimensions': {}
        }

        return self.format_and_send_request(data)['data']['dimensions']

from enum import Enum

class GlobalErrorMessage(Enum):
    WRONG_STATUS_CODE = 'Received status code is not equal to expected.'
    WRONG_ELEMENT_COUNT = 'Number of elements is not equels'
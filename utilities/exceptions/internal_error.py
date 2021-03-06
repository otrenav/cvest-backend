
from pprint import pprint


class InternalError(Exception):

    def __init__(self, message, data=None):
        super(InternalError, self).__init__(message)
        self.data = data
        print(self)

    def __str__(self):
        print("")
        print("!" * 50)
        print("CVEST INTERNAL: {}".format(
            super(InternalError, self).__str__()
        ))
        pprint(self.data)
        print("!" * 50)
        return ""

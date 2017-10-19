
from pprint import pprint


class ExternalError(Exception):

    def __init__(self, message, data=None):
        super(ExternalError, self).__init__(message)
        self.data = data
        print(self)

    def __str__(self):
        print("")
        print("!" * 50)
        print("CVEST EXTERNAL: {}".format(
            super(ExternalError, self).__str__()
        ))
        pprint(self.data)
        print("!" * 50)
        return ""

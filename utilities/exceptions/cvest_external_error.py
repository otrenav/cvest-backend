
from pprint import pprint


class CVESTExternalError(Exception):

    def __init__(self, message, data=None):
        super(CVESTExternalError, self).__init__(message)
        self.data = data
        print(self)

    def __str__(self):
        print("")
        print("!" * 50)
        print("CVEST EXTERNAL: {}".format(
            super(CVESTExternalError, self).__str__()
        ))
        pprint(self.data)
        print("!" * 50)
        return ""

import enum


class TestStatus(enum.Enum):
    NEW = 1
    SUCCESS = 2
    FAILURE = 3
    ERROR = 4
    SKIPPED = 5


def check_valid_status(status: TestStatus):
    return status in TestStatus


class TestCase:
    # fictional example class to demonstrate enum functionality in-context; do not actually use this
    def __init__(self, name, test_method):
        self.name = name
        self.status = TestStatus.NEW
        self.test_method = test_method

    def run(self):
        result_status = self.test_method()
        self.set_status(result_status)

    def set_status(self, status: TestStatus):
        self.status = status

    def is_passing(self):
        return self.status in [TestStatus.SUCCESS, TestStatus.SKIPPED]

    def string_status(self):
        status_string = ''
        match self.status:
            case TestStatus.NEW:
                status_string = f'test "{self.name}" has not been executed yet'
            case TestStatus.SUCCESS:
                status_string = f'test "{self.name}" passed'
            case TestStatus.FAILURE:
                status_string = f'test "{self.name}" failed'
            case TestStatus.ERROR:
                status_string = f'test "{self.name}" threw an exception. see file test_{self.name}_error.log for full traceback'
            case TestStatus.SKIPPED:
                status_string = f'test "{self.name}" was skipped due to [reason]'
            case _:
                status_string = f'test "{self.name}" is in an unknown state: {self.status}'
        return status_string


if __name__ == '__main__':
    case = TestCase("tc1", lambda x: x)
    print(case.string_status())
    case.set_status(TestStatus.SUCCESS)
    print(case.is_passing())
    print(case.string_status())

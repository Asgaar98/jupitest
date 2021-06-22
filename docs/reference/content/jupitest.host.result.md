
Back to [Reference Overview](https://github.com/pyrustic/jupitest/blob/master/docs/reference/README.md)

# jupitest.host.result



<br>


```python

class Result:
    """
    Holder for test result information.
    
    Test results are automatically managed by the TestCase and TestSuite
    classes, and do not need to be explicitly manipulated by writers of tests.
    
    Each instance holds the total number of tests run, and collections of
    failures and errors that occurred among those test runs. The collections
    contain tuples of (testcase, exceptioninfo), where exceptioninfo is the
    formatted traceback of the error that occurred.
    """

    def __init__(self, test_id, queue):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    def addError(self, test, err):
        """
        'err' is a tuple of values as returned by sys.exc_info()
        """

    def addExpectedFailure(self, test, err):
        """
        Called when an expected failure/error occurred.
        """

    def addFailure(self, test, err):
        """
        Called when an error has occurred. 'err' is a tuple of values as
        returned by sys.exc_info().
        """

    def addSkip(self, test, reason):
        """
        Called when a test is skipped.
        """

    def addSubTest(self, test, subtest, outcome):
        """
        Called at the end of a subtest.
        'err' is None if the subtest ended successfully, otherwise it's a
        tuple of values as returned by sys.exc_info().
        """

    def addSuccess(self, test):
        """
        Called when a test has completed successfully
        """

    def addUnexpectedSuccess(self, test):
        """
        Called when a test was expected to fail, but succeed.
        """

    def startTest(self, test):
        """
        Called when the given test is about to be run
        """

    def startTestRun(self):
        """
        Called once before any tests are executed.
        
        See startTest for a method called before each test.
        """

    def stopTest(self, test):
        """
        Called when the given test has been run
        """

    def stopTestRun(self):
        """
        Called once after all tests are executed.
        
        See stopTest for a method called after each test.
        """

```


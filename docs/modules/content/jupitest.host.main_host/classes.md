Back to [Modules overview](https://github.com/pyrustic/jupitest/blob/master/docs/modules/README.md)
  
# Module documentation
>## jupitest.host.main\_host
No description
<br>
[classes (1)](https://github.com/pyrustic/jupitest/blob/master/docs/modules/content/jupitest.host.main_host/classes.md)


## Classes
```python
class MainHost(object):
    """
    
    """

    def __init__(self, root_path, reloader, result_builder):
        """
        
        """

    def count_tests(self, path, class_name=None, method_name=None, test_loader=None):
        """
        
        """

    def run(self, test_id, queue, path, class_name=None, method_name=None, failfast=False):
        """
        
        """

    def run_suite(self, test_id, suite, queue, failfast=False):
        """
        
        """

    def stop(self, test_id):
        """
        
        """

    def tests_in_class(self, path, class_name):
        """
        
        """

    def tests_in_directory(self, path):
        """
        
        """

    def tests_in_module(self, path):
        """
        
        """

    def _convert_path_to_dotted_path(self, path, start=None):
        """
        
        """

    def _flatten_suite(self, suite, result):
        """
        
        """

    def _setup(self):
        """
        
        """

```


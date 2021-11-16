Back to [Modules overview](https://github.com/pyrustic/jupitest/blob/master/docs/modules/README.md)
  
# Module documentation
>## jupitest.view.toolbar
No description
<br>
[classes (1)](https://github.com/pyrustic/jupitest/blob/master/docs/modules/content/jupitest.view.toolbar/classes.md)


## Classes
```python
class Toolbar(viewable.Viewable):
    """
    Subclass this if you are going to create a view.
    
    Lifecycle of a view:
        1- you instantiate the view
        2- '__init__()' is implicitly called
        3- you call the method '.build()'
        4- '_build()' is implicitly called
        5- '_on_map()' is implicitly called once the widget is mapped
        6- '_on_destroy()' is implicitly called when the widget is destroyed/closed
    
    The rules to create your view is simple:
    - You need to subclass Viewable.
    - You need to implement the methods '_build()', and optionally
        implement '_on_map()' and '_on_destroy()'.
    - You need to set an instance variable '_body' with either a tk.Frame or tk.Toplevel
        in the method '_on_build()'
    That's all ! Of course, when you are ready to use the view, just call the 'build()' method.
    Calling the 'build()' method will return the body of the view. The one that you assigned
    to the instance variable '_body'. The same body can be retrieved with the property 'body'.
    The 'build()' method should be called once. Calling it more than once will still return
    the body object, but the view won't be built again.
    You can't re-build your same view instance after destroying its body.
    You can destroy the body directly, by calling the conventional tkinter destruction method
     on the view's body. But it's recommended to destroy the view by calling the view's method
     'destroy()' inherited from the class Viewable.
    The difference between these two ways of destruction is that when u call the Viewable's
     'destroy()' method, the method '_on_destroy()' will be called BEFORE the effective
     destruction of the body. If u call directly 'destroy' conventionally on the tkinter
     object (the body), the method '_on_destroy()' will be called AFTER the beginning
      of destruction of the body.
    
      By the way, you can use convenience methods "build_pack", "build_grid", "build_place"
      to build and pack/grid/place your widget in the master !!
      Use "build_wait" for toplevels if you want the app to wait till the window closes
    """

    def __init__(self, node_id, parent, callback, log_window_builder):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """

    # inherited from viewable.Viewable
    @property
    def body(self):
        """
        Get the body of this view.
        """

    @property
    def count_tests(self):
        """
        
        """

    @count_tests.setter
    def count_tests(self, val):
        """
        
        """

    @property
    def is_visible(self):
        """
        
        """

    # inherited from viewable.Viewable
    @property
    def state(self):
        """
        Return the current state of the Viewable instance.
        States are integers, you can use these constants:
            - pyrustic.view.NEW: the state just after instantiation;
            - pyrustic.view.BUILT: the state after the call of _built
            - pyrustic.view.MAPPED: the state after the call of on_map
            - pyrustic.view.DESTROYED: the state after the call of on_destroy
        """

    # inherited from viewable.Viewable
    def build(self):
        """
        Build this view object. It returns the body 
        """

    # inherited from viewable.Viewable
    def build_grid(self, cnf=None, **kwargs):
        """
        Build this view then grid it 
        """

    # inherited from viewable.Viewable
    def build_pack(self, cnf=None, **kwargs):
        """
        Build this view then pack it 
        """

    # inherited from viewable.Viewable
    def build_place(self, cnf=None, **kwargs):
        """
        Build this view then place it 
        """

    # inherited from viewable.Viewable
    def build_wait(self):
        """
        Build this view then wait till it closes.
        The view should have a tk.Toplevel as body 
        """

    # inherited from viewable.Viewable
    def destroy(self):
        """
        Destroy the body of this view 
        """

    def notify_add_error(self, test, err):
        """
        
        """

    def notify_add_expected_failure(self, test, err):
        """
        
        """

    def notify_add_failure(self, test, err):
        """
        
        """

    def notify_add_skip(self, test, reason):
        """
        
        """

    def notify_add_sub_test(self, test, subtest, outcome):
        """
        
        """

    def notify_add_success(self, test):
        """
        
        """

    def notify_add_unexpected_success(self, test):
        """
        
        """

    def notify_start_test(self, test):
        """
        
        """

    def notify_stop_test(self, test):
        """
        
        """

    def notify_time_elapsed(self, time_elapsed):
        """
        
        """

    def set_running_state(self):
        """
        
        """

    def set_stop_state(self, was_successful, log):
        """
        
        """

    def set_waiting_state(self):
        """
        
        """

    def show_or_hide(self):
        """
        
        """

    def _build(self):
        """
        Build the view here by defining the _body instance
        """

    def _get_log(self):
        """
        
        """

    def _install_default_widgets(self):
        """
        
        """

    def _on_cancel_clicked(self):
        """
        
        """

    def _on_clean_clicked(self):
        """
        
        """

    # inherited from viewable.Viewable
    def _on_destroy(self):
        """
        Put here the code that will be executed at destroy event
        """

    def _on_log_clicked(self):
        """
        
        """

    # inherited from viewable.Viewable
    def _on_map(self):
        """
        Put here the code that will be executed once
        the body is mapped.
        """

    def _on_rerun_clicked(self):
        """
        
        """

    def _on_run_clicked(self):
        """
        
        """

    def _on_stop_clicked(self):
        """
        
        """

    def _reset_data(self):
        """
        
        """

    def _reset_toolbar(self):
        """
        
        """

```


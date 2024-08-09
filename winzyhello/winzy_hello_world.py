import winzy

class HelloWorld:
    __name__ = "hello"
    @winzy.hookimpl
    def register_commands(self, subparser):
        hello_parser = subparser.add_parser("hello", description="Test plugin")
        hello_parser.set_defaults(func=self.hello)
    
    def hello(self, args):
        print("Hello! This is an example ``winzy`` plugin.")

hello_plugin = HelloWorld()

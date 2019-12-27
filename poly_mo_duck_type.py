class Pycharm:
      def execute(self):
          print("checking error")
          print("compiling the code")
class MyEditor:
    def execute(self):
        print("checking error")
        print("compiling the code")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = Pycharm()
editor = MyEditor()

lap1 = Laptop()
lap1.code(ide)
lap1.code(editor)



class aids():
    def python(self):
        print("python is very easy")
        self._java()
        
#potected:
        # base and derived class la access panna mudium
        # munnadi irukura func la self._java()
        
    def _java(self):
        print("Java is very difficult")
        self.__c()

#private
        # class kulla irukura func nala mattum dhan call panna mudium
        # munnadi irukura func la self.__c()

    def __c(self):
        print("c is modurate")

Mani=aids()
Mani.python()

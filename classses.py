class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def start(self ):
         print(f" {self.model} {self.year}")

    def stop(self):
        print(f"{self.make}  {self.year}")


cr=Car('Audi','A8','2020')
cr.start()
cr.stop()
print(cr.make)

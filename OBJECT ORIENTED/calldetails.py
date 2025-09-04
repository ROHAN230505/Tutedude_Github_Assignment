class Call details:

    def setCallDetails(self, caldetail):
        self.calldetails = caldetail
        self.cd = self.calldetails.split(":")

    def getID(self) -> int:
        id = int(self.cd[0])
        return id

    def getNumber(self) -> int:
        no = int(self.cd[1])
        return no

    def getDuration(self) -> float:
        time = float(self.cd[2])
        return time


if __name__ =='__main__':
    caldetail: str = str(input("Enter you Call Details"))
    c = Calldetails()
    c.setCallDetails(caldetail)
    print("ID IS",c.getID())
    print("Number is",c.getNumber())
    print("Duration is",c.getDuration())

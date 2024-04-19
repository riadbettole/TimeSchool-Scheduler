class Time:
    def __init__(self, fr_to):
        self.from_to = fr_to
        _from, _to = self.parseTime(fr_to)
        self.from_hour = _from
        self.to_hour = _to
        
    def parseTime(self, from_to):
        splited = from_to.split("-")
        _from = splited[0].split("h")[0]
        _to =  splited[1].split("h")[0]
        return _from, _to
    
    def __str__(self) -> str:
        return self.from_to
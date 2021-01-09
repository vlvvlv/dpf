from datetime import datetime
from mycar import db
from mycar.models import Dpfcar
lines = open("D:/행운/Car/Dpfcar.csv", "r")
i = 0
for line in lines:
    line = line.replace("\n","")
    linesplit = line.split(",")
    dpfcar = Dpfcar(carnumber = linesplit[0],
                    carnumber4 = linesplit[1],
                    caryear = linesplit[2],
                    carkind = linesplit[3],
                    create_date = datetime.now())
    db.session.add(dpfcar)
    db.session.commit()
    i = i+1
lines.close()

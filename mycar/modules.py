class Convertcarnumber:
    def __init__(self, carnumber):
        self.carnumber = carnumber

    def car_num4_trans(self):
        carnumin = self.carnumber[-4:]
        car_num4_01 = self.carnumber[:-4]+carnumin[0:2] + "**"
        car_num4_02 = self.carnumber[:-4]+carnumin[0] + "**" + carnumin[3]
        car_num4_03 = self.carnumber[:-4]+"**" + carnumin[2:4]
        return(car_num4_01, car_num4_02, car_num4_03)
"""
@author Dominik Cedro
DISCLAIMER:
    -> for method get_age I used instruction on page: https://www.delftstack.com/howto/python/python-current-year/
"""


"""
 * name,
• dob — year of birth,
• height (in cm),
* weight (in kg).
"""
import datetime
import statistics

class HealthProfile:
    good_bmi = (18.5,24.9)
    def __init__(self, name, dob, height, weight):
        # sprawdzac poprawnosc
        self.name = name
        self.dob = dob
        self.height = height
        self.weight = weight
        """
        In addition, implement the following methods:
        • get_age — which returns the age of the person in years,
        • get_target_hr — which returns the target heart rate (HR) for moderate-intensity
        physical activity,
        • get_bmi — which returns the person’s body mass index (BMI).
        """
        self.age = int(datetime.date.today().strftime("%Y")) - dob

    def get_age(self):
        #tutaj obliczac self.age a nie w __init__
        return self.age

    def get_target_hr(self):
        # zrodlo formuly
        max_heart = 220 - self.age
        high =  0.75 * max_heart
        low = 0.64 * max_heart
        mean = (0.75 * max_heart + 0.64 * max_heart)/2
        return mean

    def get_bmi(self):
        bmi_w = self.weight
        bmi_h = self.height/100
        bmi  = bmi_w/(bmi_h*bmi_h)
        return round(bmi,2)

    #static method to calculate mean and st_dev of age_list

    def calculate_age_stats(object_list):
        age_list = []
        for object in object_list:
            age_list.append(object.get_age())

        mean_age = sum(age_list) / len(age_list)
        st_dev = statistics.stdev(age_list)

        return st_dev, mean_age # raczej odwrotnie

    #statics method to find people at risk
    @staticmethod
    def find_people_at_risk(object_list):
        bmi_results = []
        for object in object_list:
            bmi = object.get_bmi()
            if bmi < HealthProfile.good_bmi[0]:
                bmi_results.append(object.name)
            elif bmi > HealthProfile.good_bmi[1]:
                bmi_results.append(object.name)
        return bmi_results



###

#demonstration of the code
Dominik = HealthProfile("Dominik",2002,185,200)
Marcel = HealthProfile("Marcel",2008,160,20)

print(Dominik.get_age())
print(Dominik.get_target_hr())
print(Dominik.get_bmi())


print(f"age stats{HealthProfile.calculate_age_stats([Dominik, Marcel])}")
print(HealthProfile.find_people_at_risk([Dominik,Marcel]))

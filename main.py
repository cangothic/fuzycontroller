from models.piecewise_functions import Piecewise_funtion
from models.model_sections import Section
if __name__ == '__main__':
    section1 = Section(3, 5, lambda x: x**2)
    section2 = Section(5, 7, lambda x: x + 25)
    section3 = Section(9, 11, lambda x: x**3)
    function = Piecewise_funtion(section1)
    function.unir(section2)
    function.unir(section3)

    for i in range(2, 14):
        print(function.function(i))


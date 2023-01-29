"""
Module to calculate the Body mass indice of a person.
:param Height: should be a positive integer or a float value. The accept unit is meter
:param weight: should be a positive integer or a float value. The accept unit is kg.
:param return: is the BMI. This parameter has no unit
Notice that it's no sense to talk of the bmi of a baby. At least the child should be
7 years old. Cosidering this, the weight should not under 20kg.
Also pay attention to the height, it should not be less than 1,5m

"""
from math import pow as puissance


def imc(height, weight):
    """
    :param height:
    :param weight:
    :return:
    """
    #To ensure that we will not compute imc for a baby under certain age
    if height < 1.5 and not(height) == 0 or weight < 20 and not(weight) == 0:
        raise ValueError("Height should be at least 1.5, also Weight value should be at least 20kg")
    #To pass the test I should learn to code defensively
    if height == 0 or weight == 0:
        raise ZeroDivisionError("Please Enter non null value for height")
    #This condition test to see if there's no negative values enter for height or weight
    if height < 0 or weight < 0:
        raise ValueError("You should consider enter positive value for height and weight")
    #These conditions are used to test if a string value is passed to our function
    if type(height) == str or type(weight) == str:
        raise TypeError("Please provide a non string value for height and weight")
    return weight / puissance(height, 2)

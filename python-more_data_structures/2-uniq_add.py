#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_nbr = set(my_list)
    # set: tous les doublons,triplés,ect.. sont automatiquement éliminés
    total = sum(uniq_nbr)

    return total

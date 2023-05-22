
def area_circulo(radio):
    pi = 3.1415
    return 2*pi*radio**2

def cilinder_volume(radio, altura):
    return area_circulo(radio)*altura

print(cilinder_volume(1,2))
# Kinetyka Michaelisa-Menten

import numpy as np
from scipy.optimize import curve_fit

###########################################a
def f(s, Vmax, Km):
#Funkcja modelu
    return Vmax * s / (Km + s)


###########################################a
def main():
    #Parametry modelu
    Vmax = 100.0
    Km = 6.0
    stdev = 5.0


    number_points = int(10)  #liczba punktów danych
    s_max = float(50)  #maksymalne stężenie substratu
    s = np.arange(number_points) * s_max / number_points   #wygenerowanie zakresu stężeń substratu
    # w równych odstępach od 0 do s_max
    v = f(s, Vmax, Km)  # obliczenia prędkość dla każdego stężenia substratu


    # Dopasowanie krzywej
    tab = np.zeros(number_points) + stdev  # odchylenia standardowe dla każdego punktu
    start = (110, 25)  # doświadczalne dopasowanie dla Vmax and Km
    popt, pcov = curve_fit(f, s, v, sigma=tab, p0=start, absolute_sigma=True)  # faktyczne dopasowanie
    print(popt)
    print(pcov)
    v_exp = f(s, *popt)
    r = v - v_exp
    chisq = np.sum((r / stdev) ** 2)
    df = number_points - 2
    print("chisq =", chisq, "         df =", df)


    # Wykreślenie wykresu zależności V od S z dopasowaniem krzywej
    import matplotlib.pyplot as plt
    plt.plot(s, v_exp)
    plt.title("Kinetyka Michaelisa-Menten")
    plt.xlabel("[S]")
    plt.ylabel("[V]")
    plt.legend()
    plt.axhline(y=0.0, color='0.75', linestyle='-')
    plt.axvline(x=0.0, color='0.75', linestyle='-')
    plt.show()


    # Wykreślenie wykresu Lineweavera-Burka
    x_int = -1 / popt[1]  # 1/Km jako wartość przecięcia z osią X
    xv = np.arange(500) / 500 * ((1 / (s[1]) - x_int)) + x_int
    yv = 1 / (f(1 / xv, popt[0], popt[1]))
    plt.plot(xv, yv)
    plt.title("Wykres Lineweavera-Burka")
    plt.xlabel("1/[S]")
    plt.ylabel("1/[V]")

    # Punkty wykresu oraz elementy wizualne
    plt.legend()
    plt.axhline(y=0.0, color='0.75', linestyle='-')
    plt.axvline(x=0.0, color='0.75', linestyle='-')

    # Opis Vmax i Km oraz elementy wizualne
    plt.annotate("-1/Km", xy=(x_int, 0), xytext=(x_int, 0.4 * 1 / popt[0]),
                 horizontalalignment='center', verticalalignment='center',
                 arrowprops=dict(facecolor="black", width=1, shrink=0.1, headwidth=5))
    plt.annotate("1/Vmax", xy=(0, 1 / popt[0]), xytext=(x_int / 2.5, 1.1 / popt[0]),
                 horizontalalignment='center', verticalalignment='center',
                 arrowprops=dict(facecolor="black", width=1, shrink=0.1, headwidth=5))

    plt.show()


###########################################a
main()


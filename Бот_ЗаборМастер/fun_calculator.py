def calculator(h, material, montage, kalytka, rab_karkas, dlina_vor, dlina_zab):
    st_zab = 0
    if material=='профнастил оцинкованный':
        if montage == 'материалы+работа':
            if dlina_zab <= 20:
                if h == 1.5:
                    st_zab=dlina_zab*2850
                elif h == 1.8:
                    st_zab = dlina_zab * 3100
                elif h == 2.0:
                    st_zab = dlina_zab * 3200
                elif h == 2.5:
                    st_zab = dlina_zab * 3750
                elif h == 3.0:
                    st_zab = dlina_zab * 5300
            if dlina_zab > 20:
                if h == 1.5:
                    st_zab = dlina_zab * 2450
                elif h == 1.8:
                    st_zab = dlina_zab * 2700
                elif h == 2.0:
                    st_zab = dlina_zab * 2800
                elif h == 2.5:
                    st_zab = dlina_zab * 3250
                elif h == 3.0:
                    st_zab = dlina_zab * 4800
        elif montage == 'только работа':
            if dlina_zab <= 20:
                if h == 1.5:
                    st_zab = dlina_zab * 1100
                elif h == 1.8:
                    st_zab = dlina_zab * 1100
                elif h == 2.0:
                    st_zab = dlina_zab * 1150
                elif h == 2.5:
                    st_zab = dlina_zab * 1300
                elif h == 3.0:
                    st_zab = dlina_zab * 1800
            if dlina_zab > 20:
                if h == 1.5:
                    st_zab = dlina_zab * 800
                elif h == 1.8:
                    st_zab = dlina_zab * 800
                elif h == 2.0:
                    st_zab = dlina_zab * 850
                elif h == 2.5:
                    st_zab = dlina_zab * 1000
                elif h == 3.0:
                    st_zab = dlina_zab * 1500
        elif dlina_vor == 0:
            pass
        elif dlina_vor == 3:
            st_zab = st_zab + 25000
        elif dlina_vor == 4:
            st_zab = st_zab + 30000
        elif kalytka =='без калитки':
            pass
        elif kalytka =='с калиткой':
            st_zab = st_zab + 15000
    elif material== 'профнастил окрашенный':
        if montage == 'материалы+работа':
            if dlina_zab <= 20:
                if h == 1.5:
                    st_zab = dlina_zab * 2950
                elif h == 1.8:
                    st_zab = dlina_zab * 3200
                elif h == 2.0:
                    st_zab = dlina_zab * 3300
                elif h == 2.5:
                    st_zab = dlina_zab * 3850
                elif h == 3.0:
                    st_zab = dlina_zab * 5500
            if dlina_zab > 20:
                if h == 1.5:
                    st_zab = dlina_zab * 2550
                elif h == 1.8:
                    st_zab = dlina_zab * 2800
                elif h == 2.0:
                    st_zab = dlina_zab * 2900
                elif h == 2.5:
                    st_zab = dlina_zab * 3350
                elif h == 3.0:
                    st_zab = dlina_zab * 5000
        elif montage == 'только работа':
            if dlina_zab <= 20:
                if h == 1.5:
                    st_zab = dlina_zab * 1100
                elif h == 1.8:
                    st_zab = dlina_zab * 1100
                elif h == 2.0:
                    st_zab = dlina_zab * 1150
                elif h == 2.5:
                    st_zab = dlina_zab * 1300
                elif h == 3.0:
                    st_zab = dlina_zab * 1800
            if dlina_zab > 20:
                if h == 1.5:
                    st_zab = dlina_zab * 800
                elif h == 1.8:
                    st_zab = dlina_zab * 800
                elif h == 2.0:
                    st_zab = dlina_zab * 850
                elif h == 2.5:
                    st_zab = dlina_zab * 1000
                elif h == 3.0:
                    st_zab = dlina_zab * 1500
        elif dlina_vor == 0:
            pass
        elif dlina_vor == 3:
            st_zab = st_zab + 25000
        elif dlina_vor == 4:
            st_zab = st_zab + 30000
        elif kalytka =='без калитки':
            pass
        elif kalytka =='с калиткой':
            st_zab = st_zab + 15000
    elif material==  'рабица оцинкованная':
        if rab_karkas == 'сетка в каркасе':
            if montage == 'материалы+работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 1850
                    elif h == 1.8:
                        st_zab = dlina_zab * 2000
                    elif h == 2.0:
                        st_zab = dlina_zab * 2150
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 1700
                    elif h == 1.8:
                        st_zab = dlina_zab * 1850
                    elif h == 2.0:
                        st_zab = dlina_zab * 2000
            elif montage == 'только работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 900
                    elif h == 1.8:
                        st_zab = dlina_zab * 950
                    elif h == 2.0:
                        st_zab = dlina_zab * 1000
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 850
                    elif h == 1.8:
                        st_zab = dlina_zab * 900
                    elif h == 2.0:
                        st_zab = dlina_zab * 950
        elif  rab_karkas == 'сетка без каркаса':
            if montage == 'материалы+работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 1500
                    elif h == 1.8:
                        st_zab = dlina_zab * 1600
                    elif h == 2.0:
                        st_zab = dlina_zab * 1850
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 1300
                    elif h == 1.8:
                        st_zab = dlina_zab * 1400
                    elif h == 2.0:
                        st_zab = dlina_zab * 1650
            elif montage == 'только работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 650
                    elif h == 1.8:
                        st_zab = dlina_zab * 700
                    elif h == 2.0:
                        st_zab = dlina_zab * 750
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 600
                    elif h == 1.8:
                        st_zab = dlina_zab * 650
                    elif h == 2.0:
                        st_zab = dlina_zab * 700
        elif dlina_vor == 0:
            pass
        elif dlina_vor == 3:
            st_zab = st_zab + 21000
        elif dlina_vor == 4:
            st_zab = st_zab + 24000
        elif kalytka =='без калитки':
            pass
        elif kalytka =='с калиткой':
            st_zab = st_zab + 14000
    elif material==  'рабица c ПВХ-покрытием':
        if rab_karkas == 'сетка в каркасе':
            if montage == 'материалы+работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 2050
                    elif h == 1.8:
                        st_zab = dlina_zab * 2300
                    elif h == 2.0:
                        st_zab = dlina_zab * 2450
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 1900
                    elif h == 1.8:
                        st_zab = dlina_zab * 2000
                    elif h == 2.0:
                        st_zab = dlina_zab * 2300
            elif montage == 'только работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 900
                    elif h == 1.8:
                        st_zab = dlina_zab * 950
                    elif h == 2.0:
                        st_zab = dlina_zab * 1000
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 850
                    elif h == 1.8:
                        st_zab = dlina_zab * 900
                    elif h == 2.0:
                        st_zab = dlina_zab * 950
        elif  rab_karkas == 'сетка без каркаса':
            if montage == 'материалы+работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 1600
                    elif h == 1.8:
                        st_zab = dlina_zab * 1700
                    elif h == 2.0:
                        st_zab = dlina_zab * 2000
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 1400
                    elif h == 1.8:
                        st_zab = dlina_zab * 1500
                    elif h == 2.0:
                        st_zab = dlina_zab * 1800
            elif montage == 'только работа':
                if dlina_zab <= 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 650
                    elif h == 1.8:
                        st_zab = dlina_zab * 700
                    elif h == 2.0:
                        st_zab = dlina_zab * 750
                elif dlina_zab > 20:
                    if h == 1.5:
                        st_zab = dlina_zab * 600
                    elif h == 1.8:
                        st_zab = dlina_zab * 650
                    elif h == 2.0:
                        st_zab = dlina_zab * 700
        elif dlina_vor == 0:
            pass
        elif dlina_vor == 3:
            st_zab = st_zab + 21000
        elif dlina_vor == 4:
            st_zab = st_zab + 24000
        elif kalytka == 'без калитки':
            pass
        elif kalytka == 'с калиткой':
            st_zab = st_zab + 14000
    return st_zab

def plus_vorota(h, material, montage, kalytka, rab_karkas, dlina_vor, dlina_zab,var):
    if dlina_vor == 0 and  kalytka == 'без калитки':
        pass
    elif  dlina_vor == 0 and  kalytka ==  'с калиткой':
        if material == 'профнастил оцинкованный':
            if montage == 'материалы+работа':
                var = var + 15000
            elif montage == 'только работа':
                 var = var + 5000

        elif material == 'профнастил окрашенный':
            if montage == 'материалы+работа':
                var = var + 16000
            elif montage == 'только работа':
                var = var + 5000
        elif material == 'рабица оцинкованная':
            if montage == 'материалы+работа':
                var = var + 14000
            elif montage == 'только работа':
                var = var + 5000

        elif material == 'рабица c ПВХ-покрытием':
            if montage == 'материалы+работа':
                var = var + 14000
            elif montage == 'только работа':
                var = var + 14000

    elif dlina_vor == 3:
        if material=='профнастил оцинкованный':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 25000
                elif kalytka == 'с калиткой':
                    var = var + 25000
                    var = var + 15000
            elif montage == 'только работа':
                if kalytka == 'без калитки':
                    var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 5000

        elif material=='профнастил окрашенный':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 28000
                elif kalytka == 'с калиткой':
                    var = var + 28000
                    var = var + 16000


            elif montage == 'только работа':
                if kalytka == 'без калитки':
                    var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 5000



        elif material == 'рабица оцинкованная':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 21000
                elif kalytka == 'с калиткой':
                    var = var + 21000
                    var = var + 14000

            elif montage == 'только работа':
                if kalytka == 'без калитки':
                    var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 5000

        elif material == 'рабица c ПВХ-покрытием':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 23000
                elif kalytka == 'с калиткой':
                    var = var + 23000
                    var = var + 14000

            elif montage == 'только работа':
                if kalytka == 'без калитки':
                    var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 14000

    elif dlina_vor == 4:
        if material == 'профнастил оцинкованный':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 30000
                elif kalytka == 'с калиткой':
                    var = var + 30000
                    var = var + 15000

            elif montage == 'только работа':
                if kalytka == 'без калитки':
                    var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 5000

        elif material == 'профнастил окрашенный':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 330000
                elif kalytka == 'с калиткой':
                    var = var + 33000
                    var = var + 16000

            elif montage == 'только работа':
                if kalytka == 'без калитки':
                    var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 5000

        elif material == 'рабица оцинкованная':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 24000
                elif kalytka == 'с калиткой':
                    var = var + 24000
                    var = var + 14000

            elif montage == 'только работа':
                if kalytka == 'без калитки':
                    var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 5000

        elif material == 'рабица c ПВХ-покрытием':
            if montage == 'материалы+работа':
                if kalytka == 'без калитки':
                    var = var + 26000
                elif kalytka == 'с калиткой':
                    var = var + 26000
                    var = var + 14000

            elif montage == 'только работа':
                if kalytka == 'без калитки':
                     var = var + 15000
                elif kalytka == 'с калиткой':
                    var = var + 15000
                    var = var + 5000

    print('Стоимость', var)
    return var
















from django.shortcuts import render


# Create your views here.
def besthome(request):
    tv_brands = {
        'Sony': [
            {
                'model': 'A95L',
                'sizes_prices': [{'size': '55"', 'price': 2799.99}, {'size': '65"', 'price': 3499.99},
                                 {'size': '77"', 'price': 4999.99}],
                'image': 'images/sony_a95l.png',
                'promo_link': 'https://www.bestbuy.com/site/sony-55-class-bravia-xr-a95l-oled-4k-uhd-smart-google-tv-2023/6553384.p?skuId=6553384'
            },
            {
                'model': 'Bravia 9',
                'sizes_prices': [{'size': '55"', 'price': 1100}, {'size': '65"', 'price': 1500},
                                 {'size': '75"', 'price': 1900}],
                'image': 'images/sony_bravia9.png'
            },
            {
                'model': 'Bravia 8',
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/sony_bravia8.png'
            },
            {
                'model': 'Bravia 7',
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/sony_bravia7.png'
            },
            {
                'model': 'X90L',
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/sony_x90l.png'
            },
            {
                'model': 'Bravia 3',
                'sizes_prices': [{'size': '55"', 'price': 700}, {'size': '65"', 'price': 1100},
                                 {'size': '75"', 'price': 1500}],
                'image': 'images/sony_bravia3.png'
            }
        ],
        'Samsung': [
            {
                'model': 'S95D',
                'sizes_prices': [{'size': '55"', 'price': 1300}, {'size': '65"', 'price': 1700},
                                 {'size': '75"', 'price': 2100}],
                'image': 'images/samsung_s95d.png'
            },
            {
                'model': 'S90D',
                'sizes_prices': [{'size': '55"', 'price': 1200}, {'size': '65"', 'price': 1600},
                                 {'size': '75"', 'price': 2000}],
                'image': 'images/samsung_s90d.png'
            },
            {
                'model': 'QN90D',
                'sizes_prices': [{'size': '55"', 'price': 1100}, {'size': '65"', 'price': 1500},
                                 {'size': '75"', 'price': 1900}],
                'image': 'images/samsung_qn90d.png'
            },
            {
                'model': 'Q80D',
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/samsung_q80d.png'
            },
            {
                'model': 'Q60D',
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/samsung_q60d.png'
            },
            {
                'model': 'DU7200',
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/samsung_du7200.png'
            }
        ],
        'LG': [
            {
                'model': 'G4',
                'sizes_prices': [{'size': '55"', 'price': 1400}, {'size': '65"', 'price': 1800},
                                 {'size': '75"', 'price': 2200}],
                'image': 'images/lg_g4.png'
            },
            {
                'model': 'C4',
                'sizes_prices': [{'size': '55"', 'price': 1300}, {'size': '65"', 'price': 1700},
                                 {'size': '75"', 'price': 2100}],
                'image': 'images/lg_c4.png'
            },
            {
                'model': 'QNED85',
                'sizes_prices': [{'size': '55"', 'price': 1200}, {'size': '65"', 'price': 1600},
                                 {'size': '75"', 'price': 2000}],
                'image': 'images/lg_qned85.png'
            },
            {
                'model': 'QNED80',
                'sizes_prices': [{'size': '55"', 'price': 1100}, {'size': '65"', 'price': 1500},
                                 {'size': '75"', 'price': 1900}],
                'image': 'images/lg_qned80.png'
            },
            {
                'model': 'UT75',
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/lg_ut75.png'
            }
        ],
        'TCL': [
            {
                'model': 'QM8',
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/tcl_qm8.png'
            },
            {
                'model': 'QD7',
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/tcl_qd7.png'
            },
            {
                'model': 'S5',
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/tcl_s5.png'
            }
        ],
        'Hisense': [
            {
                'model': 'U8N',
                'sizes_prices': [{'size': '55"', 'price': 1100}, {'size': '65"', 'price': 1500},
                                 {'size': '75"', 'price': 1900}],
                'image': 'images/hisense_u8n.png'
            },
            {
                'model': 'U7N',
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/hisense_u7n.png'
            },
            {
                'model': 'U6',
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/hisense_u6.png'
            },
            {
                'model': 'A7',
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/hisense_a7.png'
            }
        ]
    }
    return render(request, 'bestguide/besthome.html', {'tv_brands': tv_brands})


def testing(request):
    return render(request, 'bestguide/testing2.html')


def motd(request):
    return render(request, 'bestguide/testing.html')

from django.shortcuts import render


# Create your views here.
def besthome(request):
    tv_brands = {
        'Sony': [
            {
                'model': 'A95L',
                'panel_type': 'OLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 2799.99}, {'size': '65"', 'price': 3499.99},
                                 {'size': '77"', 'price': 4999.99}],
                'image': '/portfolio/assets/teles/sony_a95l.jpg',
                'promo_link': 'https://www.bestbuy.com/site/sony-55-class-bravia-xr-a95l-oled-4k-uhd-smart-google-tv-2023/6553384.p?skuId=6553384',
                'rating': '⭐⭐⭐⭐⭐'
            },
            {
                'model': 'Bravia 9',
                'panel_type': 'Mini LED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '65"', 'price': 3299.99}, {'size': '75"', 'price': 3999.99},
                                 {'size': '85"', 'price': 5499.99}],
                'image': '/portfolio/assets/teles/sony_bravia9.jpg',
                'promo_link': 'https://www.bestbuy.com/site/sony-65-class-bravia-9-mini-led-qled-4k-uhd-smart-google-tv-2024/6578568.p?skuId=6578568',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'Bravia 8',
                'panel_type': 'LED',
                'refresh_rate': '60 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/sony_bravia8.png',
                'promo_link': 'https://example.com/sony-bravia8-promo',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'Bravia 7',
                'panel_type': 'LCD',
                'refresh_rate': '60 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/sony_bravia7.png',
                'promo_link': 'https://example.com/sony-bravia7-promo',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'X90L',
                'panel_type': 'LED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/sony_x90l.png',
                'promo_link': 'https://example.com/sony-x90l-promo',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'Bravia 3',
                'panel_type': 'LCD',
                'refresh_rate': '60 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 2,
                'sizes_prices': [{'size': '55"', 'price': 700}, {'size': '65"', 'price': 1100},
                                 {'size': '75"', 'price': 1500}],
                'image': 'images/sony_bravia3.png',
                'promo_link': 'https://example.com/sony-bravia3-promo',
                'rating': '⭐⭐'
            }
        ],
        'Samsung': [
            {
                'model': 'S95D',
                'panel_type': 'OLED',
                'refresh_rate': '144 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1300}, {'size': '65"', 'price': 1700},
                                 {'size': '75"', 'price': 2100}],
                'image': 'images/samsung_s95d.png',
                'promo_link': 'https://example.com/samsung-s95d-promo',
                'rating': '⭐⭐⭐⭐⭐'
            },
            {
                'model': 'S90D',
                'panel_type': 'OLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1200}, {'size': '65"', 'price': 1600},
                                 {'size': '75"', 'price': 2000}],
                'image': 'images/samsung_s90d.png',
                'promo_link': 'https://example.com/samsung-s90d-promo',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'QN90D',
                'panel_type': 'QLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1100}, {'size': '65"', 'price': 1500},
                                 {'size': '75"', 'price': 1900}],
                'image': 'images/samsung_qn90d.png',
                'promo_link': 'https://example.com/samsung-qn90d-promo',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'Q80D',
                'panel_type': 'QLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/samsung_q80d.png',
                'promo_link': 'https://example.com/samsung-q80d-promo',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'Q60D',
                'panel_type': 'QLED',
                'refresh_rate': '60 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/samsung_q60d.png',
                'promo_link': 'https://example.com/samsung-q60d-promo',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'DU7200',
                'panel_type': 'LED',
                'refresh_rate': '60 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 2,
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/samsung_du7200.png',
                'promo_link': 'https://example.com/samsung-du7200-promo',
                'rating': '⭐⭐'
            }
        ],
        'LG': [
            {
                'model': 'G4',
                'panel_type': 'OLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'webOS',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1400}, {'size': '65"', 'price': 1800},
                                 {'size': '75"', 'price': 2200}],
                'image': 'images/lg_g4.png',
                'promo_link': 'https://example.com/lg-g4-promo',
                'rating': '⭐⭐⭐⭐⭐'
            },
            {
                'model': 'C4',
                'panel_type': 'OLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'webOS',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1300}, {'size': '65"', 'price': 1700},
                                 {'size': '75"', 'price': 2100}],
                'image': 'images/lg_c4.png',
                'promo_link': 'https://example.com/lg-c4-promo',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'QNED85',
                'panel_type': 'QNED',
                'refresh_rate': '120 Hz',
                'smart_os': 'webOS',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1200}, {'size': '65"', 'price': 1600},
                                 {'size': '75"', 'price': 2000}],
                'image': 'images/lg_qned85.png',
                'promo_link': 'https://example.com/lg-qned85-promo',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'QNED80',
                'panel_type': 'QNED',
                'refresh_rate': '60 Hz',
                'smart_os': 'webOS',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 1100}, {'size': '65"', 'price': 1500},
                                 {'size': '75"', 'price': 1900}],
                'image': 'images/lg_qned80.png',
                'promo_link': 'https://example.com/lg-qned80-promo',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'UT75',
                'panel_type': 'LED',
                'refresh_rate': '60 Hz',
                'smart_os': 'webOS',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/lg_ut75.png',
                'promo_link': 'https://example.com/lg-ut75-promo',
                'rating': '⭐⭐'
            }
        ],
        'TCL': [
            {
                'model': 'QM8',
                'panel_type': 'Mini LED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/tcl_qm8.png',
                'promo_link': 'https://example.com/tcl-qm8-promo',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'QD7',
                'panel_type': 'QLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/tcl_qd7.png',
                'promo_link': 'https://example.com/tcl-qd7-promo',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'S5',
                'panel_type': 'LED',
                'refresh_rate': '60 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 700}, {'size': '65"', 'price': 1100},
                                 {'size': '75"', 'price': 1500}],
                'image': 'images/tcl_s5.png',
                'promo_link': 'https://example.com/tcl-s5-promo',
                'rating': '⭐⭐'
            }
        ],
        'Hisense': [
            {
                'model': 'U8N',
                'panel_type': 'ULED',
                'refresh_rate': '120 Hz',
                'smart_os': 'VIDAA',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1000}, {'size': '65"', 'price': 1400},
                                 {'size': '75"', 'price': 1800}],
                'image': 'images/hisense_u8n.png',
                'promo_link': 'https://example.com/hisense-u8n-promo',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'U7N',
                'panel_type': 'ULED',
                'refresh_rate': '120 Hz',
                'smart_os': 'VIDAA',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 900}, {'size': '65"', 'price': 1300},
                                 {'size': '75"', 'price': 1700}],
                'image': 'images/hisense_u7n.png',
                'promo_link': 'https://example.com/hisense-u7n-promo',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'U6',
                'panel_type': 'ULED',
                'refresh_rate': '60 Hz',
                'smart_os': 'VIDAA',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 800}, {'size': '65"', 'price': 1200},
                                 {'size': '75"', 'price': 1600}],
                'image': 'images/hisense_u6.png',
                'promo_link': 'https://example.com/hisense-u6-promo',
                'rating': '⭐⭐'
            },
            {
                'model': 'A7',
                'panel_type': 'LED',
                'refresh_rate': '60 Hz',
                'smart_os': 'VIDAA',
                'hdmi_inputs': 2,
                'sizes_prices': [{'size': '55"', 'price': 700}, {'size': '65"', 'price': 1100},
                                 {'size': '75"', 'price': 1500}],
                'image': 'images/hisense_a7.png',
                'promo_link': 'https://example.com/hisense-a7-promo',
                'rating': '⭐⭐'
            }
        ]
    }
    return render(request, 'bestguide/besthome.html', {'tv_brands': tv_brands})


def testing(request):
    return render(request, 'bestguide/testing2.html')


def motd(request):
    return render(request, 'bestguide/testing.html')

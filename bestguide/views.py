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
                'panel_type': 'OLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 1999.99}, {'size': '65"', 'price': 2799.99},
                                 {'size': '77"', 'price': 3899.99}],
                'image': '/portfolio/assets/teles/sony_bravia8.jpg',
                'promo_link': 'https://www.bestbuy.com/site/sony-55-class-bravia-8-oled-4k-uhd-smart-google-tv-2024/6578569.p?skuId=6578569',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'Bravia 7',
                'panel_type': 'Mini LED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '55"', 'price': 1899.99},
                                 {'size': '65"', 'price': 2299.99},
                                 {'size': '75"', 'price': 2799.99},
                                 {'size': '85"', 'price': 3499.99}],
                'image': '/portfolio/assets/teles/sony_bravia7.png',
                'promo_link': 'https://www.bestbuy.com/site/sony-55-class-bravia-7-mini-led-qled-4k-uhd-smart-google-tv-2024/6578573.p?skuId=6578573',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'X90L',
                'panel_type': 'Full Array LED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '55"', 'price': 1169.99},
                                 {'size': '65"', 'price': 1199.99},
                                 {'size': '75"', 'price': 1699.99},
                                 {'size': '85"', 'price': 2199.99},
                                 {'size': '98"', 'price': 7999.99}],
                'image': '/portfolio/assets/teles/sony_x90l.jpg',
                'promo_link': 'https://www.bestbuy.com/site/sony-55-class-bravia-xr-x90l-led-4k-uhd-smart-google-tv-2023/6544734.p?skuId=6544734',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'Bravia 3',
                'panel_type': 'Direct Lit LED',
                'refresh_rate': '60 Hz',
                'smart_os': 'Google TV',
                'hdmi_inputs': 2,
                'sizes_prices': [{'size': '43"', 'price': 599.99},
                                 {'size': '50"', 'price': 599.99},
                                 {'size': '55"', 'price': 849.99},
                                 {'size': '65"', 'price': 799.99},
                                 {'size': '75"', 'price': 1299.99},
                                 {'size': '85"', 'price': 1799.99}],
                'image': '/portfolio/assets/teles/sony_bravia3.jpg',
                'promo_link': 'https://www.bestbuy.com/site/sony-43-class-bravia-3-led-4k-uhd-smart-google-tv-2024/6578580.p?skuId=6578580',
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
                'sizes_prices': [{'size': '55"', 'price': 2599.99},
                                 {'size': '65"', 'price': 3099.99},
                                 {'size': '77"', 'price': 4599.99}],
                'image': '/portfolio/assets/teles/samsung_s95d.png',
                'promo_link': 'https://www.bestbuy.com/site/samsung-55-class-s95d-series-oled-4k-glare-free-smart-tizen-tv-2024/6576559.p?skuId=6576559',
                'rating': '⭐⭐⭐⭐⭐'
            },
            {
                'model': 'S90D',
                'panel_type': 'OLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '42"', 'price': 1149.99},
                                 {'size': '48"', 'price': 1199.99},
                                 {'size': '55"', 'price': 1499.99},
                                 {'size': '65"', 'price': 1699.99},
                                 {'size': '77"', 'price': 2699.99},
                                 {'size': '83"', 'price': 4499.99}],
                'image': '/portfolio/assets/teles/samsung_s90d.png',
                'promo_link': 'https://www.bestbuy.com/site/samsung-42-class-s90d-series-oled-4k-uhd-smart-tizen-tv-2024/6578067.p?skuId=6578067',
                'rating': '⭐⭐⭐⭐⭐️'
            },
            {
                'model': 'QN90D',
                'panel_type': 'Neo QLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 4,
                'sizes_prices': [{'size': '43"', 'price': 1299.99},
                                 {'size': '50"', 'price': 1399.99},
                                 {'size': '55"', 'price': 1799.99},
                                 {'size': '65"', 'price': 2299.99},
                                 {'size': '75"', 'price': 2599.99},
                                 {'size': '85"', 'price': 4499.99}],
                'image': '/portfolio/assets/teles/samsung_qn90d.png',
                'promo_link': 'https://www.bestbuy.com/site/samsung-43-class-qn90d-series-neo-qled-4k-smart-tizen-tv-2024/6576432.p?skuId=6576432',
                'rating': '⭐⭐⭐⭐'
            },
            {
                'model': 'Q80D',
                'panel_type': 'QLED',
                'refresh_rate': '120 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '50"', 'price': 999.99},
                                 {'size': '55"', 'price': 1099.99},
                                 {'size': '65"', 'price': 1499.99},
                                 {'size': '75"', 'price': 2099.99},
                                 {'size': '85"', 'price': 2299.99}],
                'image': '/portfolio/assets/teles/samsung_q80d.png',
                'promo_link': 'https://www.bestbuy.com/site/samsung-50-class-q80d-series-qled-4k-smart-tizen-tv-2024/6576590.p?skuId=6576590',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'Q60D',
                'panel_type': 'QLED',
                'refresh_rate': '60 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 3,
                'sizes_prices': [{'size': '32"', 'price': 449.99},
                                 {'size': '43"', 'price': 499.99},
                                 {'size': '50"', 'price': 599.99},
                                 {'size': '55"', 'price': 699.99},
                                 {'size': '65"', 'price': 799.99},
                                 {'size': '75"', 'price': 1099.99},
                                 {'size': '85"', 'price': 1599.99}],
                'image': '/portfolio/assets/teles/samsung_q60d.png',
                'promo_link': 'https://www.bestbuy.com/site/samsung-32-class-q60d-series-qled-4k-smart-tizen-tv-2024/6576335.p?skuId=6576335',
                'rating': '⭐⭐⭐'
            },
            {
                'model': 'DU7200',
                'panel_type': 'LED',
                'refresh_rate': '60 Hz',
                'smart_os': 'Tizen',
                'hdmi_inputs': 2,
                'sizes_prices': [{'size': '43"', 'price': 269.99},
                                 {'size': '50"', 'price': 349.99},
                                 {'size': '55"', 'price': 379.99},
                                 {'size': '60"', 'price': 479.99},
                                 {'size': '65"', 'price': 469.99},
                                 {'size': '70"', 'price': 589.99},
                                 {'size': '75"', 'price': 699.99},
                                 {'size': '85"', 'price': 1099.99}],
                'image': '/portfolio/assets/teles/samsung_du7200.png',
                'promo_link': 'https://www.bestbuy.com/site/samsung-43-class-du7200-series-crystal-uhd-4k-smart-tizen-tv-2024/6576342.p?skuId=6576342',
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
                'sizes_prices': [{'size': '55"', 'price': 2499.99},
                                 {'size': '65"', 'price': 3099.99},
                                 {'size': '77"', 'price': 4299.99},
                                 {'size': '83"', 'price': 5999.99},
                                 {'size': '* 97"', 'price': 24999.99}],
                'image': '/portfolio/assets/teles/lg_g4.png',
                'promo_link': 'https://www.bestbuy.com/site/lg-55-class-g4-series-oled-evo-4k-uhd-smart-webos-tv-2024/6578049.p?skuId=6578049',
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

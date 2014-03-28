# installer for bootstrap
#
# Based on installer for xstats (Copyright 2014 Matthew Wall)
#
# 27 March 2014
# Configured by Nick to install bootstrap skin.

from setup import ExtensionInstaller

def loader():
    return BootstrapInstaller()

class BootstrapInstaller(ExtensionInstaller):
    def __init__(self):
        super(BootstrapInstaller, self).__init__(
            version="1.01",
            name='bootstrap',
            description='A skin based around the bootstrap framework',
            author="Nick Dajda",
            author_email="nick.dajda@gmail.com",
            config={
                'StdReport': {
                    'SmallImages': {
                        'skin':'Images'},
                    'BigImages': {
                        'skin':'Images',
                        'HTML_ROOT':'big_images/',
                        'ImageGenerator' : {
                            'image_width' : '800',
                            'image_height' : '500'}},
                    'HTMLPages': {
                        'skin':'Bootstrap'}}},

            files=[('skins/Bootstrap',
                    ['skins/Bootstrap/index.html.tmpl',
                     'skins/Bootstrap/about.html.tmpl',
                     'skins/Bootstrap/history.html.tmpl',
                     'skins/Bootstrap/month.html.tmpl',
                     'skins/Bootstrap/news.html.tmpl',
                     'skins/Bootstrap/stats.html.tmpl',
                     'skins/Bootstrap/week.html.tmpl',
                     'skins/Bootstrap/year.html.tmpl',
                     'skins/Bootstrap/skin.conf']),
                   ('skins/Bootstrap/NOAA',
                    ['skins/Bootstrap/NOAA/NOAA-YYYY.html.tmpl',
                     'skins/Bootstrap/NOAA/NOAA-YYYY-MM.txt.tmpl',
                     'skins/Bootstrap/NOAA/NOAA-YYYY.txt.tmpl']),
                   ('skins/Images', 
                    ['skins/Images/skin.conf']),
                   ('bin/user',
                    ['bin/user/gaugeengine.py',
                     'bin/user/gauges.py',
                     'bin/user/historygenerator.py']),
                   ('public_html/assets/css',
                    ['public_html/assets/css/bootstrap.css',
                     'public_html/assets/css/bootstrap.min.css',
                     'public_html/assets/css/bootstrap-responsive.css',
                     'public_html/assets/css/bootstrap-responsive.min.css',
                     'public_html/assets/css/lightbox.css']),
                   ('public_html/assets/img',
                    ['public_html/assets/img/close.png',
                     'public_html/assets/img/glyphicons-halflings.png',
                     'public_html/assets/img/glyphicons-halflings-white.png',
                     'public_html/assets/img/loading.gif',
                     'public_html/assets/img/next.png',
                     'public_html/assets/img/prev.png']),
                   ('public_html/assets/js',
                    ['public_html/assets/js/bootstrap.min.js',
                     'public_html/assets/js/jquery-1.7.2.min.js',
                     'public_html/assets/js/lightbox.js'])
                   ]
            )


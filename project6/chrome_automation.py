import webbrowser as wb

def webAuto():
    chrome_path = 'C:\Program Files (x86)\Mozilla Firefox\firefox.exes %s'
    urls = (
        'stackoverflow.com',
        'github.com/manishhedau',
        'gmail.com',
        'google.com',
        'youtube.com'
    )
    for url in urls:
        print('Opening : '+url)
        wb.get(chrome_path).open(url)

webAuto()

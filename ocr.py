import easyocr
reader = easyocr.Reader(['en'], gpu = False)

def extractpassage(imgurl):
    results = reader.readtext(imgurl)
    passage = '';
    conf = 0;
    for result in results:
        newres = result[1:];
        passage = passage + ' ' +newres[0];
        conf = conf + newres[1];
    conf = conf / len(results);
    conf = conf * 100;
    conf = round(conf, 2);
    return passage, conf;
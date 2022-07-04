from xml.etree import ElementTree as et


PATH = '34.osm'


def main():
    with open(PATH, 'r', encoding='utf-8') as file:
        data = file.readlines()
    root = et.fromstringlist(data)
    hospitals = []
    for appt in list(root):
        is_hospital = False
        adress = ''
        name = ''
        for elem in list(appt):
            if elem.get('v') == 'hospital':
                is_hospital = True
            if elem.get('k') == 'name':
                name = elem.get('v')
            if elem.get('k') == 'addr:housenumber':
                adress = elem.get('v')
            if elem.get('k') == 'addr:street':
                adress = elem.get('v') + ' ' + adress
        if is_hospital:
            hospitals.append((name, adress))
    print(len(hospitals))
    print(*sorted(hospitals, key=lambda x: x[1]), sep='\n')


if __name__ == '__main__':
    main()

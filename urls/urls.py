def parse_file(file_path):
    file = open(file_path)
    retailer_list = []

    for line in file:
        try: 
            words_in_line = len(line.split())
            if (words_in_line != 2 and words_in_line != 0):
                raise Exception(f'[Malformed URL File]: File - {file_path} | Line - {line}')
            [retailer, url] = line.split()
            
            retailer_list.append({retailer: url})
        except:
            file.close()
    file.close()
    return retailer_list

BASE_DIR = './data/'

XBOX_SERIES_X_URLS = parse_file(f'{BASE_DIR}xbox_series_x_urls.txt')
XBOX_SERIES_S_URLS = parse_file(f'{BASE_DIR}xbox_series_s_urls.txt')
PS5_DISK_URLS = parse_file(f'{BASE_DIR}ps5_disk_urls.txt')
PS5_NODISK_URLS = parse_file(f'{BASE_DIR}ps5_nodisk_urls.txt')
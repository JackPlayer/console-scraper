"""
Parses files containing urls to product pages
"""

def parse_file(file_path):
    """Parse file with lines: retailer url

    Args: 
        file_path: The path to the url file

    Returns:
        dict: {'retailer1': 'url1', 'retailer2': 'url2'...}

    """
    file = open(file_path)
    retailer_dict = {}

    for line in file:
        try: 
            words_in_line = len(line.split())

            # Malformed line. 
            if (words_in_line != 2 and words_in_line != 0):
                raise Exception(f'[Malformed URL File]: File - {file_path} | Line - {line}')
            [retailer, url] = line.split()
            
            retailer_dict[retailer] = url
        except:
            file.close()
    file.close()
    return retailer_dict

def get_urls(base_dir):
    """Gets the URLS from the console url files

    Args:
        base_dir: Directory where the url files are located
    
    Returns:
        dict: {'console':{'retailer1':'url1',...},...}
    """
    XBOX_SERIES_X_URLS = parse_file(f'{base_dir}xbox_series_x_urls.txt')
    XBOX_SERIES_S_URLS = parse_file(f'{base_dir}xbox_series_s_urls.txt')
    PS5_DISK_URLS = parse_file(f'{base_dir}ps5_disk_urls.txt')
    PS5_NODISK_URLS = parse_file(f'{base_dir}ps5_nodisk_urls.txt')
    return {
        'XBOX_SERIES_X_URLS': XBOX_SERIES_X_URLS,
        'XBOX_SERIES_S_URLS': XBOX_SERIES_S_URLS,
        'PS5_DISK_URLS': PS5_DISK_URLS,
        'PS5_NODISK_URLS': PS5_NODISK_URLS,
    }

import urllib.request
import os

data_indices = ['000014', '000014', '000019', '000019', '000035', '000035', '000058', '000058', '000063', '000063', '000070', '000070', '000155', '000155', '000333', '000333', '000402', '000402', '000409', '000409', '000513', '000513', '000522', '000522', '000524', '000524', '000546', '000546', '000568', '000568', '000583', '000583', '000606', '000606', '000615', '000615', '000631', '000631', '000633', '000633', '000651', '000651', '000677', '000677', '000725', '000725', '000733', '000733', '000735', '000735', '000763', '000763', '000779', '000779', '000792', '000792', '000801', '000801', '000825', '000825', '000848', '000848', '000856', '000856', '000877', '000877', '000898', '000898', '000912', '000912', '000921', '000921', '000927', '000927', '000932', '000932', '000935', '000935', '000950', '000950', '000952', '000952', '000962', '000962', '000969', '000969', '000975', '000975', '000979', '000979', '002003', '002003', '002004', '002004', '002010', '002010', '002018', '002018', '002019', '002019', '002020', '002020', '002021', '002021', '002022', '002022', '002037', '002037', '002042', '002042', '002047', '002047', '002049', '002049', '002052', '002052', '002062', '002062', '002070', '002070', '002095', '002095', '002113', '002113', '002120', '002120', '002134', '002134', '002135', '002135', '002140', '002140', '002162', '002162', '002168', '002168', '002185', '002185', '002193', '002193', '002199', '002199', '002211', '002211', '002252', '002252', '002253', '002253', '002283', '002283', '002284', '002284', '002314', '002314', '002318', '002318', '002320', '002320', '002328', '002328', '002346', '002346', '002352', '002352', '002353', '002353', '002361', '002361', '002383', '002383', '002399', '002399', '002401', '002401', '002411', '002411', '002419', '002419', '002425', '002425', '002448', '002448', '002452', '002452', '002460', '002460', '002463', '002463', '002472', '002472', '002496', '002496', '002500', '002500', '002506', '002506', '002539', '002539', '002547', '002547', '002557', '002557', '002558', '002558', '002560', '002560', '002571', '002571', '002585', '002585', '002595', '002595', '002598', '002598', '002613', '002613', '002628', '002628', '002673', '002673', '002679', '002679', '002683', '002683', '002686', '002686', '002687', '002687', '002692', '002692', '002697', '002697', '002700', '002700', '002724', '002724', '002746', '002746', '002751', '002751', '002768', '002768', '002770', '002770', '002774', '002774', '002785', '002785', '002792', '002792', '002816', '002816', '002820', '002820', '002838', '002838', '002841', '002841', '002855', '002855', '002872', '002872', '002892', '002892', '002906', '002906', '002913', '002913', '002920', '002920', '300003', '300003', '300008', '300008', '300029', '300029', '300030', '300030', '300051', '300051', '300065', '300065', '300068', '300068', '300076', '300076', '300079', '300079', '300082', '300082', '300083', '300083', '300087', '300087', '300096', '300096', '300102', '300102', '300106', '300106', '300120', '300120', '300124', '300124', '300139', '300139', '300147', '300147', '300153', '300153', '300154', '300154', '300159', '300159', '300181', '300181', '300187', '300187', '300213', '300213', '300220', '300220', '300225', '300225', '300235', '300235', '300236', '300236', '300242', '300242', '300247', '300247', '300257', '300257', '300271', '300271', '300278', '300278', '300286', '300286', '300292', '300292', '300299', '300299', '300307', '300307', '300320', '300320', '300322', '300322', '300324', '300324', '300329', '300329', '300338', '300338', '300348', '300348', '300356', '300356', '300389', '300389', '300398', '300398', '300403', '300403', '300414', '300414', '300422', '300422', '300426', '300426', '300438', '300438', '300441', '300441', '300445', '300445', '300452', '300452', '300456', '300456', '300467', '300467', '300469', '300469', '300492', '300492', '300495', '300495', '300507', '300507', '300526', '300526', '300529', '300529', '300542', '300542', '300571', '300571', '300580', '300580', '300587', '300587', '300618', '300618', '300626', '300626', '300643', '300643', '300654', '300654', '300656', '300656', '300663', '300663', '300686', '300686', '300688', '300688', '300690', '300690', '300707', '300707', '300713', '300713', '300730', '300730', '600008', '600008', '600020', '600020', '600023', '600023', '600027', '600027', '600037', '600037', '600048', '600048', '600052', '600052', '600060', '600060', '600067', '600067', '600073', '600073', '600076', '600076', '600091', '600091', '600093', '600093', '600102', '600102', '600104', '600104', '600106', '600106', '600126', '600126', '600139', '600139', '600141', '600141', '600157', '600157', '600165', '600165', '600175', '600175', '600178', '600178', '600242', '600242', '600255', '600255', '600261', '600261', '600269', '600269', '600293', '600293', '600307', '600307', '600332', '600332', '600340', '600340', '600343', '600343', '600359', '600359', '600380', '600380', '600399', '600399', '600410', '600410', '600480', '600480', '600485', '600485', '600513', '600513', '600533', '600533', '600537', '600537', '600543', '600543', '600547', '600547', '600557', '600557', '600590', '600590', '600594', '600594', '600605', '600605', '600616', '600616', '600627', '600627', '600631', '600631', '600637', '600637', '600644', '600644', '600659', '600659', '600673', '600673', '600684', '600684', '600701', '600701', '600731', '600731', '600736', '600736', '600740', '600740', '600779', '600779', '600780', '600780', '600784', '600784', '600821', '600821', '600826', '600826', '600834', '600834', '600842', '600842', '600870', '600870', '600871', '600871', '600885', '600885', '600897', '600897', '600903', '600903', '600967', '600967', '601003', '601003', '601008', '601008', '601113', '601113', '601126', '601126', '601128', '601128', '601139', '601139', '601177', '601177', '601208', '601208', '601225', '601225', '601228', '601228', '601288', '601288', '601398', '601398', '601515', '601515', '601555', '601555', '601567', '601567', '601898', '601898', '601988', '601988', '601999', '601999', '603012', '603012', '603032', '603032', '603033', '603033', '603066', '603066', '603086', '603086', '603090', '603090', '603178', '603178', '603179', '603179', '603223', '603223', '603226', '603226', '603316', '603316', '603320', '603320', '603330', '603330', '603333', '603333', '603355', '603355', '603385', '603385', '603533', '603533', '603535', '603535', '603656', '603656', '603659', '603659', '603678', '603678', '603833', '603833', '603906', '603906', '603939', '603939', '603970', '603970']


def save_csv(filename, content_str):
    with open('./dataset/debug/{}.csv'.format(filename), 'w', newline='') as f:
        content_str = content_str.replace('index', 'date')
        f.write(content_str)

def download():
    path = './dataset/debug'
    file_list = os.listdir(path)
    for index in data_indices:
        if '{}.csv'.format(index) in file_list:
            continue
        headers = {
            'Host': f'www.ricequant.com',
            'Connection': r'keep-alive',
            'Upgrade-Insecure-Requests': 1,
            'User-Agent': r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'DNT': 1,
            'Referer': r'https://www.ricequant.com/research/user/user_306589/edit/data/toothless_sixth/{}.csv'.format(index),
            'Accept-Encoding': r'gzip, deflate, br',
            'Accept-Language': r'zh-CN,en-US;q=0.8,en;q=0.6,de-DE;q=0.4,de;q=0.2,zh;q=0.2',
            'Cookie': r'jupyter-hub-token-user_306589="2|1:0|10:1514433744|29:jupyter-hub-token-user_306589|44:YjA2YWExNGRkYWZjNDkwNjg5Yzg2NjQxMTg2OWU5MGQ=|464d94b461e88494b1ddde513e98c2372353b01d802c1b9b034f3693eebdea44"; jupyter-hub-token="2|1:0|10:1514433744|17:jupyter-hub-token|44:YjA2YWExNGRkYWZjNDkwNjg5Yzg2NjQxMTg2OWU5MGQ=|57254ee374ae1eed9c32e751b668bbbc9598cc9c5dc3864e12c468693a882a02"; jupyter-hub-token-user_306589="2|1:0|10:1514433744|29:jupyter-hub-token-user_306589|44:YjA2YWExNGRkYWZjNDkwNjg5Yzg2NjQxMTg2OWU5MGQ=|464d94b461e88494b1ddde513e98c2372353b01d802c1b9b034f3693eebdea44"; gr_user_id=87c052b3-1697-42ab-a53a-2b442206818d; tgw_l7_route=d0bf4a9ab78d53762b596c0a48da8e7f; sid=665b11b7-adf8-4b88-ba84-1812f248da5b|fcfdc11056de5b87fe5bb7991592916c789d4bcdf8f9399dd63d8f75c900cf24b1eb06054fe72bcf3044320339523c696bf28369b12cc6d088093d2406d1f4db; gr_session_id_9bc6807c25b59135=7fae9f24-4d49-417f-b661-f61c471192cf; gr_cs1_7fae9f24-4d49-417f-b661-f61c471192cf=user_id%3A306589; Hm_lvt_cb81fd54150b99e25d085d58bbaf4a07=1514182193,1514343159; Hm_lpvt_cb81fd54150b99e25d085d58bbaf4a07=1514444278'
        }
        try:
            url = 'https://www.ricequant.com/research/user/user_306589/files/data/toothless_sixth/{}.csv?download=1'.format(index)
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as response:
                response_str = response.read().decode('gbk', 'ignore')
                print(response_str)
                save_csv(index, response_str)
        except:
            print('timeout')
            continue

    file_list = os.listdir(path)
    for f in file_list:
        file_path = os.path.join(path, f)
        with open(file_path, 'r') as fil:
            lines = fil.readlines()
            if len(lines) < 100:
                os.remove(file_path)
                print('remove {}, {}'.format(f, len(lines)))
    print('Done')


def get_list(tar, s):
    result = []
    ix = s.find(tar)
    while ix > -1:
        result.append(s[ix-6:ix])
        s = s[ix+len(tar):]
        ix = s.find(tar)
    return result


if __name__ == "__main__":
    print('start download')
    download()

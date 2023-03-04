import json
import os
import hashlib

def get_hash(filename):
    blocks = os.curdir + '/blocks/'
    return hashlib.md5(open(blocks + filename, 'rb').read()).hexdigest()

def check_block():
    blocks = os.curdir + '/blocks/'
    files = os.listdir(blocks)
    files = sorted([int(i) for i in files])
    result = []
    for file in files[1:]:
        f = open(blocks  + str(file))
        h = json.load(f)['hash']
        prev_hash = str(file - 1)
        actual_hash = get_hash(str(file - 1))
        if h == actual_hash:
            res = 'Не изменен'
        else:
            res = 'Изменен'
        result.append({
            'block' : f'block {prev_hash}',
            'res' : res
        })
    return result



def write_block(name, amount, to_whom, prev_hash=''):
    blocks_dir = os.curdir + '/blocks/'
    files = os.listdir(blocks_dir)
    files = sorted([int(i) for i in files])
    last_file = files[-1]
    filename = str(last_file + 1)
    prev_hash = get_hash(str(last_file))
    data = {
        'name': name,
        'amout': amount,
        'to_whom': to_whom,
        'hash': prev_hash
    }
    with open(blocks_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    # write_block('Aman', 2000, 'Kuban')
    print(check_block())

if __name__ == '__main__':
    main()
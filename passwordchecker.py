import requests
import hashlib
import sys

'''
Info: We are using the website https://haveibeenpwned.com/API/v3#PastesForAccount and API here,
this has list of emails and passwords that has been compromised so far
'''


def request_api_data(qury_char):
    '''
    This retruns the response from the input url, this respose will have matched rest of the hashes part from the given 5 charter input hash
    :param qury_char: last 5 digits of hash code [SHA-1 password hash]
    :return: respose 400 or 200 , this has text part to it res.text which will  have all hashes
    '''
    url = 'https://api.pwnedpasswords.com/range/' + qury_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Run Time Error: {res.status_code} please check the API and try again')
    return res


def get_password_leaks_count(in_hashes, in_tail):
    '''
    This compares the tail hash with our passwords tail hash if its matches get the count of it
    :param in_hashes: all hashes generated
    :param in_tail: our tail hash
    :return: count of matched , 0 if not matched
    '''
    hashes = (line.split(':') for line in in_hashes.text.splitlines())
    for h, count in hashes:
        # print(h, count)
        if h == in_tail:
            return count
    return 0


def pwed_api_get_hashes(password):
    '''
    This generates hash for our input password, splits first 5 char and rest which is tail
    This is calling request_api_data and get_password_leaks_count
    :param password: our testing password
    :return: count and tail of password
    '''
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5char, tail = sha1password[:5], sha1password[5:]
    hashes = request_api_data(first5char)
    return get_password_leaks_count(hashes, tail)


def main(args):
    '''
    This initiates the process takes system arguments of your passwords
    :param args: your test password or passwords
    :return: give the final text prompt!
    '''
    for password in args:
        count = pwed_api_get_hashes(password)
        if count:
            print(f'This {password} has been pawed {count}, Therefore requested to CHANGE your password')
        else:
            print(f'That a GOOD password! this {password} was NOT found')
    return 'Done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

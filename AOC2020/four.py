from aocd.models import Puzzle
from aocd import submit
import re


puzzle = Puzzle(year=2020, day=4)

test_data = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm\n\niyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\nhcl:#cfa07d byr:1929\n\nhcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm\n\nhcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in'


def count_valid_passports(data):
    valid = 0
    required_regex = re.compile(r'byr|iyr|eyr|hgt|hcl|ecl|pid')
    for person in data.split('\n\n'):
        fields = required_regex.findall(person)
        if len(fields) == 7:
            valid += 1
    return valid

def count_valid_passports_b(data):
    try:
        valid_count = 0
        valid_field_count = 0
        required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for idx, passport in enumerate(data.split('\n\n')):
            passport_d = dict()
            valid = True
            field_valid = True
            for record in re.split('\s', passport):
                key, val = record.split(':')
                passport_d[key] = val
            for f in required_fields:
                if f not in passport_d:
                    valid = False
            if valid:
                valid_count += 1
                yr_regex = r'\d{4}'
                byr = int(passport_d['byr'])
                iyr = int(passport_d['iyr'])
                eyr = int(passport_d['eyr'])

                hgt_regex = r'\d{2,3}(cm|in)'
                hgt = passport_d['hgt']
                hgt_int = int(re.match(r'\d+', hgt).group())

                hcl_regex = r'#\w{6}$'
                hcl = passport_d['hcl']

                eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                ecl = passport_d['ecl']

                pid_regex = r'\d{9}$'
                pid = passport_d['pid']

                byr_valid = iyr_valid = eyr_valid = hgt_valid = hcl_valid = ecl_valid = pid_valid = True

                if re.match(yr_regex, passport_d['byr']):
                    if byr < 1920 or byr > 2002:
                        byr_valid = False
                else:
                    byr_valid = False

                if re.match(yr_regex, passport_d['iyr']):
                    if iyr < 2010 or iyr > 2020:
                        iyr_valid = False
                else:
                    iyr_valid = False

                if re.match(yr_regex, passport_d['eyr']):
                    if eyr < 2020 or eyr > 2030:
                        eyr_valid = False
                else:
                    eyr_valid = False

                if re.match(hgt_regex, hgt):
                    if hgt.endswith('cm'):
                        if hgt_int < 150 or hgt_int > 193:
                            hgt_valid = False
                    elif hgt.endswith('in'):
                        if hgt_int < 59 or hgt_int > 76:
                            hgt_valid = False
                else:
                    hgt_valid = False

                if not re.match(r'#\w{6}$', hcl):
                    hcl_valid = False

                if ecl not in eye_colors:
                    ecl_valid = False

                if not re.match(r'\d{9}$', pid):
                    pid_valid = False
                conditions = [byr_valid, iyr_valid, eyr_valid, hgt_valid, hcl_valid, ecl_valid, pid_valid]
                if all(conditions):
                    valid_field_count += 1
    except:
        pass
    return valid_field_count

ans_b = count_valid_passports_b(puzzle.input_data)

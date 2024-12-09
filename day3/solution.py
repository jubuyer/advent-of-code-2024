import re
input_file = "data.txt"

# part 1
def p1():
    with open(input_file) as f:
        lines = f.read().splitlines()
        muls = re.findall("mul\(\d*,?\d*\)",str(lines))
        out = 0
        for mul in muls:
            nums=re.findall('\d*', mul)
            nums = [int(x) for x in nums if x.isnumeric()]
            # print(re.findall('\d*', mul))
            out+=(nums[0]*nums[1])
    print(out)
    return out
# part 2
def p2():
    with open(input_file) as f:
        lines = f.read().splitlines()
        enabled = re.split("do\(\).*don't\(\)",str(lines))
        preenabled = re.split("^.*don't\(\)",str(lines))
        postenabled = re.split("don't\(\).*$",str(lines))
        
        muls = re.findall("mul\(\d*,?\d*\)",str(enabled))
        muls.extend(re.findall("mul\(\d*,?\d*\)",str(preenabled)))
        muls.extend(re.findall("mul\(\d*,?\d*\)",str(postenabled)))
        print(muls)
        out = 0
        for mul in muls:
            nums=re.findall('\d*', mul)
            nums = [int(x) for x in nums if x.isnumeric()]
            # print(re.findall('\d*', mul))
            out+=(nums[0]*nums[1])
    print(out)
p1()
p2()
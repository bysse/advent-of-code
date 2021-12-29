import os
import re
from functools import reduce
from itertools import chain

def groups(filename, fn=None):
    """Iterator for blank line separated groups in a file without starting or trailing whitespace"""
    if not fn:
        fn = lambda x: x
    with open(filename, 'r') as fd:
        for group in fd.read().split("\n\n"):
            if group:
                yield [fn(x.strip()) for x in group.split("\n")]
 
def lines(filename):
    """Iterator for lines in a file without starting or trailing whitespace"""
    with open(filename, 'r') as fd:
        for line in fd:
            yield line.rstrip()
   

def ints(string):
    """Returns a list of all integers in the string"""
    return list(map(int, re.findall("-?[0-9]+", string)))


def extract(string, patterns, optional=False):
    """Returns the matching strings for a list of regex expressions sequentially over a string"""
    offset = 0
    result = []
    if type(patterns) != list:
        patterns = [patterns]
    for pattern in patterns:
        m = re.search(pattern, string[offset:])
        if not m:
            if optional:
                result.append(None)
            else:
                raise Exception("Can't find '" + str(pattern) + "' in string '" + string + "'")            
        offset += m.end()
        groups = m.groups()
        if groups:
            for g in groups:
                result.append(g)
        else:
            result.append(m.group(0))
    return result


def match(pattern, string):
    """Matches the pattern on the complete string"""
    return re.fullmatch(pattern, string)

def toRGB(color):
    return ((color>>16) & 0xff, (color>>8) & 0xff, color & 0xff)

def toInt(rgb):
    return (rgb[0]<<16) + (rgb[1]<<8) + (rgb[2])

def gcd(a, b):
    """Greatest common denominator"""
    if b == 0:
        return 1
    return gcd(a, a % b)

def lcd(a, b):
    """Lowest common denominator"""
    return a*b / gcd(a,b)    

#
# 2D 
#

def load2D(filename):
    data = []
    width = 0
    for line in lines(filename):
        width = max(width, len(line))
        data.append([x for x in line])    
    return data, len(data), width


def flatten2D(data):
    return "\n".join(map(lambda line: "".join(map(str, line)), data))


def find2D(needle, haystack):
    for y in range(len(haystack)):
        row = haystack[y]
        for x in range(len(row)):
            if needle == row[x]:
                return (x, y)
    return None


def count2D(needle, haystack):
    flat = chain.from_iterable(haystack)
    return reduce(lambda a, x: a+(1 if x == needle else 0), flat, 0)


def trace2D(x, y, dx, dy, w, h):
    while True:
        x += dx
        y += dy
        if x < 0 or y < 0 or x >= w or y >= h:
            break
        yield (x, y)

def iterate2D(data):
    for y in range(len(data)):
        row = data[y]
        for x in range(len(row)):
            yield x, y, row[x]

def tdlr2D(x, y, width, height, includeCenter=False):
    """ Iterator for top, down, left, right adjacent coordinates within the specified rect"""
    for dy in [-1, 1]:
        if y + dy < 0 or y + dy >= height:
            continue
        yield (x, y+dy)
    
    for dx in [-1, 1]:
        if x + dx < 0 or x + dx >= width:
            continue
        yield (x+dx, y)
    if includeCenter:
        yield (x, y)

def adjacent2D(x, y, width, height, includeCenter=False):
    """ Iterator for all adjacent coordinates within the specified rect"""
    for dy in range(-1, 2):
        if y + dy < 0 or y + dy >= height:
            continue
        for dx in range(-1, 2):
            if dx == 0 and dy == 0 and not includeCenter:
                continue
            if x + dx < 0 or x + dx >= width:
                continue
            yield (x+dx, y+dy)

def dump2D(data):
    height = len(data)
    width = max([len(row) for row in data])
    for y in range(height):
        line = data[y]
        for x in range(len(line)):
            print(line[x], end='')
        print()

def display2D(data, colors=None, output="data.png", scale=3, load=True, enable=True):
    if not enable:
        return
    if not colors:
       colors = {
                " ": (0, 0, 0),
                ".": ( 20, 20, 20),
                "#": (190,190,190),
                "|": (190, 80, 80),
                "-": (190, 80,120),
                "+": (190,120, 80)
            }

    def colorFor(x):
        if x not in colors:
            h = hash(x) & 0xffffff
            colors[x] = toRGB(h) #( (h>>16)&0xff, (h>>8)&0xff, h&0xff )
        return colors[x]                            

    height = len(data)
    width = max([len(row) for row in data])
    
    from PIL import Image
    image = Image.new('RGB', (width*scale, height*scale), "black")
    pixels = image.load()

    for y in range(height):
        line = data[y]
        for x in range(len(line)):
            if scale == 1:
                pixels[x,y] = colorFor(line[x])
            else:
                for dy in range(scale):
                    for dx in range(scale):
                        pixels[x*scale+dx,y*scale+dy] = colorFor(line[x])
        
    image.save(output)

    if load:        
        os.system("xdg-open " + str(output))


class Map(dict):
    """
    Example:
    m = Map({'first_name': 'Eduardo'}, last_name='Pool', age=24, sports=['Soccer'])
    """
    def __init__(self, *args, **kwargs):
        super(Map, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.iteritems():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.iteritems():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]


def summary(filename):    
    from statistics import mean, median
    data = list(lines(filename))
    print("Filename:    ", filename)
    print("Line count:  ", len(data))
    print("Empty lines: ", len(list(filter(lambda x: not x, data))))

    cols = []
    for line in data:
        cols.append(len(re.split(r'[ ,]+', line)))
    
    print("Columns:")
    print("  Average:    {:.1f}".format(mean(cols)))
    print("  Median:     {:.1f}".format(median(cols)))
    print("  Min:        {}".format(min(cols)))
    print("  Max:        {}".format(max(cols)))
    print("  Length:     {}".format(mean([len(x) for x in data])))

    print()
    if len(data) < 10:
        print("First 100 bytes:")
        print(data[0][:100])
    else:
        print("First 10 lines:")
        print("\n".join(data[:10]))

    

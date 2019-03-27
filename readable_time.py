def make_readable2(seconds):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
    
def make_readable(seconds):
    l = lambda s: (int(s/60), s%60)
    mm, ss = l(seconds)
    hh, mm = l(mm)
    return '%02d:%02d:%02d'%(hh,mm,ss)

print(make_readable(5))
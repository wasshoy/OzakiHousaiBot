with open('../data/interim/aozora-ozaki-mod.txt') as f:
    text = f.read()
lines = text.splitlines()
lines = [l.strip() for l in lines if not(len(l) == 0 or l[0] == '（')]
with open('../data/processed/aozora-ozaki-ku.txt', 'w') as f:
    f.write('\n'.join(lines))

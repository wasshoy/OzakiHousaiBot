from collections import defaultdict, deque
from dataclasses import dataclass
import random
import MeCab


tagger = MeCab.Tagger(
    '-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')


@dataclass
class NMarkovHousai:
    n = 2
    max_len = 25
    _model = defaultdict(list)

    def make_model(self, text):
        lines = text.split('\n')
        for l in lines:
            deq = deque(['[BOS]'], self.n)
            for c in l:
                key = tuple(deq)
                self._model[key].append(c)
                deq.append(c)
            key = tuple(deq)
            self._model[key].append('[EOS]')

    def make_sentence(self):
        value_list = []
        deq = deque([], self.n)
        deq.append('[BOS]')
        key = tuple(deq)
        while len(value_list) < 25:
            key = tuple(deq)
            value = random.choice(self._model[key])
            if value == '[EOS]':
                break
            value_list.append(value)
            deq.append(value)
        return ''.join(value_list)


if __name__ == '__main__':
    with open('../data/processed/aozora-ozaki-ku.txt') as f:
        text = f.read()
        order = 3
        housai = NMarkovHousai()
        housai.make_model(text)
        for _ in range(10):
            print(housai.make_sentence())

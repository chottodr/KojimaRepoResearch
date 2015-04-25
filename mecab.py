#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MeCab

m = MeCab.Tagger("-Ochasen")

text = raw_input(">")
print m.parse(text)

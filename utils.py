#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# JSM product code
#
# (C) Copyright 2017 Juxt SmartMandate Pvt Ltd
# All right reserved.
#
# This file is confidential and NOT open source.  Do not distribute.
#

"""
Utilities for running the sentinel code
"""

import string
from nltk.corpus import stopwords


try:
    stops = stopwords.words('english')
except LookupError:
    import nltk
    nltk.download('stopwords')
    stops = stopwords.words('english')

make_lowercase = lambda x: x.lower()
remove_unicode = lambda x: x.encode('ascii', 'ignore').decode('utf-8')
remove_tabs = lambda message: message.replace('\t', ' ')
remove_carriages = lambda message: message.replace('\r', ' ')
remove_newlines = lambda message: message.replace('\n', ' ')

get_transtable = lambda x: dict.fromkeys(map(ord, x), None)


def remove_stopwords(x):
    """Remove English stopwords from a sentence.

    :param x: String containing the sentence to remove stopwords from.
    :type x: str

    :return: String with stopwords removed.
    :rtype: str

    :Example:
    >>> sentence = '''\
    It was the best of times, it was the worst of times, it was the age of
    wisdom, it was the age of foolishness.'''
    >>> print remove_stopwords(sentence)
    It best times, worst times. It best times, worst times, age wisdom, age
    foolishness.
    """
    words = x.split(" ")
    return " ".join([w for w in words if w not in stops])


def remove_digits(x):
    """Remove digits from a string.

    :param x: String to remove digits from
    :type x: str

    :return: String with digits removed
    :rtype: str
    """
    return x.translate(get_transtable(string.digits))


def remove_punctuation(x):
    """Remove punctuation from a sentence. Any character in
    `string.punctuation` is removed.

    :param x: Sentence to remove punctuations from.
    :type x: str

    :return: String with punctuation removed.
    :rtype: str

    :Example:
    >>> sentence = '''\
    It was the best of times, it was the worst of times, it was the age of
    wisdom, it was the age of foolishness.'''
    >>> print remove_stopwords(sentence)
    It was the best of times it was the worst of times It was the best of times
    it was the worst of times it was the age of wisdom it was the age of
    foolishness
    """
    return x.translate(get_transtable(string.punctuation))

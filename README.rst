colorize pinyin
===============

search for chinese pinyin and wrap it with HTML.

module provides some useful functions for working with Chinese pinyin,
"phonetic system for transcribing the Mandarin pronunciations of
Chinese characters into the Latin alphabet" (c) `wikipedia <https://en.wikipedia.org/wiki/Pinyin>`_
.

usage sample
============

    >>> colorized_HTML_string_from_string('nǐ hǎo')
    '<span class="pinYinWrapper"><span class="t3">nǐ</span> <span class="t3">hǎo</span></span>'

    >>> ranges_of_pinyin_in_string('nǐ hǎo')
    [Range(location=0, length=2), Range(location=3, length=3)]  # == [(0, 2), (3, 3)]

requirements
============

``lxml`` is only required if you want to work with DOM.  but it does not listed in requirements because if you want to use them, surely you already have ``lxml`` on the board; for other cases we don't need additional third-party libs.

functions that designed to work with ``lxml`` marked with ``[*]``.

functions
=========

modify given DOM by replacing children text nodes containing pinyin with
wrapper element:

``colorize_DOM`` ``[*]``

undo colorize:

``uncolorize_DOM`` ``[*]``

detect and wrap pinyin with HTML in plain text string:

``colorized_HTML_string_from_string``

do the same, but returns a wrapper -- DOM element:

``colorized_HTML_element_from_string`` ``[*]``

searching for pinyin in string of text:

``ranges_of_pinyin_in_string``

finding out what tone has some pinyin word:

``determine_tone``

remove tones (diacritics) from pinyin string:

``lowercase_string_by_removing_pinyin_tones``

constants
=========

``PINYIN_LIST`` -- specially sorted list of all possible pinyin words.

``PINYIN_LIST_BY_LEN`` -- same as ``PINYIN_LIST`` but grouped by len descending.

``PINYIN_WRAPPER_CLASS`` -- default class used by ``[un]colorize_DOM``.

classes
=======

``Range`` -- 2-named-tuple with ``[0]`` location and ``[1]`` length.

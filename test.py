#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyleft 2016 Ratijas <ratijas.t@me.com>
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

import unittest
import colorize_pinyin

_1_baiwen = u'bǎiwén bùrú yījiàn // fāng’àn // fǎngán // xúniang'
_2_baiwen = u'2 bǎiwén'
_3_nongmingong = u'3 nóngmíngōng'
_4_kou_anshang = u'4 kǒu’ànshàng'
_5_kouanshang = u'5 kǒuànshàng'
_6_fengongsi = u'6 fēngōngsī'
_7_aiyo = u'7 āiyō'
_8_shenme = u'8 shénme'
_9_fadia = u'9 fādiǎ'
_10_zhiding = u'10 zhǐdìng'
_11_yi1_yi4 = u'11 yī; yì'
_12_nanguo_langxingoufei_er_eryide = u'12 nánguò // lángxīngǒufèi // èr’ěryīde'
_13_trailing = u'hánshùshì[de]'


class IgnoreLinksNodeFilterTestCase(unittest.TestCase):
    def setUp(self):
        import lxml.etree as ET
        self.ET = ET
        self.cmd = colorize_pinyin.ignore_links_node_filter

    def test_link_tag(self):
        link = self.ET.fromstring("""<A HREF='http://bkrs.info/slovo.php?ch=仁'>仁</A>""")
        self.assertFalse(self.cmd(link))

    def test_other(self):
        tag = self.ET.fromstring(
            """<div class="py">rén<img class="pointer" src="images/player/negative_small/playup.png" /></div>""")
        self.assertTrue(self.cmd(tag))


class ColorizeUncolorizeDOMTestCase(unittest.TestCase):
    def setUp(self):
        import lxml.etree as ET
        self.ET = ET
        self.maxDiff = None

    def test_bkrs_ch_ru(self):
        html_in = self.ET.fromstring(u'''<div class="ch_ru"><div>1) 从属[的] cóngshǔ[de]</div>
<div class="m2"><div class="ex">функциональные отношения - 从属关系</div></div>
<div>2) 机能[的] jīnéng[de], 宫能[的] guānnéng[-de]; 职能[的] zhínéng[de]</div>
<div class="m2"><div class="ex">функциональное заболевание - 官能[性]病</div></div>
<div class="m2"><div class="ex">функциональная ценность денег - 货币的职能价值</div></div>
<div>3) <i class="green">мат.</i> 函数[的] hánshù[de], 函数式[的] hánshùshì[de]</div>
</div>''')
        html_expected = self.ET.tostring(self.ET.fromstring(u'''<div class="ch_ru"><div><span class="pinYinWrapper">1) 从属[的] <span class="t2">cóng</span><span class="t3">shǔ</span>[<span class="t0">de</span>]</span></div>
<div class="m2"><div class="ex">функциональные отношения - 从属关系</div></div>
<div><span class="pinYinWrapper">2) 机能[的] <span class="t1">jī</span><span class="t2">néng</span>[<span class="t0">de</span>], 宫能[的] <span class="t1">guān</span><span class="t2">néng</span>[-<span class="t0">de</span>]; 职能[的] <span class="t2">zhí</span><span class="t2">néng</span>[<span class="t0">de</span>]</span></div>
<div class="m2"><div class="ex">функциональное заболевание - 官能[性]病</div></div>
<div class="m2"><div class="ex">функциональная ценность денег - 货币的职能价值</div></div>
<div>3) <i class="green">мат.</i><span class="pinYinWrapper"> 函数[的] <span class="t2">hán</span><span class="t4">shù</span>[<span class="t0">de</span>], 函数式[的] <span class="t2">hán</span><span class="t4">shù</span><span class="t4">shì</span>[<span class="t0">de</span>]</span></div>
</div>'''), encoding='unicode')
        colorize_pinyin.colorize_DOM(html_in)
        html_out = self.ET.tostring(html_in, encoding='unicode')
        self.assertEqual(html_out, html_expected)

    def test_omit_with_filter(self):
        html_in = self.ET.fromstring(u'''\
<div class="forum-post">
    <div class="author"><a href="/user/lǎowài">lǎowài</a></div>
    <div class="content">
        ...
        теперь выбираем цвета, и скачиваем ещё один архивчик:
        <ul>
            <li>(百闻不如一见 bǎiwén bùrú yījiàn)<br />
                mandarin.css.zip (Размер: 242 байт / Загрузок: 59)</li>
        </ul>
    </div>
    <div class="reply"><input type="button" value="new reply" /></div>
</div>''')
        html_expected = self.ET.tostring(self.ET.fromstring(u'''\
<div class="forum-post">
    <div class="author"><a href="/user/lǎowài">lǎowài</a></div>
    <div class="content">
        ...
        теперь выбираем цвета, и скачиваем ещё один архивчик:
        <ul>
            <li><span class="pinYinWrapper">(百闻不如一见 <span class="t3">bǎi</span><span class="t2">wén</span> <span class="t4">bù</span><span class="t2">rú</span> <span class="t1">yī</span><span class="t4">jiàn</span>)</span><br />
                mandarin.css.zip (Размер: 242 байт / Загрузок: 59)</li>
        </ul>
    </div>
    <div class="reply"><input type="button" value="new reply" /></div>
</div>'''), encoding='unicode')
        colorize_pinyin.colorize_DOM(html_in)
        html_out = self.ET.tostring(html_in, encoding='unicode')
        self.assertEqual(html_out, html_expected)

    def test_custom_class(self):
        html_in = self.ET.fromstring(
            u'''<div class="ex">很长的过程 [hěn chángde guòchéng] - очень длительный процесс</div>''')
        html_expected = self.ET.tostring(self.ET.fromstring(
            u'''<div class="ex"><span class="py">很长的过程 [<span class="third">hěn</span> <span class="second">cháng</span><span class="zero">de</span> <span class="forth">guò</span><span class="second">chéng</span>] - очень длительный процесс</span></div>'''),
            encoding='unicode')
        colorize_pinyin.colorize_DOM(html_in, None, 'py', ('zero', 'first', 'second', 'third', 'forth'))
        html_out = self.ET.tostring(html_in, encoding='unicode')
        self.assertEqual(html_out, html_expected)

    def test_uncolorize_simple(self):
        html_in = self.ET.fromstring(
            u'<div><span class="pinYinWrapper"><span class="t2">hán</span><span class="t4">shù</span><span class="t4">shì</span>[<span class="t0">de</span>]</span></div>')
        html_expected = self.ET.tostring(self.ET.fromstring(u'<div>hánshùshì[de]</div>'), encoding='unicode')
        colorize_pinyin.uncolorize_DOM(html_in)
        html_out = self.ET.tostring(html_in, encoding='unicode')
        self.assertEqual(html_out, html_expected)

    def test_uncolorize_harder(self):
        wrapper_class = u'py'
        html_in = self.ET.fromstring(u'''<div><div class="m2"><div class="ex"><span class="py">各有所长 [<span class="t4">gè</span> yŏu <span class="t0">su</span>ŏ <span class="t2">cháng</span>] - у каждого есть свои преимущества</span></div></div>
<div>5) быть сильным (<i>в какой-либо области</i>); быть мастером <i>чего-либо</i>; хорошо владеть <i>чем-либо</i></div>
<div class="m2"><div class="ex"><span class="py">他长于绘画 [<span class="t1">tā</span> <span class="t2">cháng</span><span class="t2">yú</span> <span class="t4">huì</span><span class="t4">huà</span>] - он - большой мастер в живописи</span></div></div></div>''')
        html_expected = self.ET.tostring(self.ET.fromstring(u'''<div><div class="m2"><div class="ex">各有所长 [gè yŏu suŏ cháng] - у каждого есть свои преимущества</div></div>
<div>5) быть сильным (<i>в какой-либо области</i>); быть мастером <i>чего-либо</i>; хорошо владеть <i>чем-либо</i></div>
<div class="m2"><div class="ex">他长于绘画 [tā chángyú huìhuà] - он - большой мастер в живописи</div></div></div>'''),
                                         encoding='unicode')
        colorize_pinyin.uncolorize_DOM(html_in, wrapper_class)
        html_out = self.ET.tostring(html_in, encoding='unicode')
        self.assertEqual(html_out, html_expected)

    def test_back_and_forth(self):
        html = u'''<div class="not_full"><div>有规律性的 yǒu guīlǜxìng-de; (<i>во времени</i>) 定期[的] dìngqí[de], 定时[的] dìngshí[de], 按时的 ànshíde; 经常[的] jīngcháng[de]</div>
<div class="m2"><div class="ex">регулярная жизнь - 有规律的生活</div></div>
<div class="m2"><div class="ex">регулярный рейс самолёта - 飞机定期班次</div></div>
<div class="hidden_text" style="display: block;"><div class="m2"><div class="ex">регулярный доход - 经常的收入</div></div>
<div class="m2"><div class="ex"><div class="m2">- <a href="http://bkrs.info/slovo.php?ch=регулярная армия">регулярная армия</a></div> <div class="m2">- <a href="http://bkrs.info/slovo.php?ch=регулярные войска">регулярные войска</a></div></div> <div class="m2">- <a href="http://bkrs.info/slovo.php?ch=регулярное выражение">регулярное выражение</a></div></div>
</div> </div>'''
        self.assertEqual(html, self.ET.tostring(self.ET.fromstring(html), encoding='unicode'))
        el = self.ET.fromstring(html)
        colorize_pinyin.colorize_DOM(el)
        colorize_pinyin.uncolorize_DOM(el)
        self.assertEqual(html, self.ET.tostring(el, encoding='unicode'))


class ColorizedHTMLStringTestCase(unittest.TestCase):
    def test_pairs(self):
        cmd = colorize_pinyin.colorized_HTML_string_from_string
        self.assertEqual(cmd(_1_baiwen),
                             u'<span class="pinYinWrapper"><span class="t3">bǎi</span><span class="t2">wén</span> <span class="t4">bù</span><span class="t2">rú</span> <span class="t1">yī</span><span class="t4">jiàn</span> // <span class="t1">fāng</span>’<span class="t4">àn</span> // <span class="t3">fǎn</span><span class="t2">gán</span> // <span class="t2">xú</span><span class="t0">niang</span></span>')
        self.assertEqual(cmd(_2_baiwen),
                             u'<span class="pinYinWrapper">2 <span class="t3">bǎi</span><span class="t2">wén</span></span>')
        self.assertEqual(cmd(_3_nongmingong),
                             u'<span class="pinYinWrapper">3 <span class="t2">nóng</span><span class="t2">mín</span><span class="t1">gōng</span></span>')
        self.assertEqual(cmd(_4_kou_anshang),
                             u'<span class="pinYinWrapper">4 <span class="t3">kǒu</span>’<span class="t4">àn</span><span class="t4">shàng</span></span>')
        self.assertEqual(cmd(_5_kouanshang),
                             u'<span class="pinYinWrapper">5 <span class="t3">kǒu</span><span class="t4">àn</span><span class="t4">shàng</span></span>')
        self.assertEqual(cmd(_6_fengongsi),
                             u'<span class="pinYinWrapper">6 <span class="t1">fēn</span><span class="t1">gōng</span><span class="t1">sī</span></span>')
        self.assertEqual(cmd(_7_aiyo),
                             u'<span class="pinYinWrapper">7 <span class="t1">āi</span><span class="t1">yō</span></span>')
        self.assertEqual(cmd(_8_shenme),
                             u'<span class="pinYinWrapper">8 <span class="t2">shén</span><span class="t0">me</span></span>')
        self.assertEqual(cmd(_9_fadia),
                             u'<span class="pinYinWrapper">9 <span class="t1">fā</span><span class="t3">diǎ</span></span>')
        self.assertEqual(cmd(_10_zhiding),
                             u'<span class="pinYinWrapper">10 <span class="t3">zhǐ</span><span class="t4">dìng</span></span>')
        self.assertEqual(cmd(_11_yi1_yi4),
                             u'<span class="pinYinWrapper">11 <span class="t1">yī</span>; <span class="t4">yì</span></span>')
        self.assertEqual(cmd(_12_nanguo_langxingoufei_er_eryide),
                             u'<span class="pinYinWrapper">12 <span class="t2">nán</span><span class="t4">guò</span> // <span class="t2">láng</span><span class="t1">xīn</span><span class="t3">gǒu</span><span class="t4">fèi</span> // <span class="t4">èr</span>’<span class="t3">ěr</span><span class="t1">yī</span><span class="t0">de</span></span>')
        self.assertEqual(cmd(_13_trailing),
                             u'<span class="pinYinWrapper"><span class="t2">hán</span><span class="t4">shù</span><span class="t4">shì</span>[<span class="t0">de</span>]</span>')
        self.assertEqual(cmd('nothing here.'), None)
        # uppercase?
        self.assertEqual(cmd('À!'), u'<span class="pinYinWrapper"><span class="t4">À</span>!</span>')


class ColorizedHTMLElementTestCase(unittest.TestCase):
    def should_be(self, text):
        result = colorize_pinyin.colorized_HTML_string_from_string(text)
        if result is not None:
            return self.ET.tostring(self.ET.XML(result), encoding='unicode')
        return text

    def cmd(self, text):
        result = colorize_pinyin.colorized_HTML_element_from_string(text)
        if result is not None:
            return self.ET.tostring(result, encoding='unicode')
        return text

    def setUp(self):
        import lxml.etree as ET
        self.ET = ET

    def test_pairs(self):
        for x in [_1_baiwen,
                  _2_baiwen,
                  _3_nongmingong,
                  _4_kou_anshang,
                  _5_kouanshang,
                  _6_fengongsi,
                  _7_aiyo,
                  _8_shenme,
                  _9_fadia,
                  _10_zhiding,
                  _11_yi1_yi4,
                  _12_nanguo_langxingoufei_er_eryide,
                  _13_trailing,
                  'nothing here.']:
            self.assertEqual(self.cmd(x), self.should_be(x))


class RangesOfPinyinInStringTestCase(unittest.TestCase):
    def setUp(self):
        self._cmd = colorize_pinyin.ranges_of_pinyin_in_string

    def test_one_word(self):
        self.assertEqual(self._cmd(u"bǎi"), [(0, 3)])
        self.assertEqual(self._cmd(u" jiàn."), [(1, 4)])
        self.assertEqual(self._cmd(u"...-niang, ..."), [(4, 5)])

    def test_two_words(self):
        ranges = self._cmd(u"Gōngzuò")
        self.assertEqual(ranges, [(0, 4), (4, 3)])

    def test_baiwen_buru_yijian(self):
        ranges = self._cmd(_1_baiwen)
        self.assertEqual(ranges, [
            (0, 3), (3, 3), (7, 2), (9, 2), (12, 2), (14, 4),
            (22, 4), (27, 2), (33, 3), (36, 3), (43, 2), (45, 5)])

    def test_missing_apostrophe(self):
        ranges = self._cmd('àiài')
        self.assertEqual(ranges, [(0, 2), (2, 2)])


class DetermineToneTestCase(unittest.TestCase):
    def testFristTone(self):
        self.assertEqual(1, colorize_pinyin.determine_tone('fāng'))
        self.assertEqual(1, colorize_pinyin.determine_tone('yī'))

    def testSecondTone(self):
        self.assertEqual(2, colorize_pinyin.determine_tone('gán'))
        self.assertEqual(2, colorize_pinyin.determine_tone('xún'))

    def testThirdTone(self):
        self.assertEqual(3, colorize_pinyin.determine_tone('fǎn'))
        self.assertEqual(3, colorize_pinyin.determine_tone('lǚ'))

    def testFourthTone(self, ):
        self.assertEqual(4, colorize_pinyin.determine_tone('àn'))
        self.assertEqual(4, colorize_pinyin.determine_tone('dìnggòu'))

    def testZeroTone(self):
        self.assertEqual(0, colorize_pinyin.determine_tone('de'))
        self.assertEqual(0, colorize_pinyin.determine_tone('ning'))

    def testNonPinyin(self):
        self.assertEqual(0, colorize_pinyin.determine_tone('бурда'))

    def testMixedPinyin(self):
        self.assertEqual(3, colorize_pinyin.determine_tone('bǎiwén'))


class UtilitiesTestCase(unittest.TestCase):
    def test_lowercase_string_by_rempoving_pinyin_tones(self):
        cmd = colorize_pinyin.lowercase_string_by_removing_pinyin_tones
        s_list = [
            (u"À! Zhēn měi!", u"a! zhen mei!"),
            (_1_baiwen, u'baiwen buru yijian // fang’an // fangan // xuniang'),
            ("Nǐ lái háishi bù lái?", u"ni lai haishi bu lai?"),  # not unicode
        ]
        for with_tones, clean in s_list:
            self.assertEqual(cmd(with_tones), clean)


if __name__ == '__main__':
    unittest.main()

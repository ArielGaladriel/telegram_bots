eastern_armenian = {'a': 'ա', 'b': 'բ', 'g': 'գ', 'd': 'դ', 'e': 'ե', 'z': 'զ', 'e\'': 'է', 'y\'': 'ը',
                    't\'': 'թ', 'jh': 'ժ', 'i': 'ի', 'l': 'լ', 'x': 'խ', 'c\'': 'ծ', 'k': 'կ', 'h': 'հ',
                    'd\'': 'ձ', 'gh': 'ղ', 'tw': 'ճ', 'm': 'մ', 'y': 'յ', 'n': 'ն', 'sh': 'շ', 'o': 'ո',
                    'ch': 'չ', 'p': 'պ', 'j': 'ջ', 'r\'': 'ռ', 's': 'ս', 'v': 'վ', 't': 'տ', 'r': 'ր',
                    'c': 'ց', 'w': 'ւ', 'p\'': 'փ', 'q': 'ք', 'o\'': 'օ', 'f': 'ֆ', 'u': 'ու', '&': 'և',
                    'A': 'Ա', 'B': 'Բ', 'G': 'Գ', 'D': 'Դ', 'E': 'Ե', 'Z': 'Զ', 'E\'': 'Է', 'Y\'': 'Ը',
                    'T\'': 'Թ', 'JH': 'Ժ', 'I': 'Ի', 'L': 'Լ', 'X': 'Խ', 'C\'': 'Ծ', 'K': 'Կ', 'H': 'Հ',
                    'D\'': 'Ձ', 'GH': 'Ղ', 'TW': 'Ճ', 'M': 'Մ', 'Y': 'Յ', 'N': 'Ն', 'SH': 'Շ', 'O': 'Ո',
                    'CH': 'Չ', 'P': 'Պ', 'J': 'Ջ', 'R\'': 'Ռ', 'S': 'Ս', 'V': 'Վ', 'T': 'Տ', 'R': 'Ր',
                    'C': 'Ց', 'W': 'Ւ', 'P\'': 'Փ', 'Q': 'Ք', 'O\'': 'Օ', 'F': 'Ֆ', 'U': 'ՈՒ'
                    }

western_armenian = {'a': 'ա', 'p': 'բ', 'k': 'գ', 't': 'դ', 'e': 'ե', 'z': 'զ', 'e\'': 'է', 'y': 'ը',
                    't\'': 'թ', 'zh': 'ժ', 'i': 'ի', 'l': 'լ', 'x': 'խ', 'dz': 'ծ', 'g': 'կ', 'h': 'հ',
                    'tz': 'ձ', 'gh': 'ղ', 'j': 'ճ', 'm': 'մ', 'h\'': 'յ', 'n': 'ն', 'sh': 'շ', 'o\'': 'ո',
                    'ch': 'չ', 'b': 'պ', 'ch\'': 'ջ', 'r\'': 'ռ', 's': 'ս', 'v': 'վ', 'd': 'տ', 'r': 'ր',
                    'c': 'ց', 'w': 'ւ', 'p\'': 'փ', 'q': 'ք', 'o': 'օ', 'f': 'ֆ', 'u': 'ու', '&': 'և',
                    'A': 'Ա', 'P': 'Բ', 'K': 'Գ', 'T': 'Դ', 'E': 'Ե', 'Z': 'Զ', 'E\'': 'Է', 'Y': 'Ը',
                    'T\'': 'Թ', 'ZH': 'Ժ', 'I': 'Ի', 'L': 'Լ', 'X': 'Խ', 'DZ': 'Ծ', 'G': 'Կ', 'H': 'Հ',
                    'TZ': 'Ձ', 'GH': 'Ղ', 'J': 'Ճ', 'M': 'Մ', 'H\'': 'Յ', 'N': 'Ն', 'SH': 'Շ', 'O\'': 'Ո',
                    'CH': 'Չ', 'B': 'Պ', 'CH\'': 'Ջ', 'R\'': 'Ռ', 'S': 'Ս', 'V': 'Վ', 'D': 'Տ', 'R': 'Ր',
                    'C': 'Ց', 'W': 'Ւ', 'P\'': 'Փ', 'Q': 'Ք', 'O': 'Օ', 'F': 'Ֆ', 'U': 'ՈՒ'
                    }

georgian = {'a': 'ა', 'b': 'ბ', 'g': 'გ', 'd': 'დ', 'e': 'ე', 'v': 'ვ', 'w': 'ვ', 'z': 'ზ',
            't': 'თ', 'i': 'ი', 'k\'': 'კ', 'l': 'ლ', 'm': 'მ', 'n': 'ნ', 'o': 'ო', 'p\'': 'პ',
            'zh': 'ჟ', 'r': 'რ', 's': 'ს', 't\'': 'ტ', 'u': 'უ', 'p': 'ფ', 'f': 'ფ',
            'k': 'ქ', 'gh': 'ღ', 'q': 'ყ', 'sh': 'შ', 'ch': 'ჩ', 'ts': 'ც', 'c': 'ც',
            'dz': 'ძ', 'ts\'': 'წ', 'ch\'': 'ჭ', 'kh': 'ხ', 'x': 'ხ', 'j': 'ჯ', 'h': 'ჰ'
            }


async def armenian_transliteration_eastern(text: str):
    """
    Transliteration from latin to armenian (eastern armenian)
    """
    text = text.replace('e\'', 'է').replace('y\'', 'ը').replace('t\'', 'թ').replace('jh', 'ժ'). \
        replace('c\'', 'ծ').replace('d\'', 'ձ').replace('gh', 'ղ').replace('tw', 'ճ'). \
        replace('sh', 'շ').replace('ch', 'չ').replace('r\'', 'ռ').replace('p\'', 'փ').replace('o\'', 'օ'). \
        replace('E\'', 'Է').replace('Y\'', 'Ը').replace('T\'', 'Թ').replace('JH', 'Ժ').replace('C\'', 'Ծ'). \
        replace('D\'', 'Ձ').replace('GH', 'Ղ').replace('TW', 'Ճ').replace('SH', 'Շ').replace('CH', 'Չ'). \
        replace('R\'', 'Ռ').replace('P\'', 'Փ').replace('O\'', 'Օ')
    for i in text:
        if i in eastern_armenian:
            text = text.replace(i, eastern_armenian[i])
    return text


async def armenian_transliteration_western(text: str):
    """
    Transliteration from latin to armenian (western armenian)
    """
    text = text.replace('e\'', 'է').replace('t\'', 'թ').replace('zh', 'ժ').replace('dz', 'ծ'). \
        replace('tz', 'ձ').replace('gh', 'ղ').replace('h\'', 'յ').replace('sh', 'շ').replace('o\'', 'ո'). \
        replace('ch', 'չ').replace('ch\'', 'ջ').replace('r\'', 'ռ').replace('p\'', 'փ').replace('E\'', 'Է'). \
        replace('T\'', 'Թ').replace('ZH', 'Ժ').replace('DZ', 'Ծ').replace('TZ', 'Ձ').replace('GH', 'Ղ'). \
        replace('H\'', 'Յ').replace('SH', 'Շ').replace('O\'', 'Ո').replace('CH', 'Չ').replace('CH\'', 'Ջ'). \
        replace('R\'', 'Ռ').replace('P\'', 'Փ')
    for i in text:
        if i in western_armenian:
            text = text.replace(i, western_armenian[i])
    return text


async def georgian_transliteration(text: str):
    """
    Transliteration from latin to georgian
    """
    text = text.lower().replace('k\'', 'კ').replace('p\'', 'პ').replace('zh', 'ჟ').replace('t\'', 'ტ').\
        replace('gh', 'ღ').replace('sh', 'შ').replace('ch', 'ჩ').replace('ts', 'ც').\
        replace('dz', 'ძ').replace('ts\'', 'წ').replace('ch\'', 'ჭ').replace('kh', 'ხ')
    for i in text:
        if i in georgian:
            text = text.replace(i, georgian[i])
    return text


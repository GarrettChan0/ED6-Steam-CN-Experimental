import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R1200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '古罗尼山道方向'),
    TXT(0x02, '柏斯方向'),
    TXT(0x03, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1200.x'
    header.mapIndex       = 61
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3CC
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFE3AE0,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFEF278,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 61,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10320._CH', 'ED6_DT09/CH10320P._CP'),
        ('ED6_DT09/CH10321._CH', 'ED6_DT09/CH10321P._CP'),
        ('ED6_DT09/CH10350._CH', 'ED6_DT09/CH10350P._CP'),
        ('ED6_DT09/CH10351._CH', 'ED6_DT09/CH10351P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
    ]

# id: 0x10002 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -205290,
            z                   = -150,
            y                   = -15350,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -91180,
            z                   = 0,
            y                   = -70080,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -143880,
            z           = -10,
            y           = -61790,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -158850,
            z           = -20,
            y           = -50270,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F6,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -173400,
            z           = 20,
            y           = -48970,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -167290,
            z           = 0,
            y           = -1300,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x00F7,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1AA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1AA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -128190,
            triggerZ            = 0,
            triggerY            = -64590,
            triggerRange        = 1500,
            actorX              = -128190,
            actorZ              = 1500,
            actorY              = -64590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -192620,
            triggerZ            = 0,
            triggerY            = -46900,
            triggerRange        = 1000,
            actorX              = -192620,
            actorZ              = 1000,
            actorY              = -46900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1F2
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1F3
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -278000, -176000, 196633)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 2, 0x38A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_217',
    )

    OP_6F(0x0000, 0)

    Jump('loc_21E')

    def _loc_217(): pass

    label('loc_217')

    OP_6F(0x0000, 60)

    def _loc_21E(): pass

    label('loc_21E')

    Return()

# id: 0x0002 offset: 0x21F
@scena.Code('ReInit')
def ReInit():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　柏斯市\n',
            '西　拉文努村　　２８７塞尔矩\n',
            '　　古罗尼山顶　４４１塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0003 offset: 0x296
@scena.Code('func_03_296')
def func_03_296():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0071, 2, 0x38A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_380',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01FC, 1)"),
            Expr.Return,
        ),
        'loc_30A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0071, 2, 0x38A))

    Jump('loc_37D')

    def _loc_30A(): pass

    label('loc_30A')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '复苏药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_37D(): pass

    label('loc_37D')

    Jump('loc_3B6')

    def _loc_380(): pass

    label('loc_380')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x7D)
    def _loc_3B6(): pass

    label('loc_3B6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

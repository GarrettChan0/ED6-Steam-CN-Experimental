import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1500_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1500   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '罗伊德'),
    TXT(0x02, '艾露凯'),
    TXT(0x03, '阿妮特'),
    TXT(0x04, '努西'),
    TXT(0x05, '约修亚'),
    TXT(0x06, '书'),
    TXT(0x07, '目标用摄像机'),
    TXT(0x08, '小船'),
    TXT(0x09, '安塞尔新街方向'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1500.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5C7A
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0xFFFFE4A8,
            dword_04        = 0x00000000,
            dword_08        = 0x00014050,
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
            word_30         = 225,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 50,
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
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00013._CH', 'ED6_DT07/CH00013P._CP'),
        ('ED6_DT06/CH20032._CH', 'ED6_DT06/CH20032P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT06/CH20030._CH', 'ED6_DT06/CH20030P._CP'),
        ('ED6_DT07/CH00003._CH', 'ED6_DT07/CH00003P._CP'),
        ('ED6_DT06/CH20092._CH', 'ED6_DT06/CH20092P._CP'),
        ('ED6_DT06/CH20161._CH', 'ED6_DT06/CH20161P._CP'),
    ]

# id: 0x10002 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -44990,
            z                   = -1970,
            y                   = 38500,
            direction           = 190,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -9420,
            z                   = 400,
            y                   = 41260,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 3200,
            z                   = -2000,
            y                   = 42700,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = -45026,
            z                   = -4000,
            y                   = 32900,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -3882,
            z                   = 500,
            y                   = 41320,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01D4,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = -4990,
            z                   = 900,
            y                   = 41500,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1703943,
            chipIndex           = 7,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0184,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -8640,
            z                   = 0,
            y                   = 96040,
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

# id: 0x10003 offset: 0x22A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x22A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -34266,
            y           = -3000,
            z           = 54198,
            range       = -31910,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000C274,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
        ScenaEventData(
            x           = -29829,
            y           = -3000,
            z           = 55042,
            range       = -27300,
            dword_10    = 0x000003E8,
            dword_14    = 0x0000C5B2,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000E,
        ),
        ScenaEventData(
            x           = -5850,
            y           = -1000,
            z           = 80880,
            range       = -10140,
            dword_10    = 0x000007D0,
            dword_14    = 0x00014438,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000F,
        ),
    )

# id: 0x10005 offset: 0x28A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -2900,
            triggerZ            = -3000,
            triggerY            = 30600,
            triggerRange        = 3000,
            actorX              = -2900,
            actorZ              = -3000,
            actorY              = 30600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x006B, 6, 0x35E)),
            Expr.Return,
        ),
        'loc_2C2',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)

    Jump('loc_3A5')

    def _loc_2C2(): pass

    label('loc_2C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Return,
        ),
        'loc_2CC',
    )

    Jump('loc_3A5')

    def _loc_2CC(): pass

    label('loc_2CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_2E5',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)
    OP_71(0x0003, 0x0004)

    Jump('loc_3A5')

    def _loc_2E5(): pass

    label('loc_2E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            Expr.Return,
        ),
        'loc_319',
    )

    SetChrChipByIndex(0x000C, 5)
    SetChrPos(0x000C, -6920, 700, 41300, 90)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)
    OP_71(0x0003, 0x0004)

    Jump('loc_3A5')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 5, 0x33D)),
            Expr.Return,
        ),
        'loc_332',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)
    OP_71(0x0003, 0x0004)

    Jump('loc_3A5')

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 4, 0x33C)),
            Expr.Return,
        ),
        'loc_345',
    )

    SetChrChipByIndex(0x0008, 10)
    TerminateThread(0x0008, 0xFF)

    Jump('loc_3A5')

    def _loc_345(): pass

    label('loc_345')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_35D',
    )

    SetChrChipByIndex(0x0008, 10)
    TerminateThread(0x0008, 0xFF)
    SetChrFlags(0x0008, 0x0010)

    Jump('loc_3A5')

    def _loc_35D(): pass

    label('loc_35D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_376',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)
    ClearChrFlags(0x000A, 0x0080)

    Jump('loc_3A5')

    def _loc_376(): pass

    label('loc_376')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 2, 0x312)),
            Expr.Return,
        ),
        'loc_38A',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)

    Jump('loc_3A5')

    def _loc_38A(): pass

    label('loc_38A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 1, 0x301)),
            Expr.Return,
        ),
        'loc_3A5',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0008)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3B3',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0009)

    def _loc_3B3(): pass

    label('loc_3B3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_3CF',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x46),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x000D)

    def _loc_3CF(): pass

    label('loc_3CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_3EB',
    )

    SetMapFlags(0x10000000)
    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x000B)
    OP_B1('t1500_y')

    def _loc_3EB(): pass

    label('loc_3EB')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_3F7'),
        (-1, 'loc_40D'),
    )

    def _loc_3F7(): pass

    label('loc_3F7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 3, 0x33B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_40A',
    )

    SetScenaFlags(ScenaFlag(0x0067, 3, 0x33B))
    Event(0, 0x0008)

    def _loc_40A(): pass

    label('loc_40A')

    Jump('loc_40D')

    def _loc_40D(): pass

    label('loc_40D')

    Return()

# id: 0x0001 offset: 0x40E
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -145000, -73000, 196678)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_43D',
    )

    OP_B1('t1500_y')

    Jump('loc_446')

    def _loc_43D(): pass

    label('loc_43D')

    OP_B1('t1500_n')

    def _loc_446(): pass

    label('loc_446')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 7, 0x33F)),
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_45A',
    )

    ClearChrFlags(0x000C, 0x0080)

    Jump('loc_466')

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_466',
    )

    OP_64(0x00, 0x0001)

    def _loc_466(): pass

    label('loc_466')

    PlaySE(460, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x46C
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_481',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_481(): pass

    label('loc_481')

    Return()

# id: 0x0003 offset: 0x482
@scena.Code('func_03_482')
def func_03_482():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4A5',
    )

    OP_8D(0x00FE, 2000, 45800, 3600, 39900, 2000)

    Jump('func_03_482')

    def _loc_4A5(): pass

    label('loc_4A5')

    Return()

# id: 0x0004 offset: 0x4A6
@scena.Code('func_04_4A6')
def func_04_4A6():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Return,
        ),
        'loc_5F1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '虽然只是看了一下，\n',
            '不过我觉得你的天分还是挺高的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F嘿嘿，真的吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '其实我从小就很喜欢钓鱼的呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过和罗伊德叔叔比起来，\n',
            '我也只是玩玩的程度而已啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也不能这么说，\n',
            '如果你认真锻炼下去，\n',
            '要进入我们『钓公师团』也不是件难事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EE')

    def _loc_5AF(): pass

    label('loc_5AF')

    ChrTalk(
        0x00FE,
        (
            '看来湖里的动静\n',
            '也越来越小了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在已经傍晚了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EE(): pass

    label('loc_5EE')

    Jump('loc_2278')

    def _loc_5F1(): pass

    label('loc_5F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            Expr.Return,
        ),
        'loc_619',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，小姑娘你也想钓鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2278')

    def _loc_619(): pass

    label('loc_619')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 5, 0x33D)),
            Expr.Return,
        ),
        'loc_681',
    )

    ChrTalk(
        0x00FE,
        (
            '今天又让那家伙\n',
            '逃过了我的追捕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '看来要选择一个更好的位置才行，\n',
            '再努力一下试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2278')

    def _loc_681(): pass

    label('loc_681')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 2, 0x33A)),
            Expr.Return,
        ),
        'loc_2278',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 4, 0x33C)),
            Expr.Return,
        ),
        'loc_2084',
    )

    SetScenaFlags(ScenaFlag(0x0067, 5, 0x33D))
    OP_28(0x0038, 0x01, 0x0004)
    OP_28(0x0038, 0x01, 0x0008)
    OP_28(0x0038, 0x01, 0x0010)
    OP_28(0x0038, 0x01, 0x0020)
    SetChrDirection(0x00FE, 180, 0)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-44970, -1970, 39550, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(261, 0)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0103, 0x0004)
    SetChrPos(0x0101, -44510, -1970, 39560, 180)
    SetChrPos(0x0102, -44260, -1970, 40650, 180)
    SetChrPos(0x0103, -45160, -1970, 40920, 180)
    SetChrPos(0x0104, -45360, -1970, 39650, 180)
    OP_0D()

    NpcTalk(
        0x00FE,
        '拿着钓鱼竿的男人',
        (
            '#1230030662V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030663V#501F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030664V叔叔，您是不是那个\n',
            '从王都过来的罗伊德先生呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '拿着钓鱼竿的男人',
        (
            '#1230030665V………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030666V#014F好厉害的集中力……\n',
            '除了鱼之外，眼中简直容不下任何东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030667V#030F呵呵，真没办法。\n',
            '看来要我亲自出马才行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030668V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0104, 0x0040)
    SetChrFlags(0x0104, 0x0004)
    ChrWalkTo(0x0104, -45430, -1970, 38570, 2000, 0x00)
    SetChrDirection(0x0104, 135, 400)
    OP_62(0x0104, 0x00000000, 2000, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)

    ChrTalk(
        0x0104,
        (
            '#0040030669V#035F……呼～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '奥利维尔向男人的耳朵里吹了一口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_9E(0x00FE, 60, 0, 500, 8000)

    NpcTalk(
        0x00FE,
        '拿着钓鱼竿的男人',
        (
            '#1230030670V#5S哎呀呀呀啊～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09A6')
    def lambda_09A6():
        ChrWalkTo(0x00FE, -45500, -1970, 39460, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_09A6)

    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    WaitForThreadExit(0x0104, 0x0001)
    SetChrDirection(0x0104, 135, 400)
    SetChrChipByIndex(0x00FE, 0)
    ChrTurnDirection(0x00FE, 0x0104, 400)
    ClearChrFlags(0x0104, 0x0040)
    ClearChrFlags(0x0104, 0x0004)

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '#1230030671V你、你们是谁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '中年男子',
        (
            '#1230030672V什、什么时候站在这里的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030673V#509F好、好下流～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030674V#025F这种动作也敢做出来，\n',
            '光是看到就起了一身鸡皮疙瘩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030675V#031F哎呀，没办法嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030676V刚才叫他的时候一点反应也没有，\n',
            '看来集中力不是一般的强哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030677V#010F请问您是罗伊德先生吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#1230030678V啊、啊啊，就是我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#1230030679V对了，你们怎么知道我的名字？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030680V#020F其实是一位住在\n',
            '柏斯的老伯告诉我们的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030681V可以打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-44670, -2000, 43660, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    ClearChrFlags(0x0102, 0x0004)
    ClearChrFlags(0x0103, 0x0004)
    SetChrPos(0x00FE, -44640, -2000, 42760, 0)
    SetChrPos(0x0101, -44550, -2000, 44760, 180)
    SetChrPos(0x0102, -45710, -2000, 44500, 135)
    SetChrPos(0x0103, -43620, -2000, 44550, 225)
    SetChrPos(0x0104, -44920, -2000, 45730, 180)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#1230030682V#5P原来如此……\n',
            '你们是从库瓦诺那儿听说我的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030683V#5P啊啊，我的确是看到了。\n',
            '就在前天夜晚，几个奇怪的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030684V#006F果然是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030685V可以把那天看到的事情\n',
            '详细地告诉我们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030686V#5P……在此之前我想问一句。\n',
            '你们是不是游击士？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030687V#5P我说的话是不是牵涉到什么案件？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030688V#012F现在还不能断定。\n',
            '不过，相关联的可能性还是有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030689V#5P我知道了……\n',
            '既然是这样，我一定会协助你们的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030690V#5P前天晚上……\n',
            '也就是我在小艇上夜钓的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030691V#5P因为和努西苦战了一整天，\n',
            '累得不行了所以想回旅馆休息。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030692V#5P天色也已经晚了，\n',
            '住宿的客人也都休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030693V#022F请等一下。\n',
            '……你说的『努西』是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0008, 0x0103, 400)

    ChrTalk(
        0x0008,
        (
            '#1230030694V#5P#3S你可要认真听好了！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030695V#5P所谓的努西，\n',
            '是生活在这个瓦雷利亚湖的\n',
            '一种十分巨大的鱼精。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030696V#5P十年来，努西一直都是\n',
            '我们这些钓鱼爱好者最热衷的话题，\n',
            '但它同时也是一种让人难以捉摸的鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030030697V#522F（不妙……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030698V#017F（不小心让他兴致高昂起来了……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030699V#004F有、有这么厉害的鱼吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#1230030700V#5P对啊，要知道这五年来，\n',
            '我一直在追踪那家伙啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030701V#5P不过，那家伙的脾性反复无常，\n',
            '一时游到这来一时游到那去，\n',
            '一时吃这种鱼饵一时吃那种鱼饵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030702V#5P最近，我听说那家伙在这附近出现，\n',
            '就急忙从王都追了过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030703V#035F呵呵，多么狂热的激情啊。\n',
            '对于你的心情我非常地理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030704V若是看到了中意的东西，\n',
            '我也一定会想尽办法得到它。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030705V譬如说『格兰·夏利拿』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030706V#509F那样也叫得到吗？\n',
            '应该是不问自取偷偷喝完才对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030707V#026F咳咳……回到正题吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030708V#020F那么罗伊德先生，\n',
            '你夜钓回来之后又怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030709V#5P啊、啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030710V#5P之后，我就把小艇放好，\n',
            '接着正要走回旅馆睡觉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030711V#5P就在那时，我看到了奇怪的二人组合。\n',
            '他们从旅馆出来，走到外面的街道上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030712V#014F走到街道上……\n',
            '而且是在深夜的时候？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030713V#5P啊啊，我不会看错的。\n',
            '就是走到安塞尔新街那里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030714V#5P我本来以为他们\n',
            '是外出游玩晚归的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030715V#5P不过深更半夜才回来也太奇怪了吧。\n',
            '所以第二天，我向旅馆的人打听了一下，\n',
            '不过大家都说不认识这些家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030716V#5P当时我以为自己看到了幽灵，\n',
            '不禁感觉背后发寒。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030717V#580F幽、幽灵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030718V会、会出现吗？在这里！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030719V#5P哈哈，我看到的是两人一起，\n',
            '而且还是一男一女的年轻组合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030720V#5P或许那两人是一对得不到\n',
            '身边人的承认而徇情的恋人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030721V#504F啊～～～别、别再说了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030030722V#027F哎呀哎呀。\n',
            '你还是怕听到幽灵这类的话题啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020030723V#019F就是越害怕才越想听嘛，\n',
            '怪谭之类的，还有不可思议的故事之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030724V#031F呵呵，看艾丝蒂尔君\n',
            '害怕得尖叫起来的样子，\n',
            '真是越看越可爱，越看越动人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030725V简直就像在寒风中战栗的小猫㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTurnDirection(0x0101, 0x0104, 800)

    ChrTalk(
        0x0101,
        (
            '#0010030726V#009F#5P哼！再说这种话就小心你的门牙！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030727V#5P哈哈哈……\n',
            '幽灵什么的只是开玩笑而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17CF')
    def lambda_17CF():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_17CF)

    @scena.Lambda('lambda_17DD')
    def lambda_17DD():
        SetChrDirection(0x00FE, 135, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_17DD)

    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0008,
        (
            '#1230030728V#5P当时我还不敢肯定，\n',
            '不过那对男女应该不是情侣。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030729V#5P因为我看到那个女子穿着很怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030730V#014F穿着很怪……这怎么说呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030731V#5P我只是看到背影，\n',
            '也不敢肯定有没有看错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030732V#5P不过看样子她穿的就是校服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030733V#580F校服？难道说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030734V#012F杰尼丝王立学院的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030735V#5P呵呵，你们知道得很清楚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030736V#5P我的外甥女也在那学校念书，\n',
            '所以我看得出那就是王立学院的校服。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030737V#026F原来如此……\n',
            '终于知道所谓的奇怪家伙是谁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030738V#005F怪不得被人叫做奇怪的家伙！\n',
            '肯定是那个嚣张的男人婆！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030739V总算抓到你的尾巴了～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030740V#5P怎么了……\n',
            '难道你们认识他们吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030741V#5P我觉得那两个人选择在\n',
            '深夜出现可能是出于什么目的吧，\n',
            '这一点你们也最好注意一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030742V#5P对了，我还听他们说过\n',
            '今天半夜会再来这里一次的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030743V#014F啊？真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030744V#5P对对，那个年轻男子亲口说过，\n',
            '两天后还会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030745V#5P他的口气十分认真，让我印象很深。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030746V#020F原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030747V这是很重要的线索啊。\n',
            '感谢你的合作，之后就交给我们吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030748V我们绝对会好好利用这些线索的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030749V#5P呼，太好了……\n',
            '有你这句话我就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030750V#5P突然感觉如释重负啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030751V#5P……这下可安心了。\n',
            '我又可以安安稳稳地钓鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1230030752V#5P这次不会让你逃掉的！\n',
            '各位朋友，我这就先失陪了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D3F')
    def lambda_1D3F():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1D3F')

    DispatchAsync2(0x0101, 0x0001, lambda_1D3F)

    @scena.Lambda('lambda_1D50')
    def lambda_1D50():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1D50')

    DispatchAsync2(0x0102, 0x0001, lambda_1D50)

    @scena.Lambda('lambda_1D61')
    def lambda_1D61():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1D61')

    DispatchAsync2(0x0103, 0x0001, lambda_1D61)

    @scena.Lambda('lambda_1D72')
    def lambda_1D72():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1D72')

    DispatchAsync2(0x0104, 0x0001, lambda_1D72)

    ChrWalkTo(0x0008, -42560, -2000, 43210, 6000, 0x00)
    ChrWalkTo(0x0008, -36240, -2000, 48830, 6000, 0x00)
    SetChrFlags(0x0008, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x0104, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010030753V#506F#5P好一个钓鱼迷呢……\n',
            '这样的集中力我们还真是比不上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030754V#010F那个所谓的『钓公师团』，\n',
            '不知道是一个什么样的组织呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0103, 400)

    ChrTalk(
        0x0104,
        (
            '#0040030755V#033F听到现在，\n',
            '我连那对男女是什么来头也还没搞清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030756V究竟你们在调查什么事情，\n',
            '可以向我详细地解释一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0104, 400)
    ChrTurnDirection(0x0103, 0x0104, 400)

    ChrTalk(
        0x0103,
        (
            '#0030030757V#020F也对。\n',
            '事情大致是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '雪拉扎德向奥利维尔讲解了关于\n',
            '在洛连特出现的空贼团少女乔丝特的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0104,
        (
            '#0040030758V#030F原来如此……还真是\n',
            '踏破铁鞋无觅处，得来全不费功夫。 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030759V这么说，今天晚上有好戏看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030760V#020F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030761V为了慎重起见，\n',
            '我们也要租一间房间落脚比较好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030762V而且必须等到今天半夜才能行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030763V#006F#5P嗯。\n',
            '我们回柜台那里去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Jump('loc_2278')

    def _loc_2084(): pass

    label('loc_2084')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_21F1',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))
    SetScenaFlags(ScenaFlag(0x006D, 1, 0x369))

    NpcTalk(
        0x00FE,
        '拿着钓鱼竿的男人',
        (
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F那个～能打扰一下吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x00FE,
        '拿着钓鱼竿的男人',
        (
            '……………………………\n',
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F（啊呀，没有反应呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（看上去他的精神很集中啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#033F（……原来如此。\n',
            '　这就是所谓的钓鱼狂人啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#035F（呵呵，真是一个有趣的人啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#509F（你有立场说别人吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2278')

    def _loc_21F1(): pass

    label('loc_21F1')

    NpcTalk(
        0x00FE,
        '拿着钓鱼竿的男人',
        (
            '……………………………\n',
            '……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '男人集中精力在钓鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_2278(): pass

    label('loc_2278')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x227C
@scena.Code('func_05_227C')
def func_05_227C():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2346',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '这个旅馆真是适合我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '周围的景色也很优美，\n',
            '料理也相当美味哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '假如能在这里住下去是最好不过了，\n',
            '真是好得不会让人舍得离开这里半步啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经在这里住了好几天了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2394')

    def _loc_2346(): pass

    label('loc_2346')

    ChrTalk(
        0x00FE,
        (
            '嗯～\n',
            '这个旅馆真是适合我啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '周围的景色也很优美，\n',
            '料理也相当美味哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2394(): pass

    label('loc_2394')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x2398
@scena.Code('func_06_2398')
def func_06_2398():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0065, 3, 0x32B)),
            Expr.Return,
        ),
        'loc_23E6',
    )

    ChrTalk(
        0x00FE,
        (
            '下午打算和母亲\n',
            '一起在湖上划划船……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还能够顺便消消食。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2434')

    def _loc_23E6(): pass

    label('loc_23E6')

    ChrTalk(
        0x00FE,
        (
            '嗯，怎么说呢，\n',
            '这里的风真的很清爽。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这里散步\n',
            '的确让人心旷神怡啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2434(): pass

    label('loc_2434')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x2438
@scena.Code('func_07_2438')
def func_07_2438():
    TalkBegin(0x000C)
    ClearChrFlags(0x00FE, 0x0010)
    ChrTurnDirection(0x00FE, 0x0000, 0)

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x5A),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_245D',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_2478')

    def _loc_245D(): pass

    label('loc_245D')

    If(
        (
            (Expr.GetChrWork, 0xC, 0x4),
            (Expr.PushLong, 0x10E),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2473',
    )

    SetChrSubChip(0x00FE, 1)

    Jump('loc_2478')

    def _loc_2473(): pass

    label('loc_2473')

    SetChrSubChip(0x00FE, 2)

    def _loc_2478(): pass

    label('loc_2478')

    SetChrDirection(0x00FE, 90, 0)
    SetChrFlags(0x00FE, 0x0010)

    ChrTalk(
        0x000C,
        (
            '#0020030899V#014F你不是去钓鱼吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030900V说到钓鱼的场所，\n',
            '我想那个码头应该很不错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030901V#007F哼……\n',
            '约修亚你也来钓一下嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030902V你的技术不是也不错嘛～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0020030903V#019F我可不像你那么熟练。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030904V#010F不过让我在这里\n',
            '看一下你平时修行的成果也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x00FE, 0)
    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x2590
@scena.Code('func_08_2590')
def func_08_2590():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-12880, 0, 26810, 0)
    CameraSetDistance(5900, 0)
    OP_6C(45000, 0)
    OP_12(0x00009470, 0x00030D40, 0x00000000)
    SetChrPos(0x0101, -9345, 0, 78200, 180)
    SetChrPos(0x0102, -10370, 0, 78100, 180)
    SetChrPos(0x0104, -8638, 0, 79300, 180)
    SetChrPos(0x0103, -9788, 0, 79400, 180)

    @scena.Lambda('lambda_2611')
    def lambda_2611():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2611)

    Sleep(1000)

    @scena.Lambda('lambda_2626')
    def lambda_2626():
        CameraMove(-9385, 0, 77797, 9000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2626)

    CameraSetDistance(3000, 9000)
    OP_12(0x00009470, 0x000186A0, 0x00001F40)

    ChrTalk(
        0x0101,
        (
            '#0010030621V#000F#3P这里就是瓦雷利亚湖的北岸吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030622V果然是个气氛不错的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030623V#010F#1P是啊，住宿环境也相当好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030624V#020F#2P我之前因为工作关系也在这里住过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030625V美酒香醇、住所一流。\n',
            '确实是个无可挑剔的休闲胜地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030626V#007F#3P嗯，这我也知道。\n',
            '可我们毕竟不是来度假的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0104, 0x0101, 400)

    ChrTalk(
        0x0104,
        (
            '#0040030627V#033F#4P哎呀，不是吗？\n',
            '可我确实有这个意思啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030628V#035F白天，躺在微摇的小艇上小憩，\n',
            '夜晚，品尝各式各样的美酒佳肴……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030629V人生最惬意的假期莫过于此。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0104, 400)
    ChrTurnDirection(0x0102, 0x0104, 400)
    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030630V#009F#3P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030631V#018F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030632V#027F#2P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040030633V#031F#4P哈·哈·哈。\n',
            '开个玩笑而已嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030634V享受假期无论何时都可以，\n',
            '现在还是先享受对付空贼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040030635V我奥利维尔，\n',
            '可是一个很会分辨轻重缓急的人哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030636V#007F#3P这可不是什么\n',
            '享受不享受的问题啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030030637V#020F#2P呵呵，别管他了。\n',
            '让他一个人慢慢享受到发烂好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030030638V老伯说的那位钓友就在旅馆落脚，\n',
            '我们还是快点进去找他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030639V#010F#1P嗯，就是前天深夜目击到\n',
            '可疑人物的那位旅馆客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0038, 0x01, 0x0001)
    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x2A6C
@scena.Code('func_09_2A6C')
def func_09_2A6C():
    EventBegin(0x00)
    CameraMove(1920, -2000, 40480, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    SetChrPos(0x0101, -5540, 500, 43050, 180)
    SetChrPos(0x0102, -5540, 500, 43050, 180)
    FadeIn(1500, 0)
    OP_0D()

    @scena.Lambda('lambda_2ADD')
    def lambda_2ADD():
        ChrWalkTo(0x00FE, 970, -2000, 42510, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2ADD)

    Sleep(800)

    @scena.Lambda('lambda_2AFD')
    def lambda_2AFD():
        ChrWalkTo(0x00FE, 970, -2000, 42510, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2AFD)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2B1D')
    def lambda_2B1D():
        CameraMove(1490, -2000, 38380, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_2B1D)

    @scena.Lambda('lambda_2B35')
    def lambda_2B35():
        ChrWalkTo(0x00FE, 2260, -2000, 39790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B35)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_2B55')
    def lambda_2B55():
        ChrWalkTo(0x00FE, 1640, -2000, 41220, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2B55)

    WaitForThreadExit(0x0101, 0x0001)
    SetChrDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0102, 0x0001)
    SetChrDirection(0x0102, 180, 400)
    WaitForThreadExit(0x0102, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#0010030883V#004F#1P呜哇～\n',
            '#001F这里的风景好美啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030884V感觉湖水好像在发光一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030885V#010F据说王都就在湖的对岸。\n',
            '不过现在雾气比较大，暂时看不到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030886V不愧为王国最大的湖啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030887V#006F#1P嗯，在这里钓鱼的话，\n',
            '肯定会好玩得不得了的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030888V#010F不如试一下吧？\n',
            '难得这里的气氛这么好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030889V#501F#1P嗯，说的也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030890V#501F那约修亚你玩什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030891V#010F至于我嘛，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020030892V我这里有本很想看的书，\n',
            '所以会在那边的座位上呆一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030893V#009F#1P咦……看书一点都不好玩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030894V是男孩子的话，\n',
            '就应该多运动运动才对嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020030895V#019F啊哈哈……\n',
            '运动方面交给你就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2DFC')
    def lambda_2DFC():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_2DFC')

    DispatchAsync2(0x0101, 0x0001, lambda_2DFC)

    SetChrDirection(0x0102, 270, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    ChrWalkTo(0x0102, -5760, 500, 42760, 3000, 0x00)
    SetChrChipByIndex(0x000C, 5)
    SetChrPos(0x000C, -6920, 700, 41300, 90)
    ClearChrFlags(0x000C, 0x0080)
    TerminateThread(0x0101, 0xFF)
    FormationDelMember(0x01, 0xFF)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x03, 0xFF)
    SetChrPos(0x0101, 2260, -2000, 39790, 225)
    ChrTurnDirection(0x0101, 0x000C, 0)

    ChrTalk(
        0x0101,
        (
            '#0010030896V#007F#1P嘁……\n',
            '约修亚真没意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030897V#006F算了算了。\n',
            '还是马上挑一个场地吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 225, 400)
    CameraMove(0, -2000, 35324, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010030898V#006F嗯……\n',
            '栈桥周围的环境好像比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0067, 7, 0x33F))
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x2F25
@scena.Code('func_0A_2F25')
def func_0A_2F25():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FC9',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)

    ChrTalk(
        0x0101,
        (
            '#0010030935V#006F嗯……\n',
            '还是觉得这里最好呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030936V呵呵呵，还是快点开始吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【开始钓鱼】\n'),
            TXT(0x01, '【再等一下】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000001, 'loc_2FED'),
        (0x00000000, 'loc_3053'),
        (-1, 'loc_3FC7'),
    )

    def _loc_2FED(): pass

    label('loc_2FED')

    ChrTalk(
        0x0101,
        (
            '#0010030937V#000F唔……\n',
            '虽然觉得这里不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030938V还是去向旅馆的人\n',
            '打听打听有没有更好的地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FC7')

    def _loc_3053(): pass

    label('loc_3053')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 4, 0x344)),
            Expr.Return,
        ),
        'loc_3F6C',
    )

    ChrWalkTo(0x0101, -2930, -1970, 32500, 2000, 0x00)
    SetChrDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0001, 0x0002)

    @scena.Lambda('lambda_3080')
    def lambda_3080():
        CameraMove(-3320, -1970, 30110, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3080)

    @scena.Lambda('lambda_3098')
    def lambda_3098():
        OP_6C(225000, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3098)

    @scena.Lambda('lambda_30A8')
    def lambda_30A8():
        CameraSetDistance(3290, 3500)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_30A8)

    @scena.Lambda('lambda_30B8')
    def lambda_30B8():
        OP_67(0, 9780, -10000, 3500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_30B8)

    Sleep(3500)

    def _loc_30CF(): pass

    label('loc_30CF')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F4F',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31F5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010030939V#000F那么，要不要换个方向呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【换】\n'),
            TXT(0x01, '【不换】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_317A'),
        (0x00000001, 'loc_31EF'),
        (-1, 'loc_31F2'),
    )

    def _loc_317A(): pass

    label('loc_317A')

    ClearChrFlags(0x0101, 0x0002)

    @scena.Lambda('lambda_3185')
    def lambda_3185():
        CameraMove(-2930, -1970, 32500, 1200)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3185)

    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    ChrJumpTo(0x0101, -2930, -1970, 32500, 600, 3000)
    WaitForThreadExit(0x0000, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010030940V#000F嗯～\n',
            '往哪个方向钓鱼比较好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_31F2')

    def _loc_31EF(): pass

    label('loc_31EF')

    Jump('loc_31F2')

    def _loc_31F2(): pass

    label('loc_31F2')

    Jump('loc_325A')

    def _loc_31F5(): pass

    label('loc_31F5')

    SetChrDirection(0x0101, 225, 400)
    Sleep(400)

    SetChrDirection(0x0101, 135, 400)
    Sleep(400)

    SetChrDirection(0x0101, 180, 400)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010030941V#000F对了，在这栈桥钓鱼的话，\n',
            '面向哪个方向比较好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_325A(): pass

    label('loc_325A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3441',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【位于西侧的栈桥周围】\n'),
            TXT(0x01, '【太阳照耀下的南侧湖面】\n'),
            TXT(0x02, '【东侧的林木树枝延伸处附近】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3309'),
        (0x00000001, 'loc_3355'),
        (0x00000002, 'loc_33A1'),
        (-1, 'loc_33ED'),
    )

    def _loc_3309(): pass

    label('loc_3309')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3319')
    def lambda_3319():
        SetChrDirection(0x0101, 253, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3319)

    @scena.Lambda('lambda_3327')
    def lambda_3327():
        OP_6C(278000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3327)

    @scena.Lambda('lambda_3337')
    def lambda_3337():
        CameraSetDistance(3290, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3337)

    CameraMove(-6980, -2200, 31000, 2000)

    Jump('loc_33ED')

    def _loc_3355(): pass

    label('loc_3355')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x64),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_3365')
    def lambda_3365():
        SetChrDirection(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3365)

    @scena.Lambda('lambda_3373')
    def lambda_3373():
        OP_6C(232000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3373)

    @scena.Lambda('lambda_3383')
    def lambda_3383():
        CameraSetDistance(3290, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3383)

    CameraMove(-3010, -2200, 29250, 2000)

    Jump('loc_33ED')

    def _loc_33A1(): pass

    label('loc_33A1')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xC8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_33B1')
    def lambda_33B1():
        SetChrDirection(0x0101, 100, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_33B1)

    @scena.Lambda('lambda_33BF')
    def lambda_33BF():
        OP_6C(149000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_33BF)

    @scena.Lambda('lambda_33CF')
    def lambda_33CF():
        CameraSetDistance(3290, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_33CF)

    CameraMove(1790, -2200, 32590, 2000)

    Jump('loc_33ED')

    def _loc_33ED(): pass

    label('loc_33ED')

    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010030942V#006F嗯嗯，大概就选这边吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030943V#505F那么，用什么来做饵呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3554')

    def _loc_3441(): pass

    label('loc_3441')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x64),
            Expr.Div2,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x64),
            Expr.Mul2,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000000, 'loc_346A'),
        (0x00000064, 'loc_34AC'),
        (0x000000C8, 'loc_34EE'),
        (-1, 'loc_3530'),
    )

    def _loc_346A(): pass

    label('loc_346A')

    @scena.Lambda('lambda_3470')
    def lambda_3470():
        SetChrDirection(0x0101, 253, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3470)

    @scena.Lambda('lambda_347E')
    def lambda_347E():
        OP_6C(278000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_347E)

    @scena.Lambda('lambda_348E')
    def lambda_348E():
        CameraSetDistance(3290, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_348E)

    CameraMove(-6980, -2200, 31000, 1000)

    Jump('loc_3530')

    def _loc_34AC(): pass

    label('loc_34AC')

    @scena.Lambda('lambda_34B2')
    def lambda_34B2():
        SetChrDirection(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34B2)

    @scena.Lambda('lambda_34C0')
    def lambda_34C0():
        OP_6C(232000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_34C0)

    @scena.Lambda('lambda_34D0')
    def lambda_34D0():
        CameraSetDistance(3290, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_34D0)

    CameraMove(-3010, -2200, 29250, 1000)

    Jump('loc_3530')

    def _loc_34EE(): pass

    label('loc_34EE')

    @scena.Lambda('lambda_34F4')
    def lambda_34F4():
        SetChrDirection(0x0101, 100, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_34F4)

    @scena.Lambda('lambda_3502')
    def lambda_3502():
        OP_6C(149000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3502)

    @scena.Lambda('lambda_3512')
    def lambda_3512():
        CameraSetDistance(3290, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3512)

    CameraMove(1790, -2200, 32590, 1000)

    Jump('loc_3530')

    def _loc_3530(): pass

    label('loc_3530')

    ChrTalk(
        0x0101,
        (
            '#0010030944V#000F这次用什么鱼饵呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3554(): pass

    label('loc_3554')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【鱼拟饵】\n'),
            TXT(0x01, '【生鱼饵】\n'),
            TXT(0x02, '【虫拟饵】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_35CA'),
        (0x00000001, 'loc_35D7'),
        (0x00000002, 'loc_35E4'),
        (-1, 'loc_35F1'),
    )

    def _loc_35CA(): pass

    label('loc_35CA')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_35F1')

    def _loc_35D7(): pass

    label('loc_35D7')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0xA),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_35F1')

    def _loc_35E4(): pass

    label('loc_35E4')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x14),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_35F1')

    def _loc_35F1(): pass

    label('loc_35F1')

    ChrTalk(
        0x0101,
        (
            '#0010030945V#001F好～啦，\n',
            '接下来就可以悠然自得地等鱼上钩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1500)
    SetChrFlags(0x0101, 0x0004)
    SetChrChipByIndex(0x0101, 11)
    SetChrFlags(0x0101, 0x0002)
    SetChrFlags(0x0101, 0x0020)
    SetChrSubChip(0x0101, 0)

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x64),
            Expr.Div,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_369E',
    )

    SetChrPos(0x0101, -2950, -2200, 32080, 225)
    OP_0D()

    @scena.Lambda('lambda_367C')
    def lambda_367C():
        CameraSetDistance(3000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_367C)

    @scena.Lambda('lambda_368C')
    def lambda_368C():
        CameraMove(-4440, -2200, 30770, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_368C)

    def _loc_369E(): pass

    label('loc_369E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x64),
            Expr.Div,
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36EB',
    )

    SetChrPos(0x0101, -2960, -2200, 32049, 180)
    OP_0D()

    @scena.Lambda('lambda_36C9')
    def lambda_36C9():
        CameraSetDistance(3000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_36C9)

    @scena.Lambda('lambda_36D9')
    def lambda_36D9():
        CameraMove(-2990, -2200, 31970, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_36D9)

    def _loc_36EB(): pass

    label('loc_36EB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x64),
            Expr.Div,
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3738',
    )

    SetChrPos(0x0101, -2029, -2200, 32970, 90)
    OP_0D()

    @scena.Lambda('lambda_3716')
    def lambda_3716():
        CameraSetDistance(3000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_3716)

    @scena.Lambda('lambda_3726')
    def lambda_3726():
        CameraMove(100, -2200, 32640, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3726)

    def _loc_3738(): pass

    label('loc_3738')

    PlaySE(132, 0x00, 0x64)
    OP_99(0x0101, 0x00, 0x06, 1500)
    Sleep(400)

    PlaySE(25, 0x00, 0x64)
    Sleep(1200)

    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)

    ExecExpressionWithReg(
        0x0003,
        (
            Expr.Rand,
            (Expr.PushLong, 0x4),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3788',
    )

    Sleep(4000)

    Jump('loc_37C4')

    def _loc_3788(): pass

    label('loc_3788')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_379D',
    )

    Sleep(3000)

    Jump('loc_37C4')

    def _loc_379D(): pass

    label('loc_379D')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37B2',
    )

    Sleep(5000)

    Jump('loc_37C4')

    def _loc_37B2(): pass

    label('loc_37B2')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_37C4',
    )

    Sleep(2000)

    def _loc_37C4(): pass

    label('loc_37C4')

    TerminateThread(0x0101, 0xFF)
    Fade(1000)

    @scena.Lambda('lambda_37D3')
    def lambda_37D3():
        CameraSetDistance(2800, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_37D3)

    @scena.Lambda('lambda_37E3')
    def lambda_37E3():
        OP_99(0x00FE, 0x08, 0x0C, 1500)
        Yield()

        Jump('lambda_37E3')

    DispatchAsync2(0x0101, 0x0003, lambda_37E3)

    OP_63(0x0101)
    Sleep(700)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010030946V#508F太棒了，等到了！\n',
            '终于有鱼上钩了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030947V#002F好，接下来就是关键了。\n',
            '怎么把鱼钓上来才好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【一口气钓上来】\n'),
            TXT(0x01, '【再等待一会儿】\n'),
            TXT(0x02, '【慢慢地把鱼儿搞累】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010030948V#009F好！看看我的绝招！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3932'),
        (0x00000001, 'loc_395A'),
        (0x00000002, 'loc_39DF'),
        (-1, 'loc_3A56'),
    )

    def _loc_3932(): pass

    label('loc_3932')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x0),
            Expr.Add2,
            Expr.Return,
        ),
    )

    TerminateThread(0x0101, 0xFF)
    OP_99(0x0101, 0x06, 0x03, 1500)
    PlaySE(24, 0x00, 0x64)
    OP_99(0x0101, 0x03, 0x01, 1500)

    Jump('loc_3A56')

    def _loc_395A(): pass

    label('loc_395A')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    TerminateThread(0x0101, 0xFF)
    OP_99(0x0101, 0x06, 0x04, 1500)
    Sleep(300)

    OP_99(0x0101, 0x04, 0x06, 1500)
    Sleep(100)

    OP_99(0x0101, 0x06, 0x04, 1500)
    Sleep(200)

    OP_99(0x0101, 0x06, 0x04, 1500)
    Sleep(300)

    OP_99(0x0101, 0x04, 0x06, 1500)
    Sleep(100)

    OP_99(0x0101, 0x06, 0x04, 1500)
    Sleep(200)

    OP_99(0x0101, 0x04, 0x06, 1500)
    OP_99(0x0101, 0x06, 0x03, 1500)
    PlaySE(24, 0x00, 0x64)
    OP_99(0x0101, 0x03, 0x01, 1500)

    Jump('loc_3A56')

    def _loc_39DF(): pass

    label('loc_39DF')

    ExecExpressionWithReg(
        0x0001,
        (
            (Expr.PushLong, 0x2),
            Expr.Add2,
            Expr.Return,
        ),
    )

    TerminateThread(0x0101, 0xFF)
    OP_99(0x0101, 0x06, 0x04, 1500)
    Sleep(300)

    OP_99(0x0101, 0x04, 0x06, 1500)
    Sleep(100)

    OP_99(0x0101, 0x06, 0x04, 1500)
    Sleep(100)

    OP_99(0x0101, 0x06, 0x04, 1500)
    OP_99(0x0101, 0x06, 0x01, 1500)
    OP_9E(0x0101, 30, 0, 1000, 6000)
    OP_99(0x0101, 0x01, 0x03, 2500)
    OP_99(0x0101, 0x03, 0x01, 2500)
    PlaySE(24, 0x00, 0x64)

    Jump('loc_3A56')

    def _loc_3A56(): pass

    label('loc_3A56')

    Sleep(1000)

    OP_99(0x0101, 0x10, 0x12, 1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000064, 'loc_3AF3'),
        (0x00000066, 'loc_3AF3'),
        (0x00000070, 'loc_3AF3'),
        (0x00000079, 'loc_3AF3'),
        (0x0000007A, 'loc_3AF3'),
        (0x000000DC, 'loc_3AF3'),
        (0x00000000, 'loc_3B0F'),
        (0x0000000A, 'loc_3B0F'),
        (0x00000014, 'loc_3B0F'),
        (0x00000016, 'loc_3B0F'),
        (0x0000006E, 'loc_3B0F'),
        (0x0000006F, 'loc_3B0F'),
        (0x00000078, 'loc_3B0F'),
        (0x000000CA, 'loc_3B0F'),
        (0x000000D2, 'loc_3B0F'),
        (0x00000001, 'loc_3B29'),
        (0x0000000C, 'loc_3B29'),
        (0x00000065, 'loc_3B29'),
        (0x000000C8, 'loc_3B29'),
        (0x000000D4, 'loc_3B29'),
        (0x00000015, 'loc_3B47'),
        (0x000000C9, 'loc_3B47'),
        (0x000000D3, 'loc_3B47'),
        (0x000000DD, 'loc_3B47'),
        (0x0000000B, 'loc_3B61'),
        (0x000000DE, 'loc_3B61'),
        (0x00000002, 'loc_3B7B'),
        (-1, 'loc_3B93'),
    )

    def _loc_3AF3(): pass

    label('loc_3AF3')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '开孔长靴',
            (TxtCtl.SetColor, 0x0),
            '钓上来了！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3B93')

    def _loc_3B0F(): pass

    label('loc_3B0F')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '胡瓜鱼',
            (TxtCtl.SetColor, 0x0),
            '钓上来了！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3B93')

    def _loc_3B29(): pass

    label('loc_3B29')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '利贝尔鲫鱼',
            (TxtCtl.SetColor, 0x0),
            '钓上来了！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3B93')

    def _loc_3B47(): pass

    label('loc_3B47')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '虹鳟鱼',
            (TxtCtl.SetColor, 0x0),
            '钓上来了！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3B93')

    def _loc_3B61(): pass

    label('loc_3B61')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '橙河鱼',
            (TxtCtl.SetColor, 0x0),
            '钓上来了！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3B93')

    def _loc_3B7B(): pass

    label('loc_3B7B')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '拖鱼',
            (TxtCtl.SetColor, 0x0),
            '钓上来了！',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_3B93')

    def _loc_3B93(): pass

    label('loc_3B93')

    FadeIn(300, 0)
    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1000, 0)
    OP_0D()

    Switch(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        (0x00000064, 'loc_3C27'),
        (0x00000066, 'loc_3C27'),
        (0x00000070, 'loc_3C27'),
        (0x00000079, 'loc_3C27'),
        (0x0000007A, 'loc_3C27'),
        (0x000000DC, 'loc_3C27'),
        (0x00000000, 'loc_3C4F'),
        (0x0000000A, 'loc_3C4F'),
        (0x00000014, 'loc_3C4F'),
        (0x00000016, 'loc_3C4F'),
        (0x0000006E, 'loc_3C4F'),
        (0x0000006F, 'loc_3C4F'),
        (0x00000078, 'loc_3C4F'),
        (0x000000CA, 'loc_3C4F'),
        (0x000000D2, 'loc_3C4F'),
        (0x00000001, 'loc_3C82'),
        (0x0000000C, 'loc_3C82'),
        (0x00000065, 'loc_3C82'),
        (0x000000C8, 'loc_3C82'),
        (0x000000D4, 'loc_3C82'),
        (0x00000015, 'loc_3CB6'),
        (0x000000C9, 'loc_3CB6'),
        (0x000000D3, 'loc_3CB6'),
        (0x000000DD, 'loc_3CB6'),
        (0x0000000B, 'loc_3CE4'),
        (0x000000DE, 'loc_3CE4'),
        (0x00000002, 'loc_3D27'),
        (-1, 'loc_3DCC'),
    )

    def _loc_3C27(): pass

    label('loc_3C27')

    AddItem(0x011B, 1)

    ChrTalk(
        0x0101,
        (
            '#0010030949V#509F啊，怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DCC')

    def _loc_3C4F(): pass

    label('loc_3C4F')

    AddItem(0x03AC, 1)

    ChrTalk(
        0x0101,
        (
            '#0010030950V#506F啊呀，\n',
            '这小鱼还真可爱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DCC')

    def _loc_3C82(): pass

    label('loc_3C82')

    AddItem(0x03AD, 1)

    ChrTalk(
        0x0101,
        (
            '#0010030951V#501F唉，这个就当作热身运动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DCC')

    def _loc_3CB6(): pass

    label('loc_3CB6')

    AddItem(0x03AE, 1)

    ChrTalk(
        0x0101,
        (
            '#0010030952V#000F嗯，这个收获还可以。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DCC')

    def _loc_3CE4(): pass

    label('loc_3CE4')

    AddItem(0x03AF, 1)

    ChrTalk(
        0x0101,
        (
            '#0010030953V#508F哇，大鱼啊大鱼啊！\n',
            '没想到今天收获这么棒⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DCC')

    def _loc_3D27(): pass

    label('loc_3D27')

    AddItem(0x03B0, 1)

    ChrTalk(
        0x0101,
        (
            '#0010030954V#001F太好啦～！\n',
            '很久没有钓到这么大的鱼了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030955V#507F这么大的鱼，\n',
            '说不定能打破自己的纪录了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030956V#502F它一咬钩我就知道\n',
            '不是条普通的鱼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3DCC')

    def _loc_3DCC(): pass

    label('loc_3DCC')

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DE6',
    )

    WaitEffect(0x0D, 0x01)

    def _loc_3DE6(): pass

    label('loc_3DE6')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3DF6',
    )

    WaitEffect(0x0D, 0x02)

    def _loc_3DF6(): pass

    label('loc_3DF6')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E06',
    )

    WaitEffect(0x0D, 0x03)

    def _loc_3E06(): pass

    label('loc_3E06')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E16',
    )

    WaitEffect(0x0D, 0x04)

    def _loc_3E16(): pass

    label('loc_3E16')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E26',
    )

    WaitEffect(0x0D, 0x05)

    def _loc_3E26(): pass

    label('loc_3E26')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E36',
    )

    WaitEffect(0x0D, 0x06)

    def _loc_3E36(): pass

    label('loc_3E36')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E46',
    )

    WaitEffect(0x0D, 0x07)

    def _loc_3E46(): pass

    label('loc_3E46')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E56',
    )

    WaitEffect(0x0D, 0x08)

    def _loc_3E56(): pass

    label('loc_3E56')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E66',
    )

    WaitEffect(0x0D, 0x09)

    def _loc_3E66(): pass

    label('loc_3E66')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E76',
    )

    WaitEffect(0x0D, 0x0A)

    def _loc_3E76(): pass

    label('loc_3E76')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E86',
    )

    Jump('loc_3F4F')

    def _loc_3E86(): pass

    label('loc_3E86')

    OP_99(0x0101, 0x12, 0x10, 1500)
    Sleep(50)

    SetChrSubChip(0x0101, 0)

    ChrTalk(
        0x0101,
        (
            '#0010030957V#505F接下来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030958V要做些什么好呢。\n',
            '再继续钓鱼吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '【继续钓鱼】\n'),
            TXT(0x01, '【不再钓了】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3F47',
    )

    Jump('loc_3F4F')

    def _loc_3F47(): pass

    label('loc_3F47')

    Sleep(100)

    Jump('loc_30CF')

    def _loc_3F4F(): pass

    label('loc_3F4F')

    SetScenaFlags(ScenaFlag(0x0068, 5, 0x345))
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T1500._SN', 100, 0, 1)
    IdleLoop()

    Jump('loc_3FC4')

    def _loc_3F6C(): pass

    label('loc_3F6C')

    SetScenaFlags(ScenaFlag(0x0068, 6, 0x346))

    ChrTalk(
        0x0101,
        (
            '#0010030959V#004F啊……\n',
            '我还没有钓鱼竿呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030960V不知道能不能\n',
            '向旅馆的人借一支呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_3FC4(): pass

    label('loc_3FC4')

    Jump('loc_3FC7')

    def _loc_3FC7(): pass

    label('loc_3FC7')

    EventEnd(0x00)

    def _loc_3FC9(): pass

    label('loc_3FC9')

    Return()

# id: 0x000B offset: 0x3FCA
@scena.Code('func_0B_3FCA')
def func_0B_3FCA():
    EventBegin(0x00)
    FadeIn(5000, 0)
    CameraMove(-3320, -1970, 30110, 0)
    OP_6C(257000, 0)
    CameraSetDistance(3290, 0)
    OP_67(0, 6980, -10000, 0)
    SetChrPos(0x0101, -2930, -1970, 32500, 180)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, -4850, 1140, 41360, 0)
    OP_64(0x00, 0x0001)
    SetChrFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_403F')
    def lambda_403F():
        CameraMove(-3013, -1970, 32740, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_403F)

    @scena.Lambda('lambda_4057')
    def lambda_4057():
        CameraSetDistance(2800, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_4057)

    @scena.Lambda('lambda_4067')
    def lambda_4067():
        OP_6C(315000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4067)

    @scena.Lambda('lambda_4077')
    def lambda_4077():
        OP_67(0, 11000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4077)

    Sleep(5000)

    ChrTalk(
        0x0101,
        (
            '#0010030969V#501F啊～已经傍晚了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010030970V#006F嗯！\n',
            '今天战果累累呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030971V#001F看呀看呀，约修亚。\n',
            '今天我钓到一条大～鱼呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4125')
    def lambda_4125():
        CameraMove(-4150, 500, 37765, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4125)

    @scena.Lambda('lambda_413D')
    def lambda_413D():
        OP_67(0, 4400, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_413D)

    @scena.Lambda('lambda_4155')
    def lambda_4155():
        CameraSetDistance(3600, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4155)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010030972V#004F……咦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4184')
    def lambda_4184():
        CameraMove(-3850, 500, 42640, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4184)

    @scena.Lambda('lambda_419C')
    def lambda_419C():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_419C)

    @scena.Lambda('lambda_41B4')
    def lambda_41B4():
        CameraSetDistance(2800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_41B4)

    ChrWalkTo(0x0101, -3000, -2000, 38146, 6000, 0x00)
    ChrWalkTo(0x0101, 1440, -2000, 39270, 6000, 0x00)
    ChrWalkTo(0x0101, 1440, -2000, 40950, 6000, 0x00)
    ChrWalkTo(0x0101, -3850, 500, 42640, 6000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010030973V#002F约修亚？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    SetChrDirection(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030974V#004F哎呀，这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -4124, 500, 42035, 2000, 0x00)
    SetChrFlags(0x000D, 0x0080)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '《实录·百日战役》',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    AddItem(0x0331, 1)

    ChrTalk(
        0x0101,
        (
            '#0010030975V#501F约修亚忘了拿吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030976V这个约修亚，虽说平时做事很稳妥，\n',
            '不过也经常露出马虎的一面呢～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010030977V#001F算了，我先帮他收起来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 90, 400)
    Sleep(200)

    SetChrDirection(0x0101, 225, 400)
    Sleep(200)

    SetChrDirection(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010030978V#000F话说回来，\n',
            '约修亚到底跑到哪去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x43B0
@scena.Code('func_0C_43B0')
def func_0C_43B0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4CB6',
    )

    EventBegin(0x00)
    FormationAddMember(0x01, 0xFF)
    SetChrPos(0x0102, -44990, -1970, 38500, 180)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0101, 0x0102, 0)

    @scena.Lambda('lambda_43FB')
    def lambda_43FB():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_43FB)

    CameraMove(-44640, -1970, 41750, 3000)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    SetChrPos(0x0101, -40520, -2000, 48190, 194)

    ChrTalk(
        0x0102,
        (
            '#0020031025V#013F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031026V呀嗬～沉默的少年。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 255, 200)
    ChrWalkTo(0x0101, -44870, -2000, 43078, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031027V#006F怎么站在这里\n',
            '一动不动地发呆啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_44E6')
    def lambda_44E6():
        ChrWalkTo(0x00FE, -45000, -1970, 40650, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_44E6)

    ChrTurnDirection(0x0102, 0x0101, 400)
    CameraMove(-45080, -2000, 39790, 1500)

    ChrTalk(
        0x0102,
        (
            '#0020031028V#019F哈哈……\n',
            '我并没有发呆啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031029V#010F已经钓完鱼了吗？\n',
            '今天玩得很开心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031030V#001F嗯，非常开心。\n',
            '很久都没有这么痛快了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031031V#501F啊……对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -45030, -1970, 39500, 3000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把《实录·百日战役》拿了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010031032V#006F#2P真是的～说自己想要看书，\n',
            '看完了却不把书收拾好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031033V你呀，有时候也挺马虎的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031034V#013F……啊啊……\n',
            '刚才把那本书看完了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031035V#010F觉得眼睛有点累，\n',
            '于是就在周围走走散一下心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1200)

    OP_92(0x0101, 0x0102, 650, 2000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010031036V#007F#2P哼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrFlags(0x0102, 0x0004)
    SetChrDirection(0x0102, 45, 0)
    ChrMoveTo(0x0102, -45440, -1970, 38220, 2000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020031037V#014F怎、怎么了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031038V#509F#2P难道你又开始一个人沉思，\n',
            '想一些乱七八糟的问题？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031039V你这种性格啊，我可是最了解不过的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031040V#013F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031041V#002F#2P这样很不公平呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031042V因为你总会在我失意的时候陪伴着我，\n',
            '在我悲伤的时候给我安慰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031043V#003F虽然我也知道，\n',
            '自己还无法像老爸那样值得依靠……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_48D7')
    def lambda_48D7():
        CameraMove(-44980, -1970, 39200, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_48D7)

    ChrWalkTo(0x0101, -44650, -1970, 38260, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0101, 0)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010031044V#000F#4P不过，我至少还可以像这样呆在你身边。\n',
            '无论何时何地，我都可以为你分担烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031045V#013F#1P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031046V…………抱歉…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031047V#006F#4P这个时候，\n',
            '应该是说谢谢才对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031048V#006F虽说约修亚你头脑很聪明，\n',
            '不过毕竟也有需要别人安慰的时候啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031049V#010F#1P哈哈，说的也对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031050V#019F谢谢你，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031051V#502F#4P嗯嗯，别客气别客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031052V#004F啊……对了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031053V#001F吹一曲口琴给我听吧。\n',
            '就当作是报答我的礼物。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031054V#015F#1P如你所愿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031055V#010F『星之所在』，可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031056V#001F#4P嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x00000BB8)

    @scena.Lambda('lambda_4B5F')
    def lambda_4B5F():
        OP_69(0x0102, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4B5F)

    @scena.Lambda('lambda_4B6D')
    def lambda_4B6D():
        CameraSetDistance(2600, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_4B6D)

    ChrMoveTo(0x0101, -44300, -1970, 38180, 1000, 0x00)
    Sleep(500)

    ChrJumpTo(0x0101, -43950, -1600, 38170, 700, 5000)
    SetChrChipByIndex(0x0101, 9)
    WaitForThreadExit(0x0000, 0x0001)
    Sleep(1000)

    Fade(250)
    SetChrChipByIndex(0x0102, 8)
    Sleep(1000)

    OP_0D()

    @scena.Lambda('lambda_4BCC')
    def lambda_4BCC():
        OP_99(0x00FE, 0x00, 0x07, 800)
        Yield()

        Jump('lambda_4BCC')

    DispatchAsync2(0x0102, 0x0001, lambda_4BCC)

    Sleep(500)

    PlayBGM(70)
    Sleep(5000)

    SetChrPos(0x000F, -30770, -3000, 32509, 273)
    SetChrFlags(0x000F, 0x0040)
    OP_A1(0x000F, 0x0003)
    OP_72(0x0003, 0x0004)
    Sleep(100)

    Fade(1000)
    TerminateThread(0x0008, 0xFF)
    SetChrBattleFlags(0x0008, 0x0020)
    SetChrPos(0x0008, -29670, -2900, 32420, 150)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0008, 0x0008)
    ClearChrFlags(0x0008, 0x0004)
    SetChrChipByIndex(0x0008, 10)
    SetChrSubChip(0x0008, 0)
    CameraMove(-29670, -1970, 32420, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(213000, 0)
    OP_6E(307, 0)
    Sleep(2000)

    OP_62(0x0008, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    SetChrSubChip(0x0008, 2)
    Sleep(3000)

    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    SetMapFlags(0x02000000)
    NewScene('ED6_DT01/T1510._SN', 100, 0, 0)
    IdleLoop()

    def _loc_4CB6(): pass

    label('loc_4CB6')

    Return()

# id: 0x000D offset: 0x4CB7
@scena.Code('func_0D_4CB7')
def func_0D_4CB7():
    SetChrFlags(0x0008, 0x0080)
    EventBegin(0x00)
    SetChrFlags(0x0102, 0x0004)
    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x0102, -45440, -1970, 38220, 90)
    SetChrPos(0x0101, -43950, -1600, 38170, 270)
    SetChrChipByIndex(0x0101, 9)
    SetChrChipByIndex(0x0102, 8)

    @scena.Lambda('lambda_4CFA')
    def lambda_4CFA():
        OP_99(0x00FE, 0x00, 0x07, 800)
        Yield()

        Jump('lambda_4CFA')

    DispatchAsync2(0x0102, 0x0001, lambda_4CFA)

    CameraMove(-44980, -1970, 39200, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_21()
    TerminateThread(0x0102, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031057V#008F#4P啊……怎么说呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031058V总觉得这首曲子……\n',
            '在夕阳之下倾听的时候，\n',
            '有种让人忍不住流泪的悲伤意境。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(250)
    SetChrChipByIndex(0x0102, 65535)
    SetChrSubChip(0x0102, 0)
    OP_0D()
    Sleep(500)

    SetChrDirection(0x0102, 180, 400)
    PlayBGM(48)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020031059V#013F#1P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031060V你还是一样……\n',
            '什么都没有问过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031061V#002F#4P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031062V#506F啊哈……我们不是约定了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031063V直到你愿意向我倾诉之前，\n',
            '我什么都不会问的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031064V#006F而且……已经五年了。\n',
            '我们两个，不是一直都相处得很好吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031065V#013F#1P是啊……已经五年了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031066V为什么你能什么都不问？\n',
            '就这样接纳我，和我一起生活呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031067V#015F那一天，被父亲从外面抱回来，\n',
            '满身伤痕的孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031068V对一个从没讲过自己的过去、\n',
            '来历不明的男孩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 200)
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020031069V#012F#1P……为什么你们可以\n',
            '这么宽容地接纳这样一个人……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_5031')
    def lambda_5031():
        ChrJumpTo(0x00FE, -44300, -1970, 38180, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_5031)

    ChrTalk(
        0x0101,
        (
            '#0010031070V#501F#4P嘿咻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_506F')
    def lambda_506F():
        CameraMove(-45440, -1970, 38220, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_506F)

    ChrWalkTo(0x0101, -44650, -1970, 38260, 1000, 0x00)
    SetChrDirection(0x0101, 180, 400)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010031071V#006F这是理所当然的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031072V因为约修亚是我们的家人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031073V#014F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031074V#006F之前不是跟你说过吗。\n',
            '我呢，其实一直以来\n',
            '都非常清楚你的事情哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031075V#007F比如说喜欢看书啦，\n',
            '平时有空就喜欢摆弄武器啦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031076V虽然平时待人彬彬有礼，\n',
            '不过也一直与别人保持距离……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031077V#018F等、等一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031078V#001F不过，你真的很会照顾人哦，\n',
            '应该说是标准的居家型好男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031079V#014F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031080V#007F当然了，在我们相识之前，\n',
            '你去过哪里做过什么我都不清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031081V不过不单是你，\n',
            '就连老爸以前的事情我也不是很清楚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031082V#006F就算这样，我和老爸依旧是一家人，\n',
            '这一点永远都不会改变啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031083V我很清楚老爸的性格、爱好，\n',
            '还有料理的口味。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031084V正因为朝夕相处，共同生活，\n',
            '才能够亲身感觉到这一切。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031085V#001F约修亚对我来说，也是一样的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031086V#015F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031087V#011F我真的……说不过你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031088V从最初见面时就知道了……\n',
            '就在你用力使出飞踢的那一刻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031089V#004F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031090V我、我有做过这种事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031091V#019F嗯，而且是对一个受伤的男孩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031092V#008F啊、啊哈哈……\n',
            '小时候不懂事嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031093V#010F是是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031094V#015F喂，艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031095V#501F怎么了，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031096V#012F这个案件，无论如何也要解决。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031097V虽然还不知道\n',
            '父亲是不是真的被抓了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031098V但我们一定要查个水落石出，绝对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031099V#006F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031100V那当然啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031101V#010F呵呵……\n',
            '是时候回去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031102V旅馆已经准备好饭菜了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031103V#007F嗯，我饿得肚子咕咕响呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031104V#006F那我们就好好地大吃一顿，\n',
            '为今晚的作战行动做好准备。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)
    FadeOut(1500, 0, -1)
    OP_0D()
    SetChrPos(0x0101, -44940, -2000, 42440, 0)
    SetChrPos(0x0102, -44940, -2000, 42440, 0)
    OP_69(0x0101, 0)
    SetScenaFlags(ScenaFlag(0x0069, 4, 0x34C))
    Sleep(500)

    FadeIn(1000, 0)
    PlayBGM(15)
    EventEnd(0x00)
    ClearChrFlags(0x0101, 0x0004)
    ClearChrFlags(0x0102, 0x0004)
    ClearMapFlags(0x10000000)

    Return()

# id: 0x000E offset: 0x572B
@scena.Code('func_0E_572B')
def func_0E_572B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 5, 0x34D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5A7B',
    )

    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0069, 5, 0x34D))
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010031105V#004F啊，忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_577C')
    def lambda_577C():
        ChrTurnDirection(0x0101, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_577C)

    @scena.Lambda('lambda_578A')
    def lambda_578A():
        OP_6C(45000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_578A)

    CameraMove(-30910, -850, 52160, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010031106V#000F约修亚，这本书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031107V#014F啊啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0102, 900, 2000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔把《实录·百日战役》拿了出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0102,
        (
            '#0020031108V#010F我已经看完了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031109V而且这本书挺占地方的，怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '『我也想看一下。』\n'),
            TXT(0x01, '『不如送给别人吧。』\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5906'),
        (0x00000001, 'loc_5A22'),
        (-1, 'loc_5A79'),
    )

    def _loc_5906(): pass

    label('loc_5906')

    ChrTalk(
        0x0101,
        (
            '#0010031110V#501F看起来是本很深奥的书啊。\n',
            '不过我也想看一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031111V#010F我想对你来说没什么难懂的，\n',
            '因为有很多内容你应该都知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031112V艾丝蒂尔，就试试看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031113V#006F好的，我挑战一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '《实录·百日战役》',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0069, 1, 0x349))

    Jump('loc_5A79')

    def _loc_5A22(): pass

    label('loc_5A22')

    RemoveItem(0x0331, 1)

    ChrTalk(
        0x0101,
        (
            '#0010031114V#501F送给谁呢？\n',
            '还是扔掉吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031115V#010F是啊……就这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A79')

    def _loc_5A79(): pass

    label('loc_5A79')

    EventEnd(0x00)

    def _loc_5A7B(): pass

    label('loc_5A7B')

    Return()

# id: 0x000F offset: 0x5A7C
@scena.Code('func_0F_5A7C')
def func_0F_5A7C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0067, 6, 0x33E)),
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B09',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5ABD',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x0101,
        (
            '#0010031016V#000F啊……\n',
            '这边是街道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5AF0')

    def _loc_5ABD(): pass

    label('loc_5ABD')

    ChrTalk(
        0x0101,
        (
            '#0010031017V#007F……他不可能一个人出去散步吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5AF0(): pass

    label('loc_5AF0')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    EventEnd(0x00)

    Jump('loc_5C59')

    def _loc_5B09(): pass

    label('loc_5B09')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0068, 5, 0x345)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5B7F',
    )

    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0010031018V#000F啊……\n',
            '这边是街道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031019V真是的，\n',
            '约修亚到底跑到哪里去了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    EventEnd(0x00)

    Jump('loc_5C59')

    def _loc_5B7F(): pass

    label('loc_5B7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 4, 0x34C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0069, 6, 0x34E)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5C59',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C07',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020031020V#010F艾丝蒂尔，你去哪儿？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031021V我们该回房间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031022V#000F嗯，明～白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5C3E')

    def _loc_5C07(): pass

    label('loc_5C07')

    ChrTalk(
        0x0102,
        (
            '#0020031023V#010F这边是街道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031024V我们回房间去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5C3E(): pass

    label('loc_5C3E')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_5C59(): pass

    label('loc_5C59')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

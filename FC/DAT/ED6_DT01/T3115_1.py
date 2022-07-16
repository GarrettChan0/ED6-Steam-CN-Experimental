import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3115_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3115_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3115.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x4F63
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
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
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
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
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0xA9
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xAA
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(2300, 0, 2540, 0)
    SetChrPos(0x0101, 1850, 0, 1780, 0)
    SetChrPos(0x0102, 3300, 0, 2100, 0)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_103',
    )

    SetChrPos(0x0107, 2650, 0, 1120, 0)

    def _loc_103(): pass

    label('loc_103')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_122',
    )

    SetChrPos(0x013C, 2530, 0, 3050, 359)

    def _loc_122(): pass

    label('loc_122')

    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0550181117V#800F咦，怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181001V喵呀～～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550181119V#802F哦，安东尼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181120V你那样叫，\n',
            '是想说些什么吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x013C,
        (
            '#2030181121V喵～噢，\n',
            '喵呀～～噢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(120)

    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181122V#509F唔，这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181123V#017F怎么看都很有嫌疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070181124V#561F是啊～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0008,
        (
            '#0550181125V#802F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181126V你们在说什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181127V#002F工房长先生，\n',
            '今天你去过医务室吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0550181128V#802F啊…………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550181129V#805F没、没有……\n',
            '没有去过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181130V#012F我们正在寻找\n',
            '被人从医务室里带走的香烟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181131V让我们对这个房间\n',
            '进行一下调查好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0550181132V#806F唔，哦，\n',
            '倒是没什么不行的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181133V#507F那就不用顾虑了，\n',
            '让我们好好调查一番吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002C, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x430
@scena.Code('func_03_430')
def func_03_430():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-102680, 0, 106860, 0)
    SetChrPos(0x0101, -103170, 0, 107210, 90)
    SetChrPos(0x0102, -102910, 0, 106140, 40)
    SetChrPos(0x0107, -104120, 0, 106520, 90)

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_49A',
    )

    SetChrPos(0x013C, -104780, 0, 107680, 90)

    def _loc_49A(): pass

    label('loc_49A')

    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010180648V#000F不好意思，可以打扰一下吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180649V您是普罗梅笛先生……吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x0013, 0x0010)
    TalkBegin(0x0013)
    ClearChrFlags(0x0013, 0x0010)
    OP_62(0x00FE, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    OP_4A(0x00FE, 255)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2080180650V嗯，\n',
            '我就是普罗梅笛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180651V有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180652V#006F嗯，有点小事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180653V是这样的，\n',
            '我们在找运输车用的导力引擎。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180654V想问一下普罗梅笛先生，\n',
            '如果您知道放在哪里的话，\n',
            '可以告诉我们吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180655V运输车用的\n',
            '导力引擎吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180656V实在很抱歉，\n',
            '我完全不知道放在哪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180657V#004F咦？怎么会呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180658V#014F我们听说普罗梅笛先生您\n',
            '是负责管理运输车的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2080180659V啊～～\n',
            '那是很久以前的事情了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180660V那个职务是轮流担当的，\n',
            '会定期更换人员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180661V而且………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180662V如果问我现在的负责人是谁，\n',
            '老实说我也不知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180663V#007F呼………………\n',
            '想问的他都抢先回答了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180664V那么，这样就行了吧？\n',
            '我还有很多事情要做。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180665V#010F非常抱歉，\n',
            '在您百忙之中前来打扰。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2080180666V嗯，那我先去忙别的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0013, 360, 400)
    OP_4B(0x00FE, 255)

    @scena.Lambda('lambda_0853')
    def lambda_0853():
        CameraMove(-103770, 0, 106670, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0853)

    SetChrDirection(0x0101, 223, 400)
    SetChrDirection(0x0102, 286, 400)
    WaitForThreadExit(0x00FE, 0x0001)

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_A55',
    )

    ChrTalk(
        0x0101,
        (
            '#0010180667V#003F唔……\n',
            '怎么和之前说的不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180668V#561F不、不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180669V因为设备的管理\n',
            '是件相当麻烦的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180670V#013F普罗梅笛先生不知道的话……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180671V就只剩在『卡佩尔』上\n',
            '看到过的那个线索了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180672V#505F嗯，\n',
            '应该在地下工场的入口……\n',
            '资料上面是这么记载的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180673V#060F啊，\n',
            '那是卡鲁迪亚隧道的出口。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180674V那片区域放置了各种各样的零部件。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180675V#010F好，\n',
            '那么我们就到地下去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180676V#006F嗯，好的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC0')

    def _loc_A55(): pass

    label('loc_A55')

    ChrTalk(
        0x0101,
        (
            '#0010180677V#003F唔……这下麻烦了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180678V怎么和之前说的不一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180668V#561F不、不好意思。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070180669V因为设备的管理\n',
            '是件相当麻烦的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180681V#010F算了，这也是没办法事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180682V我们还是想想其他办法\n',
            '去调查一下运输车的事情吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180683V我想应该会有其他线索的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0029, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_DBF',
    )

    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010180684V#505F别的办法……吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180685V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180686V#004F……啊，我想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BFA')
    def lambda_0BFA():
        ChrTurnDirection(0x0107, 0x0101, 0)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0BFA)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180687V#014F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180688V#002F你想想，\n',
            '不久之前我们不是利用了一个\n',
            '什么导力器收集了不少信息吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180689V#060F是演算导力器『卡佩尔』对吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180690V#000F对对，就是它。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180691V#505F我记得那个时候\n',
            '好像看到了有关运输车的事项……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0107, 400)

    ChrTalk(
        0x0102,
        (
            '#0020180692V#014F对啊…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180693V『卡佩尔』里面的确应该有\n',
            '运输车的相关记录。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180694V#010F我们立刻就去调查吧，\n',
            '演算室在五楼哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010180695V#508F好！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0029, 0x01, 0x0004)

    Jump('loc_EC0')

    def _loc_DBF(): pass

    label('loc_DBF')

    ChrTalk(
        0x0101,
        (
            '#0010180696V#505F找其他的方法……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180697V话是这么说，\n',
            '可应该不会那么简单的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020180698V#010F不过，\n',
            '在这里干着急也不是办法。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020180699V也许会有线索的。\n',
            '总之先在工房里转转看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070180700V#060F嗯，好～的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010180701V#006F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010180702V那我们走吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC0(): pass

    label('loc_EC0')

    Sleep(400)

    OP_28(0x0029, 0x01, 0x0001)
    OP_28(0x0029, 0x01, 0x0002)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xED7
@scena.Code('func_04_ED7')
def func_04_ED7():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F5C',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_F5C(): pass

    label('loc_F5C')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F7B',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_F7B(): pass

    label('loc_F7B')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F9A',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_F9A(): pass

    label('loc_F9A')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FB9',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_FB9(): pass

    label('loc_FB9')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FD3',
    )

    @scena.Lambda('lambda_0FCB')
    def lambda_0FCB():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0FCB)

    def _loc_FD3(): pass

    label('loc_FD3')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_FED',
    )

    @scena.Lambda('lambda_0FE5')
    def lambda_0FE5():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0FE5)

    def _loc_FED(): pass

    label('loc_FED')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1007',
    )

    @scena.Lambda('lambda_0FFF')
    def lambda_0FFF():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0FFF)

    def _loc_1007(): pass

    label('loc_1007')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1021',
    )

    @scena.Lambda('lambda_1019')
    def lambda_1019():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1019)

    def _loc_1021(): pass

    label('loc_1021')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_103B',
    )

    @scena.Lambda('lambda_1033')
    def lambda_1033():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_1033)

    def _loc_103B(): pass

    label('loc_103B')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1285',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181239V#000F嗯～打扰一下好吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181240V我们两个是看了公告板而来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1119',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181248V啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181249V来得好晚呀。\n',
            '我还以为你们不来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181247V#506F对不起啊，\n',
            '因为有重要任务在身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1252')

    def _loc_1119(): pass

    label('loc_1119')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_11BB',
    )

    ChrTalk(
        0x00FE,
        (
            '#2120181245V啊……\n',
            '你们终于来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181246V唉，游击士协会\n',
            '哪个支部都是人手不足，\n',
            '这也是没办法的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181247V#506F对不起啊，\n',
            '因为有重要任务在身。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1252')

    def _loc_11BB(): pass

    label('loc_11BB')

    ChrTalk(
        0x00FE,
        (
            '#2120181241V啊……\n',
            '来得好快呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181242V我刚刚才\n',
            '把委托贴上去呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150561V#001F呵呵呵⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181244V#006F我们也是刚调到这里来的，\n',
            '所以干劲十足呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1252(): pass

    label('loc_1252')

    ChrTalk(
        0x00FE,
        (
            '#2120181251V我这就把任务内容予以说明，\n',
            '可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12DB')

    def _loc_1285(): pass

    label('loc_1285')

    ChrTalk(
        0x00FE,
        (
            '#2120181256V咦，是你们。\n',
            '终于来了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181257V我这就把任务内容予以说明，\n',
            '可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_12DB(): pass

    label('loc_12DB')

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
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
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
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13D5',
    )

    ChrTalk(
        0x0101,
        (
            '#0010181252V#501F啊，对不起。\n',
            '现在还不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181253V啊，是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181254V那么等你们办完事了\n',
            '就再到这里来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010170025V#006F嗯，我知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002D, 0x01, 0x4000)

    @scena.Lambda('lambda_13CA')
    def lambda_13CA():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_13CA)

    EventEnd(0x00)

    Return()

    def _loc_13D5(): pass

    label('loc_13D5')

    ChrTalk(
        0x0101,
        (
            '#0010150317V#006F嗯，明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181259V#010F募集临时图书馆员……\n',
            '没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181260V嗯，是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181261V有一些让人\n',
            '束手无策的麻烦事呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181262V#004F束手无策？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181263V啊，这个我们之后再说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181264V在此之前，\n',
            '还有件事情想让你们解决。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181265V我先拜托你们\n',
            '这件事情好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181266V#010F是什么样的事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181267V工房的研究室\n',
            '经常从资料室这里借书……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181268V可是有时期限到了，\n',
            '书却还没有归还。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181269V首先你们就去\n',
            '把那些书找回来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181270V#000F这样啊，很简单嘛。\n',
            '大致到哪里去找呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181271V嗯，借书人的所在地有……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181272V三楼的设计室以及\n',
            '四楼的实验室和医务室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181273V#000F三楼的设计室以及\n',
            '四楼的实验室和医务室……嗯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181274V………………就这些吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181275V嗯，是呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181276V请尽快地找回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181277V#001F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181278V#010F我们会很快找回来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002D, 0x04, 0x04)
    OP_28(0x002D, 0x04, 0x08)
    OP_28(0x002D, 0x01, 0x0001)
    OP_28(0x002D, 0x01, 0x0002)
    Call(1, 0x000D)

    @scena.Lambda('lambda_1750')
    def lambda_1750():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1750)

    EventEnd(0x00)

    Return()

# id: 0x0005 offset: 0x175B
@scena.Code('func_05_175B')
def func_05_175B():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17E0',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_17E0(): pass

    label('loc_17E0')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_17FF',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_17FF(): pass

    label('loc_17FF')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_181E',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_181E(): pass

    label('loc_181E')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_183D',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_183D(): pass

    label('loc_183D')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1857',
    )

    @scena.Lambda('lambda_184F')
    def lambda_184F():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_184F)

    def _loc_1857(): pass

    label('loc_1857')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_1871',
    )

    @scena.Lambda('lambda_1869')
    def lambda_1869():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1869)

    def _loc_1871(): pass

    label('loc_1871')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_188B',
    )

    @scena.Lambda('lambda_1883')
    def lambda_1883():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1883)

    def _loc_188B(): pass

    label('loc_188B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_18A5',
    )

    @scena.Lambda('lambda_189D')
    def lambda_189D():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_189D)

    def _loc_18A5(): pass

    label('loc_18A5')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_18BF',
    )

    @scena.Lambda('lambda_18B7')
    def lambda_18B7():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_18B7)

    def _loc_18BF(): pass

    label('loc_18BF')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181310V怎么样？\n',
            '任务进展的如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181311V#001F呵呵呵～⊙\n',
            '拿来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Return,
        ),
        'loc_1970',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '结晶光学论集',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0342, 1)

    def _loc_1970(): pass

    label('loc_1970')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Return,
        ),
        'loc_19C5',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '明日料理',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0341, 1)

    def _loc_19C5(): pass

    label('loc_19C5')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Return,
        ),
        'loc_1A22',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '猫语日常会话入门',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0340, 1)

    def _loc_1A22(): pass

    label('loc_1A22')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_239F',
    )

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '全部的书都归还了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【募集临时图书馆员】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181282V嗯……没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181283V这么一来，\n',
            '所有的书都找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181284V辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181315V#502F哼哼，这种工作简直轻而易举。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181316V#019F的确是小事一桩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181317V哎呀，果然很靠得住呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181318V那么我就立刻\n',
            '把正式的任务拜托给你们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181319V#501F啊，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181320V就是刚才所说的\n',
            '让人束手无策的麻烦事吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181321V#014F究竟是什么样的任务呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181322V基本的目的还是和刚才一样，\n',
            '找回过了归还期限的资料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181323V需要去寻找的书名为\n',
            '《艾尔贝啄木鸟的生态》。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181324V#015F先记录下来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181325V#000F啊，好的好的…………\n',
            '《啄木鸟的生态》……对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181326V#505F与鸟有关的书……吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E4D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_1DBD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181327V#060F嗯。\n',
            '也许是～吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181328V因为艾尔贝啄木鸟是\n',
            '在很久很久以前出现过的鸟的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E22')

    def _loc_1DBD(): pass

    label('loc_1DBD')

    ChrTalk(
        0x0107,
        (
            '#0070181329V#060F啊，是的。\n',
            '我觉得没错～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181330V因为艾尔贝啄木鸟是\n',
            '在很久很久以前出现过的鸟的名字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E22(): pass

    label('loc_1E22')

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010181331V#000F呼～原来是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E4D(): pass

    label('loc_1E4D')

    ChrTurnDirection(0x0102, 0x00FE, 400)

    ChrTalk(
        0x0102,
        (
            '#0020181332V#010F那么，有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181333V嗯，线索是有的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181334V……请看这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x00FE, 400)
    Sleep(100)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            '#2130181335V',
            (TxtCtl.SetColor, 0x0),
            '到山村的　池中伫立的　石人\n',
            '旁边看看吧　会有收获的',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010181336V#505F虽然记下来了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181337V…………这是什么意思呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181338V是这本书的借书卡\n',
            '上面写的文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181339V总而言之，\n',
            '这个好像就是书的隐藏地点的相关提示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181340V#004F隐藏地点的提示……吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181341V这么说来，\n',
            '一开始借书时就打算把书藏起来了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181342V嗯，好像是的。\n',
            '这是过去的研究员所做的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181343V至于为什么要把书藏起来，\n',
            '我就怎么也想不明白了……\n',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181344V不过，奇怪的人是很多的，\n',
            '这已经可算是这里的传统了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2155',
    )

    OP_62(0x0107, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0107,
        (
            '#0070181345V#067F啊、啊哈哈…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2155(): pass

    label('loc_2155')

    ChrTalk(
        0x00FE,
        (
            '#2120181346V那么接下来就拜托你们了。\n',
            '好好加油去找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010181347V#004F等、等一下，\n',
            '就只有这点线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181348V啊，就只有这些哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181349V正因为如此，\n',
            '我才会委托游击士协会嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181350V#007F呼………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181351V这、这么一说，\n',
            '我就觉得没希望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181352V#010F……我明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181353V困难的任务更要\n',
            '加倍地努力去做才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181354V就在蔡斯周围的地区调查，\n',
            '一定可以找到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181355V我会在这里等着的。\n',
            '找到书之后就把它拿来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181356V#007F呼…………\n',
            '只有加油干了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181357V哦呵呵，我很期待哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23F5')

    def _loc_239F(): pass

    label('loc_239F')

    ChrTalk(
        0x00FE,
        (
            '#2120181282V嗯……没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181359V那么，\n',
            '剩下的书也拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x000D)

    @scena.Lambda('lambda_23EA')
    def lambda_23EA():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_23EA)

    EventEnd(0x00)

    Return()

    def _loc_23F5(): pass

    label('loc_23F5')

    Call(1, 0x000D)

    @scena.Lambda('lambda_23FF')
    def lambda_23FF():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_23FF)

    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x0020)
    OP_28(0x002E, 0x04, 0x02)
    OP_28(0x002E, 0x04, 0x04)
    OP_28(0x002E, 0x04, 0x08)
    OP_28(0x002E, 0x01, 0x0001)
    OP_28(0x002E, 0x01, 0x0002)
    OP_28(0x002E, 0x01, 0x0004)
    OP_28(0x002E, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x243C
@scena.Code('func_06_243C')
def func_06_243C():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24C1',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_24C1(): pass

    label('loc_24C1')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24E0',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_24E0(): pass

    label('loc_24E0')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24FF',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_24FF(): pass

    label('loc_24FF')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_251E',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_251E(): pass

    label('loc_251E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2538',
    )

    @scena.Lambda('lambda_2530')
    def lambda_2530():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2530)

    def _loc_2538(): pass

    label('loc_2538')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2552',
    )

    @scena.Lambda('lambda_254A')
    def lambda_254A():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_254A)

    def _loc_2552(): pass

    label('loc_2552')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_256C',
    )

    @scena.Lambda('lambda_2564')
    def lambda_2564():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2564)

    def _loc_256C(): pass

    label('loc_256C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2586',
    )

    @scena.Lambda('lambda_257E')
    def lambda_257E():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_257E)

    def _loc_2586(): pass

    label('loc_2586')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_25A0',
    )

    @scena.Lambda('lambda_2598')
    def lambda_2598():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_2598)

    def _loc_25A0(): pass

    label('loc_25A0')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181279V哎呀……………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181280V把书拿回来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181281V#508F嗯，拿来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Return,
        ),
        'loc_2662',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '结晶光学论集',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0342, 1)

    def _loc_2662(): pass

    label('loc_2662')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Return,
        ),
        'loc_26B7',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '明日料理',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0341, 1)

    def _loc_26B7(): pass

    label('loc_26B7')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Return,
        ),
        'loc_2714',
    )

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '猫语日常会话入门',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0340, 1)

    def _loc_2714(): pass

    label('loc_2714')

    If(
        (
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2983',
    )

    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '全部的书都归还了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【募集临时图书馆员】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181282V嗯……没错……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181283V这么一来，\n',
            '所有的书都找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181284V辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181285V#010F对不起，\n',
            '这么晚才来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181286V没关系，\n',
            '你们还有别的重要工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181287V在你们最忙的时候\n',
            '还是能坚持完成了任务，\n',
            '我已经很感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181288V#001F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181289V彼此彼此，非常感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181290V那你们以后也要继续努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151344V#000F再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x0020)

    Jump('loc_2C4C')

    def _loc_2983(): pass

    label('loc_2983')

    ChrTalk(
        0x00FE,
        (
            '#2120181293V嗯，没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181294V对了，\n',
            '剩下的书我已经收回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181295V所以，\n',
            '委托就此中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181211V#004F咦……怎么会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181297V我从协会那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181298V你们马上就要\n',
            '调到别的支部去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181299V所以调离之前，\n',
            '必须将委托的事宜整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181300V#013F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181301V对不起。\n',
            '工作半途而废了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181302V#003F真的很抱歉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181303V哎呀，不用在意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181304V你们还有别的重要工作嘛。\n',
            '这也是没办法的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181305V#000F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181306V感谢你们的帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181307V要打起精神哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181309V#508F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【募集临时图书馆员】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x0040)
    Call(1, 0x000D)

    def _loc_2C4C(): pass

    label('loc_2C4C')

    OP_28(0x002D, 0x04, 0x10)
    OP_28(0x002D, 0x01, 0x4000)
    Call(1, 0x000D)

    @scena.Lambda('lambda_2C61')
    def lambda_2C61():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2C61)

    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x2C6C
@scena.Code('func_07_2C6C')
def func_07_2C6C():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CF1',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_2CF1(): pass

    label('loc_2CF1')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D10',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_2D10(): pass

    label('loc_2D10')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D2F',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_2D2F(): pass

    label('loc_2D2F')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D4E',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_2D4E(): pass

    label('loc_2D4E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2D68',
    )

    @scena.Lambda('lambda_2D60')
    def lambda_2D60():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2D60)

    def _loc_2D68(): pass

    label('loc_2D68')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2D82',
    )

    @scena.Lambda('lambda_2D7A')
    def lambda_2D7A():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_2D7A)

    def _loc_2D82(): pass

    label('loc_2D82')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2D9C',
    )

    @scena.Lambda('lambda_2D94')
    def lambda_2D94():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_2D94)

    def _loc_2D9C(): pass

    label('loc_2D9C')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2DB6',
    )

    @scena.Lambda('lambda_2DAE')
    def lambda_2DAE():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_2DAE)

    def _loc_2DB6(): pass

    label('loc_2DB6')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_2DD0',
    )

    @scena.Lambda('lambda_2DC8')
    def lambda_2DC8():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_2DC8)

    def _loc_2DD0(): pass

    label('loc_2DD0')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181360V啊……\n',
            '有什么进展吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181361V#001F嗯，很顺利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181362V#006F书已经带回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181363V#010F请您确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '艾尔贝啄木鸟的生态',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0343, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181364V……哎呀，真让我惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181365V的确是这本书呢。\n',
            '终于找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181366V#502F呵呵呵。\n',
            '我们还只是小试牛刀而已呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181367V说实话，\n',
            '我一直认为已经不可能找回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181368V能够找回来\n',
            '真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181369V这样一来，我就可以放心地\n',
            '把剩下的任务交给你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010181370V#004F啊……………！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181371V……什么，剩下的任务？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181372V#014F……还有其他的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181373V那个研究员隐藏起来的书\n',
            '一共有三本呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181374V就是说，\n',
            '还剩下后面的两本哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181375V……我之前没有说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181376V#509F完全没有，根本就是头一次听说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181377V哎呀，这可真是奇怪了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181378V不过这样也不错嘛。\n',
            '现在你们已经是骑虎难下了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181379V就请你们\n',
            '坚持到最后吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181380V#505F好吧，\n',
            '这倒是没什么关系…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181381V只要别再出现那种含义不明的文字就行了，\n',
            '那东西真是让人摸不着头脑呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x04)"),
            Expr.Return,
        ),
        'loc_3298',
    )

    ChrTalk(
        0x0102,
        (
            '#0020181382V#017F说起来，\n',
            '在卢安也遇到过这样的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3298(): pass

    label('loc_3298')

    ChrTalk(
        0x00FE,
        (
            '#2120181383V哎呀，\n',
            '你们不用担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181384V这本书的提示\n',
            '并不是什么文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181385V#004F啊，真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181386V事实胜于雄辩，\n',
            '我这就让你们看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '　● 　 ●　\n',
            '　　 ×\n',
            '　● 　 ●　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010181387V#509F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181388V……我、我无话可说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181389V#014F……一点说明都没有呢。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_34CA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3478',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181390V#063F……●和×吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181391V唔～是说×记号的地方\n',
            '就是书的所在地吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_34CA')

    def _loc_3478(): pass

    label('loc_3478')

    ChrTalk(
        0x0107,
        (
            '#0070181392V#063F……●和×吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070181393V唔～是说×记号的地方\n',
            '就是书的所在地吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_34CA(): pass

    label('loc_34CA')

    ChrTalk(
        0x00FE,
        (
            '#2120181394V要寻找的这本书名为\n',
            '《哈茨少年冒险记·下》哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181395V#000F好的好的，\n',
            '《哈茨少年冒险记·下》对吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181396V资料室里只留有上卷，\n',
            '『下卷在哪里？』想看的人经常这么嚷。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181397V好了，\n',
            '你们就鼓足干劲去找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181398V#013F话虽如此，\n',
            '这次的更难解决啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181399V#007F与现在这个相比，\n',
            '反而觉得有文字的要简单一些呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181400V……算了，不管写了什么，\n',
            '都还是要去找啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181401V那么，\n',
            '就请你们继续努力寻找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181402V和刚才一样，\n',
            '我会在这里等着的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181403V#010F那么我们就出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181404V#006F好的，加油干吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002E, 0x04, 0x10)
    OP_28(0x002E, 0x01, 0x0020)
    OP_28(0x002F, 0x04, 0x02)
    OP_28(0x002F, 0x04, 0x04)
    OP_28(0x002F, 0x04, 0x08)
    OP_28(0x002F, 0x01, 0x0001)
    OP_28(0x002F, 0x01, 0x0002)
    OP_28(0x002F, 0x01, 0x0004)
    Call(1, 0x000D)

    @scena.Lambda('lambda_3723')
    def lambda_3723():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3723)

    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x372E
@scena.Code('func_08_372E')
def func_08_372E():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37B3',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_37B3(): pass

    label('loc_37B3')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37D2',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_37D2(): pass

    label('loc_37D2')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_37F1',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_37F1(): pass

    label('loc_37F1')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3810',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_3810(): pass

    label('loc_3810')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_382A',
    )

    @scena.Lambda('lambda_3822')
    def lambda_3822():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3822)

    def _loc_382A(): pass

    label('loc_382A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3844',
    )

    @scena.Lambda('lambda_383C')
    def lambda_383C():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_383C)

    def _loc_3844(): pass

    label('loc_3844')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_385E',
    )

    @scena.Lambda('lambda_3856')
    def lambda_3856():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3856)

    def _loc_385E(): pass

    label('loc_385E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3878',
    )

    @scena.Lambda('lambda_3870')
    def lambda_3870():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3870)

    def _loc_3878(): pass

    label('loc_3878')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3892',
    )

    @scena.Lambda('lambda_388A')
    def lambda_388A():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_388A)

    def _loc_3892(): pass

    label('loc_3892')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181405V啊……\n',
            '你们把书拿来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181406V#006F嗯，对啊，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181363V#010F请您确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '艾尔贝啄木鸟的生态',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0343, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181364V……哎呀，真让我惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181365V的确是这本书呢。\n',
            '终于找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181285V#010F对不起，\n',
            '这么晚才来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181286V没关系，\n',
            '你们还有别的重要工作嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181287V在你们最忙的时候\n',
            '还是能完成了任务，\n',
            '我已经很感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181305V#000F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181414V那再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181307V各位请慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181309V#508F再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002E, 0x04, 0x10)
    OP_28(0x002E, 0x01, 0x0020)
    OP_28(0x002D, 0x01, 0x4000)
    Call(1, 0x000D)

    @scena.Lambda('lambda_3B46')
    def lambda_3B46():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3B46)

    EventEnd(0x00)

    Return()

# id: 0x0009 offset: 0x3B51
@scena.Code('func_09_3B51')
def func_09_3B51():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BD6',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_3BD6(): pass

    label('loc_3BD6')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3BF5',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_3BF5(): pass

    label('loc_3BF5')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C14',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_3C14(): pass

    label('loc_3C14')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C33',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_3C33(): pass

    label('loc_3C33')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3C4D',
    )

    @scena.Lambda('lambda_3C45')
    def lambda_3C45():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_3C45)

    def _loc_3C4D(): pass

    label('loc_3C4D')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3C67',
    )

    @scena.Lambda('lambda_3C5F')
    def lambda_3C5F():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_3C5F)

    def _loc_3C67(): pass

    label('loc_3C67')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3C81',
    )

    @scena.Lambda('lambda_3C79')
    def lambda_3C79():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_3C79)

    def _loc_3C81(): pass

    label('loc_3C81')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3C9B',
    )

    @scena.Lambda('lambda_3C93')
    def lambda_3C93():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_3C93)

    def _loc_3C9B(): pass

    label('loc_3C9B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_3CB5',
    )

    @scena.Lambda('lambda_3CAD')
    def lambda_3CAD():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_3CAD)

    def _loc_3CB5(): pass

    label('loc_3CB5')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181418V哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181419V……难道，\n',
            '你们已经找到书了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181420V#502F呵呵呵，的确找到了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181421V#010F请您确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '哈茨少年冒险记·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【续·临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0344, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181422V……嗯，确实是这本呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181423V那么，\n',
            '这样就只剩最后一本了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181424V#007F呼，好歹也让我喘口气吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181425V#006F那么，\n',
            '接下来要找的是什么书呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181426V哦呵呵，不要着急，\n',
            '我这就告诉你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181427V最后要找的是名为\n',
            '《３１棵丝柏树》的书。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181428V……这是它对应的借书卡，\n',
            '在这上面又写着\n',
            '一些含义不明的文字。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            '#2130181429V',
            (TxtCtl.SetColor, 0x0),
            '　去问风景今何在\n',
            '　呀，山上耸立３\n',
            '　１棵丝柏。钟楼\n',
            '　宁远音，隔世的\n',
            '　饱经之苦如斜木\n',
            '　之坡上滚落酒桶\n',
            '　长阵，接近梦中\n',
            '　沉眠不绝的我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x0101,
        (
            '#0010181430V#509F这次的更古怪啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181431V#007F算了，\n',
            '不管怎么说都只有知难而进了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181432V#010F又是谜语吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_40C3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_40A5',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181433V#062F嗯，好像是～呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_40C3')

    def _loc_40A5(): pass

    label('loc_40A5')

    ChrTalk(
        0x0107,
        (
            '#0070181434V#062F好像是～呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_40C3(): pass

    label('loc_40C3')

    ChrTalk(
        0x00FE,
        (
            '#2120181435V已经对这个\n',
            '驾轻就熟了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181436V呵呵……\n',
            '这样就可以一气呵成了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181437V为了彻底达到目标，\n',
            '好好地加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181438V#508F那我们就出发了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181439V#010F告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002F, 0x04, 0x10)
    OP_28(0x002F, 0x01, 0x0010)
    OP_28(0x0030, 0x04, 0x02)
    OP_28(0x0030, 0x04, 0x04)
    OP_28(0x0030, 0x04, 0x08)
    OP_28(0x0030, 0x01, 0x0001)
    OP_28(0x0030, 0x01, 0x0002)
    Call(1, 0x000D)

    @scena.Lambda('lambda_41B1')
    def lambda_41B1():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_41B1)

    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x41BC
@scena.Code('func_0A_41BC')
def func_0A_41BC():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4241',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_4241(): pass

    label('loc_4241')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4260',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_4260(): pass

    label('loc_4260')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_427F',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_427F(): pass

    label('loc_427F')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_429E',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_429E(): pass

    label('loc_429E')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_42B8',
    )

    @scena.Lambda('lambda_42B0')
    def lambda_42B0():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_42B0)

    def _loc_42B8(): pass

    label('loc_42B8')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_42D2',
    )

    @scena.Lambda('lambda_42CA')
    def lambda_42CA():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_42CA)

    def _loc_42D2(): pass

    label('loc_42D2')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_42EC',
    )

    @scena.Lambda('lambda_42E4')
    def lambda_42E4():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_42E4)

    def _loc_42EC(): pass

    label('loc_42EC')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4306',
    )

    @scena.Lambda('lambda_42FE')
    def lambda_42FE():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_42FE)

    def _loc_4306(): pass

    label('loc_4306')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4320',
    )

    @scena.Lambda('lambda_4318')
    def lambda_4318():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_4318)

    def _loc_4320(): pass

    label('loc_4320')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181418V哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181441V你们把书拿来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181442V#508F嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181363V#010F请您确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '哈茨少年冒险记·下',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【续·临时图书馆员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0344, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181364V……哎呀，真让我惊讶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181365V的确是这本书呢。\n',
            '终于找回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181446V这样嘛，\n',
            '委托就此中止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181447V#004F咦……为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181448V不是说还有书没有收回来吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181297V我从协会那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181298V你们马上就要\n',
            '调到别的支部去了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181299V所以调离之前，\n',
            '必须将委托的事宜整理好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181300V#013F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020181301V对不起。\n',
            '工作半途而废了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181286V你们还有别的重要工作嘛。\n',
            '这也是没办法的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181455V你们能做到这个份上\n',
            '已经足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181456V剩下的工作\n',
            '由蔡斯支部的其他人\n',
            '去完成就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181457V#006F嗯……谢谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181289V彼此彼此，非常感谢你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181290V那你们以后也要继续努力哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181291V#010F感谢最近一段时间\n',
            '您对我们的诸多照顾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010151344V#000F再见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x002F, 0x04, 0x10)
    OP_28(0x002F, 0x01, 0x0010)
    OP_28(0x002F, 0x01, 0x0020)
    OP_28(0x002D, 0x01, 0x4000)
    Call(1, 0x000D)

    @scena.Lambda('lambda_473E')
    def lambda_473E():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_473E)

    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x4749
@scena.Code('func_0B_4749')
def func_0B_4749():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-101090, 0, 5020, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -102420, 0, 3650, 45)
    SetChrPos(0x0102, -101580, 0, 3120, 41)

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47CE',
    )

    SetChrPos(0x0107, -102560, 0, 2630, 45)

    def _loc_47CE(): pass

    label('loc_47CE')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_47ED',
    )

    SetChrPos(0x0106, -103730, 0, 3450, 45)

    def _loc_47ED(): pass

    label('loc_47ED')

    If(
        (
            (Expr.Eval, "OP_42(0x003B)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_480C',
    )

    SetChrPos(0x013C, -103730, 0, 3450, 45)

    def _loc_480C(): pass

    label('loc_480C')

    If(
        (
            (Expr.Eval, "OP_42(0x000F)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_482B',
    )

    SetChrPos(0x0110, -103380, 0, 2360, 45)

    def _loc_482B(): pass

    label('loc_482B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4845',
    )

    @scena.Lambda('lambda_483D')
    def lambda_483D():
        ChrTurnDirection(0x0000, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_483D)

    def _loc_4845(): pass

    label('loc_4845')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_485F',
    )

    @scena.Lambda('lambda_4857')
    def lambda_4857():
        ChrTurnDirection(0x0001, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4857)

    def _loc_485F(): pass

    label('loc_485F')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4879',
    )

    @scena.Lambda('lambda_4871')
    def lambda_4871():
        ChrTurnDirection(0x0002, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_4871)

    def _loc_4879(): pass

    label('loc_4879')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_4893',
    )

    @scena.Lambda('lambda_488B')
    def lambda_488B():
        ChrTurnDirection(0x0003, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_488B)

    def _loc_4893(): pass

    label('loc_4893')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_48AD',
    )

    @scena.Lambda('lambda_48A5')
    def lambda_48A5():
        ChrTurnDirection(0x0004, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0004, 0x0001, lambda_48A5)

    def _loc_48AD(): pass

    label('loc_48AD')

    ChrTurnDirection(0x0010, 0x0101, 400)
    OP_0D()

    ChrTalk(
        0x00FE,
        (
            '#2120181418V哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181486V……难道？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181487V#006F嗯，\n',
            '最后一本书也已经找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181488V#010F为了慎重起见，\n',
            '还请您确认一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '归还了',
            (TxtCtl.SetColor, 0x2),
            '３１棵丝柏树',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    PlaySE(23, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【再续·临时图书管理员的加班】',
            (TxtCtl.SetColor, 0x0),
            '完成！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(0x0345, 1)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181489V……嗯，就是它没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181490V好厉害呀，\n',
            '真的把３本都找到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181491V#001F嘿嘿，\n',
            '因为我们很努力地找啊找啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181492V#000F啊，对了……\n',
            '我们还找到了其他的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181493V#010F是和书放在一起的……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '约修亚说明了找到犯人留下的字条\n',
            '和结晶回路的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)

    ChrTalk(
        0x00FE,
        (
            '#2120181494V呼～\n',
            '竟然是出于这样的动机。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181495V唉，不管是什么样的理由，\n',
            '也不能给别人制造这么大的麻烦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181496V那个结晶回路\n',
            '你们就拿去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181497V因为让你们费了不少功夫，\n',
            '就算是回报吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150603V#001F嗯，非常感谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181499V#010F那么，到现在为止，\n',
            '任务已经做完了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181500V嗯，是呀。\n',
            '任务已经全部完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181501V#007F呼，太好了～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010181502V我到现在都还觉得\n',
            '会有新任务冒出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4CEC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070181503V#061F嘿嘿，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4CEC(): pass

    label('loc_4CEC')

    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181504V由于你们的努力，\n',
            '麻烦事已经全部解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181505V呵呵，\n',
            '真的很感谢你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181506V托你们的福，\n',
            '最近一段时间我也没事了，太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150156V#501F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '#2120181508V……没、没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#2120181509V那么，辛苦你们了。\n',
            '如果再有事情还要麻烦你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010181510V#001F嗯，交给我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020181511V#010F承蒙您多方的关照，\n',
            '告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0001, 6, 0xE))
    OP_28(0x0030, 0x04, 0x10)
    OP_28(0x0030, 0x01, 0x0008)
    Call(1, 0x000D)

    @scena.Lambda('lambda_4E66')
    def lambda_4E66():
        SetChrDirection(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4E66)

    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x4E71
@scena.Code('func_0C_4E71')
def func_0C_4E71():
    Sleep(100)

    PlaySE(17, 0x00, 0x64)
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '结晶光学论集',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(0x0342, 1)
    SetChrFlags(0x0018, 0x0080)
    OP_64(0x07, 0x0001)
    OP_28(0x002D, 0x01, 0x0004)
    TalkEnd(0x00FF)

    Return()

# id: 0x000D offset: 0x4EDA
@scena.Code('func_0D_4EDA')
def func_0D_4EDA():
    If(
        (
            (Expr.Eval, "OP_29(0x002E, 0x01, 0x0020)"),
            Expr.Return,
        ),
        'loc_4EE9',
    )

    OP_65(0x0D, 0x0001)

    def _loc_4EE9(): pass

    label('loc_4EE9')

    If(
        (
            (Expr.Eval, "OP_29(0x002F, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_4EF8',
    )

    OP_65(0x09, 0x0001)

    def _loc_4EF8(): pass

    label('loc_4EF8')

    If(
        (
            (Expr.Eval, "OP_29(0x0030, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_4F07',
    )

    OP_65(0x0E, 0x0001)

    def _loc_4F07(): pass

    label('loc_4F07')

    If(
        (
            (Expr.Eval, "OP_40(0x0342)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0004)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4F1C',
    )

    OP_65(0x0A, 0x0001)

    def _loc_4F1C(): pass

    label('loc_4F1C')

    If(
        (
            (Expr.Eval, "OP_40(0x0341)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0008)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4F31',
    )

    OP_65(0x0B, 0x0001)

    def _loc_4F31(): pass

    label('loc_4F31')

    If(
        (
            (Expr.Eval, "OP_40(0x0340)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x002D, 0x01, 0x0010)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4F46',
    )

    OP_65(0x0C, 0x0001)

    def _loc_4F46(): pass

    label('loc_4F46')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)

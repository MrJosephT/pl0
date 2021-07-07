table = {
'乘法运算符':{
    'times':'乘法运算符->times',
    'slash':'乘法运算符->slash'
},
'关系运算符':{
    'lss':'关系运算符->lss' ,
    'leq':'关系运算符->leq',
    'neq':'关系运算符->neq',
    'eql' :'关系运算符->eql',
    'gtr' :'关系运算符->gtr',
    'geq':'关系运算符->geq'
},
'写语句':{
    'writesym':'写语句->writesym lparan 表达式 写语句后缀 rparan'
},
'写语句后缀':{
    'comma':'写语句后缀->comma 表达式 写语句后缀',
    'rparan':'写语句后缀->ϵ'
},
'分程序':{
    'constsym':'分程序->常量说明 变量说明 过程说明 语句',
    'beginsym':'分程序->常量说明 变量说明 过程说明 语句',
    'callsym':'分程序->常量说明 变量说明 过程说明 语句',
    'ident' :'分程序->常量说明 变量说明 过程说明 语句',
    'ifsym':'分程序->常量说明 变量说明 过程说明 语句',
    'proceduresym' :'分程序->常量说明 变量说明 过程说明 语句',
    'readsym':'分程序->常量说明 变量说明 过程说明 语句',
    'writesym':'分程序->常量说明 变量说明 过程说明 语句',
    'varsym' :'分程序->常量说明 变量说明 过程说明 语句',
    'whilesym' :'分程序->常量说明 变量说明 过程说明 语句',
    'period' :'分程序->常量说明 变量说明 过程说明 语句',
    'semicolon':'分程序->常量说明 变量说明 过程说明 语句'
},
'加法运算符':{
    'plus':'加法运算符->plus',
    'minus':'加法运算符->minus'
},
'变量说明':{
    'varsym':'变量说明->varsym ident 变量说明后缀 semicolon',
    'period':'变量说明->ϵ',
    'semicolon':'变量说明->ϵ',
    'beginsym':'变量说明->ϵ',
    'callsym':'变量说明->ϵ',
    'ident':'变量说明->ϵ',
    'ifsym':'变量说明->ϵ',
    'proceduresym':'变量说明->ϵ',
    'readsym':'变量说明->ϵ',
    'writesym':'变量说明->ϵ',
    'whilesym':'变量说明->ϵ'
},
'变量说明后缀':{
    'comma':'变量说明后缀->comma ident 变量说明后缀',
    'semicolon':'变量说明后缀->ϵ'
},
'因子':{
    'lparan' :'因子->lparan 表达式 rparan',
    'ident':'因子->ident',
    'number':'因子->number'
},
'复合语句':{
    'beginsym':'复合语句->beginsym 语句 复合语句后缀 endsym'
},
'复合语句后缀':{
    'semicolon':'复合语句后缀->semicolon 语句 复合语句后缀',
    'endsym':'复合语句后缀->ϵ'
},
'常量定义':{
    'ident':'常量定义->ident eql number'
},
'常量说明':{
    'constsym' :'常量说明->constsym 常量定义 常量说明后缀 semicolon',
    'period' :'常量说明->ϵ',
    'semicolon' :'常量说明->ϵ',
    'beginsym':'常量说明->ϵ',
    'callsym' :'常量说明->ϵ',
    'ident':'常量说明->ϵ',
    'ifsym':'常量说明->ϵ',
    'proceduresym':'常量说明->ϵ',
    'readsym' :'常量说明->ϵ',
    'writesym' :'常量说明->ϵ',
    'varsym' :'常量说明->ϵ',
    'whilesym':'常量说明->ϵ'
},
'常量说明后缀':{
    'comma':'常量说明后缀->comma 常量定义 常量说明后缀',
    'semicolon':'常量说明后缀->ϵ'
},
'当循环语句':{
    'whilesym':'当循环语句->whilesym 条件 dosym 语句'
},
'条件':{
    'lparan':'条件->表达式 关系运算符 表达式',
    'plus':'条件->表达式 关系运算符 表达式',
    'minus' :'条件->表达式 关系运算符 表达式',
    'ident':'条件->表达式 关系运算符 表达式',
    'number':'条件->表达式 关系运算符 表达式',
    'oddsym':'条件->oddsym 表达式'
},
'条件语句':{
    'ifsym':'条件语句->ifsym 条件 thensym 语句'
},
'程序':{
    'period':'程序->分程序 period',
    'beginsym':'程序->分程序 period',
    'callsym' :'程序->分程序 period',
    'constsym':'程序->分程序 period',
    'ident':'程序->分程序 period',
    'ifsym':'程序->分程序 period',
    'proceduresym':'程序->分程序 period',
    'readsym' :'程序->分程序 period',
    'writesym' :'程序->分程序 period',
    'varsym':'程序->分程序 period',
    'whilesym':'程序->分程序 period'
},
'表达式':{
    'lparan':'表达式->项 表达式后缀',
    'plus':'表达式->加法运算符 项 表达式后缀 ',
    'minus':'表达式->加法运算符 项 表达式后缀 ',
    'ident':'表达式->项 表达式后缀',
    'number':'表达式->项 表达式后缀'
},
'表达式后缀':{
    'plus' :'表达式后缀->加法运算符 项 表达式后缀',
    'minus' :'表达式后缀->加法运算符 项 表达式后缀',
    'rparan' :'表达式后缀->ϵ',
    'period' :'表达式后缀->ϵ',
    'semicolon' :'表达式后缀->ϵ',
    'comma' :'表达式后缀->ϵ',
    'lss' :'表达式后缀->ϵ',
    'leq':'表达式后缀->ϵ',
    'neq':'表达式后缀->ϵ',
    'eql' :'表达式后缀->ϵ',
    'gtr':'表达式后缀->ϵ',
    'geq' :'表达式后缀->ϵ',
    'dosym':'表达式后缀->ϵ',
    'endsym':'表达式后缀->ϵ',
    'thensym':'表达式后缀->ϵ'
},
'语句':{
    'beginsym':'语句->复合语句',
    'callsym':'语句->过程调用语句',
    'ident':'语句->赋值语句',
    'ifsym' :'语句->条件语句',
    'readsym':'语句->读语句',
    'writesym':'语句->写语句',
    'whilesym':'语句->当循环语句',
    'period':'语句->ϵ',
    'semicolon':'语句->ϵ',
    'endsym':'语句->ϵ'
},
'读语句':{
    'readsym':'读语句->readsym lparan ident 读语句后缀 rparan'
},
'读语句后缀':{
    'comma':'读语句后缀->comma ident 读语句后缀',
    'rparan':'读语句后缀->ϵ'

},
'赋值语句':{
    'ident':'赋值语句->ident becomes 表达式'
},
'过程说明':{
    'proceduresym' :'过程说明->过程首部 分程序 semicolon 过程说明',
    'period':'过程说明->ϵ',
    'semicolon':'过程说明->ϵ',
    'beginsym':'过程说明->ϵ',
    'callsym':'过程说明->ϵ',
    'ident':'过程说明->ϵ',
    'ifsym' :'过程说明->ϵ',
    'readsym':'过程说明->ϵ',
    'writesym':'过程说明->ϵ',
    'whilesym':'过程说明->ϵ'
},
'过程调用语句':{
    'callsym':'过程调用语句->callsym ident'
},
'过程首部':{
    'proceduresym':'过程首部->proceduresym ident semicolon'
},
'项':{
    'lparan' :'项->因子 项后缀',
    'ident':'项->因子 项后缀',
    'number':'项->因子 项后缀'
},
'项后缀':{
    'times' :'项后缀->乘法运算符 因子 项后缀',
    'slash':'项后缀->乘法运算符 因子 项后缀',
    'rparan':'项后缀->ϵ',
    'plus':'项后缀->ϵ',
    'comma' :'项后缀->ϵ',
    'minus':'项后缀->ϵ',
    'period':'项后缀->ϵ',
    'semicolon':'项后缀->ϵ',
    'lss':'项后缀->ϵ',
    'leq':'项后缀->ϵ',
    'neq':'项后缀->ϵ',
    'eql':'项后缀->ϵ',
    'gtr':'项后缀->ϵ',
    'geq':'项后缀->ϵ',
    'dosym':'项后缀->ϵ',
    'endsym':'项后缀->ϵ',
    'thensym':'项后缀->ϵ'
}
}
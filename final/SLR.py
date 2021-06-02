END_MARK ='$'

SLR_TABLE = [
    {
        'vtype': 's5', 'class': 's6', '$': 'r4',
        'CODE': 1, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4
    },
    {
        '$': 'acc'
    },
    {
        'vtype': 's5', 'class': 's6', '$': 'r4',
        'CODE': 7, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4
    },
    {
        'vtype': 's5', 'class': 's6', '$': 'r4',
        'CODE': 8, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4
    },
    {
        'vtype': 's5', 'class': 's6', '$': 'r4',
        'CODE': 9, 'VDECL': 2, 'FDECL': 3, 'CDECL': 4
    },
    {
        'id': 's10',
        'ASSIGN': 11
    },
    {
        'id': 's12'
    },
    {
        '$': 'r1'
    },
    {
        '$': 'r2'
    },
    {
        '$': 'r3'
    },
    {
        'semi': 's13', 'assign': 's15', 'lparen': 's14'
    },
    {
        'semi': 's16'
    },
    {
        'lbrace': 's17'
    },
    {
        'vtype': 'r5', 'id': 'r5', 'rbrace': 'r5', 'if': 'r5', 'while': 'r5', 'return': 'r5', 'class': 'r5', '$': 'r5'
    },
    {
        'vtype': 's19', 'rparen': 'r21',
        'ARG': 18
    },
    {
        'id': 's28', 'literal': 's22', 'character': 's23', 'boolstr': 's24', 'lparen': 's27', 'num': 's29',
        'RHS': 20, 'EXPR': 21, 'TERM': 25, 'FACTOR': 26
    },
    {
        'vtype': 'r6', 'id': 'r6', 'rbrace': 'r6', 'if': 'r6', 'while': 'r6', 'return': 'r6', 'class': 'r6', '$': 'r6'
    },
    {
        'vtype': 's5', 'rbrace': 'r40',
        'VDECL': 31, 'FDECL': 32, 'ODECL': 30
    },
    {
        'rparen': 's33'
    },
    {
        'id': 's34'
    },
    {
        'semi': 'r7'
    },
    {
        'semi': 'r8'
    },
    {
        'semi': 'r9'
    },
    {
        'semi': 'r10'
    },
    {
        'semi': 'r11'
    },
    {
        'semi': 'r13', 'addsub': 's35', 'rparen': 'r13'
    },
    {
        'semi': 'r15', 'addsub': 'r15', 'multdiv': 's36', 'rparen': 'r15'
    },
    {
        'id': 's28', 'lparen': 's27', 'num': 's29',
        'EXPR': 37, 'TERM': 25, 'FACTOR': 26
    },
    {
        'semi': 'r17', 'addsub': 'r17', 'multdiv': 'r17', 'rparen': 'r17'
    },
    {
        'semi': 'r18', 'addsub': 'r18', 'multdiv': 'r18', 'rparen': 'r18'
    },
    {
        'rbrace': 's38'
    },
    {
        'vtype': 's5', 'rbrace': 'r40',
        'CODE': 31, 'FDECL': 32, 'ODECL': 39
    },
    {
        'vtype': 's5', 'rbrace': 'r40',
        'CODE': 31, 'FDECL': 32, 'ODECL': 40
    },
    {
        'lbrace': 's41',
    },
    {
        'rparen': 'r23', 'comma': 's43',
        'MOREARGS': 42
    },
    {
        'id': 's28', 'lparen': 's27', 'num': 's29',
        'EXPR': 44, 'TERM': 25, 'FACTOR': 26
    },
    {
        'id': 's28', 'lparen': 's27', 'num': 's29',
        'TERM': 45, 'FACTOR': 26
    },
    {
        'rparen': 's46'
    },
    {
      'vtype': 'r37', 'class': 'r37', '$': 'r37'
    },
    {
        'rbrace': 'r38'
    },
    {
        'rbrace': 'r39'
    },
    {
        'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25',
        'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 47, 'STMT': 48
    },
    {
        'rparen': 'r20'
    },
    {
        'vtype': 's55'
    },
    {
        'semi': 'r12', 'rparen': 'r12'
    },
    {
        'semi': 'r14', 'addsub': 'r14', 'rparen': 'r14'
    },
    {
        'semi': 'r16', 'addsub': 'r16', 'multdiv': 'r16', 'rparen': 'r16'
    },
    {
        'return': 's57',
        'RETURN': 56
    },
    {
        'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25',
        'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 58, 'STMT': 48
    },
    {
        'vtype': 'r26', 'id': 'r26', 'rbrace': 'r26', 'if': 'r26', 'while': 'r26', 'return': 'r26'
    },
    {
        'semi': 's59'
    },
    {
        'lparen': 's60'
    },
    {
        'lparen': 's61'
    },
    {
        'id': 's62',
        'ASSIGN': 11
    },
    {
        'assign': 's15'
    },
    {
        'id': 's63'
    },
    {
        'rbrace': 's64'
    },
    {
        'id': 's28', 'literal': 's22', 'character': 's23', 'boolstr': 's24', 'lparen': 's27', 'num': 's29',
        'RHS': 65, 'EXPR': 21, 'TERM': 25, 'FACTOR': 26
    },
    {
        'rbrace': 'r24', 'return': 'r24'
    },
    {
        'vtype': 'r27', 'id': 'r27', 'rbrace': 'r27', 'if': 'r27', 'while': 'r27', 'return': 'r27'
    },
    {
        'boolstr': 's69', 'lparen': 's68',
        'COND': 66,	'T': 67
    },
    {
        'boolstr': 's69', 'lparen': 's68',
        'COND': 70,	'T': 67
    },
    {
        'semi': 's13', 'assign': 's15'
    },
    {
        'rparen': 'r23', 'comma': 's43',
        'MOREARGS': 71
    },
    {
        'vtype': 'r19', 'rbrace': 'r19', 'class': 'r19', '$': 'r19'
    },
    {
        'semi': 's72'
    },
    {
        'rparen': 's73'
    },
    {
        'rparen': 'r31', 'comp': 's74'
    },
    {
        'boolstr': 's69', 'lparen': 's68',
        'COND': 75, 'T': 67
    },
    {
        'rparen': 'r33', 'comp': 'r33'
    },
    {
        'rparen': 's76'
    },
    {
        'rparen': 'r22'
    },
    {
        'rbrace': 'r36'
    },
    {
        'lbrace': 's77'
    },
    {
        'boolstr': 's69', 'lparen': 's68',
        'T': 78
    },
    {
        'rparen': 's79'
    },
    {
        'lbrace': 's80'
    },
    {
        'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25',
        'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 81,	'STMT': 48
    },
    {
        'rparen': 'r30'
    },
    {
        'rparen': 'r32', 'comp': 'r32'
    },
    {
        'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25',
        'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 82,	'STMT': 48
    },
    {
        'rbrace': 's83'
    },
    {
        'rbrace': 's84'
    },
    {
        'vtype': 'r35', 'id': 'r35', 'rbrace': 'r35', 'if': 'r35', 'while': 'r35', 'else': 's86', 'return': 'r35',
        'ELSE': 85
    },
    {
        'vtype': 'r29', 'id': 'r29', 'rbrace': 'r29', 'if': 'r29', 'while': 'r29', 'return': 'r29'
    },
    {
        'vtype': 'r28', 'id': 'r28', 'rbrace': 'r28', 'if': 'r28', 'while': 'r28', 'return': 'r28'
    },
    {
        'lbrace': 's87'
    },
    {
        'vtype': 's53', 'id': 's54', 'rbrace': 'r25', 'if': 's51', 'while': 's52', 'return': 'r25',
        'VDECL': 49, 'ASSIGN': 50, 'BLOCK': 88,	'STMT': 48
    },
    {
        'rbrace': 's89'
    },
    {
        'vtype': 'r34', 'id': 'r34', 'rbrace': 'r34', 'if': 'r34', 'while': 'r34', 'return': 'r34'
    }
]
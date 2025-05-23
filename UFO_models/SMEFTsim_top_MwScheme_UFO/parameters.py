# This file was automatically created by FeynRules 2.3.35
# Mathematica version: 12.1.0 for Linux x86 (64-bit) (March 18, 2020)
# Date: Mon 24 Aug 2020 00:42:28

import configuration

from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cG = Parameter(name = 'cG',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_G',
               lhablock = 'SMEFT',
               lhacode = [ 1 ])

cW = Parameter(name = 'cW',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_W',
               lhablock = 'SMEFT',
               lhacode = [ 2 ])

cH = Parameter(name = 'cH',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = 'c_H',
               lhablock = 'SMEFT',
               lhacode = [ 3 ])

cHbox = Parameter(name = 'cHbox',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{H \\square }',
                  lhablock = 'SMEFT',
                  lhacode = [ 4 ])

cHDD = Parameter(name = 'cHDD',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HD}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 5 ])

cHG = Parameter(name = 'cHG',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HG}}',
                lhablock = 'SMEFT',
                lhacode = [ 6 ])

cHW = Parameter(name = 'cHW',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HW}}',
                lhablock = 'SMEFT',
                lhacode = [ 7 ])

cHB = Parameter(name = 'cHB',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{HB}}',
                lhablock = 'SMEFT',
                lhacode = [ 8 ])

cHWB = Parameter(name = 'cHWB',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HWB}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 9 ])

cuHRe = Parameter(name = 'cuHRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuHRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 10 ])

ctHRe = Parameter(name = 'ctHRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctHRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 11 ])

cdHRe = Parameter(name = 'cdHRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdHRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 12 ])

cbHRe = Parameter(name = 'cbHRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbHRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 13 ])

cuGRe = Parameter(name = 'cuGRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuGRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 14 ])

ctGRe = Parameter(name = 'ctGRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctGRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 15 ])

cuWRe = Parameter(name = 'cuWRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuWRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 16 ])

ctWRe = Parameter(name = 'ctWRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctWRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 17 ])

cuBRe = Parameter(name = 'cuBRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuBRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 18 ])

ctBRe = Parameter(name = 'ctBRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctBRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 19 ])

cdGRe = Parameter(name = 'cdGRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdGRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 20 ])

cbGRe = Parameter(name = 'cbGRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbGRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 21 ])

cdWRe = Parameter(name = 'cdWRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdWRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 22 ])

cbWRe = Parameter(name = 'cbWRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbWRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 23 ])

cdBRe = Parameter(name = 'cdBRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdBRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 24 ])

cbBRe = Parameter(name = 'cbBRe',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbBRe}',
                  lhablock = 'SMEFT',
                  lhacode = [ 25 ])

cHj1 = Parameter(name = 'cHj1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Hj}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 26 ])

cHQ1 = Parameter(name = 'cHQ1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HQ}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 27 ])

cHj3 = Parameter(name = 'cHj3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Hj}}^3',
                 lhablock = 'SMEFT',
                 lhacode = [ 28 ])

cHQ3 = Parameter(name = 'cHQ3',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{HQ}}^3',
                 lhablock = 'SMEFT',
                 lhacode = [ 29 ])

cHu = Parameter(name = 'cHu',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{Hu}}',
                lhablock = 'SMEFT',
                lhacode = [ 30 ])

cHt = Parameter(name = 'cHt',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{Ht}}',
                lhablock = 'SMEFT',
                lhacode = [ 31 ])

cHd = Parameter(name = 'cHd',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{Hd}}',
                lhablock = 'SMEFT',
                lhacode = [ 32 ])

cHbq = Parameter(name = 'cHbq',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Hb}}',
                 lhablock = 'SMEFT',
                 lhacode = [ 33 ])

cHudRe = Parameter(name = 'cHudRe',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{cHudRe}',
                   lhablock = 'SMEFT',
                   lhacode = [ 34 ])

cHtbRe = Parameter(name = 'cHtbRe',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{cHtbRe}',
                   lhablock = 'SMEFT',
                   lhacode = [ 35 ])

cjj11 = Parameter(name = 'cjj11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{jj}}^{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 36 ])

cjj18 = Parameter(name = 'cjj18',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{jj}}^{18}',
                  lhablock = 'SMEFT',
                  lhacode = [ 37 ])

cjj31 = Parameter(name = 'cjj31',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{jj}}^{31}',
                  lhablock = 'SMEFT',
                  lhacode = [ 38 ])

cjj38 = Parameter(name = 'cjj38',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{jj}}^{38}',
                  lhablock = 'SMEFT',
                  lhacode = [ 39 ])

cQj11 = Parameter(name = 'cQj11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Qj}}^{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 40 ])

cQj18 = Parameter(name = 'cQj18',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Qj}}^{18}',
                  lhablock = 'SMEFT',
                  lhacode = [ 41 ])

cQj31 = Parameter(name = 'cQj31',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Qj}}^{31}',
                  lhablock = 'SMEFT',
                  lhacode = [ 42 ])

cQj38 = Parameter(name = 'cQj38',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Qj}}^{38}',
                  lhablock = 'SMEFT',
                  lhacode = [ 43 ])

cQQ1 = Parameter(name = 'cQQ1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{QQ}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 44 ])

cQQ8 = Parameter(name = 'cQQ8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{QQ}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 45 ])

cuu1 = Parameter(name = 'cuu1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{uu}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 46 ])

cuu8 = Parameter(name = 'cuu8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{uu}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 47 ])

ctt = Parameter(name = 'ctt',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{tt}}',
                lhablock = 'SMEFT',
                lhacode = [ 48 ])

ctu1 = Parameter(name = 'ctu1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{tu}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 49 ])

ctu8 = Parameter(name = 'ctu8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{tu}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 50 ])

cdd1 = Parameter(name = 'cdd1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{dd}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 51 ])

cdd8 = Parameter(name = 'cdd8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{dd}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 52 ])

cbb = Parameter(name = 'cbb',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = 'c_{\\text{bb}}',
                lhablock = 'SMEFT',
                lhacode = [ 53 ])

cbd1 = Parameter(name = 'cbd1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{bd}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 54 ])

cbd8 = Parameter(name = 'cbd8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{bd}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 55 ])

cud1 = Parameter(name = 'cud1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{ud}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 56 ])

ctb1 = Parameter(name = 'ctb1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{tb}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 57 ])

ctd1 = Parameter(name = 'ctd1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{td}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 58 ])

cbu1 = Parameter(name = 'cbu1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{bu}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 59 ])

cud8 = Parameter(name = 'cud8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{ud}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 60 ])

ctb8 = Parameter(name = 'ctb8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{tb}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 61 ])

ctd8 = Parameter(name = 'ctd8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{td}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 62 ])

cbu8 = Parameter(name = 'cbu8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{bu}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 63 ])

cutbd1Re = Parameter(name = 'cutbd1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cutbd1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 64 ])

cutbd8Re = Parameter(name = 'cutbd8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cutbd8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 65 ])

cju1 = Parameter(name = 'cju1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{ju}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 66 ])

cQu1 = Parameter(name = 'cQu1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qu}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 67 ])

cju8 = Parameter(name = 'cju8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{ju}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 68 ])

cQu8 = Parameter(name = 'cQu8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qu}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 69 ])

ctj1 = Parameter(name = 'ctj1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{tj}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 70 ])

ctj8 = Parameter(name = 'ctj8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{tj}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 71 ])

cQt1 = Parameter(name = 'cQt1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qt}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 72 ])

cQt8 = Parameter(name = 'cQt8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qt}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 73 ])

cjd1 = Parameter(name = 'cjd1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{jd}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 74 ])

cjd8 = Parameter(name = 'cjd8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{jd}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 75 ])

cQd1 = Parameter(name = 'cQd1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qd}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 76 ])

cQd8 = Parameter(name = 'cQd8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qd}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 77 ])

cbj1 = Parameter(name = 'cbj1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{bj}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 78 ])

cbj8 = Parameter(name = 'cbj8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{bj}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 79 ])

cQb1 = Parameter(name = 'cQb1',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qb}}^1',
                 lhablock = 'SMEFT',
                 lhacode = [ 80 ])

cQb8 = Parameter(name = 'cQb8',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = 'c_{\\text{Qb}}^8',
                 lhablock = 'SMEFT',
                 lhacode = [ 81 ])

cjQtu1Re = Parameter(name = 'cjQtu1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQtu1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 82 ])

cjQtu8Re = Parameter(name = 'cjQtu8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQtu8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 83 ])

cjQbd1Re = Parameter(name = 'cjQbd1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQbd1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 84 ])

cjQbd8Re = Parameter(name = 'cjQbd8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQbd8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 85 ])

cjujd1Re = Parameter(name = 'cjujd1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjujd1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 86 ])

cjujd8Re = Parameter(name = 'cjujd8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjujd8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 87 ])

cjujd11Re = Parameter(name = 'cjujd11Re',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cjujd11Re}',
                      lhablock = 'SMEFT',
                      lhacode = [ 88 ])

cjujd81Re = Parameter(name = 'cjujd81Re',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cjujd81Re}',
                      lhablock = 'SMEFT',
                      lhacode = [ 89 ])

cQtjd1Re = Parameter(name = 'cQtjd1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtjd1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 90 ])

cQtjd8Re = Parameter(name = 'cQtjd8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtjd8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 91 ])

cjuQb1Re = Parameter(name = 'cjuQb1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjuQb1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 92 ])

cjuQb8Re = Parameter(name = 'cjuQb8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjuQb8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 93 ])

cQujb1Re = Parameter(name = 'cQujb1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQujb1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 94 ])

cQujb8Re = Parameter(name = 'cQujb8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQujb8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 95 ])

cjtQd1Re = Parameter(name = 'cjtQd1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjtQd1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 96 ])

cjtQd8Re = Parameter(name = 'cjtQd8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjtQd8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 97 ])

cQtQb1Re = Parameter(name = 'cQtQb1Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtQb1Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 98 ])

cQtQb8Re = Parameter(name = 'cQtQb8Re',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtQb8Re}',
                     lhablock = 'SMEFT',
                     lhacode = [ 99 ])

ceHRe11 = Parameter(name = 'ceHRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 100 ])

ceHRe22 = Parameter(name = 'ceHRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 101 ])

ceHRe33 = Parameter(name = 'ceHRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 102 ])

ceWRe11 = Parameter(name = 'ceWRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 103 ])

ceWRe22 = Parameter(name = 'ceWRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 104 ])

ceWRe33 = Parameter(name = 'ceWRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 105 ])

ceBRe11 = Parameter(name = 'ceBRe11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe11}',
                    lhablock = 'SMEFT',
                    lhacode = [ 106 ])

ceBRe22 = Parameter(name = 'ceBRe22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe22}',
                    lhablock = 'SMEFT',
                    lhacode = [ 107 ])

ceBRe33 = Parameter(name = 'ceBRe33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBRe33}',
                    lhablock = 'SMEFT',
                    lhacode = [ 108 ])

cHl111 = Parameter(name = 'cHl111',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Hl}}^1{}_{11}',
                   lhablock = 'SMEFT',
                   lhacode = [ 109 ])

cHl122 = Parameter(name = 'cHl122',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Hl}}^1{}_{22}',
                   lhablock = 'SMEFT',
                   lhacode = [ 110 ])

cHl133 = Parameter(name = 'cHl133',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Hl}}^1{}_{33}',
                   lhablock = 'SMEFT',
                   lhacode = [ 111 ])

cHl311 = Parameter(name = 'cHl311',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Hl}}^3{}_{11}',
                   lhablock = 'SMEFT',
                   lhacode = [ 112 ])

cHl322 = Parameter(name = 'cHl322',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Hl}}^3{}_{22}',
                   lhablock = 'SMEFT',
                   lhacode = [ 113 ])

cHl333 = Parameter(name = 'cHl333',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Hl}}^3{}_{33}',
                   lhablock = 'SMEFT',
                   lhacode = [ 114 ])

cHe11 = Parameter(name = 'cHe11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{He}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 115 ])

cHe22 = Parameter(name = 'cHe22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{He}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 116 ])

cHe33 = Parameter(name = 'cHe33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{He}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 117 ])

cll1111 = Parameter(name = 'cll1111',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{1111}',
                    lhablock = 'SMEFT',
                    lhacode = [ 118 ])

cll2222 = Parameter(name = 'cll2222',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{2222}',
                    lhablock = 'SMEFT',
                    lhacode = [ 119 ])

cll3333 = Parameter(name = 'cll3333',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{3333}',
                    lhablock = 'SMEFT',
                    lhacode = [ 120 ])

cll1122 = Parameter(name = 'cll1122',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{1122}',
                    lhablock = 'SMEFT',
                    lhacode = [ 121 ])

cll1133 = Parameter(name = 'cll1133',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{1133}',
                    lhablock = 'SMEFT',
                    lhacode = [ 122 ])

cll2233 = Parameter(name = 'cll2233',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{2233}',
                    lhablock = 'SMEFT',
                    lhacode = [ 123 ])

cll1221 = Parameter(name = 'cll1221',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{1221}',
                    lhablock = 'SMEFT',
                    lhacode = [ 124 ])

cll1331 = Parameter(name = 'cll1331',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{1331}',
                    lhablock = 'SMEFT',
                    lhacode = [ 125 ])

cll2332 = Parameter(name = 'cll2332',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ll}}_{2332}',
                    lhablock = 'SMEFT',
                    lhacode = [ 126 ])

clj111 = Parameter(name = 'clj111',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{lj}}^1{}_{11}',
                   lhablock = 'SMEFT',
                   lhacode = [ 127 ])

clj122 = Parameter(name = 'clj122',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{lj}}^1{}_{22}',
                   lhablock = 'SMEFT',
                   lhacode = [ 128 ])

clj133 = Parameter(name = 'clj133',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{lj}}^1{}_{33}',
                   lhablock = 'SMEFT',
                   lhacode = [ 129 ])

clj311 = Parameter(name = 'clj311',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{lj}}^3{}_{11}',
                   lhablock = 'SMEFT',
                   lhacode = [ 130 ])

clj322 = Parameter(name = 'clj322',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{lj}}^3{}_{22}',
                   lhablock = 'SMEFT',
                   lhacode = [ 131 ])

clj333 = Parameter(name = 'clj333',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{lj}}^3{}_{33}',
                   lhablock = 'SMEFT',
                   lhacode = [ 132 ])

cQl111 = Parameter(name = 'cQl111',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Ql}}^1{}_{11}',
                   lhablock = 'SMEFT',
                   lhacode = [ 133 ])

cQl122 = Parameter(name = 'cQl122',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Ql}}^1{}_{22}',
                   lhablock = 'SMEFT',
                   lhacode = [ 134 ])

cQl133 = Parameter(name = 'cQl133',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Ql}}^1{}_{33}',
                   lhablock = 'SMEFT',
                   lhacode = [ 135 ])

cQl311 = Parameter(name = 'cQl311',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Ql}}^3{}_{11}',
                   lhablock = 'SMEFT',
                   lhacode = [ 136 ])

cQl322 = Parameter(name = 'cQl322',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Ql}}^3{}_{22}',
                   lhablock = 'SMEFT',
                   lhacode = [ 137 ])

cQl333 = Parameter(name = 'cQl333',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{\\text{Ql}}^3{}_{33}',
                   lhablock = 'SMEFT',
                   lhacode = [ 138 ])

cee1111 = Parameter(name = 'cee1111',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ee}}_{1111}',
                    lhablock = 'SMEFT',
                    lhacode = [ 139 ])

cee2222 = Parameter(name = 'cee2222',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ee}}_{2222}',
                    lhablock = 'SMEFT',
                    lhacode = [ 140 ])

cee3333 = Parameter(name = 'cee3333',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ee}}_{3333}',
                    lhablock = 'SMEFT',
                    lhacode = [ 141 ])

cee1122 = Parameter(name = 'cee1122',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ee}}_{1122}',
                    lhablock = 'SMEFT',
                    lhacode = [ 142 ])

cee1133 = Parameter(name = 'cee1133',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ee}}_{1133}',
                    lhablock = 'SMEFT',
                    lhacode = [ 143 ])

cee2233 = Parameter(name = 'cee2233',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{ee}}_{2233}',
                    lhablock = 'SMEFT',
                    lhacode = [ 144 ])

ceu11 = Parameter(name = 'ceu11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{eu}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 145 ])

ceu22 = Parameter(name = 'ceu22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{eu}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 146 ])

ceu33 = Parameter(name = 'ceu33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{eu}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 147 ])

cte11 = Parameter(name = 'cte11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{te}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 148 ])

cte22 = Parameter(name = 'cte22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{te}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 149 ])

cte33 = Parameter(name = 'cte33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{te}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 150 ])

ced11 = Parameter(name = 'ced11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ed}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 151 ])

ced22 = Parameter(name = 'ced22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ed}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 152 ])

ced33 = Parameter(name = 'ced33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ed}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 153 ])

cbe11 = Parameter(name = 'cbe11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{be}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 154 ])

cbe22 = Parameter(name = 'cbe22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{be}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 155 ])

cbe33 = Parameter(name = 'cbe33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{be}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 156 ])

cje11 = Parameter(name = 'cje11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{je}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 157 ])

cje22 = Parameter(name = 'cje22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{je}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 158 ])

cje33 = Parameter(name = 'cje33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{je}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 159 ])

cQe11 = Parameter(name = 'cQe11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Qe}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 160 ])

cQe22 = Parameter(name = 'cQe22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Qe}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 161 ])

cQe33 = Parameter(name = 'cQe33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{Qe}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 162 ])

clu11 = Parameter(name = 'clu11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{lu}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 163 ])

clu22 = Parameter(name = 'clu22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{lu}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 164 ])

clu33 = Parameter(name = 'clu33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{lu}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 165 ])

ctl11 = Parameter(name = 'ctl11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{tl}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 166 ])

ctl22 = Parameter(name = 'ctl22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{tl}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 167 ])

ctl33 = Parameter(name = 'ctl33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{tl}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 168 ])

cld11 = Parameter(name = 'cld11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ld}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 169 ])

cld22 = Parameter(name = 'cld22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ld}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 170 ])

cld33 = Parameter(name = 'cld33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{ld}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 171 ])

cbl11 = Parameter(name = 'cbl11',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{bl}}_{11}',
                  lhablock = 'SMEFT',
                  lhacode = [ 172 ])

cbl22 = Parameter(name = 'cbl22',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{bl}}_{22}',
                  lhablock = 'SMEFT',
                  lhacode = [ 173 ])

cbl33 = Parameter(name = 'cbl33',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\text{bl}}_{33}',
                  lhablock = 'SMEFT',
                  lhacode = [ 174 ])

cle1111 = Parameter(name = 'cle1111',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{1111}',
                    lhablock = 'SMEFT',
                    lhacode = [ 175 ])

cle2222 = Parameter(name = 'cle2222',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{2222}',
                    lhablock = 'SMEFT',
                    lhacode = [ 176 ])

cle3333 = Parameter(name = 'cle3333',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{3333}',
                    lhablock = 'SMEFT',
                    lhacode = [ 177 ])

cle1122 = Parameter(name = 'cle1122',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{1122}',
                    lhablock = 'SMEFT',
                    lhacode = [ 178 ])

cle1133 = Parameter(name = 'cle1133',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{1133}',
                    lhablock = 'SMEFT',
                    lhacode = [ 179 ])

cle2233 = Parameter(name = 'cle2233',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{2233}',
                    lhablock = 'SMEFT',
                    lhacode = [ 180 ])

cle2211 = Parameter(name = 'cle2211',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{2211}',
                    lhablock = 'SMEFT',
                    lhacode = [ 181 ])

cle3311 = Parameter(name = 'cle3311',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{3311}',
                    lhablock = 'SMEFT',
                    lhacode = [ 182 ])

cle3322 = Parameter(name = 'cle3322',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{3322}',
                    lhablock = 'SMEFT',
                    lhacode = [ 183 ])

cle1221 = Parameter(name = 'cle1221',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{1221}',
                    lhablock = 'SMEFT',
                    lhacode = [ 184 ])

cle1331 = Parameter(name = 'cle1331',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{1331}',
                    lhablock = 'SMEFT',
                    lhacode = [ 185 ])

cle2332 = Parameter(name = 'cle2332',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{\\text{le}}_{2332}',
                    lhablock = 'SMEFT',
                    lhacode = [ 186 ])

cledjRe11 = Parameter(name = 'cledjRe11',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cledjRe11}',
                      lhablock = 'SMEFT',
                      lhacode = [ 187 ])

cledjRe22 = Parameter(name = 'cledjRe22',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cledjRe22}',
                      lhablock = 'SMEFT',
                      lhacode = [ 188 ])

cledjRe33 = Parameter(name = 'cledjRe33',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cledjRe33}',
                      lhablock = 'SMEFT',
                      lhacode = [ 189 ])

clebQRe11 = Parameter(name = 'clebQRe11',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{clebQRe11}',
                      lhablock = 'SMEFT',
                      lhacode = [ 190 ])

clebQRe22 = Parameter(name = 'clebQRe22',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{clebQRe22}',
                      lhablock = 'SMEFT',
                      lhacode = [ 191 ])

clebQRe33 = Parameter(name = 'clebQRe33',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{clebQRe33}',
                      lhablock = 'SMEFT',
                      lhacode = [ 192 ])

cleju1Re11 = Parameter(name = 'cleju1Re11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju1Re11}',
                       lhablock = 'SMEFT',
                       lhacode = [ 193 ])

cleju1Re22 = Parameter(name = 'cleju1Re22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju1Re22}',
                       lhablock = 'SMEFT',
                       lhacode = [ 194 ])

cleju1Re33 = Parameter(name = 'cleju1Re33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju1Re33}',
                       lhablock = 'SMEFT',
                       lhacode = [ 195 ])

cleQt1Re11 = Parameter(name = 'cleQt1Re11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt1Re11}',
                       lhablock = 'SMEFT',
                       lhacode = [ 196 ])

cleQt1Re22 = Parameter(name = 'cleQt1Re22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt1Re22}',
                       lhablock = 'SMEFT',
                       lhacode = [ 197 ])

cleQt1Re33 = Parameter(name = 'cleQt1Re33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt1Re33}',
                       lhablock = 'SMEFT',
                       lhacode = [ 198 ])

cleju3Re11 = Parameter(name = 'cleju3Re11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju3Re11}',
                       lhablock = 'SMEFT',
                       lhacode = [ 199 ])

cleju3Re22 = Parameter(name = 'cleju3Re22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju3Re22}',
                       lhablock = 'SMEFT',
                       lhacode = [ 200 ])

cleju3Re33 = Parameter(name = 'cleju3Re33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju3Re33}',
                       lhablock = 'SMEFT',
                       lhacode = [ 201 ])

cleQt3Re11 = Parameter(name = 'cleQt3Re11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt3Re11}',
                       lhablock = 'SMEFT',
                       lhacode = [ 202 ])

cleQt3Re22 = Parameter(name = 'cleQt3Re22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt3Re22}',
                       lhablock = 'SMEFT',
                       lhacode = [ 203 ])

cleQt3Re33 = Parameter(name = 'cleQt3Re33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt3Re33}',
                       lhablock = 'SMEFT',
                       lhacode = [ 204 ])

cGtil = Parameter(name = 'cGtil',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\tilde{G}}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 1 ])

cWtil = Parameter(name = 'cWtil',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = 'c_{\\tilde{W}}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 2 ])

cHGtil = Parameter(name = 'cHGtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{G}}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 3 ])

cHWtil = Parameter(name = 'cHWtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{W}}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 4 ])

cHBtil = Parameter(name = 'cHBtil',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = 'c_{H \\tilde{B}}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 5 ])

cHWBtil = Parameter(name = 'cHWBtil',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = 'c_{B H \\tilde{W}}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 6 ])

cuGIm = Parameter(name = 'cuGIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuGIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 7 ])

ctGIm = Parameter(name = 'ctGIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctGIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 8 ])

cuWIm = Parameter(name = 'cuWIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuWIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 9 ])

ctWIm = Parameter(name = 'ctWIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctWIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 10 ])

cuBIm = Parameter(name = 'cuBIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuBIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 11 ])

ctBIm = Parameter(name = 'ctBIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctBIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 12 ])

cdGIm = Parameter(name = 'cdGIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdGIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 13 ])

cbGIm = Parameter(name = 'cbGIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbGIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 14 ])

cdWIm = Parameter(name = 'cdWIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdWIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 15 ])

cbWIm = Parameter(name = 'cbWIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbWIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 16 ])

cdBIm = Parameter(name = 'cdBIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdBIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 17 ])

cbBIm = Parameter(name = 'cbBIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbBIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 18 ])

cuHIm = Parameter(name = 'cuHIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cuHIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 19 ])

ctHIm = Parameter(name = 'ctHIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{ctHIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 20 ])

cdHIm = Parameter(name = 'cdHIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cdHIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 21 ])

cbHIm = Parameter(name = 'cbHIm',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{cbHIm}',
                  lhablock = 'SMEFTcpv',
                  lhacode = [ 22 ])

cHudIm = Parameter(name = 'cHudIm',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{cHudIm}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 23 ])

cHtbIm = Parameter(name = 'cHtbIm',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{cHtbIm}',
                   lhablock = 'SMEFTcpv',
                   lhacode = [ 24 ])

cutbd1Im = Parameter(name = 'cutbd1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cutbd1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 25 ])

cutbd8Im = Parameter(name = 'cutbd8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cutbd8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 26 ])

cjQtu1Im = Parameter(name = 'cjQtu1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQtu1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 27 ])

cjQtu8Im = Parameter(name = 'cjQtu8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQtu8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 28 ])

cjQbd1Im = Parameter(name = 'cjQbd1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQbd1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 29 ])

cjQbd8Im = Parameter(name = 'cjQbd8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjQbd8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 30 ])

cjujd1Im = Parameter(name = 'cjujd1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjujd1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 31 ])

cjujd8Im = Parameter(name = 'cjujd8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjujd8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 32 ])

cjujd11Im = Parameter(name = 'cjujd11Im',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cjujd11Im}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 33 ])

cjujd81Im = Parameter(name = 'cjujd81Im',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cjujd81Im}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 34 ])

cQtjd1Im = Parameter(name = 'cQtjd1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtjd1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 35 ])

cQtjd8Im = Parameter(name = 'cQtjd8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtjd8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 36 ])

cjuQb1Im = Parameter(name = 'cjuQb1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjuQb1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 37 ])

cjuQb8Im = Parameter(name = 'cjuQb8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjuQb8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 38 ])

cQujb1Im = Parameter(name = 'cQujb1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQujb1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 39 ])

cQujb8Im = Parameter(name = 'cQujb8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQujb8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 40 ])

cjtQd1Im = Parameter(name = 'cjtQd1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjtQd1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 41 ])

cjtQd8Im = Parameter(name = 'cjtQd8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cjtQd8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 42 ])

cQtQb1Im = Parameter(name = 'cQtQb1Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtQb1Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 43 ])

cQtQb8Im = Parameter(name = 'cQtQb8Im',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{cQtQb8Im}',
                     lhablock = 'SMEFTcpv',
                     lhacode = [ 44 ])

ceHIm11 = Parameter(name = 'ceHIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 45 ])

ceHIm22 = Parameter(name = 'ceHIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 46 ])

ceHIm33 = Parameter(name = 'ceHIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceHIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 47 ])

ceWIm11 = Parameter(name = 'ceWIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 48 ])

ceWIm22 = Parameter(name = 'ceWIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 49 ])

ceWIm33 = Parameter(name = 'ceWIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceWIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 50 ])

ceBIm11 = Parameter(name = 'ceBIm11',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm11}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 51 ])

ceBIm22 = Parameter(name = 'ceBIm22',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm22}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 52 ])

ceBIm33 = Parameter(name = 'ceBIm33',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{ceBIm33}',
                    lhablock = 'SMEFTcpv',
                    lhacode = [ 53 ])

cledjIm11 = Parameter(name = 'cledjIm11',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cledjIm11}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 54 ])

cledjIm22 = Parameter(name = 'cledjIm22',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cledjIm22}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 55 ])

cledjIm33 = Parameter(name = 'cledjIm33',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{cledjIm33}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 56 ])

clebQIm11 = Parameter(name = 'clebQIm11',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{clebQIm11}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 57 ])

clebQIm22 = Parameter(name = 'clebQIm22',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{clebQIm22}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 58 ])

clebQIm33 = Parameter(name = 'clebQIm33',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{clebQIm33}',
                      lhablock = 'SMEFTcpv',
                      lhacode = [ 59 ])

cleju1Im11 = Parameter(name = 'cleju1Im11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju1Im11}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 60 ])

cleju1Im22 = Parameter(name = 'cleju1Im22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju1Im22}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 61 ])

cleju1Im33 = Parameter(name = 'cleju1Im33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju1Im33}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 62 ])

cleju3Im11 = Parameter(name = 'cleju3Im11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju3Im11}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 63 ])

cleju3Im22 = Parameter(name = 'cleju3Im22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju3Im22}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 64 ])

cleju3Im33 = Parameter(name = 'cleju3Im33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleju3Im33}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 65 ])

cleQt1Im11 = Parameter(name = 'cleQt1Im11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt1Im11}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 66 ])

cleQt1Im22 = Parameter(name = 'cleQt1Im22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt1Im22}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 67 ])

cleQt1Im33 = Parameter(name = 'cleQt1Im33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt1Im33}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 68 ])

cleQt3Im11 = Parameter(name = 'cleQt3Im11',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt3Im11}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 69 ])

cleQt3Im22 = Parameter(name = 'cleQt3Im22',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt3Im22}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 70 ])

cleQt3Im33 = Parameter(name = 'cleQt3Im33',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{cleQt3Im33}',
                       lhablock = 'SMEFTcpv',
                       lhacode = [ 71 ])

LambdaSMEFT = Parameter(name = 'LambdaSMEFT',
                        nature = 'external',
                        type = 'real',
                        value = 1000,
                        texname = '\\Lambda',
                        lhablock = 'SMEFTcutoff',
                        lhacode = [ 1 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.387,
               texname = '\\text{MW}',
               lhablock = 'SMINPUTS',
               lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663787,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1179,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

linearPropCorrections = Parameter(name = 'linearPropCorrections',
                                  nature = 'external',
                                  type = 'real',
                                  value = 0,
                                  texname = '\\text{linearPropCorrections}',
                                  lhablock = 'SWITCHES',
                                  lhacode = [ 1 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00467,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00216,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.093,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.18,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172.76,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00216,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172.76,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00467,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.093,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.18,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.09,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.33,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

cuH = Parameter(name = 'cuH',
                nature = 'internal',
                type = 'complex',
                value = 'cuHRe + cuHIm*complex(0,1)',
                texname = 'c_{\\text{uH}}')

ctHH = Parameter(name = 'ctHH',
                 nature = 'internal',
                 type = 'complex',
                 value = 'ctHRe + ctHIm*complex(0,1)',
                 texname = 'c_{\\text{tH}}')

cdH = Parameter(name = 'cdH',
                nature = 'internal',
                type = 'complex',
                value = 'cdHRe + cdHIm*complex(0,1)',
                texname = 'c_{\\text{dH}}')

cbH = Parameter(name = 'cbH',
                nature = 'internal',
                type = 'complex',
                value = 'cbHRe + cbHIm*complex(0,1)',
                texname = 'c_{\\text{bH}}')

cuG = Parameter(name = 'cuG',
                nature = 'internal',
                type = 'complex',
                value = 'cuGRe + cuGIm*complex(0,1)',
                texname = 'c_{\\text{uG}}')

ctG = Parameter(name = 'ctG',
                nature = 'internal',
                type = 'complex',
                value = 'ctGRe + ctGIm*complex(0,1)',
                texname = 'c_{\\text{tG}}')

cuW = Parameter(name = 'cuW',
                nature = 'internal',
                type = 'complex',
                value = 'cuWRe + cuWIm*complex(0,1)',
                texname = 'c_{\\text{uW}}')

ctW = Parameter(name = 'ctW',
                nature = 'internal',
                type = 'complex',
                value = 'ctWRe + ctWIm*complex(0,1)',
                texname = 'c_{\\text{tW}}')

cuB = Parameter(name = 'cuB',
                nature = 'internal',
                type = 'complex',
                value = 'cuBRe + cuBIm*complex(0,1)',
                texname = 'c_{\\text{uB}}')

ctB = Parameter(name = 'ctB',
                nature = 'internal',
                type = 'complex',
                value = 'ctBRe + ctBIm*complex(0,1)',
                texname = 'c_{\\text{tB}}')

cdG = Parameter(name = 'cdG',
                nature = 'internal',
                type = 'complex',
                value = 'cdGRe + cdGIm*complex(0,1)',
                texname = 'c_{\\text{dG}}')

cbG = Parameter(name = 'cbG',
                nature = 'internal',
                type = 'complex',
                value = 'cbGRe + cbGIm*complex(0,1)',
                texname = 'c_{\\text{bG}}')

cdW = Parameter(name = 'cdW',
                nature = 'internal',
                type = 'complex',
                value = 'cdWRe + cdWIm*complex(0,1)',
                texname = 'c_{\\text{dW}}')

cbW = Parameter(name = 'cbW',
                nature = 'internal',
                type = 'complex',
                value = 'cbWRe + cbWIm*complex(0,1)',
                texname = 'c_{\\text{bW}}')

cdB = Parameter(name = 'cdB',
                nature = 'internal',
                type = 'complex',
                value = 'cdBRe + cdBIm*complex(0,1)',
                texname = 'c_{\\text{dB}}')

cbBB = Parameter(name = 'cbBB',
                 nature = 'internal',
                 type = 'complex',
                 value = 'cbBRe + cbBIm*complex(0,1)',
                 texname = 'c_{\\text{bB}}')

cHud = Parameter(name = 'cHud',
                 nature = 'internal',
                 type = 'complex',
                 value = 'cHudRe + cHudIm*complex(0,1)',
                 texname = 'c_{\\text{Hud}}')

cHtb = Parameter(name = 'cHtb',
                 nature = 'internal',
                 type = 'complex',
                 value = 'cHtbRe + cHtbIm*complex(0,1)',
                 texname = 'c_{\\text{Htb}}')

cutbd1 = Parameter(name = 'cutbd1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cutbd1Re + cutbd1Im*complex(0,1)',
                   texname = 'c_{\\text{utbd}}^1')

cutbd8 = Parameter(name = 'cutbd8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cutbd8Re + cutbd8Im*complex(0,1)',
                   texname = 'c_{\\text{utbd}}^8')

cjQtu1 = Parameter(name = 'cjQtu1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjQtu1Re + cjQtu1Im*complex(0,1)',
                   texname = 'c_{\\text{jQtu}}^1')

cjQtu8 = Parameter(name = 'cjQtu8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjQtu8Re + cjQtu8Im*complex(0,1)',
                   texname = 'c_{\\text{jQtu}}^8')

cjQbd1 = Parameter(name = 'cjQbd1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjQbd1Re + cjQbd1Im*complex(0,1)',
                   texname = 'c_{\\text{jQbd}}^1')

cjQbd8 = Parameter(name = 'cjQbd8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjQbd8Re + cjQbd8Im*complex(0,1)',
                   texname = 'c_{\\text{jQbd}}^8')

cjujd1 = Parameter(name = 'cjujd1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjujd1Re + cjujd1Im*complex(0,1)',
                   texname = 'c_{\\text{jujd}}^1')

cjujd8 = Parameter(name = 'cjujd8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjujd8Re + cjujd8Im*complex(0,1)',
                   texname = 'c_{\\text{jujd}}^8')

cjujd11 = Parameter(name = 'cjujd11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cjujd11Re + cjujd11Im*complex(0,1)',
                    texname = 'c_{\\text{jujd}}^{\\text{Prime}}')

cjujd81 = Parameter(name = 'cjujd81',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cjujd81Re + cjujd81Im*complex(0,1)',
                    texname = 'c_{\\text{jujd}}^{8 \\text{Prime}}')

cQtjd1 = Parameter(name = 'cQtjd1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cQtjd1Re + cQtjd1Im*complex(0,1)',
                   texname = 'c_{\\text{Qtjd}}^1')

cQtjd8 = Parameter(name = 'cQtjd8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cQtjd8Re + cQtjd8Im*complex(0,1)',
                   texname = 'c_{\\text{Qtjd}}^8')

cjuQb1 = Parameter(name = 'cjuQb1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjuQb1Re + cjuQb1Im*complex(0,1)',
                   texname = 'c_{\\text{juQb}}^1')

cjuQb8 = Parameter(name = 'cjuQb8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjuQb8Re + cjuQb8Im*complex(0,1)',
                   texname = 'c_{\\text{juQb}}^8')

cQujb1 = Parameter(name = 'cQujb1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cQujb1Re + cQujb1Im*complex(0,1)',
                   texname = 'c_{\\text{Qujb}}^1')

cQujb8 = Parameter(name = 'cQujb8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cQujb8Re + cQujb8Im*complex(0,1)',
                   texname = 'c_{\\text{Qujb}}^8')

cjtQd1 = Parameter(name = 'cjtQd1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjtQd1Re + cjtQd1Im*complex(0,1)',
                   texname = 'c_{\\text{jtQd}}^1')

cjtQd8 = Parameter(name = 'cjtQd8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cjtQd8Re + cjtQd8Im*complex(0,1)',
                   texname = 'c_{\\text{jtQd}}^8')

cQtQb1 = Parameter(name = 'cQtQb1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cQtQb1Re + cQtQb1Im*complex(0,1)',
                   texname = 'c_{\\text{QtQb}}^1')

cQtQb8 = Parameter(name = 'cQtQb8',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cQtQb8Re + cQtQb8Im*complex(0,1)',
                   texname = 'c_{\\text{QtQb}}^8')

ceH11 = Parameter(name = 'ceH11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceHRe11 + ceHIm11*complex(0,1)',
                  texname = 'c_{\\text{eH}}_{11}')

ceH22 = Parameter(name = 'ceH22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceHRe22 + ceHIm22*complex(0,1)',
                  texname = 'c_{\\text{eH}}_{22}')

ceH33 = Parameter(name = 'ceH33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceHRe33 + ceHIm33*complex(0,1)',
                  texname = 'c_{\\text{eH}}_{33}')

ceW11 = Parameter(name = 'ceW11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceWRe11 + ceWIm11*complex(0,1)',
                  texname = 'c_{\\text{eW}}_{11}')

ceW22 = Parameter(name = 'ceW22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceWRe22 + ceWIm22*complex(0,1)',
                  texname = 'c_{\\text{eW}}_{22}')

ceW33 = Parameter(name = 'ceW33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceWRe33 + ceWIm33*complex(0,1)',
                  texname = 'c_{\\text{eW}}_{33}')

ceB11 = Parameter(name = 'ceB11',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceBRe11 + ceBIm11*complex(0,1)',
                  texname = 'c_{\\text{eB}}_{11}')

ceB22 = Parameter(name = 'ceB22',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceBRe22 + ceBIm22*complex(0,1)',
                  texname = 'c_{\\text{eB}}_{22}')

ceB33 = Parameter(name = 'ceB33',
                  nature = 'internal',
                  type = 'complex',
                  value = 'ceBRe33 + ceBIm33*complex(0,1)',
                  texname = 'c_{\\text{eB}}_{33}')

cledj11 = Parameter(name = 'cledj11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cledjRe11 + cledjIm11*complex(0,1)',
                    texname = 'c_{\\text{ledj}}_{11}')

cledj22 = Parameter(name = 'cledj22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cledjRe22 + cledjIm22*complex(0,1)',
                    texname = 'c_{\\text{ledj}}_{22}')

cledj33 = Parameter(name = 'cledj33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'cledjRe33 + cledjIm33*complex(0,1)',
                    texname = 'c_{\\text{ledj}}_{33}')

clebQ11 = Parameter(name = 'clebQ11',
                    nature = 'internal',
                    type = 'complex',
                    value = 'clebQRe11 + clebQIm11*complex(0,1)',
                    texname = 'c_{\\text{lebQ}}_{11}')

clebQ22 = Parameter(name = 'clebQ22',
                    nature = 'internal',
                    type = 'complex',
                    value = 'clebQRe22 + clebQIm22*complex(0,1)',
                    texname = 'c_{\\text{lebQ}}_{22}')

clebQ33 = Parameter(name = 'clebQ33',
                    nature = 'internal',
                    type = 'complex',
                    value = 'clebQRe33 + clebQIm33*complex(0,1)',
                    texname = 'c_{\\text{lebQ}}_{33}')

cleju111 = Parameter(name = 'cleju111',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleju1Re11 + cleju1Im11*complex(0,1)',
                     texname = 'c_{\\text{leju}}^1{}_{11}')

cleju122 = Parameter(name = 'cleju122',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleju1Re22 + cleju1Im22*complex(0,1)',
                     texname = 'c_{\\text{leju}}^1{}_{22}')

cleju133 = Parameter(name = 'cleju133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleju1Re33 + cleju1Im33*complex(0,1)',
                     texname = 'c_{\\text{leju}}^1{}_{33}')

cleju311 = Parameter(name = 'cleju311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleju3Re11 + cleju3Im11*complex(0,1)',
                     texname = 'c_{\\text{leju}}^3{}_{11}')

cleju322 = Parameter(name = 'cleju322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleju3Re22 + cleju3Im22*complex(0,1)',
                     texname = 'c_{\\text{leju}}^3{}_{22}')

cleju333 = Parameter(name = 'cleju333',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleju3Re33 + cleju3Im33*complex(0,1)',
                     texname = 'c_{\\text{leju}}^3{}_{33}')

cleQt111 = Parameter(name = 'cleQt111',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleQt1Re11 + cleQt1Im11*complex(0,1)',
                     texname = 'c_{\\text{leQt}}^1{}_{11}')

cleQt122 = Parameter(name = 'cleQt122',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleQt1Re22 + cleQt1Im22*complex(0,1)',
                     texname = 'c_{\\text{leQt}}^1{}_{22}')

cleQt133 = Parameter(name = 'cleQt133',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleQt1Re33 + cleQt1Im33*complex(0,1)',
                     texname = 'c_{\\text{leQt}}^1{}_{33}')

cleQt311 = Parameter(name = 'cleQt311',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleQt3Re11 + cleQt3Im11*complex(0,1)',
                     texname = 'c_{\\text{leQt}}^3{}_{11}')

cleQt322 = Parameter(name = 'cleQt322',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleQt3Re22 + cleQt3Im22*complex(0,1)',
                     texname = 'c_{\\text{leQt}}^3{}_{22}')

cleQt333 = Parameter(name = 'cleQt333',
                     nature = 'internal',
                     type = 'complex',
                     value = 'cleQt3Re33 + cleQt3Im33*complex(0,1)',
                     texname = 'c_{\\text{leQt}}^3{}_{33}')

MWsm = Parameter(name = 'MWsm',
                 nature = 'internal',
                 type = 'real',
                 value = 'MW',
                 texname = '\\text{MWsm}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MW**2*(1 - MW**2/MZ**2)*cmath.sqrt(2))/cmath.pi',
                texname = '\\alpha _{\\text{EW}}')

vevhat = Parameter(name = 'vevhat',
                   nature = 'internal',
                   type = 'real',
                   value = '1/(2**0.25*cmath.sqrt(Gf))',
                   texname = '\\hat{v}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = '(Gf*MH**2)/cmath.sqrt(2)',
                texname = '\\text{lam}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

Gstrong = Parameter(name = 'Gstrong',
              nature = 'internal',
              type = 'real',
              value = 'G' if configuration.norm_chromo_gs else '1.',
              texname = '\\text{Gstrong}')

sth2 = Parameter(name = 'sth2',
                 nature = 'internal',
                 type = 'real',
                 value = '1 - MW**2/MZ**2',
                 texname = '\\text{sth2}')

propCorr = Parameter(name = 'propCorr',
                     nature = 'internal',
                     type = 'real',
                     value = 'abs(linearPropCorrections)/(abs(linearPropCorrections) + 10**-40)',
                     texname = '\\Delta _{\\text{prop.}}')

MZ1 = Parameter(name = 'MZ1',
                nature = 'internal',
                type = 'real',
                value = 'MZ',
                texname = '\\text{MZ}\'')

MH1 = Parameter(name = 'MH1',
                nature = 'internal',
                type = 'real',
                value = 'MH',
                texname = '\\text{MH}\'')

MT1 = Parameter(name = 'MT1',
                nature = 'internal',
                type = 'real',
                value = 'MT',
                texname = '\\text{MT}\'')

WZ1 = Parameter(name = 'WZ1',
                nature = 'internal',
                type = 'real',
                value = 'WZ',
                texname = '\\text{WZ}\'')

WW1 = Parameter(name = 'WW1',
                nature = 'internal',
                type = 'real',
                value = 'WW',
                texname = '\\text{WW}\'')

WH1 = Parameter(name = 'WH1',
                nature = 'internal',
                type = 'real',
                value = 'WH',
                texname = '\\text{WH}\'')

WT1 = Parameter(name = 'WT1',
                nature = 'internal',
                type = 'real',
                value = 'WT',
                texname = '\\text{WT}\'')

gHgg2 = Parameter(name = 'gHgg2',
                  nature = 'internal',
                  type = 'real',
                  value = '(-7*aS)/(720.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^2')

gHgg4 = Parameter(name = 'gHgg4',
                  nature = 'internal',
                  type = 'real',
                  value = 'aS/(360.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^4')

gHgg5 = Parameter(name = 'gHgg5',
                  nature = 'internal',
                  type = 'real',
                  value = 'aS/(20.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^5')

cth = Parameter(name = 'cth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(1 - sth2)',
                texname = 'c_{\\theta }')

MW1 = Parameter(name = 'MW1',
                nature = 'internal',
                type = 'real',
                value = 'MWsm',
                texname = '\\text{MW}\'')

sth = Parameter(name = 'sth',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(sth2)',
                texname = 's_{\\theta }')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vevhat',
               texname = 'y^b')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vevhat',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vevhat',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vevhat',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vevhat',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vevhat',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vevhat',
               texname = 'y^t')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vevhat',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vevhat',
                texname = '\\text{yup}')

gHgg1 = Parameter(name = 'gHgg1',
                  nature = 'internal',
                  type = 'real',
                  value = 'G**2/(48.*cmath.pi**2)',
                  texname = 'g_{\\text{HGG}}^1')

gHgg3 = Parameter(name = 'gHgg3',
                  nature = 'internal',
                  type = 'real',
                  value = '(aS*G)/(60.*cmath.pi)',
                  texname = 'g_{\\text{HGG}}^3')

dGf = Parameter(name = 'dGf',
                nature = 'internal',
                type = 'real',
                value = '((cHl311 + cHl322 - cll1221/2.)*vevhat**2)/LambdaSMEFT**2',
                texname = '\\text{dGf}')

dkH = Parameter(name = 'dkH',
                nature = 'internal',
                type = 'real',
                value = '((cHbox - cHDD/4.)*vevhat**2)/LambdaSMEFT**2',
                texname = '\\text{dkH}')

vevT = Parameter(name = 'vevT',
                 nature = 'internal',
                 type = 'real',
                 value = '(1 + dGf/2.)*vevhat',
                 texname = '\\text{vevT}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cth',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sth',
               texname = 'g_w')

yb0 = Parameter(name = 'yb0',
                nature = 'internal',
                type = 'complex',
                value = '(1 - dGf/2.)*yb + (vevhat**2*complexconjugate(cbH))/(2.*LambdaSMEFT**2)',
                texname = '\\text{yb0}')

yt0 = Parameter(name = 'yt0',
                nature = 'internal',
                type = 'complex',
                value = '(1 - dGf/2.)*yt + (vevhat**2*complexconjugate(ctHH))/(2.*LambdaSMEFT**2)',
                texname = '\\text{yt0}')

gHaa = Parameter(name = 'gHaa',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(-1.75 + (4*(0.3333333333333333 + (7*MH**2)/(360.*MT**2)))/3. - (29*MH**6)/(16800.*MWsm**6) - (19*MH**4)/(1680.*MWsm**4) - (11*MH**2)/(120.*MWsm**2)))/(8.*cmath.pi**2)',
                 texname = 'g_{\\text{H$\\gamma \\gamma $}}')

gHza = Parameter(name = 'gHza',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee**2*(((0.4583333333333333 + (29*MH**6)/(100800.*MWsm**6) + (19*MH**4)/(10080.*MWsm**4) + (11*MH**2)/(720.*MWsm**2) + (MH**4*MZ**2)/(2100.*MWsm**6) + (MH**2*MZ**2)/(280.*MWsm**4) + (7*MZ**2)/(180.*MWsm**2) + (67*MH**2*MZ**4)/(100800.*MWsm**6) + (53*MZ**4)/(10080.*MWsm**4) + (43*MZ**6)/(50400.*MWsm**6) - (31*cth**2)/(24.*sth**2) - (29*cth**2*MH**6)/(20160.*MWsm**6*sth**2) - (19*cth**2*MH**4)/(2016.*MWsm**4*sth**2) - (11*cth**2*MH**2)/(144.*MWsm**2*sth**2) - (cth**2*MH**4*MZ**2)/(560.*MWsm**6*sth**2) - (31*cth**2*MH**2*MZ**2)/(2520.*MWsm**4*sth**2) - (cth**2*MZ**2)/(9.*MWsm**2*sth**2) - (43*cth**2*MH**2*MZ**4)/(20160.*MWsm**6*sth**2) - (17*cth**2*MZ**4)/(1120.*MWsm**4*sth**2) - (5*cth**2*MZ**6)/(2016.*MWsm**6*sth**2))*sth)/cth + ((0.3333333333333333 + (7*MH**2)/(360.*MT**2) + (11*MZ**2)/(360.*MT**2))*(0.5 - (4*sth**2)/3.))/(cth*sth)))/(4.*cmath.pi**2)',
                 texname = 'g_{\\text{HZ$\\gamma $}}')

dMZ2 = Parameter(name = 'dMZ2',
                 nature = 'internal',
                 type = 'real',
                 value = '((cHDD/2. + 2*cHWB*cth*sth)*vevhat**2)/LambdaSMEFT**2',
                 texname = '\\text{dMZ2}')

dMH2 = Parameter(name = 'dMH2',
                 nature = 'internal',
                 type = 'real',
                 value = '2*dkH - (3*cH*vevhat**2)/(2.*lam*LambdaSMEFT**2)',
                 texname = '\\text{dMH2}')

dgw = Parameter(name = 'dgw',
                nature = 'internal',
                type = 'real',
                value = '-dGf/2.',
                texname = '\\text{dgw}')

barlam = Parameter(name = 'barlam',
                   nature = 'internal',
                   type = 'real',
                   value = '(1 - dGf - dMH2)*lam',
                   texname = '\\text{barlam}')

dWT = Parameter(name = 'dWT',
                nature = 'internal',
                type = 'real',
                value = '2*WT*(dgw + (vevhat*(ee*(3*cHtbRe*MB*MT*MWsm**2 + cHQ3*((MB**2 - MT**2)**2 + (MB**2 + MT**2)*MWsm**2 - 2*MWsm**4))*vevhat + 6*MWsm**2*(ctWRe*MT*(MB**2 - MT**2 + MWsm**2) + cbWRe*MB*(-MB**2 + MT**2 + MWsm**2))*sth*cmath.sqrt(2)))/(ee*LambdaSMEFT**2*((MB**2 - MT**2)**2 + (MB**2 + MT**2)*MWsm**2 - 2*MWsm**4)))',
                texname = '\\text{dWT}')

dWW = Parameter(name = 'dWW',
                nature = 'internal',
                type = 'real',
                value = '(2*dgw + (2*(6*cHj3 + cHl311 + cHl322 + cHl333)*vevhat**2)/(9.*LambdaSMEFT**2))*WW',
                texname = '\\text{dWW}')

gwsh = Parameter(name = 'gwsh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dgw - (cHW*vevhat**2)/LambdaSMEFT**2))/sth',
                 texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(1 - (3*cH*vevhat**2)/(8.*lam*LambdaSMEFT**2))*vevT',
                texname = '\\text{vev}')

dg1 = Parameter(name = 'dg1',
                nature = 'internal',
                type = 'real',
                value = '(-dGf - dMZ2/sth**2)/2.',
                texname = '\\text{dg1}')

dWHc = Parameter(name = 'dWHc',
                 nature = 'internal',
                 type = 'real',
                 value = 'yc/(yc + 10**-40)*(-0.02884*dGf + ((0.05768*cHbox - 0.01442*cHDD - 0.05768*cuHRe)*vevhat**2)/LambdaSMEFT**2)',
                 texname='\\text{dWHc}')

dWHb = Parameter(name = 'dWHb',
                 nature = 'internal',
                 type = 'real',
                 value = 'yb/(yb + 10**-40)*(vevhat**2*(-1.1618*cbHRe)/(LambdaSMEFT**2*(yb+10**-40)) - 0.5809*dGf + vevhat**2*(1.1618*cHbox - 0.29045*cHDD)/LambdaSMEFT**2)',
                 texname='\\text{dWHb}')

dWHta = Parameter(name = 'dWHta',
                 nature = 'internal',
                 type = 'real',
                 value = 'ytau/(ytau + 10**-40)*(-0.06256*dGf + vevhat**2*(-0.12512*ceHRe33)/(LambdaSMEFT**2*(ytau+10**-40)) + vevhat**2*( 0.12512*cHbox - 0.03128*cHDD)/(LambdaSMEFT**2))',
                 texname='\\text{dWHta}')

dWH = Parameter(name = 'dWH',
                nature = 'internal',
                type = 'real',
                value = 'WH*(-0.24161*dGf + 0.96644*dgw + 0.48322*dkH - 0.11186509426655454*dWW + (0.3641037844923816*cHj3*vevhat**2)/LambdaSMEFT**2 + (0.05869435902885915*cHl311*vevhat**2)/LambdaSMEFT**2 + (0.05869435902885915*cHl322*vevhat**2)/LambdaSMEFT**2 + (0.05869435902885915*cHl333*vevhat**2)/LambdaSMEFT**2 + (0.1636*cHG*MT**2*vevhat**2)/(LambdaSMEFT**2*(-0.5*gHgg2*MH**2 + gHgg1*MT**2)) + (cHW*(-0.35937785117066967*gHaa*gHza + 0.006164*cth*gHaa*sth + 0.00454*gHza*sth**2)*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + (cHWB*(-0.00454*cth*gHza*sth + gHaa*(-0.0030819999999999997 + 0.006163999999999999*sth**2))*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + (cHB*(-0.006163999999999999*cth*gHaa*sth - 0.00454*gHza*(-1. + sth**2))*vevhat**2)/(gHaa*gHza*LambdaSMEFT**2) + dWHc + dWHb + dWHta)',
                texname = '\\text{dWH}')

dWZ = Parameter(name = 'dWZ',
                nature = 'internal',
                type = 'real',
                value = 'WZ*(-1 + (36*cth*MB*MZ**2*sth*(cbWRe*cth + cbBRe*sth)*(-3 + 4*sth**2)*vevhat*cmath.sqrt(2)*cmath.sqrt(-4*MB**2 + MZ**2) + ee*LambdaSMEFT**2*(2*MZ**3*(27 + 54*dgw - 54*(1 + dg1 + dgw)*sth**2 + 76*(1 + 4*dg1 - 2*dgw)*sth**4 + 152*(-dg1 + dgw)*sth**6) + MZ**2*(9 + 18*dgw - 6*(2 + dg1 + 3*dgw)*sth**2 + 8*(1 + 4*dg1 - 2*dgw)*sth**4 + 16*(-dg1 + dgw)*sth**6)*cmath.sqrt(-4*MB**2 + MZ**2) + MB**2*(-9 - 18*dgw - 6*(4 + 11*dg1 - 3*dgw)*sth**2 + 16*(1 + 4*dg1 - 2*dgw)*sth**4 + 32*(-dg1 + dgw)*sth**6)*cmath.sqrt(-4*MB**2 + MZ**2)) + 2*ee*vevhat**2*(36*cHj3*MZ**3 + 6*cHl311*MZ**3 + 6*cHl322*MZ**3 + 6*cHl333*MZ**3 + 9*(3*cHbq - cHQ1 - cHQ3)*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + 9*cHQ1*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + 9*cHQ3*MZ**2*cmath.sqrt(-4*MB**2 + MZ**2) + 3*cHWB*cth*(-7*MB**2 + MZ**2)*sth*cmath.sqrt(-4*MB**2 + MZ**2) + 8*cHWB*cth*sth**3*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) - 8*cHWB*cth*sth**5*(2*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(19*MZ + cmath.sqrt(-4*MB**2 + MZ**2))) + 6*sth**2*(-2*(cHbq + cHQ1 + cHQ3)*MB**2*cmath.sqrt(-4*MB**2 + MZ**2) + MZ**2*(-((2*cHd + cHe11 + cHe22 + cHe33 - 2*cHj1 + 6*cHj3 + cHl111 + cHl122 + cHl133 + cHl311 + cHl322 + cHl333 - 4*cHu)*MZ) - (cHbq + cHQ1 + cHQ3)*cmath.sqrt(-4*MB**2 + MZ**2)))))/(ee*LambdaSMEFT**2*(2*MZ**3*(27 - 54*sth**2 + 76*sth**4) + MZ**2*(9 - 12*sth**2 + 8*sth**4)*cmath.sqrt(-4*MB**2 + MZ**2) + MB**2*(-9 - 24*sth**2 + 16*sth**4)*cmath.sqrt(-4*MB**2 + MZ**2))))',
                texname = '\\text{dWZ}')

g1sh = Parameter(name = 'g1sh',
                 nature = 'internal',
                 type = 'real',
                 value = '(ee*(1 + dg1 - (cHB*vevhat**2)/LambdaSMEFT**2))/cth',
                 texname = 'g_1')


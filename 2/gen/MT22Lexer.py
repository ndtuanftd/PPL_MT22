# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/2/src/main/mt22/parser\MT22.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,68,572,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,
        65,7,65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,
        71,2,72,7,72,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,3,10,265,8,10,1,11,1,11,1,11,1,
        11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,
        16,1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,20,1,20,1,20,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,
        22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,
        24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,27,1,
        27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,29,1,
        29,1,29,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,
        31,1,31,1,31,1,32,1,32,1,33,1,33,1,34,1,34,1,35,1,35,1,36,1,36,1,
        37,1,37,1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,41,1,41,1,
        41,1,42,1,42,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,46,1,46,1,
        46,1,47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,
        53,1,53,1,54,1,54,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,58,5,
        58,452,8,58,10,58,12,58,455,9,58,1,59,1,59,1,59,5,59,460,8,59,10,
        59,12,59,463,9,59,1,59,3,59,466,8,59,1,60,1,60,1,60,3,60,471,8,60,
        1,60,3,60,474,8,60,1,60,1,60,1,61,1,61,1,61,5,61,481,8,61,10,61,
        12,61,484,9,61,1,61,1,61,1,61,1,62,1,62,1,62,1,62,5,62,493,8,62,
        10,62,12,62,496,9,62,1,62,3,62,499,8,62,1,62,1,62,1,62,1,62,1,63,
        1,63,1,63,1,63,5,63,509,8,63,10,63,12,63,512,9,63,1,63,1,63,1,63,
        1,63,1,63,1,64,4,64,520,8,64,11,64,12,64,521,1,64,1,64,1,65,1,65,
        1,65,5,65,529,8,65,10,65,12,65,532,9,65,1,65,1,65,1,66,1,66,1,66,
        5,66,539,8,66,10,66,12,66,542,9,66,1,66,1,66,1,66,1,67,1,67,1,67,
        1,68,1,68,4,68,552,8,68,11,68,12,68,553,1,69,1,69,3,69,558,8,69,
        1,69,4,69,561,8,69,11,69,12,69,562,1,70,1,70,1,70,1,71,1,71,1,72,
        1,72,1,72,3,482,494,510,0,73,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,
        17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,
        39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,
        61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,
        83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,
        52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,121,61,
        123,62,125,63,127,64,129,65,131,66,133,67,135,68,137,0,139,0,141,
        0,143,0,145,0,1,0,10,3,0,65,90,95,95,97,122,1,0,49,57,2,0,48,57,
        95,95,1,0,10,10,3,0,9,10,13,13,32,32,3,0,34,34,69,70,79,79,2,0,69,
        69,101,101,2,0,43,43,45,45,1,0,48,57,8,0,34,34,39,39,92,92,98,98,
        102,102,110,110,114,114,116,116,586,0,1,1,0,0,0,0,3,1,0,0,0,0,5,
        1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,
        0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,
        0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,
        0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,
        0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,
        0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,
        0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,
        0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,
        0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,
        0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,
        1,0,0,0,0,107,1,0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,
        0,115,1,0,0,0,0,117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,
        0,0,0,0,125,1,0,0,0,0,127,1,0,0,0,0,129,1,0,0,0,0,131,1,0,0,0,0,
        133,1,0,0,0,0,135,1,0,0,0,1,147,1,0,0,0,3,159,1,0,0,0,5,172,1,0,
        0,0,7,182,1,0,0,0,9,193,1,0,0,0,11,205,1,0,0,0,13,218,1,0,0,0,15,
        229,1,0,0,0,17,241,1,0,0,0,19,247,1,0,0,0,21,264,1,0,0,0,23,266,
        1,0,0,0,25,271,1,0,0,0,27,277,1,0,0,0,29,285,1,0,0,0,31,288,1,0,
        0,0,33,293,1,0,0,0,35,299,1,0,0,0,37,305,1,0,0,0,39,309,1,0,0,0,
        41,318,1,0,0,0,43,321,1,0,0,0,45,329,1,0,0,0,47,336,1,0,0,0,49,343,
        1,0,0,0,51,348,1,0,0,0,53,353,1,0,0,0,55,359,1,0,0,0,57,363,1,0,
        0,0,59,372,1,0,0,0,61,375,1,0,0,0,63,383,1,0,0,0,65,389,1,0,0,0,
        67,391,1,0,0,0,69,393,1,0,0,0,71,395,1,0,0,0,73,397,1,0,0,0,75,399,
        1,0,0,0,77,401,1,0,0,0,79,404,1,0,0,0,81,407,1,0,0,0,83,410,1,0,
        0,0,85,413,1,0,0,0,87,415,1,0,0,0,89,417,1,0,0,0,91,420,1,0,0,0,
        93,423,1,0,0,0,95,426,1,0,0,0,97,428,1,0,0,0,99,430,1,0,0,0,101,
        432,1,0,0,0,103,434,1,0,0,0,105,436,1,0,0,0,107,438,1,0,0,0,109,
        440,1,0,0,0,111,442,1,0,0,0,113,444,1,0,0,0,115,446,1,0,0,0,117,
        448,1,0,0,0,119,465,1,0,0,0,121,467,1,0,0,0,123,477,1,0,0,0,125,
        488,1,0,0,0,127,504,1,0,0,0,129,519,1,0,0,0,131,525,1,0,0,0,133,
        535,1,0,0,0,135,546,1,0,0,0,137,549,1,0,0,0,139,555,1,0,0,0,141,
        564,1,0,0,0,143,567,1,0,0,0,145,569,1,0,0,0,147,148,5,114,0,0,148,
        149,5,101,0,0,149,150,5,97,0,0,150,151,5,100,0,0,151,152,5,73,0,
        0,152,153,5,110,0,0,153,154,5,116,0,0,154,155,5,101,0,0,155,156,
        5,103,0,0,156,157,5,101,0,0,157,158,5,114,0,0,158,2,1,0,0,0,159,
        160,5,112,0,0,160,161,5,114,0,0,161,162,5,105,0,0,162,163,5,110,
        0,0,163,164,5,116,0,0,164,165,5,73,0,0,165,166,5,110,0,0,166,167,
        5,116,0,0,167,168,5,101,0,0,168,169,5,103,0,0,169,170,5,101,0,0,
        170,171,5,114,0,0,171,4,1,0,0,0,172,173,5,114,0,0,173,174,5,101,
        0,0,174,175,5,97,0,0,175,176,5,100,0,0,176,177,5,70,0,0,177,178,
        5,108,0,0,178,179,5,111,0,0,179,180,5,97,0,0,180,181,5,116,0,0,181,
        6,1,0,0,0,182,183,5,119,0,0,183,184,5,114,0,0,184,185,5,105,0,0,
        185,186,5,116,0,0,186,187,5,101,0,0,187,188,5,70,0,0,188,189,5,108,
        0,0,189,190,5,111,0,0,190,191,5,97,0,0,191,192,5,116,0,0,192,8,1,
        0,0,0,193,194,5,114,0,0,194,195,5,101,0,0,195,196,5,97,0,0,196,197,
        5,100,0,0,197,198,5,66,0,0,198,199,5,111,0,0,199,200,5,111,0,0,200,
        201,5,108,0,0,201,202,5,101,0,0,202,203,5,97,0,0,203,204,5,110,0,
        0,204,10,1,0,0,0,205,206,5,112,0,0,206,207,5,114,0,0,207,208,5,105,
        0,0,208,209,5,110,0,0,209,210,5,116,0,0,210,211,5,66,0,0,211,212,
        5,111,0,0,212,213,5,111,0,0,213,214,5,108,0,0,214,215,5,101,0,0,
        215,216,5,97,0,0,216,217,5,110,0,0,217,12,1,0,0,0,218,219,5,114,
        0,0,219,220,5,101,0,0,220,221,5,97,0,0,221,222,5,100,0,0,222,223,
        5,83,0,0,223,224,5,116,0,0,224,225,5,114,0,0,225,226,5,105,0,0,226,
        227,5,110,0,0,227,228,5,103,0,0,228,14,1,0,0,0,229,230,5,112,0,0,
        230,231,5,114,0,0,231,232,5,105,0,0,232,233,5,110,0,0,233,234,5,
        116,0,0,234,235,5,83,0,0,235,236,5,116,0,0,236,237,5,114,0,0,237,
        238,5,105,0,0,238,239,5,110,0,0,239,240,5,103,0,0,240,16,1,0,0,0,
        241,242,5,115,0,0,242,243,5,117,0,0,243,244,5,112,0,0,244,245,5,
        101,0,0,245,246,5,114,0,0,246,18,1,0,0,0,247,248,5,112,0,0,248,249,
        5,114,0,0,249,250,5,101,0,0,250,251,5,118,0,0,251,252,5,101,0,0,
        252,253,5,110,0,0,253,254,5,116,0,0,254,255,5,68,0,0,255,256,5,101,
        0,0,256,257,5,102,0,0,257,258,5,97,0,0,258,259,5,117,0,0,259,260,
        5,108,0,0,260,261,5,116,0,0,261,20,1,0,0,0,262,265,3,49,24,0,263,
        265,3,33,16,0,264,262,1,0,0,0,264,263,1,0,0,0,265,22,1,0,0,0,266,
        267,5,97,0,0,267,268,5,117,0,0,268,269,5,116,0,0,269,270,5,111,0,
        0,270,24,1,0,0,0,271,272,5,98,0,0,272,273,5,114,0,0,273,274,5,101,
        0,0,274,275,5,97,0,0,275,276,5,107,0,0,276,26,1,0,0,0,277,278,5,
        98,0,0,278,279,5,111,0,0,279,280,5,111,0,0,280,281,5,108,0,0,281,
        282,5,101,0,0,282,283,5,97,0,0,283,284,5,110,0,0,284,28,1,0,0,0,
        285,286,5,100,0,0,286,287,5,111,0,0,287,30,1,0,0,0,288,289,5,101,
        0,0,289,290,5,108,0,0,290,291,5,115,0,0,291,292,5,101,0,0,292,32,
        1,0,0,0,293,294,5,102,0,0,294,295,5,97,0,0,295,296,5,108,0,0,296,
        297,5,115,0,0,297,298,5,101,0,0,298,34,1,0,0,0,299,300,5,102,0,0,
        300,301,5,108,0,0,301,302,5,111,0,0,302,303,5,97,0,0,303,304,5,116,
        0,0,304,36,1,0,0,0,305,306,5,102,0,0,306,307,5,111,0,0,307,308,5,
        114,0,0,308,38,1,0,0,0,309,310,5,102,0,0,310,311,5,117,0,0,311,312,
        5,110,0,0,312,313,5,99,0,0,313,314,5,116,0,0,314,315,5,105,0,0,315,
        316,5,111,0,0,316,317,5,110,0,0,317,40,1,0,0,0,318,319,5,105,0,0,
        319,320,5,102,0,0,320,42,1,0,0,0,321,322,5,105,0,0,322,323,5,110,
        0,0,323,324,5,116,0,0,324,325,5,101,0,0,325,326,5,103,0,0,326,327,
        5,101,0,0,327,328,5,114,0,0,328,44,1,0,0,0,329,330,5,114,0,0,330,
        331,5,101,0,0,331,332,5,116,0,0,332,333,5,117,0,0,333,334,5,114,
        0,0,334,335,5,110,0,0,335,46,1,0,0,0,336,337,5,115,0,0,337,338,5,
        116,0,0,338,339,5,114,0,0,339,340,5,105,0,0,340,341,5,110,0,0,341,
        342,5,103,0,0,342,48,1,0,0,0,343,344,5,116,0,0,344,345,5,114,0,0,
        345,346,5,117,0,0,346,347,5,101,0,0,347,50,1,0,0,0,348,349,5,118,
        0,0,349,350,5,111,0,0,350,351,5,105,0,0,351,352,5,100,0,0,352,52,
        1,0,0,0,353,354,5,119,0,0,354,355,5,104,0,0,355,356,5,105,0,0,356,
        357,5,108,0,0,357,358,5,101,0,0,358,54,1,0,0,0,359,360,5,111,0,0,
        360,361,5,117,0,0,361,362,5,116,0,0,362,56,1,0,0,0,363,364,5,99,
        0,0,364,365,5,111,0,0,365,366,5,110,0,0,366,367,5,116,0,0,367,368,
        5,105,0,0,368,369,5,110,0,0,369,370,5,117,0,0,370,371,5,101,0,0,
        371,58,1,0,0,0,372,373,5,111,0,0,373,374,5,102,0,0,374,60,1,0,0,
        0,375,376,5,105,0,0,376,377,5,110,0,0,377,378,5,104,0,0,378,379,
        5,101,0,0,379,380,5,114,0,0,380,381,5,105,0,0,381,382,5,116,0,0,
        382,62,1,0,0,0,383,384,5,97,0,0,384,385,5,114,0,0,385,386,5,114,
        0,0,386,387,5,97,0,0,387,388,5,121,0,0,388,64,1,0,0,0,389,390,5,
        43,0,0,390,66,1,0,0,0,391,392,5,45,0,0,392,68,1,0,0,0,393,394,5,
        42,0,0,394,70,1,0,0,0,395,396,5,47,0,0,396,72,1,0,0,0,397,398,5,
        37,0,0,398,74,1,0,0,0,399,400,5,33,0,0,400,76,1,0,0,0,401,402,5,
        38,0,0,402,403,5,38,0,0,403,78,1,0,0,0,404,405,5,124,0,0,405,406,
        5,124,0,0,406,80,1,0,0,0,407,408,5,33,0,0,408,409,5,61,0,0,409,82,
        1,0,0,0,410,411,5,61,0,0,411,412,5,61,0,0,412,84,1,0,0,0,413,414,
        5,60,0,0,414,86,1,0,0,0,415,416,5,62,0,0,416,88,1,0,0,0,417,418,
        5,60,0,0,418,419,5,61,0,0,419,90,1,0,0,0,420,421,5,62,0,0,421,422,
        5,61,0,0,422,92,1,0,0,0,423,424,5,58,0,0,424,425,5,58,0,0,425,94,
        1,0,0,0,426,427,5,91,0,0,427,96,1,0,0,0,428,429,5,93,0,0,429,98,
        1,0,0,0,430,431,5,40,0,0,431,100,1,0,0,0,432,433,5,41,0,0,433,102,
        1,0,0,0,434,435,5,123,0,0,435,104,1,0,0,0,436,437,5,125,0,0,437,
        106,1,0,0,0,438,439,5,58,0,0,439,108,1,0,0,0,440,441,5,59,0,0,441,
        110,1,0,0,0,442,443,5,46,0,0,443,112,1,0,0,0,444,445,5,44,0,0,445,
        114,1,0,0,0,446,447,5,61,0,0,447,116,1,0,0,0,448,453,7,0,0,0,449,
        452,3,143,71,0,450,452,7,0,0,0,451,449,1,0,0,0,451,450,1,0,0,0,452,
        455,1,0,0,0,453,451,1,0,0,0,453,454,1,0,0,0,454,118,1,0,0,0,455,
        453,1,0,0,0,456,466,5,48,0,0,457,461,7,1,0,0,458,460,7,2,0,0,459,
        458,1,0,0,0,460,463,1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,462,
        464,1,0,0,0,463,461,1,0,0,0,464,466,6,59,0,0,465,456,1,0,0,0,465,
        457,1,0,0,0,466,120,1,0,0,0,467,473,3,119,59,0,468,474,3,137,68,
        0,469,471,3,137,68,0,470,469,1,0,0,0,470,471,1,0,0,0,471,472,1,0,
        0,0,472,474,3,139,69,0,473,468,1,0,0,0,473,470,1,0,0,0,474,475,1,
        0,0,0,475,476,6,60,1,0,476,122,1,0,0,0,477,482,5,34,0,0,478,481,
        3,141,70,0,479,481,8,3,0,0,480,478,1,0,0,0,480,479,1,0,0,0,481,484,
        1,0,0,0,482,483,1,0,0,0,482,480,1,0,0,0,483,485,1,0,0,0,484,482,
        1,0,0,0,485,486,5,34,0,0,486,487,6,61,2,0,487,124,1,0,0,0,488,489,
        5,47,0,0,489,490,5,47,0,0,490,494,1,0,0,0,491,493,9,0,0,0,492,491,
        1,0,0,0,493,496,1,0,0,0,494,495,1,0,0,0,494,492,1,0,0,0,495,498,
        1,0,0,0,496,494,1,0,0,0,497,499,5,13,0,0,498,497,1,0,0,0,498,499,
        1,0,0,0,499,500,1,0,0,0,500,501,5,10,0,0,501,502,1,0,0,0,502,503,
        6,62,3,0,503,126,1,0,0,0,504,505,5,47,0,0,505,506,5,42,0,0,506,510,
        1,0,0,0,507,509,9,0,0,0,508,507,1,0,0,0,509,512,1,0,0,0,510,511,
        1,0,0,0,510,508,1,0,0,0,511,513,1,0,0,0,512,510,1,0,0,0,513,514,
        5,42,0,0,514,515,5,47,0,0,515,516,1,0,0,0,516,517,6,63,3,0,517,128,
        1,0,0,0,518,520,7,4,0,0,519,518,1,0,0,0,520,521,1,0,0,0,521,519,
        1,0,0,0,521,522,1,0,0,0,522,523,1,0,0,0,523,524,6,64,3,0,524,130,
        1,0,0,0,525,530,5,34,0,0,526,529,8,5,0,0,527,529,3,141,70,0,528,
        526,1,0,0,0,528,527,1,0,0,0,529,532,1,0,0,0,530,528,1,0,0,0,530,
        531,1,0,0,0,531,533,1,0,0,0,532,530,1,0,0,0,533,534,6,65,4,0,534,
        132,1,0,0,0,535,540,5,34,0,0,536,539,3,141,70,0,537,539,8,3,0,0,
        538,536,1,0,0,0,538,537,1,0,0,0,539,542,1,0,0,0,540,538,1,0,0,0,
        540,541,1,0,0,0,541,543,1,0,0,0,542,540,1,0,0,0,543,544,3,145,72,
        0,544,545,6,66,5,0,545,134,1,0,0,0,546,547,9,0,0,0,547,548,6,67,
        6,0,548,136,1,0,0,0,549,551,5,46,0,0,550,552,3,143,71,0,551,550,
        1,0,0,0,552,553,1,0,0,0,553,551,1,0,0,0,553,554,1,0,0,0,554,138,
        1,0,0,0,555,557,7,6,0,0,556,558,7,7,0,0,557,556,1,0,0,0,557,558,
        1,0,0,0,558,560,1,0,0,0,559,561,7,8,0,0,560,559,1,0,0,0,561,562,
        1,0,0,0,562,560,1,0,0,0,562,563,1,0,0,0,563,140,1,0,0,0,564,565,
        5,92,0,0,565,566,7,9,0,0,566,142,1,0,0,0,567,568,7,8,0,0,568,144,
        1,0,0,0,569,570,5,92,0,0,570,571,8,9,0,0,571,146,1,0,0,0,21,0,264,
        451,453,461,465,470,473,480,482,494,498,510,521,528,530,538,540,
        553,557,562,7,1,59,0,1,60,1,1,61,2,6,0,0,1,65,3,1,66,4,1,67,5
    ]

class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    BOOLIT = 11
    AUTO = 12
    BREAK = 13
    BOOLEAN = 14
    DO = 15
    ELSE = 16
    FALSE = 17
    FLOAT = 18
    FOR = 19
    FUNCTION = 20
    IF = 21
    INTEGER = 22
    RETURN = 23
    STRING = 24
    TRUE = 25
    VOID = 26
    WHILE = 27
    OUT = 28
    CONTINUE = 29
    OF = 30
    INHERIT = 31
    ARRAY = 32
    ADDOP = 33
    SUBOP = 34
    MULOP = 35
    DIVOP = 36
    MODOP = 37
    NOT = 38
    AND = 39
    OR = 40
    NOT_EQUAL = 41
    EQUAL = 42
    LT = 43
    GT = 44
    LE = 45
    GE = 46
    CONCAT = 47
    LSB = 48
    RSB = 49
    LB = 50
    RB = 51
    LCB = 52
    RCB = 53
    COLON = 54
    SEMI = 55
    DOT = 56
    COMMA = 57
    ASSIGN = 58
    ID = 59
    INTLIT = 60
    FLOATLIT = 61
    STRINGLIT = 62
    Cpp_COMMENT = 63
    C_COMMENT = 64
    WS = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInteger'", "'printInteger'", "'readFloat'", "'writeFloat'", 
            "'readBoolean'", "'printBoolean'", "'readString'", "'printString'", 
            "'super'", "'preventDefault'", "'auto'", "'break'", "'boolean'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'integer'", "'return'", "'string'", "'true'", "'void'", 
            "'while'", "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'!='", 
            "'=='", "'<'", "'>'", "'<='", "'>='", "'::'", "'['", "']'", 
            "'('", "')'", "'{'", "'}'", "':'", "';'", "'.'", "','", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BOOLIT", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
            "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", 
            "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", 
            "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NOT", 
            "AND", "OR", "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", "CONCAT", 
            "LSB", "RSB", "LB", "RB", "LCB", "RCB", "COLON", "SEMI", "DOT", 
            "COMMA", "ASSIGN", "ID", "INTLIT", "FLOATLIT", "STRINGLIT", 
            "Cpp_COMMENT", "C_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "BOOLIT", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "VOID", "WHILE", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "MODOP", "NOT", "AND", "OR", 
                  "NOT_EQUAL", "EQUAL", "LT", "GT", "LE", "GE", "CONCAT", 
                  "LSB", "RSB", "LB", "RB", "LCB", "RCB", "COLON", "SEMI", 
                  "DOT", "COMMA", "ASSIGN", "ID", "INTLIT", "FLOATLIT", 
                  "STRINGLIT", "Cpp_COMMENT", "C_COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR", "DECPART", "EXPONENT", 
                  "Escape", "DIGIT", "NotEscape" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.INTLIT_action 
            actions[60] = self.FLOATLIT_action 
            actions[61] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[67] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = self.text.replace('_', '')

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	self.text = self.text.replace('_', '')

     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	raise UncloseString(self.text[1:-1])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(self.text[1:-1])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     



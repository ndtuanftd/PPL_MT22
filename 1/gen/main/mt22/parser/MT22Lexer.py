# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/1/src/main/mt22/parser\MT22.g4 by ANTLR 4.11.1
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
        4,0,56,445,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,
        1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,16,1,16,1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,
        1,18,1,18,1,18,1,18,1,19,1,19,1,19,5,19,241,8,19,10,19,12,19,244,
        9,19,1,19,3,19,247,8,19,1,19,1,19,1,19,3,19,252,8,19,1,19,1,19,1,
        20,1,20,3,20,258,8,20,1,20,4,20,261,8,20,11,20,12,20,262,1,21,1,
        21,1,21,3,21,268,8,21,1,21,5,21,271,8,21,10,21,12,21,274,9,21,1,
        21,3,21,277,8,21,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,
        22,288,8,22,1,23,1,23,1,23,1,23,5,23,294,8,23,10,23,12,23,297,9,
        23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,3,24,306,8,24,1,25,1,25,3,
        25,310,8,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,
        31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,1,35,1,
        35,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,
        40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,
        47,1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,1,52,1,52,1,53,1,
        53,1,54,1,54,5,54,377,8,54,10,54,12,54,380,9,54,1,55,4,55,383,8,
        55,11,55,12,55,384,1,55,1,55,1,56,1,56,1,56,1,56,5,56,393,8,56,10,
        56,12,56,396,9,56,1,56,1,56,1,56,1,56,1,56,1,57,1,57,1,57,1,57,5,
        57,407,8,57,10,57,12,57,410,9,57,1,57,1,57,1,58,1,58,1,58,1,59,1,
        59,1,59,1,59,5,59,421,8,59,10,59,12,59,424,9,59,1,59,1,59,1,60,1,
        60,5,60,430,8,60,10,60,12,60,433,9,60,1,60,1,60,5,60,437,8,60,10,
        60,12,60,440,9,60,1,60,1,60,1,61,1,61,3,394,431,438,0,62,1,1,3,2,
        5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,
        15,31,16,33,17,35,18,37,19,39,20,41,0,43,21,45,22,47,23,49,0,51,
        0,53,24,55,25,57,26,59,27,61,28,63,29,65,30,67,31,69,32,71,33,73,
        34,75,35,77,36,79,37,81,38,83,39,85,40,87,41,89,42,91,43,93,44,95,
        45,97,46,99,47,101,48,103,49,105,0,107,0,109,50,111,51,113,52,115,
        53,117,54,119,55,121,56,123,0,1,0,12,2,0,69,69,101,101,2,0,43,43,
        45,45,1,0,49,57,2,0,34,34,92,92,7,0,39,39,92,92,98,98,102,102,110,
        110,114,114,116,116,5,0,8,10,12,13,34,34,39,39,92,92,1,0,48,57,3,
        0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,
        32,32,2,0,10,10,13,13,8,0,34,34,39,39,92,92,98,98,102,102,110,110,
        114,114,116,116,459,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,
        0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,
        0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,
        0,0,0,39,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,53,1,0,
        0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,
        0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,
        0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,
        0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,
        0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,
        0,0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,
        117,1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,1,125,1,0,0,0,3,130,1,0,
        0,0,5,136,1,0,0,0,7,144,1,0,0,0,9,147,1,0,0,0,11,153,1,0,0,0,13,
        158,1,0,0,0,15,162,1,0,0,0,17,171,1,0,0,0,19,174,1,0,0,0,21,182,
        1,0,0,0,23,189,1,0,0,0,25,196,1,0,0,0,27,202,1,0,0,0,29,207,1,0,
        0,0,31,211,1,0,0,0,33,220,1,0,0,0,35,223,1,0,0,0,37,231,1,0,0,0,
        39,251,1,0,0,0,41,255,1,0,0,0,43,276,1,0,0,0,45,287,1,0,0,0,47,289,
        1,0,0,0,49,305,1,0,0,0,51,309,1,0,0,0,53,311,1,0,0,0,55,313,1,0,
        0,0,57,315,1,0,0,0,59,317,1,0,0,0,61,319,1,0,0,0,63,321,1,0,0,0,
        65,323,1,0,0,0,67,326,1,0,0,0,69,329,1,0,0,0,71,332,1,0,0,0,73,335,
        1,0,0,0,75,337,1,0,0,0,77,340,1,0,0,0,79,342,1,0,0,0,81,345,1,0,
        0,0,83,348,1,0,0,0,85,350,1,0,0,0,87,352,1,0,0,0,89,354,1,0,0,0,
        91,356,1,0,0,0,93,358,1,0,0,0,95,360,1,0,0,0,97,362,1,0,0,0,99,364,
        1,0,0,0,101,366,1,0,0,0,103,368,1,0,0,0,105,370,1,0,0,0,107,372,
        1,0,0,0,109,374,1,0,0,0,111,382,1,0,0,0,113,388,1,0,0,0,115,402,
        1,0,0,0,117,413,1,0,0,0,119,416,1,0,0,0,121,427,1,0,0,0,123,443,
        1,0,0,0,125,126,5,97,0,0,126,127,5,117,0,0,127,128,5,116,0,0,128,
        129,5,111,0,0,129,2,1,0,0,0,130,131,5,98,0,0,131,132,5,114,0,0,132,
        133,5,101,0,0,133,134,5,97,0,0,134,135,5,107,0,0,135,4,1,0,0,0,136,
        137,5,98,0,0,137,138,5,111,0,0,138,139,5,111,0,0,139,140,5,108,0,
        0,140,141,5,101,0,0,141,142,5,97,0,0,142,143,5,110,0,0,143,6,1,0,
        0,0,144,145,5,100,0,0,145,146,5,111,0,0,146,8,1,0,0,0,147,148,5,
        102,0,0,148,149,5,108,0,0,149,150,5,111,0,0,150,151,5,97,0,0,151,
        152,5,116,0,0,152,10,1,0,0,0,153,154,5,101,0,0,154,155,5,108,0,0,
        155,156,5,115,0,0,156,157,5,101,0,0,157,12,1,0,0,0,158,159,5,102,
        0,0,159,160,5,111,0,0,160,161,5,114,0,0,161,14,1,0,0,0,162,163,5,
        102,0,0,163,164,5,117,0,0,164,165,5,110,0,0,165,166,5,99,0,0,166,
        167,5,116,0,0,167,168,5,105,0,0,168,169,5,111,0,0,169,170,5,110,
        0,0,170,16,1,0,0,0,171,172,5,105,0,0,172,173,5,102,0,0,173,18,1,
        0,0,0,174,175,5,105,0,0,175,176,5,110,0,0,176,177,5,116,0,0,177,
        178,5,101,0,0,178,179,5,103,0,0,179,180,5,101,0,0,180,181,5,114,
        0,0,181,20,1,0,0,0,182,183,5,114,0,0,183,184,5,101,0,0,184,185,5,
        116,0,0,185,186,5,117,0,0,186,187,5,114,0,0,187,188,5,110,0,0,188,
        22,1,0,0,0,189,190,5,115,0,0,190,191,5,116,0,0,191,192,5,114,0,0,
        192,193,5,105,0,0,193,194,5,110,0,0,194,195,5,103,0,0,195,24,1,0,
        0,0,196,197,5,119,0,0,197,198,5,104,0,0,198,199,5,105,0,0,199,200,
        5,108,0,0,200,201,5,101,0,0,201,26,1,0,0,0,202,203,5,118,0,0,203,
        204,5,111,0,0,204,205,5,105,0,0,205,206,5,100,0,0,206,28,1,0,0,0,
        207,208,5,111,0,0,208,209,5,117,0,0,209,210,5,116,0,0,210,30,1,0,
        0,0,211,212,5,99,0,0,212,213,5,111,0,0,213,214,5,110,0,0,214,215,
        5,116,0,0,215,216,5,105,0,0,216,217,5,110,0,0,217,218,5,117,0,0,
        218,219,5,101,0,0,219,32,1,0,0,0,220,221,5,111,0,0,221,222,5,102,
        0,0,222,34,1,0,0,0,223,224,5,105,0,0,224,225,5,110,0,0,225,226,5,
        104,0,0,226,227,5,101,0,0,227,228,5,114,0,0,228,229,5,105,0,0,229,
        230,5,116,0,0,230,36,1,0,0,0,231,232,5,97,0,0,232,233,5,114,0,0,
        233,234,5,114,0,0,234,235,5,97,0,0,235,236,5,121,0,0,236,38,1,0,
        0,0,237,238,3,43,21,0,238,242,3,95,47,0,239,241,3,105,52,0,240,239,
        1,0,0,0,241,244,1,0,0,0,242,240,1,0,0,0,242,243,1,0,0,0,243,246,
        1,0,0,0,244,242,1,0,0,0,245,247,3,41,20,0,246,245,1,0,0,0,246,247,
        1,0,0,0,247,252,1,0,0,0,248,249,3,43,21,0,249,250,3,41,20,0,250,
        252,1,0,0,0,251,237,1,0,0,0,251,248,1,0,0,0,252,253,1,0,0,0,253,
        254,6,19,0,0,254,40,1,0,0,0,255,257,7,0,0,0,256,258,7,1,0,0,257,
        256,1,0,0,0,257,258,1,0,0,0,258,260,1,0,0,0,259,261,3,105,52,0,260,
        259,1,0,0,0,261,262,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,
        42,1,0,0,0,264,277,3,107,53,0,265,272,7,2,0,0,266,268,5,95,0,0,267,
        266,1,0,0,0,267,268,1,0,0,0,268,269,1,0,0,0,269,271,3,105,52,0,270,
        267,1,0,0,0,271,274,1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,
        275,1,0,0,0,274,272,1,0,0,0,275,277,6,21,1,0,276,264,1,0,0,0,276,
        265,1,0,0,0,277,44,1,0,0,0,278,279,5,116,0,0,279,280,5,114,0,0,280,
        281,5,117,0,0,281,288,5,101,0,0,282,283,5,102,0,0,283,284,5,97,0,
        0,284,285,5,108,0,0,285,286,5,115,0,0,286,288,5,101,0,0,287,278,
        1,0,0,0,287,282,1,0,0,0,288,46,1,0,0,0,289,295,5,34,0,0,290,291,
        5,92,0,0,291,294,9,0,0,0,292,294,8,3,0,0,293,290,1,0,0,0,293,292,
        1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,298,
        1,0,0,0,297,295,1,0,0,0,298,299,5,34,0,0,299,300,6,23,2,0,300,48,
        1,0,0,0,301,302,5,92,0,0,302,306,7,4,0,0,303,304,5,39,0,0,304,306,
        5,34,0,0,305,301,1,0,0,0,305,303,1,0,0,0,306,50,1,0,0,0,307,310,
        8,5,0,0,308,310,3,49,24,0,309,307,1,0,0,0,309,308,1,0,0,0,310,52,
        1,0,0,0,311,312,5,43,0,0,312,54,1,0,0,0,313,314,5,45,0,0,314,56,
        1,0,0,0,315,316,5,42,0,0,316,58,1,0,0,0,317,318,5,47,0,0,318,60,
        1,0,0,0,319,320,5,37,0,0,320,62,1,0,0,0,321,322,5,33,0,0,322,64,
        1,0,0,0,323,324,5,38,0,0,324,325,5,38,0,0,325,66,1,0,0,0,326,327,
        5,124,0,0,327,328,5,124,0,0,328,68,1,0,0,0,329,330,5,61,0,0,330,
        331,5,61,0,0,331,70,1,0,0,0,332,333,5,33,0,0,333,334,5,61,0,0,334,
        72,1,0,0,0,335,336,5,60,0,0,336,74,1,0,0,0,337,338,5,60,0,0,338,
        339,5,61,0,0,339,76,1,0,0,0,340,341,5,62,0,0,341,78,1,0,0,0,342,
        343,5,62,0,0,343,344,5,61,0,0,344,80,1,0,0,0,345,346,5,58,0,0,346,
        347,5,58,0,0,347,82,1,0,0,0,348,349,5,40,0,0,349,84,1,0,0,0,350,
        351,5,41,0,0,351,86,1,0,0,0,352,353,5,91,0,0,353,88,1,0,0,0,354,
        355,5,93,0,0,355,90,1,0,0,0,356,357,5,123,0,0,357,92,1,0,0,0,358,
        359,5,125,0,0,359,94,1,0,0,0,360,361,5,46,0,0,361,96,1,0,0,0,362,
        363,5,44,0,0,363,98,1,0,0,0,364,365,5,59,0,0,365,100,1,0,0,0,366,
        367,5,58,0,0,367,102,1,0,0,0,368,369,5,61,0,0,369,104,1,0,0,0,370,
        371,7,6,0,0,371,106,1,0,0,0,372,373,5,48,0,0,373,108,1,0,0,0,374,
        378,7,7,0,0,375,377,7,8,0,0,376,375,1,0,0,0,377,380,1,0,0,0,378,
        376,1,0,0,0,378,379,1,0,0,0,379,110,1,0,0,0,380,378,1,0,0,0,381,
        383,7,9,0,0,382,381,1,0,0,0,383,384,1,0,0,0,384,382,1,0,0,0,384,
        385,1,0,0,0,385,386,1,0,0,0,386,387,6,55,3,0,387,112,1,0,0,0,388,
        389,5,47,0,0,389,390,5,42,0,0,390,394,1,0,0,0,391,393,9,0,0,0,392,
        391,1,0,0,0,393,396,1,0,0,0,394,395,1,0,0,0,394,392,1,0,0,0,395,
        397,1,0,0,0,396,394,1,0,0,0,397,398,5,42,0,0,398,399,5,47,0,0,399,
        400,1,0,0,0,400,401,6,56,3,0,401,114,1,0,0,0,402,403,5,47,0,0,403,
        404,5,47,0,0,404,408,1,0,0,0,405,407,8,10,0,0,406,405,1,0,0,0,407,
        410,1,0,0,0,408,406,1,0,0,0,408,409,1,0,0,0,409,411,1,0,0,0,410,
        408,1,0,0,0,411,412,6,57,3,0,412,116,1,0,0,0,413,414,9,0,0,0,414,
        415,6,58,4,0,415,118,1,0,0,0,416,422,5,34,0,0,417,418,5,92,0,0,418,
        421,7,11,0,0,419,421,8,5,0,0,420,417,1,0,0,0,420,419,1,0,0,0,421,
        424,1,0,0,0,422,420,1,0,0,0,422,423,1,0,0,0,423,425,1,0,0,0,424,
        422,1,0,0,0,425,426,6,59,5,0,426,120,1,0,0,0,427,431,5,34,0,0,428,
        430,9,0,0,0,429,428,1,0,0,0,430,433,1,0,0,0,431,432,1,0,0,0,431,
        429,1,0,0,0,432,434,1,0,0,0,433,431,1,0,0,0,434,438,3,123,61,0,435,
        437,9,0,0,0,436,435,1,0,0,0,437,440,1,0,0,0,438,439,1,0,0,0,438,
        436,1,0,0,0,439,441,1,0,0,0,440,438,1,0,0,0,441,442,6,60,6,0,442,
        122,1,0,0,0,443,444,7,5,0,0,444,124,1,0,0,0,22,0,242,246,251,257,
        262,267,272,276,287,293,295,305,309,378,384,394,408,420,422,431,
        438,7,1,19,0,1,21,1,1,23,2,6,0,0,1,58,3,1,59,4,1,60,5
    ]

class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTO = 1
    BREAK = 2
    BOOLEAN = 3
    DO = 4
    FLOAT = 5
    ELSE = 6
    FOR = 7
    FUNCTION = 8
    IF = 9
    INT = 10
    RETURN = 11
    STRING = 12
    WHILE = 13
    VOID = 14
    OUT = 15
    CONTINUE = 16
    OF = 17
    INHERIT = 18
    ARRAY = 19
    FLOATLIT = 20
    INTLIT = 21
    BOOLLIT = 22
    STRINGLIT = 23
    ADDOP = 24
    SUBOP = 25
    MULOP = 26
    DIVOP = 27
    MODOP = 28
    NEGOP = 29
    ANDOP = 30
    OROP = 31
    EQOP = 32
    NEQOP = 33
    LTOP = 34
    LEOP = 35
    GTOP = 36
    GEOP = 37
    STRINGCONCAT = 38
    LB = 39
    RB = 40
    LSB = 41
    RSB = 42
    LCB = 43
    RCB = 44
    DOT = 45
    COMMA = 46
    SM = 47
    COLON = 48
    ASSIGN = 49
    ID = 50
    WS = 51
    BLOCKCOMMENT = 52
    LINECOMMENT = 53
    ERROR_CHAR = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'float'", "'else'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", 
            "':'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "FLOAT", "ELSE", "FOR", "FUNCTION", 
            "IF", "INT", "RETURN", "STRING", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "FLOATLIT", "INTLIT", "BOOLLIT", "STRINGLIT", 
            "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", "NEGOP", "ANDOP", 
            "OROP", "EQOP", "NEQOP", "LTOP", "LEOP", "GTOP", "GEOP", "STRINGCONCAT", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "SM", 
            "COLON", "ASSIGN", "ID", "WS", "BLOCKCOMMENT", "LINECOMMENT", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "FLOAT", "ELSE", "FOR", 
                  "FUNCTION", "IF", "INT", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "FLOATLIT", 
                  "EXPORNENT", "INTLIT", "BOOLLIT", "STRINGLIT", "ESC_SEQ", 
                  "SUB_STRING", "ADDOP", "SUBOP", "MULOP", "DIVOP", "MODOP", 
                  "NEGOP", "ANDOP", "OROP", "EQOP", "NEQOP", "LTOP", "LEOP", 
                  "GTOP", "GEOP", "STRINGCONCAT", "LB", "RB", "LSB", "RSB", 
                  "LCB", "RCB", "DOT", "COMMA", "SM", "COLON", "ASSIGN", 
                  "DIGIT", "ZERO", "ID", "WS", "BLOCKCOMMENT", "LINECOMMENT", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESCAPE" ]

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
            actions[19] = self.FLOATLIT_action 
            actions[21] = self.INTLIT_action 
            actions[23] = self.STRINGLIT_action 
            actions[58] = self.ERROR_CHAR_action 
            actions[59] = self.UNCLOSE_STRING_action 
            actions[60] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    self.text = self.text.replace('_', '')
                
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    self.text = self.text.replace('_', '')
                
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    self.text = self.text[1:-1]
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

                    self.text = self.text[1:]
                    raise UncloseString(self.text)
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

                    self.text = self.text[1:]
                    raise IllegalEscape(self.text)
                
     


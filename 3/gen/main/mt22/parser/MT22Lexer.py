# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/3/src/main/mt22/parser\MT22.g4 by ANTLR 4.11.1
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
        4,0,67,594,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
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
        71,2,72,7,72,2,73,7,73,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,
        18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,24,1,
        24,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,
        29,1,29,1,30,1,30,1,30,1,31,1,31,1,32,1,32,1,32,1,33,1,33,1,33,1,
        34,1,34,1,35,1,35,1,36,1,36,1,37,1,37,1,38,1,38,1,39,1,39,1,40,1,
        40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,1,44,1,45,1,45,1,46,1,46,1,
        46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,
        47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,
        48,1,48,1,48,1,48,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,49,1,49,1,
        49,1,49,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,50,1,
        50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,
        51,1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,
        52,1,52,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,
        53,1,54,1,54,1,54,1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,
        55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,1,56,1,
        56,1,56,1,56,1,56,1,56,3,56,447,8,56,1,57,1,57,1,58,1,58,1,59,1,
        59,1,59,3,59,456,8,59,1,59,5,59,459,8,59,10,59,12,59,462,9,59,1,
        59,3,59,465,8,59,1,60,1,60,5,60,469,8,60,10,60,12,60,472,9,60,1,
        61,1,61,3,61,476,8,61,1,61,1,61,1,62,1,62,1,62,5,62,483,8,62,10,
        62,12,62,486,9,62,1,62,3,62,489,8,62,1,62,1,62,5,62,493,8,62,10,
        62,12,62,496,9,62,1,62,3,62,499,8,62,1,62,1,62,1,62,3,62,504,8,62,
        1,62,1,62,1,63,1,63,1,63,1,64,1,64,1,64,5,64,514,8,64,10,64,12,64,
        517,9,64,1,65,1,65,1,65,1,65,1,65,1,66,1,66,5,66,526,8,66,10,66,
        12,66,529,9,66,1,67,4,67,532,8,67,11,67,12,67,533,1,67,1,67,1,68,
        1,68,1,68,1,68,5,68,542,8,68,10,68,12,68,545,9,68,1,68,1,68,1,68,
        1,68,1,68,1,69,1,69,1,69,1,69,5,69,556,8,69,10,69,12,69,559,9,69,
        1,69,1,69,1,70,1,70,1,70,1,71,1,71,1,71,1,71,5,71,570,8,71,10,71,
        12,71,573,9,71,1,71,1,71,1,72,1,72,5,72,579,8,72,10,72,12,72,582,
        9,72,1,72,1,72,5,72,586,8,72,10,72,12,72,589,9,72,1,72,1,72,1,73,
        1,73,3,543,580,587,0,74,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,
        19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,
        41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,
        63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,81,41,83,42,
        85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,51,103,52,105,
        53,107,54,109,55,111,56,113,57,115,0,117,0,119,58,121,0,123,0,125,
        59,127,0,129,0,131,60,133,61,135,62,137,63,139,64,141,65,143,66,
        145,67,147,0,1,0,11,1,0,48,57,1,0,49,57,2,0,69,69,101,101,2,0,43,
        43,45,45,8,0,34,34,39,39,92,92,98,98,102,102,110,110,114,114,116,
        116,2,0,34,34,92,92,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,
        97,122,3,0,9,10,13,13,32,32,2,0,10,10,13,13,5,0,8,10,12,13,34,34,
        39,39,92,92,608,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,
        0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,
        0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,
        0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,
        0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,
        0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,
        0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,
        0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,
        0,79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,
        0,89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,
        0,99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,
        0,0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,119,1,0,0,0,0,125,
        1,0,0,0,0,131,1,0,0,0,0,133,1,0,0,0,0,135,1,0,0,0,0,137,1,0,0,0,
        0,139,1,0,0,0,0,141,1,0,0,0,0,143,1,0,0,0,0,145,1,0,0,0,1,149,1,
        0,0,0,3,154,1,0,0,0,5,160,1,0,0,0,7,168,1,0,0,0,9,171,1,0,0,0,11,
        177,1,0,0,0,13,182,1,0,0,0,15,186,1,0,0,0,17,195,1,0,0,0,19,198,
        1,0,0,0,21,206,1,0,0,0,23,213,1,0,0,0,25,220,1,0,0,0,27,226,1,0,
        0,0,29,231,1,0,0,0,31,235,1,0,0,0,33,244,1,0,0,0,35,247,1,0,0,0,
        37,255,1,0,0,0,39,261,1,0,0,0,41,263,1,0,0,0,43,265,1,0,0,0,45,267,
        1,0,0,0,47,269,1,0,0,0,49,271,1,0,0,0,51,273,1,0,0,0,53,276,1,0,
        0,0,55,279,1,0,0,0,57,282,1,0,0,0,59,285,1,0,0,0,61,287,1,0,0,0,
        63,290,1,0,0,0,65,292,1,0,0,0,67,295,1,0,0,0,69,298,1,0,0,0,71,300,
        1,0,0,0,73,302,1,0,0,0,75,304,1,0,0,0,77,306,1,0,0,0,79,308,1,0,
        0,0,81,310,1,0,0,0,83,312,1,0,0,0,85,314,1,0,0,0,87,316,1,0,0,0,
        89,318,1,0,0,0,91,320,1,0,0,0,93,322,1,0,0,0,95,334,1,0,0,0,97,347,
        1,0,0,0,99,357,1,0,0,0,101,368,1,0,0,0,103,380,1,0,0,0,105,393,1,
        0,0,0,107,404,1,0,0,0,109,416,1,0,0,0,111,422,1,0,0,0,113,446,1,
        0,0,0,115,448,1,0,0,0,117,450,1,0,0,0,119,464,1,0,0,0,121,466,1,
        0,0,0,123,473,1,0,0,0,125,503,1,0,0,0,127,507,1,0,0,0,129,515,1,
        0,0,0,131,518,1,0,0,0,133,523,1,0,0,0,135,531,1,0,0,0,137,537,1,
        0,0,0,139,551,1,0,0,0,141,562,1,0,0,0,143,565,1,0,0,0,145,576,1,
        0,0,0,147,592,1,0,0,0,149,150,5,97,0,0,150,151,5,117,0,0,151,152,
        5,116,0,0,152,153,5,111,0,0,153,2,1,0,0,0,154,155,5,98,0,0,155,156,
        5,114,0,0,156,157,5,101,0,0,157,158,5,97,0,0,158,159,5,107,0,0,159,
        4,1,0,0,0,160,161,5,98,0,0,161,162,5,111,0,0,162,163,5,111,0,0,163,
        164,5,108,0,0,164,165,5,101,0,0,165,166,5,97,0,0,166,167,5,110,0,
        0,167,6,1,0,0,0,168,169,5,100,0,0,169,170,5,111,0,0,170,8,1,0,0,
        0,171,172,5,102,0,0,172,173,5,108,0,0,173,174,5,111,0,0,174,175,
        5,97,0,0,175,176,5,116,0,0,176,10,1,0,0,0,177,178,5,101,0,0,178,
        179,5,108,0,0,179,180,5,115,0,0,180,181,5,101,0,0,181,12,1,0,0,0,
        182,183,5,102,0,0,183,184,5,111,0,0,184,185,5,114,0,0,185,14,1,0,
        0,0,186,187,5,102,0,0,187,188,5,117,0,0,188,189,5,110,0,0,189,190,
        5,99,0,0,190,191,5,116,0,0,191,192,5,105,0,0,192,193,5,111,0,0,193,
        194,5,110,0,0,194,16,1,0,0,0,195,196,5,105,0,0,196,197,5,102,0,0,
        197,18,1,0,0,0,198,199,5,105,0,0,199,200,5,110,0,0,200,201,5,116,
        0,0,201,202,5,101,0,0,202,203,5,103,0,0,203,204,5,101,0,0,204,205,
        5,114,0,0,205,20,1,0,0,0,206,207,5,114,0,0,207,208,5,101,0,0,208,
        209,5,116,0,0,209,210,5,117,0,0,210,211,5,114,0,0,211,212,5,110,
        0,0,212,22,1,0,0,0,213,214,5,115,0,0,214,215,5,116,0,0,215,216,5,
        114,0,0,216,217,5,105,0,0,217,218,5,110,0,0,218,219,5,103,0,0,219,
        24,1,0,0,0,220,221,5,119,0,0,221,222,5,104,0,0,222,223,5,105,0,0,
        223,224,5,108,0,0,224,225,5,101,0,0,225,26,1,0,0,0,226,227,5,118,
        0,0,227,228,5,111,0,0,228,229,5,105,0,0,229,230,5,100,0,0,230,28,
        1,0,0,0,231,232,5,111,0,0,232,233,5,117,0,0,233,234,5,116,0,0,234,
        30,1,0,0,0,235,236,5,99,0,0,236,237,5,111,0,0,237,238,5,110,0,0,
        238,239,5,116,0,0,239,240,5,105,0,0,240,241,5,110,0,0,241,242,5,
        117,0,0,242,243,5,101,0,0,243,32,1,0,0,0,244,245,5,111,0,0,245,246,
        5,102,0,0,246,34,1,0,0,0,247,248,5,105,0,0,248,249,5,110,0,0,249,
        250,5,104,0,0,250,251,5,101,0,0,251,252,5,114,0,0,252,253,5,105,
        0,0,253,254,5,116,0,0,254,36,1,0,0,0,255,256,5,97,0,0,256,257,5,
        114,0,0,257,258,5,114,0,0,258,259,5,97,0,0,259,260,5,121,0,0,260,
        38,1,0,0,0,261,262,5,43,0,0,262,40,1,0,0,0,263,264,5,45,0,0,264,
        42,1,0,0,0,265,266,5,42,0,0,266,44,1,0,0,0,267,268,5,47,0,0,268,
        46,1,0,0,0,269,270,5,37,0,0,270,48,1,0,0,0,271,272,5,33,0,0,272,
        50,1,0,0,0,273,274,5,38,0,0,274,275,5,38,0,0,275,52,1,0,0,0,276,
        277,5,124,0,0,277,278,5,124,0,0,278,54,1,0,0,0,279,280,5,61,0,0,
        280,281,5,61,0,0,281,56,1,0,0,0,282,283,5,33,0,0,283,284,5,61,0,
        0,284,58,1,0,0,0,285,286,5,60,0,0,286,60,1,0,0,0,287,288,5,60,0,
        0,288,289,5,61,0,0,289,62,1,0,0,0,290,291,5,62,0,0,291,64,1,0,0,
        0,292,293,5,62,0,0,293,294,5,61,0,0,294,66,1,0,0,0,295,296,5,58,
        0,0,296,297,5,58,0,0,297,68,1,0,0,0,298,299,5,40,0,0,299,70,1,0,
        0,0,300,301,5,41,0,0,301,72,1,0,0,0,302,303,5,91,0,0,303,74,1,0,
        0,0,304,305,5,93,0,0,305,76,1,0,0,0,306,307,5,123,0,0,307,78,1,0,
        0,0,308,309,5,125,0,0,309,80,1,0,0,0,310,311,5,46,0,0,311,82,1,0,
        0,0,312,313,5,44,0,0,313,84,1,0,0,0,314,315,5,59,0,0,315,86,1,0,
        0,0,316,317,5,58,0,0,317,88,1,0,0,0,318,319,5,61,0,0,319,90,1,0,
        0,0,320,321,5,34,0,0,321,92,1,0,0,0,322,323,5,114,0,0,323,324,5,
        101,0,0,324,325,5,97,0,0,325,326,5,100,0,0,326,327,5,73,0,0,327,
        328,5,110,0,0,328,329,5,116,0,0,329,330,5,101,0,0,330,331,5,103,
        0,0,331,332,5,101,0,0,332,333,5,114,0,0,333,94,1,0,0,0,334,335,5,
        112,0,0,335,336,5,114,0,0,336,337,5,105,0,0,337,338,5,110,0,0,338,
        339,5,116,0,0,339,340,5,73,0,0,340,341,5,110,0,0,341,342,5,116,0,
        0,342,343,5,101,0,0,343,344,5,103,0,0,344,345,5,101,0,0,345,346,
        5,114,0,0,346,96,1,0,0,0,347,348,5,114,0,0,348,349,5,101,0,0,349,
        350,5,97,0,0,350,351,5,100,0,0,351,352,5,70,0,0,352,353,5,108,0,
        0,353,354,5,111,0,0,354,355,5,97,0,0,355,356,5,116,0,0,356,98,1,
        0,0,0,357,358,5,119,0,0,358,359,5,114,0,0,359,360,5,105,0,0,360,
        361,5,116,0,0,361,362,5,101,0,0,362,363,5,70,0,0,363,364,5,108,0,
        0,364,365,5,111,0,0,365,366,5,97,0,0,366,367,5,116,0,0,367,100,1,
        0,0,0,368,369,5,114,0,0,369,370,5,101,0,0,370,371,5,97,0,0,371,372,
        5,100,0,0,372,373,5,66,0,0,373,374,5,111,0,0,374,375,5,111,0,0,375,
        376,5,108,0,0,376,377,5,101,0,0,377,378,5,97,0,0,378,379,5,110,0,
        0,379,102,1,0,0,0,380,381,5,112,0,0,381,382,5,114,0,0,382,383,5,
        105,0,0,383,384,5,110,0,0,384,385,5,116,0,0,385,386,5,66,0,0,386,
        387,5,111,0,0,387,388,5,111,0,0,388,389,5,108,0,0,389,390,5,101,
        0,0,390,391,5,97,0,0,391,392,5,110,0,0,392,104,1,0,0,0,393,394,5,
        114,0,0,394,395,5,101,0,0,395,396,5,97,0,0,396,397,5,100,0,0,397,
        398,5,83,0,0,398,399,5,116,0,0,399,400,5,114,0,0,400,401,5,105,0,
        0,401,402,5,110,0,0,402,403,5,103,0,0,403,106,1,0,0,0,404,405,5,
        112,0,0,405,406,5,114,0,0,406,407,5,105,0,0,407,408,5,110,0,0,408,
        409,5,116,0,0,409,410,5,83,0,0,410,411,5,116,0,0,411,412,5,114,0,
        0,412,413,5,105,0,0,413,414,5,110,0,0,414,415,5,103,0,0,415,108,
        1,0,0,0,416,417,5,115,0,0,417,418,5,117,0,0,418,419,5,112,0,0,419,
        420,5,101,0,0,420,421,5,114,0,0,421,110,1,0,0,0,422,423,5,112,0,
        0,423,424,5,114,0,0,424,425,5,101,0,0,425,426,5,118,0,0,426,427,
        5,101,0,0,427,428,5,110,0,0,428,429,5,116,0,0,429,430,5,68,0,0,430,
        431,5,101,0,0,431,432,5,102,0,0,432,433,5,97,0,0,433,434,5,117,0,
        0,434,435,5,108,0,0,435,436,5,116,0,0,436,112,1,0,0,0,437,438,5,
        116,0,0,438,439,5,114,0,0,439,440,5,117,0,0,440,447,5,101,0,0,441,
        442,5,102,0,0,442,443,5,97,0,0,443,444,5,108,0,0,444,445,5,115,0,
        0,445,447,5,101,0,0,446,437,1,0,0,0,446,441,1,0,0,0,447,114,1,0,
        0,0,448,449,7,0,0,0,449,116,1,0,0,0,450,451,5,48,0,0,451,118,1,0,
        0,0,452,465,3,117,58,0,453,460,7,1,0,0,454,456,5,95,0,0,455,454,
        1,0,0,0,455,456,1,0,0,0,456,457,1,0,0,0,457,459,3,115,57,0,458,455,
        1,0,0,0,459,462,1,0,0,0,460,458,1,0,0,0,460,461,1,0,0,0,461,463,
        1,0,0,0,462,460,1,0,0,0,463,465,6,59,0,0,464,452,1,0,0,0,464,453,
        1,0,0,0,465,120,1,0,0,0,466,470,3,81,40,0,467,469,3,115,57,0,468,
        467,1,0,0,0,469,472,1,0,0,0,470,468,1,0,0,0,470,471,1,0,0,0,471,
        122,1,0,0,0,472,470,1,0,0,0,473,475,7,2,0,0,474,476,7,3,0,0,475,
        474,1,0,0,0,475,476,1,0,0,0,476,477,1,0,0,0,477,478,3,119,59,0,478,
        124,1,0,0,0,479,480,3,119,59,0,480,484,3,81,40,0,481,483,3,115,57,
        0,482,481,1,0,0,0,483,486,1,0,0,0,484,482,1,0,0,0,484,485,1,0,0,
        0,485,488,1,0,0,0,486,484,1,0,0,0,487,489,3,123,61,0,488,487,1,0,
        0,0,488,489,1,0,0,0,489,504,1,0,0,0,490,494,3,81,40,0,491,493,3,
        115,57,0,492,491,1,0,0,0,493,496,1,0,0,0,494,492,1,0,0,0,494,495,
        1,0,0,0,495,498,1,0,0,0,496,494,1,0,0,0,497,499,3,123,61,0,498,497,
        1,0,0,0,498,499,1,0,0,0,499,504,1,0,0,0,500,501,3,119,59,0,501,502,
        3,123,61,0,502,504,1,0,0,0,503,479,1,0,0,0,503,490,1,0,0,0,503,500,
        1,0,0,0,504,505,1,0,0,0,505,506,6,62,1,0,506,126,1,0,0,0,507,508,
        5,92,0,0,508,509,7,4,0,0,509,128,1,0,0,0,510,511,5,92,0,0,511,514,
        7,4,0,0,512,514,8,5,0,0,513,510,1,0,0,0,513,512,1,0,0,0,514,517,
        1,0,0,0,515,513,1,0,0,0,515,516,1,0,0,0,516,130,1,0,0,0,517,515,
        1,0,0,0,518,519,3,91,45,0,519,520,3,129,64,0,520,521,3,91,45,0,521,
        522,6,65,2,0,522,132,1,0,0,0,523,527,7,6,0,0,524,526,7,7,0,0,525,
        524,1,0,0,0,526,529,1,0,0,0,527,525,1,0,0,0,527,528,1,0,0,0,528,
        134,1,0,0,0,529,527,1,0,0,0,530,532,7,8,0,0,531,530,1,0,0,0,532,
        533,1,0,0,0,533,531,1,0,0,0,533,534,1,0,0,0,534,535,1,0,0,0,535,
        536,6,67,3,0,536,136,1,0,0,0,537,538,5,47,0,0,538,539,5,42,0,0,539,
        543,1,0,0,0,540,542,9,0,0,0,541,540,1,0,0,0,542,545,1,0,0,0,543,
        544,1,0,0,0,543,541,1,0,0,0,544,546,1,0,0,0,545,543,1,0,0,0,546,
        547,5,42,0,0,547,548,5,47,0,0,548,549,1,0,0,0,549,550,6,68,3,0,550,
        138,1,0,0,0,551,552,5,47,0,0,552,553,5,47,0,0,553,557,1,0,0,0,554,
        556,8,9,0,0,555,554,1,0,0,0,556,559,1,0,0,0,557,555,1,0,0,0,557,
        558,1,0,0,0,558,560,1,0,0,0,559,557,1,0,0,0,560,561,6,69,3,0,561,
        140,1,0,0,0,562,563,9,0,0,0,563,564,6,70,4,0,564,142,1,0,0,0,565,
        571,5,34,0,0,566,567,5,92,0,0,567,570,7,4,0,0,568,570,8,10,0,0,569,
        566,1,0,0,0,569,568,1,0,0,0,570,573,1,0,0,0,571,569,1,0,0,0,571,
        572,1,0,0,0,572,574,1,0,0,0,573,571,1,0,0,0,574,575,6,71,5,0,575,
        144,1,0,0,0,576,580,5,34,0,0,577,579,9,0,0,0,578,577,1,0,0,0,579,
        582,1,0,0,0,580,581,1,0,0,0,580,578,1,0,0,0,581,583,1,0,0,0,582,
        580,1,0,0,0,583,587,3,147,73,0,584,586,9,0,0,0,585,584,1,0,0,0,586,
        589,1,0,0,0,587,588,1,0,0,0,587,585,1,0,0,0,588,590,1,0,0,0,589,
        587,1,0,0,0,590,591,6,72,6,0,591,146,1,0,0,0,592,593,7,10,0,0,593,
        148,1,0,0,0,22,0,446,455,460,464,470,475,484,488,494,498,503,513,
        515,527,533,543,557,569,571,580,587,7,1,59,0,1,62,1,1,65,2,6,0,0,
        1,70,3,1,71,4,1,72,5
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
    ADDOP = 20
    SUBOP = 21
    MULOP = 22
    DIVOP = 23
    MODOP = 24
    NEGOP = 25
    ANDOP = 26
    OROP = 27
    EQOP = 28
    NEQOP = 29
    LTOP = 30
    LEOP = 31
    GTOP = 32
    GEOP = 33
    STRINGCONCAT = 34
    LB = 35
    RB = 36
    LSB = 37
    RSB = 38
    LCB = 39
    RCB = 40
    DOT = 41
    COMMA = 42
    SM = 43
    COLON = 44
    ASSIGN = 45
    DOUBLEQUOTE = 46
    READ_INTEGER = 47
    PRINT_INTEGER = 48
    READ_FLOAT = 49
    WRITE_FLOAT = 50
    READ_BOOLEAN = 51
    PRINT_BOOLEAN = 52
    READ_STRING = 53
    PRINT_STRING = 54
    SUPER = 55
    PREVENT_DEFAULT = 56
    BOOLLIT = 57
    INTLIT = 58
    FLOATLIT = 59
    STRINGLIT = 60
    ID = 61
    WS = 62
    BLOCKCOMMENT = 63
    LINECOMMENT = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'float'", "'else'", 
            "'for'", "'function'", "'if'", "'integer'", "'return'", "'string'", 
            "'while'", "'void'", "'out'", "'continue'", "'of'", "'inherit'", 
            "'array'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", 
            "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "';'", 
            "':'", "'='", "'\"'", "'readInteger'", "'printInteger'", "'readFloat'", 
            "'writeFloat'", "'readBoolean'", "'printBoolean'", "'readString'", 
            "'printString'", "'super'", "'preventDefault'" ]

    symbolicNames = [ "<INVALID>",
            "AUTO", "BREAK", "BOOLEAN", "DO", "FLOAT", "ELSE", "FOR", "FUNCTION", 
            "IF", "INT", "RETURN", "STRING", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "ADDOP", "SUBOP", "MULOP", "DIVOP", 
            "MODOP", "NEGOP", "ANDOP", "OROP", "EQOP", "NEQOP", "LTOP", 
            "LEOP", "GTOP", "GEOP", "STRINGCONCAT", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "DOT", "COMMA", "SM", "COLON", "ASSIGN", "DOUBLEQUOTE", 
            "READ_INTEGER", "PRINT_INTEGER", "READ_FLOAT", "WRITE_FLOAT", 
            "READ_BOOLEAN", "PRINT_BOOLEAN", "READ_STRING", "PRINT_STRING", 
            "SUPER", "PREVENT_DEFAULT", "BOOLLIT", "INTLIT", "FLOATLIT", 
            "STRINGLIT", "ID", "WS", "BLOCKCOMMENT", "LINECOMMENT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "AUTO", "BREAK", "BOOLEAN", "DO", "FLOAT", "ELSE", "FOR", 
                  "FUNCTION", "IF", "INT", "RETURN", "STRING", "WHILE", 
                  "VOID", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "ADDOP", 
                  "SUBOP", "MULOP", "DIVOP", "MODOP", "NEGOP", "ANDOP", 
                  "OROP", "EQOP", "NEQOP", "LTOP", "LEOP", "GTOP", "GEOP", 
                  "STRINGCONCAT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                  "DOT", "COMMA", "SM", "COLON", "ASSIGN", "DOUBLEQUOTE", 
                  "READ_INTEGER", "PRINT_INTEGER", "READ_FLOAT", "WRITE_FLOAT", 
                  "READ_BOOLEAN", "PRINT_BOOLEAN", "READ_STRING", "PRINT_STRING", 
                  "SUPER", "PREVENT_DEFAULT", "BOOLLIT", "DIGIT", "ZERO", 
                  "INTLIT", "DECIMAL", "EXPORNENT", "FLOATLIT", "ESC_SEQ", 
                  "SUB_STRING", "STRINGLIT", "ID", "WS", "BLOCKCOMMENT", 
                  "LINECOMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ESCAPE" ]

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
            actions[62] = self.FLOATLIT_action 
            actions[65] = self.STRINGLIT_action 
            actions[70] = self.ERROR_CHAR_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
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
                
     



from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

class CAR:
  SONATA = "HYUNDAI SONATA"
  SONATA_TURBO = "HYUNDAI SONATA Turbo"
  GRANDEUR = "HYUNDAI GRANDEUR"
  GRANDEUR_HEV = "HYUNDAI GRANDEUR Hybrid"
  GENESIS = "GENESIS"
  SANTAFE = "HYUNDAI SANTAFE"
  KONA = "HYUNDAI KONA"
  KONA_HEV = "HYUNDAI KONA Hybrid"
  KONA_EV = "HYUNDAI KONA ELECTRIC"
  IONIQ_HEV = "HYUNDAI IONIQ HYBRID"
  IONIQ_EV = "HYUNDAI IONIQ ELECTRIC"
  K5 = "KIA K5"
  K5_HEV = "KIA K5 Hybrid"
  K7 = "KIA K7"
  K7_HEV = "KIA K7 Hybrid"
  STINGER = "KIA STINGER"
  SORENTO = "KIA SORENTO"
  NEXO = "HYUNDAI NEXO"
  MOHAVE = "KIA MOHAVE"


class Buttons:
  NONE = 0
  RES_ACCEL = 1
  SET_DECEL = 2
  CANCEL = 4

FINGERPRINTS = {
  CAR.SONATA: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1444: 8, 1456: 4, 1470: 8
  },
  {
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 625: 8, 688: 5, 790: 8, 809: 8, 832: 8, 897: 8, 899: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1366: 8, 1367: 8, 1369: 8, 1371: 8, 1407: 8, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1460: 8, 1470: 8, 1472: 8, 1491: 8, 1530: 8, 1990: 8, 1998: 8, 2016: 8, 2024: 8
  }],
  CAR.SONATA_TURBO: [{
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1371: 8, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1460: 8, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 2015: 8, 2024: 8
  },
  {
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1314: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1460: 8, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1905: 8, 1913: 8, 1990: 8, 1998: 8, 2006: 8, 2014: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  }],
  CAR.GRANDEUR: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1185: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8
  }],
  CAR.GRANDEUR_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 546: 8, 576: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1156: 8, 1157: 4, 1168: 7, 1173: 8, 1185: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 865: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1108: 8, 1136: 6, 1138: 5, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 516: 8, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 865: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1108: 8, 1136: 6, 1138: 5, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.GENESIS: [{
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1268: 8, 1280: 1, 1281: 3, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1427: 6, 1434: 2, 1437: 8, 1456: 4
  },
  {
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1378: 4, 1379: 8, 1384: 5, 1407: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4
  },
  {
    67: 8, 68: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 7, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 5, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1334: 8, 1335: 8, 1345: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1378: 4, 1384: 5, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1437: 8, 1456: 4
  }],
  CAR.SANTAFE: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1379: 8, 1384: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  },
  {
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 764: 8, 809: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1183: 8, 1186: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 2000: 8, 2004: 8, 2008: 8, 2012: 8
  },
  {
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 912: 7, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1180: 8, 1183: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8, 1628: 8, 1629: 8, 1630: 8, 1631: 8, 1674: 8, 1675: 8, 1676: 8, 1677: 8, 1791: 8, 2015: 8
  },
  {
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 593: 8, 608: 8, 688: 6, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1170: 8, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1227: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 8, 1379: 8, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8, 1479: 8
  }],
  CAR.KONA: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 354: 3, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1156: 8, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1193: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1394: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8
  }],
  CAR.KONA_HEV: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 354: 3, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1394: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1990: 8, 1998: 8, 2001: 8, 2004: 8, 2009: 8, 2012: 8, 2015: 8
  }],
  CAR.KONA_EV: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 354: 3, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1394: 8, 1407: 8, 1414: 3, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1988: 8, 1990: 8, 1998: 8, 2001: 8, 2004: 8, 2009: 8, 2012: 8, 2015: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1157: 4, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1378: 4, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 546: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1157: 4, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1378: 4, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 546: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1157: 4, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 546: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1157: 4, 1168: 7, 1173: 8, 1183: 8, 1186: 2, 1191: 2, 1193: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1378: 4, 1379: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1473: 8, 1507: 8, 1535: 8
  }],
  CAR.IONIQ_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1173: 8, 1225: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470:8, 1476: 8, 1535: 8
  }],
  CAR.IONIQ_EV: [{
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 7, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1168: 7, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1425: 2, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1507: 8, 1535: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 7, 545: 8, 546: 8, 548: 8, 549: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1168: 7, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1507: 8, 1535: 8
  },
  {
    127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 7, 546: 8, 832: 8, 881: 8, 882: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 6, 1168: 7, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1322: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1407: 8, 1419: 8, 1426: 8, 1427: 6, 1429: 8, 1430: 8, 1456: 4, 1470: 8, 1507: 8
  }],
  CAR.K5: [{
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 273: 8, 274: 8, 275: 8, 339: 8, 356: 4, 399: 8, 447: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 884: 8, 897: 8, 899: 8, 902: 8, 903: 6, 909: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1186: 2, 1191: 2, 1253: 8, 1254: 8, 1255: 8, 1265: 4, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1414: 3, 1415: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1472: 8, 1486: 8, 1487: 8, 1491: 8, 1530: 8, 1532: 5, 1952: 8, 1960: 8, 1988: 8, 1996: 8, 2001: 8, 2004: 8, 2008: 8, 2009: 8, 2012: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8
  },
  {
    64: 8, 66: 8, 67: 8, 68: 8, 127: 8, 128: 8, 129: 8, 273: 8, 274: 8, 275: 8, 339: 8, 354: 3, 356: 4, 399: 8, 512: 6, 544: 8, 593: 8, 608: 8, 688: 5, 790: 8, 809: 8, 832: 8, 897: 8, 899: 8, 902: 8, 903: 6, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1151: 6, 1168: 7, 1170: 8, 1265: 4, 1268: 8, 1280: 1, 1282: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1349: 8, 1351: 8, 1353: 8, 1356: 8, 1363: 8, 1365: 8, 1366: 8, 1367: 8, 1369: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1440: 8, 1456: 4, 1470: 8, 1472: 8, 1491: 8, 1492: 8
  }],
  CAR.K5_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 6, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1168: 7, 1173: 8, 1236: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  },
  {
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 909: 8, 912: 7, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 6, 1151: 6, 1168: 7, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1407: 8, 1419: 8, 1420: 8, 1425: 2, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.K7: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1444: 8, 1456: 4, 1470: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 608: 8, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1162: 4, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1444: 8, 1456: 4, 1470: 8
  }],
  CAR.K7_HEV: [{
    68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 544: 8, 576: 8, 593: 8, 688: 5, 832: 8, 865: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1096: 8, 1102: 8, 1108: 8, 1136: 6, 1138: 5, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1210: 8, 1227: 8, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1343: 8, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1379: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1448: 8, 1456: 4, 1470: 8, 1476: 8, 1535: 8
  }],
  CAR.STINGER: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1378: 4, 1379: 8, 1384: 8, 1407: 8, 1419: 8, 1425: 2, 1427: 6, 1456: 4, 1470: 8
  },
  {
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 358: 6, 359: 8, 544: 8, 576: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1157: 4, 1168: 7, 1170: 8, 1173: 8, 1184: 8, 1265: 4, 1280: 1, 1281: 4, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 4, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1437: 8, 1456: 4, 1470: 8
  }],
  CAR.NEXO: [{
    127: 8, 145: 8, 146: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 512: 6, 544: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 908: 8, 909: 8, 912: 7, 916: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1173: 8, 1174: 8, 1180: 8, 1183: 8, 1186: 2, 1191: 2, 1192: 8, 1193: 8, 1210: 8, 1219: 8, 1220: 8, 1222: 6, 1223: 8, 1224: 8, 1227: 8, 1230: 6, 1231: 6, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1297: 8, 1298: 8, 1305: 8, 1312: 8, 1315: 8, 1316: 8, 1322: 8, 1324: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1437: 8, 1456: 4, 1460: 8, 1470: 8, 1484: 8, 1507: 8, 1520: 8, 1535: 8
  },
  {
    127: 8, 145: 8, 146: 8, 304: 8, 320: 8, 339: 8, 352: 8, 356: 4, 512: 6, 544: 8, 546: 8, 593: 8, 688: 5, 832: 8, 881: 8, 882: 8, 897: 8, 902: 8, 903: 8, 905: 8, 908: 8, 909: 8, 912: 7, 916: 8, 1056: 8, 1057: 8, 1078: 4, 1136: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 7, 1173: 8, 1174: 8, 1180: 8, 1183: 8, 1186: 2, 1191: 2, 1192: 8, 1193: 8, 1210: 8, 1219: 8, 1220: 8, 1222: 6, 1223: 8, 1224: 8, 1227: 8, 1230: 6, 1231: 6, 1265: 4, 1268: 8, 1280: 1, 1287: 4, 1290: 8, 1291: 8, 1292: 8, 1294: 8, 1297: 8, 1298: 8, 1305: 8, 1312: 8, 1315: 8, 1316: 8, 1322: 8, 1324: 8, 1342: 6, 1345: 8, 1348: 8, 1355: 8, 1363: 8, 1369: 8, 1371: 8, 1407: 8, 1419: 8, 1427: 6, 1429: 8, 1430: 8, 1437: 8, 1456: 4, 1460: 8, 1470: 8, 1484: 8, 1507: 8, 1520: 8, 1535: 8
  }],
  CAR.MOHAVE: [{
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 8, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1123: 8, 1136: 8, 1145: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1170: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1280: 8, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1479: 8
  },
  {
    67: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 516: 8, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 8, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 905: 8, 909: 8, 913: 8, 916: 8, 1040: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1123: 8, 1136: 8, 1145: 8, 1151: 8, 1155: 8, 1156: 8, 1157: 4, 1162: 8, 1164: 8, 1168: 8, 1170: 8, 1173: 8, 1180: 8, 1186: 2, 1191: 2, 1193: 8, 1210: 8, 1225: 8, 1227: 8, 1265: 4, 1280: 8, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1479: 8
  }],
  CAR.SORENTO: [{
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1064: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1168: 7, 1170: 8, 1173: 8, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1331: 8, 1332: 8, 1333: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1370: 8, 1371: 8, 1384: 8, 1407: 8, 1411: 8, 1419: 8, 1425: 2, 1427: 6, 1444: 8, 1456: 4, 1470: 8, 1489: 1
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 8, 1168: 7, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1479: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 546: 8, 548: 8, 550: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 8, 1168: 7, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1479: 8
  },
  {
    67: 8, 68: 8, 127: 8, 304: 8, 320: 8, 339: 8, 356: 4, 544: 8, 593: 8, 608: 8, 688: 5, 809: 8, 832: 8, 854: 7, 870: 7, 871: 8, 872: 8, 897: 8, 902: 8, 903: 8, 909: 8, 916: 8, 1040: 8, 1042: 8, 1056: 8, 1057: 8, 1078: 4, 1107: 5, 1136: 8, 1151: 6, 1156: 8, 1157: 4, 1162: 8, 1168: 7, 1170: 8, 1173: 8, 1186: 2, 1191: 2, 1265: 4, 1280: 1, 1287: 4, 1290: 8, 1292: 8, 1294: 8, 1312: 8, 1322: 8, 1342: 6, 1345: 8, 1348: 8, 1363: 8, 1369: 8, 1371: 8, 1378: 8, 1384: 8, 1407: 8, 1419: 8, 1427: 6, 1456: 4, 1470: 8, 1479: 8
  }],
}

ECU_FINGERPRINT = {
  Ecu.fwdCamera: [832, 1156, 1191, 1342]
}

CHECKSUM = {
  "crc8": [CAR.SANTAFE],
  "6B": [CAR.SORENTO, CAR.GENESIS],
}

FEATURES = {
  "use_cluster_gears": [CAR.KONA, CAR.GRANDEUR, CAR.K7],  # Use Cluster for Gear Selection, rather than Transmission
  "use_tcu_gears": [CAR.K5, CAR.SONATA, CAR.SONATA_TURBO],  # Use TCU Message for Gear Selection
  "use_elect_gears": [CAR.K5_HEV, CAR.GRANDEUR_HEV, CAR.IONIQ_HEV, CAR.IONIQ_EV, CAR.KONA_HEV, CAR.KONA_EV, CAR.NEXO],
}

DBC = {
  CAR.SONATA: dbc_dict('hyundai_kia_generic', None),
  CAR.SONATA_TURBO: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR: dbc_dict('hyundai_kia_generic', None),
  CAR.GRANDEUR_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.GENESIS: dbc_dict('hyundai_kia_generic', None),
  CAR.SANTAFE: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.KONA_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.IONIQ_EV: dbc_dict('hyundai_kia_generic', None),
  CAR.K5: dbc_dict('hyundai_kia_generic', None),
  CAR.K5_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.K7: dbc_dict('hyundai_kia_generic', None),
  CAR.K7_HEV: dbc_dict('hyundai_kia_generic', None),
  CAR.STINGER: dbc_dict('hyundai_kia_generic', None),
  CAR.NEXO: dbc_dict('hyundai_kia_generic', None),
  CAR.MOHAVE: dbc_dict('hyundai_kia_generic', None),
  CAR.SORENTO: dbc_dict('hyundai_kia_generic', None),
}

STEER_THRESHOLD = 150

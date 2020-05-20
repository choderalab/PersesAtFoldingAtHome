class System(object):
    def __init__(self):
        self.name = name
        self.name_to_index = name_to_index
        self.index_to_name = index_to_name
        self.name_pairs = name_pairs
        self.index_pairs = index_pairs
        self.color = None        

class Bace(System):
    name = 'Bace'
    bace = ['CAT-13f','CAT-13d','CAT-4c','CAT-13b','CAT-4l','CAT-13m','CAT-4k','CAT-13n','CAT-13o','CAT-13a','CAT-13k','CAT-17a','CAT-17f','CAT-13i','CAT-17d','CAT-13c','CAT-17c','CAT-24','CAT-17i','CAT-13g','CAT-4j','CAT-17b','CAT-4p','CAT-17h','CAT-4b','CAT-17g','CAT-4d','CAT-4m','CAT-13e','CAT-4n','CAT-4o','CAT-4a','CAT-13j','CAT-13h','CAT-4i','CAT-17e']
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(bace):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('CAT-13b','CAT-17g'), ('CAT-13a','CAT-17g'), ('CAT-13e','CAT-17g'), ('CAT-4m','CAT-4c'), ('CAT-13k','CAT-4d'), ('CAT-24','CAT-17e'), ('CAT-13g','CAT-17g'), ('CAT-13d','CAT-13h'), ('CAT-13a','CAT-17i'), ('CAT-4m','CAT-13j'), ('CAT-13a','CAT-13m'), ('CAT-4l','CAT-13k'), ('CAT-13o','CAT-17i'), ('CAT-4c','CAT-4o'), ('CAT-4j','CAT-4o'), ('CAT-4i','CAT-13m'), ('CAT-24','CAT-17i'), ('CAT-13j','CAT-4o'), ('CAT-4n','CAT-13k'), ('CAT-4o','CAT-4b'), ('CAT-17i','CAT-13f'), ('CAT-17c','CAT-17e'), ('CAT-13k','CAT-4b'), ('CAT-4m','CAT-4j'), ('CAT-13n','CAT-13k'), ('CAT-13d','CAT-17h'), ('CAT-17b','CAT-13d'), ('CAT-4m','CAT-4n'), ('CAT-4m','CAT-13k'), ('CAT-13c','CAT-17i'), ('CAT-4a','CAT-4o'), ('CAT-13h','CAT-17i'), ('CAT-4o','CAT-4d'), ('CAT-17g','CAT-17c'), ('CAT-4a','CAT-13k'), ('CAT-13d','CAT-17d'), ('CAT-17g','CAT-17f'), ('CAT-13e','CAT-17i'), ('CAT-13d','CAT-13b'), ('CAT-17g','CAT-13i'), ('CAT-4m','CAT-13m'), ('CAT-17g','CAT-13c'), ('CAT-17i','CAT-17a'), ('CAT-13d','CAT-13f'), ('CAT-17f','CAT-17e'), ('CAT-13d','CAT-17a'), ('CAT-17g','CAT-17d'), ('CAT-13n','CAT-13a'), ('CAT-13o','CAT-17h'), ('CAT-17b','CAT-17e'), ('CAT-4k','CAT-4o'), ('CAT-4m','CAT-4l'), ('CAT-4m','CAT-4k'), ('CAT-13n','CAT-4i'), ('CAT-13g','CAT-17i'), ('CAT-4p','CAT-13k'), ('CAT-4m','CAT-4p'), ('CAT-13d','CAT-13i')]    
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))

    def __init__(self):
        super(System, self).__init__()

class Cdk2(System):
    name = 'Cdk2'
    cdk2 = ['30','28' ,'1oiy' ,'1oi9' ,'32' ,'1oiu' ,'29' ,'1h1r' ,'21' ,'26' ,'1h1s' ,'31' ,'20' ,'22' ,'17' ,'1h1q']
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(cdk2):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('22','1h1r') ,('17','1h1q') ,('17','21') ,('17','22') ,('20','1h1q') ,('26','1h1q') ,('26','1oi9') ,('28','26') ,('28','31') ,('29','26') ,('30','26') ,('30','31') ,('31','32') ,('1h1r','1oi9') ,('1h1r','21') ,('1h1s','1oiy') ,('1h1s','26') ,('1oi9','20') ,('1oiu','26') ,('1oiu','1h1q') ,('1oiy','1oi9') ,('1oiy','32') ,('1oiy','29') ,('1oiy','31') ,('1oiy','1h1q')]
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))
        
    def __init__(self):
        super(System, self).__init__()

class Jnk1(System):
    name = 'Jnk1'
    jnk1 = ['18629-1','18634-1','18628-1','18660-1','18624-1','18633-1','18635-1','17124-1','18625-1','18659-1','18637-1','18638-1','18652-1','18627-1','18658-1','18630-1','18639-1','18631-1','18632-1','18636-1','18626-1']
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(jnk1):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('17124-1','18634-1'), ('18626-1','18624-1'), ('18636-1','18625-1'), ('18632-1','18624-1'), ('18635-1','18625-1'), ('18626-1','18658-1'), ('18639-1','18658-1'), ('18626-1','18625-1'), ('18638-1','18658-1'), ('18628-1','18624-1'), ('18631-1','18660-1'), ('18638-1','18634-1'), ('18626-1','18632-1'), ('18626-1','18630-1'), ('18631-1','18624-1'), ('18629-1','18627-1'), ('18634-1','18637-1'), ('18626-1','18627-1'), ('18631-1','18652-1'), ('18637-1','18631-1'), ('18626-1','18634-1'), ('18633-1','18624-1'), ('17124-1','18631-1'), ('18627-1','18630-1'), ('18659-1','18634-1'), ('18636-1','18624-1'), ('18626-1','18628-1'), ('18626-1','18660-1'), ('18626-1','18659-1'), ('18639-1','18634-1'), ('18635-1','18624-1')]
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))
        
    def __init__(self):
        super(System, self).__init__()

class Mcl1(System):
    name = 'Mcl1'
    mcl1 = ['26','48','33','46','35','31','52','68','32','38','51','50','28','66','39','37','30','54','44','23','29','40','62','61','49','64','41','65','58','63','27','47','57','56','53','36','60','45','42','67','34','43']
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(mcl1):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('50','60'), ('56','35'), ('65','60'), ('26','57'), ('58','60'), ('62','45'), ('60','36'), ('30','27'), ('33','27'), ('43','27'), ('67','58'), ('67','32'), ('30','40'), ('38','60'), ('41','35'), ('54','23'), ('56','60'), ('66','42'), ('29','40'), ('26','44'), ('49','35'), ('29','35'), ('42','51'), ('39','32'), ('35','37'), ('28','35'), ('35','53'), ('67','63'), ('27','45'), ('41','32'), ('67','53'), ('35','33'), ('27','46'), ('66','23'), ('67','61'), ('57','23'), ('30','35'), ('61','60'), ('67','31'), ('32','46'), ('35','60'), ('31','35'), ('62','26'), ('35','36'), ('26','64'), ('38','35'), ('35','34'), ('29','27'), ('48','27'), ('68','45'), ('63','60'), ('54','42'), ('44','23'), ('28','27'), ('67','27'), ('52','60'), ('27','23'), ('49','67'), ('28','47'), ('67','52'), ('30','48'), ('67','35'), ('32','34'), ('65','67'), ('67','50'), ('35','39'), ('43','47'), ('67','37'), ('42','64'), ('51','45'), ('68','23')]
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))
        
    def __init__(self):
        super(System, self).__init__()

class P38a(System):
    name = 'p38a'
    p38a = ['p38a_2n','p38a_3flz','p38a_2h','p38a_2s','p38a_2bb','p38a_2q','p38a_2z','p38a_3fmh','p38a_2f','p38a_2v','p38a_3fln','p38a_2t','p38a_2r','p38a_3fly','p38a_2u','p38a_2l','p38a_2aa','p38a_2gg','p38a_2k','p38a_3flq','p38a_2p','p38a_3fmk','p38a_2j','p38a_2g','p38a_2c','p38a_2x','p38a_3flw','p38a_2e','p38a_2ee','p38a_2y','p38a_2i','p38a_2o','p38a_2ff','p38a_2m']
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(p38a):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('p38a_2aa','p38a_2bb') ,('p38a_2aa','p38a_3flw') ,('p38a_2e','p38a_2j') ,('p38a_2ee','p38a_2j') ,('p38a_2ee','p38a_3fln') ,('p38a_2g','p38a_2c') ,('p38a_2g','p38a_2f') ,('p38a_2g','p38a_2h') ,('p38a_2g','p38a_2i') ,('p38a_2gg','p38a_2j') ,('p38a_2j','p38a_2f') ,('p38a_2j','p38a_2ff') ,('p38a_2j','p38a_2h') ,('p38a_2j','p38a_2q') ,('p38a_2j','p38a_2r') ,('p38a_2l','p38a_2j') ,('p38a_2l','p38a_2n') ,('p38a_2l','p38a_2o') ,('p38a_2l','p38a_2p') ,('p38a_2m','p38a_2j') ,('p38a_2m','p38a_2k') ,('p38a_2s','p38a_2l') ,('p38a_2t','p38a_2j') ,('p38a_2u','p38a_2k') ,('p38a_2u','p38a_2q') ,('p38a_2v','p38a_2bb') ,('p38a_2v','p38a_2j') ,('p38a_2v','p38a_2x') ,('p38a_2v','p38a_2y') ,('p38a_2v','p38a_3fln') ,('p38a_2v','p38a_3fly') ,('p38a_2v','p38a_3fmh') ,('p38a_2v','p38a_3fmk') ,('p38a_2z','p38a_2aa') ,('p38a_2z','p38a_2y') ,('p38a_2z','p38a_3flq') ,('p38a_2z','p38a_3flw') ,('p38a_2z','p38a_3fmk') ,('p38a_3fln','p38a_2e') ,('p38a_3fln','p38a_2ff') ,('p38a_3fln','p38a_2g') ,('p38a_3fln','p38a_2gg') ,('p38a_3fln','p38a_2i') ,('p38a_3fln','p38a_2k') ,('p38a_3fln','p38a_2n') ,('p38a_3fln','p38a_2o') ,('p38a_3fln','p38a_2p') ,('p38a_3fln','p38a_2r') ,('p38a_3fln','p38a_2s') ,('p38a_3fln','p38a_2t') ,('p38a_3fln','p38a_3flz') ,('p38a_3fly','p38a_2x') ,('p38a_3fly','p38a_3flq') ,('p38a_3fly','p38a_3fmh') ,('p38a_3flz','p38a_2c') ,('p38a_3flz','p38a_2g')]
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))
        
    def __init__(self):
        super(System, self).__init__()

class Ptp1b(System):
    name = 'Ptp1b'
    ptp1b = ['23469','23472','23474','23480','23470','23486','20669(2qbr)','23482','23483','23473','20670(2qbs)','23468','23475','20667(2qbp)','23477','23471','23485','23467','23466','23476','23484','23479','23330(2qbq)'] 
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(ptp1b):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('23466','23475') ,('23467','23466') ,('23467','23468') ,('23467','23469') ,('23467','23470') ,('23467','23473') ,('23467','23474') ,('23467','23475') ,('23467','23476') ,('23469','23472') ,('23469','20669(2qbr)') ,('23471','23466') ,('23471','23468') ,('23471','23470') ,('23473','20669(2qbr)') ,('23474','23466') ,('23476','23466') ,('23477','23466') ,('23477','23467') ,('23477','23479') ,('23477','23482') ,('23477','23483') ,('23477','23330(2qbq)') ,('23480','23479') ,('23480','23482') ,('23482','23479'),('23482','23485') ,('23482','23486') ,('23483','23479') ,('23484','23479') ,('23484','23482') ,('23484','23485') ,('23484','23486') ,('23485','23479') ,('23486','23479') ,('23486','23485') ,('20667(2qbp)','23479') ,('20667(2qbp)','23482') ,('20667(2qbp)','23484') ,('20667(2qbp)','23485') ,('20667(2qbp)','23486') ,('20669(2qbr)','23466') ,('20669(2qbr)','23472') ,('20670(2qbs)','23466') ,('20670(2qbs)','23477') ,('20670(2qbs)','23479') ,('20670(2qbs)','23482') ,('20670(2qbs)','23483') ,('20670(2qbs)','23330(2qbq)')] 
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))
        
    def __init__(self):
        super(System, self).__init__()

class Thrombin(System):
    name = 'Thrombin'
    thrombin = ['1b','1d','3b','1a','6a','7a','3a','5','6b','6e','1c']
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(thrombin):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('1d','6e'),('1d','5'),('1b','3b'),('6a','1b'),('1b','1c'),('1d','1c'),('1b','1a'),('1a','5'),('3a','1d'),('6a','6b'),('1d','7a'),('1b','7a'),('3a','1b'),('1d','1a'),('1a','3b'),('6e','6b')]
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))

    def __init__(self):
        super(System, self).__init__()
        
class Tyk2(System):
    name = 'Tyk2'
    tyk2 = ['ejm_31','jmc_30','ejm_50','ejm_46','ejm_55','ejm_43','jmc_28','ejm_49','ejm_45','ejm_44','jmc_27','ejm_48','ejm_47','jmc_23','ejm_42','ejm_54']
    name_to_index = {}
    index_to_name = {}
    for i,lig in enumerate(tyk2):
        name_to_index[lig] = i
        index_to_name[i] = lig
    name_pairs = [('ejm_31','ejm_46') ,('ejm_31','ejm_43') ,('ejm_31','ejm_45') ,('ejm_31','jmc_28') ,('ejm_31','ejm_48') ,('ejm_42','ejm_48') ,('ejm_42','ejm_55') ,('ejm_42','ejm_54') ,('ejm_43','ejm_55') ,('ejm_44','ejm_55') ,('ejm_44','ejm_42') ,('ejm_45','ejm_42') ,('ejm_47','ejm_31') ,('ejm_47','ejm_55') ,('ejm_49','ejm_31') ,('ejm_49','ejm_50') ,('ejm_50','ejm_42') ,('ejm_55','ejm_54') ,('jmc_23','ejm_55') ,('jmc_23','ejm_46') ,('jmc_23','jmc_27') ,('jmc_23','jmc_30') ,('jmc_28','jmc_27') ,('jmc_28','jmc_30')] 
    index_pairs = []
    for a,b in name_pairs:
        index_pairs.append((name_to_index[a],name_to_index[b]))
        
    def __init__(self):
        super(System, self).__init__()
    #def __init__(self):
    #    self.name = name
    #    self.name_to_index = name_to_index
    #    self.index_to_name = index_to_name
    #    self.name_pairs = name_pairs
    #    self.index_pairs = index_pairs
    #    self.color = None  

def check_missing_results(target,all_sims):
    import copy
    still_to_run = copy.deepcopy(target.index_pairs)
    for sim in all_sims:
        lig_id_a = int(sim.ligA)
        lig_id_b = int(sim.ligB)
        still_to_run.remove((lig_id_a,lig_id_b))
    return still_to_run

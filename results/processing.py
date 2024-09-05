import csv
import base64
import zlib
import json
import haversine as hs



class Participant:
    def __init__(self, uid):
        self.uid = uid              # User id (generated on the platform)
                                    ### TASK 1
        self.task1 = None           # First task (always AB)
        self.map1 = None            # First map (color map or default/grey map)
        self.confidence1 = None     # Confidence level (1 - 5)
        self.information1 = None    # Amount of information (1 - 5)
        self.strategy1 = None       # Strategy adopted (text)
        self.inside1 = None         # How many points inside of the path (integer)
        self.outside1 = None        # How many points outside of the path (integer)
        self.arrival1 = None        # Arrival on the exact location (True/False)
        self.moves1 = None
        self.ratio1 = None          # inside1/(inside1+outside1)
        self.time1 = None
        self.explore1 = None
                                    ### TASK 2
        self.task2 = None           # First task (always CD)
        self.map2 = None            # First map (color map or default/grey map)
        self.confidence2 = None     # Confidence level (1 - 5)
        self.information2 = None    # Amount of information (1 - 5)
        self.strategy2 = None       # Strategy adopted (text)
        self.inside2 = None         # How many points inside of the path (integer)
        self.outside2 = None        # How many points outside of the path (integer)
        self.arrival2 = None        # Arrival on the exact location (True/False)
        self.moves2 = None
        self.ratio2 = None          # inside2/(inside2+outside2)
        self.time2 = None
        self.explore2 = None
                                    ### Final questions
        self.understanding = None   # Understands the representation (text)
        self.familiarity = None     # Familiarity with GSV (1 - 5)
        self.studyarea = None       # Familiarity with study area (1 - 5)
        self.pointing = None        # Pointing device used (text)
        self.browser = None         # Web browser used (text)
        self.cvd = None             # Color vision deficiencies (Yes/No)
        self.cvdYes = None          # If yes what ? (text)
        self.gender = None          # Gender (text)
        self.age = None             # Age (integer)
        self.remarks = None         # Additional remarks or comments (text)






beg_geojson = '{"type": "FeatureCollection","crs": {"type": "name","properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},"features":'
end_geojson = '}'

path1 = [
  [
    16.3140799,
    48.2182966
  ],
  [
    16.314055172787914,
    48.21831339207219
  ],
  [
    16.314124257285332,
    48.21833910867256
  ],
  [
    16.31413025056661,
    48.21827637268029
  ],
  [
    16.314273312738155,
    48.218273644502474
  ],
  [
    16.314409568829348,
    48.21825414130723
  ],
  [
    16.31454120108549,
    48.21823312874192
  ],
  [
    16.314670835446545,
    48.21821264030398
  ],
  [
    16.31479879966489,
    48.21819192710224
  ],
  [
    16.314925119390242,
    48.21817121915725
  ],
  [
    16.31504003971758,
    48.21814141662079
  ],
  [
    16.315118284346394,
    48.21821605558022
  ],
  [
    16.315164332450518,
    48.218324984783685
  ],
  [
    16.315193236173407,
    48.21840742304679
  ],
  [
    16.315222952373976,
    48.21849161325486
  ],
  [
    16.315245121855288,
    48.218560383035694
  ],
  [
    16.315269099591063,
    48.21862047504015
  ],
  [
    16.31529940191127,
    48.21870715158237
  ],
  [
    16.31533706791409,
    48.218794393587245
  ],
  [
    16.31538854943414,
    48.21887674361493
  ],
  [
    16.315448242158674,
    48.21895680876065
  ],
  [
    16.315511348267727,
    48.21903520885711
  ],
  [
    16.315578761538173,
    48.21911719014144
  ],
  [
    16.315630630506185,
    48.219203925566994
  ],
  [
    16.315648542921934,
    48.21926248502714
  ],
  [
    16.315713714798413,
    48.2192429554607
  ],
  [
    16.315778477521413,
    48.219220680361424
  ],
  [
    16.315923228021052,
    48.21915591701316
  ],
  [
    16.31603532540982,
    48.21911460251005
  ],
  [
    16.316149724245935,
    48.21907271942346
  ],
  [
    16.31626231071342,
    48.2190314893968
  ],
  [
    16.316377174441683,
    48.21899039554661
  ],
  [
    16.316493792899603,
    48.21894966969647
  ],
  [
    16.316614164093885,
    48.21890878749114
  ],
  [
    16.316735415587605,
    48.21886995877805
  ],
  [
    16.3168192034481,
    48.218836345147324
  ],
  [
    16.316863701396976,
    48.21883672970179
  ],
  [
    16.316994486449204,
    48.218810539014925
  ],
  [
    16.31712025156822,
    48.21878850663242
  ],
  [
    16.31725143985206,
    48.218766542376294
  ],
  [
    16.31739029849344,
    48.21874696852432
  ],
  [
    16.31757577572274,
    48.218724665300414
  ],
  [
    16.317711174663692,
    48.21870388009162
  ],
  [
    16.317841097633508,
    48.2186816316478
  ],
  [
    16.31796916915825,
    48.21866183400925
  ],
  [
    16.31809568670488,
    48.21864070392639
  ],
  [
    16.31822158057882,
    48.21861982024347
  ],
  [
    16.318342011966134,
    48.21859544558698
  ],
  [
    16.318419590468707,
    48.21860722416468
  ],
  [
    16.318478196382575,
    48.21857002598279
  ],
  [
    16.31862284740102,
    48.218554127082534
  ],
  [
    16.318757115589193,
    48.218532725846295
  ],
  [
    16.318881591557368,
    48.218511112631596
  ],
  [
    16.31900643310574,
    48.21849123816707
  ],
  [
    16.319129328068264,
    48.21847234796923
  ],
  [
    16.31926409043706,
    48.21845383502211
  ],
  [
    16.319332315890957,
    48.2184450789991
  ],
  [
    16.319335430943788,
    48.2185226981763
  ],
  [
    16.319370595128287,
    48.218610147760586
  ],
  [
    16.319398995118807,
    48.218697490654506
  ],
  [
    16.31943019209326,
    48.218782868479195
  ],
  [
    16.319459383656596,
    48.2188693173487
  ],
  [
    16.319488659928044,
    48.21895590987745
  ],
  [
    16.319519892070915,
    48.219041906360395
  ],
  [
    16.31955206823617,
    48.219127453990396
  ],
  [
    16.319586842187633,
    48.21921293552894
  ],
  [
    16.319622744390948,
    48.21929716223331
  ],
  [
    16.319646768923185,
    48.21941529704828
  ],
  [
    16.319676855910526,
    48.219456658040194
  ],
  [
    16.319553996559833,
    48.2194789720333
  ],
  [
    16.319430453318613,
    48.21950590461234
  ],
  [
    16.319306227446607,
    48.219533170102686
  ],
  [
    16.319158530768764,
    48.21956665475435
  ],
  [
    16.31900554221539,
    48.21960309069631
  ],
  [
    16.318907049734115,
    48.2196305861806
  ],
  [
    16.318791719205773,
    48.21965616750683
  ],
  [
    16.3188208175456,
    48.21970219188595
  ],
  [
    16.31887623355537,
    48.21978038621556
  ],
  [
    16.318938070039327,
    48.21985959465844
  ],
  [
    16.318998437268604,
    48.2199376144097
  ],
  [
    16.319061582253955,
    48.220017178166
  ],
  [
    16.319124351353224,
    48.220093679965444
  ]
]

path2 = [
  [
    16.3190267,
    48.2175543
  ],
  [
    16.319021311800316,
    48.217567018764534
  ],
  [
    16.318904455481288,
    48.217568746210546
  ],
  [
    16.318784244326697,
    48.217586778301396
  ],
  [
    16.318656538263813,
    48.2176064459046
  ],
  [
    16.318527837046304,
    48.217626102281265
  ],
  [
    16.31839883987456,
    48.21764525614531
  ],
  [
    16.318266967398376,
    48.2176647501807
  ],
  [
    16.318130600722785,
    48.21768481986053
  ],
  [
    16.318062599393336,
    48.21769525669211
  ],
  [
    16.317935813333495,
    48.21771517917286
  ],
  [
    16.317813444551177,
    48.21773383565844
  ],
  [
    16.31768547763722,
    48.21775361794039
  ],
  [
    16.317557376372243,
    48.21777373126863
  ],
  [
    16.317428541217083,
    48.21779371744229
  ],
  [
    16.317298263908505,
    48.21781367947683
  ],
  [
    16.317166375314546,
    48.21783333030726
  ],
  [
    16.317117405224987,
    48.21784660830355
  ],
  [
    16.317070383058844,
    48.21788071792575
  ],
  [
    16.31712975000281,
    48.217960594580525
  ],
  [
    16.317155739364843,
    48.21805280600563
  ],
  [
    16.31718090738451,
    48.218132436845046
  ],
  [
    16.31721162083185,
    48.2182199877666
  ],
  [
    16.317245563163645,
    48.21831189996913
  ],
  [
    16.317280215461516,
    48.218399423701214
  ],
  [
    16.317326127917216,
    48.218482193137845
  ],
  [
    16.31738027862909,
    48.21860038502067
  ],
  [
    16.31737885725529,
    48.21872307610971
  ],
  [
    16.31738027862909,
    48.21860038502067
  ],
  [
    16.31737885725529,
    48.21872307610971
  ],
  [
    16.317454651292348,
    48.218737608257904
  ],
  [
    16.31737885725529,
    48.21872307610971
  ],
  [
    16.317454651292348,
    48.218737608257904
  ],
  [
    16.31739029849344,
    48.21874696852432
  ],
  [
    16.31725143985206,
    48.218766542376294
  ],
  [
    16.31712025156822,
    48.21878850663242
  ],
  [
    16.316994486449204,
    48.218810539014925
  ],
  [
    16.316863701396976,
    48.21883672970179
  ],
  [
    16.3168192034481,
    48.218836345147324
  ],
  [
    16.316882843313486,
    48.218919186145136
  ],
  [
    16.316942794096605,
    48.21899968092171
  ],
  [
    16.317004169304138,
    48.21907942322053
  ],
  [
    16.317066672949256,
    48.21915791066928
  ],
  [
    16.31712894734839,
    48.21923526281783
  ],
  [
    16.317189939860054,
    48.219312489855916
  ],
  [
    16.317250822410934,
    48.219389343409624
  ],
  [
    16.317312650644638,
    48.21946668285906
  ],
  [
    16.31737341746771,
    48.21954464430535
  ],
  [
    16.31743467389188,
    48.21962269048417
  ],
  [
    16.317497111613356,
    48.21970087662212
  ],
  [
    16.317558925896005,
    48.2197793093874
  ],
  [
    16.317620482213275,
    48.21985450722865
  ],
  [
    16.317677657538198,
    48.21992208308012
  ],
  [
    16.3177387371385,
    48.21999423372291
  ],
  [
    16.317746040840024,
    48.2200148326485
  ],
  [
    16.31777726858078,
    48.22002774412521
  ],
  [
    16.31760696703505,
    48.22006630673664
  ],
  [
    16.317488565543535,
    48.22010737157742
  ],
  [
    16.3173704010533,
    48.22014902516744
  ],
  [
    16.317253637965724,
    48.220191565656705
  ],
  [
    16.317136858146984,
    48.22023426429561
  ],
  [
    16.31701882773907,
    48.22027558633926
  ],
  [
    16.31690154633112,
    48.22031594221497
  ],
  [
    16.316786743174795,
    48.22035547000528
  ],
  [
    16.3166707256689,
    48.22039517429734
  ],
  [
    16.316645855137864,
    48.22038055862898
  ],
  [
    16.316602040766625,
    48.220445292184394
  ],
  [
    16.316465101838283,
    48.220471676240315
  ],
  [
    16.316338936459992,
    48.22051597286367
  ],
  [
    16.316220624267885,
    48.220560919307516
  ],
  [
    16.316103647167644,
    48.220602165111714
  ],
  [
    16.315985711114976,
    48.220639732242375
  ],
  [
    16.315849914595088,
    48.22067942929759
  ],
  [
    16.315751696580243,
    48.22071093378201
  ],
  [
    16.31573851914714,
    48.22071970710231
  ],
  [
    16.31563554639263,
    48.220758058578454
  ],
  [
    16.315511524696067,
    48.22080375671582
  ],
  [
    16.315385746520775,
    48.22084815178747
  ],
  [
    16.315265337321517,
    48.22089028544355
  ],
  [
    16.315147472888274,
    48.22093095801982
  ],
  [
    16.315033657314466,
    48.22097197667925
  ],
  [
    16.314907521408465,
    48.221047279179494
  ],
  [
    16.314818737361332,
    48.22103829551917
  ],
  [
    16.314863378996698,
    48.221076217299476
  ],
  [
    16.314929829492684,
    48.2211455636138
  ],
  [
    16.31499288425189,
    48.221227793018734
  ],
  [
    16.31505914449801,
    48.221304647450495
  ],
  [
    16.31512233468681,
    48.22138132510494
  ],
  [
    16.31518267668478,
    48.221459507952275
  ]
]

arrival1 = [
            [16.319182766515816, 48.22016894517528],
            [16.319124351353224, 48.220093679965444],
            [16.319061582253955, 48.220017178166]
            ]

arrival2 = [
            [16.31512233468681, 48.22138132510494],
            [16.31518267668478, 48.221459507952275],
            [16.315239915330245, 48.22153783055302]
            ]

# arrival1 = [16.319124351353224, 48.220093679965444]

# arrival2 = [16.31518267668478, 48.221459507952275]

participants = []





csv1 = open('NT1.csv', newline='\n')
reader1 = csv.DictReader(csv1)

for row in reader1:

    # Decompress GeoJSON track
    compressed_base64 = row['Do not change this text !'].replace(' ', '+')
    compressed_bytes = base64.b64decode(compressed_base64)
    decompressed_bytes = zlib.decompress(compressed_bytes)
    decompressed_string = decompressed_bytes.decode('utf-8')
    geojson_object = json.loads(beg_geojson + decompressed_string + end_geojson)

    # Save GeoJSON track into a file
    prop = geojson_object['features'][0]['properties']
    uid = prop['uid']
    task = prop['task']
    map = prop['map']
    f = open('tracks/' + uid + '_' + task + '_' + map + '.geojson', 'w')
    f.write(json.dumps(geojson_object, indent=2))
    f.close()

    # Create new participants
    p = Participant(uid)
    p.task1 = task
    p.map1 = map
    p.confidence1 = row["How confident did you feel when navigating from A to B?"]
    p.information1 = row["How would you grade the amount of information on the map? (3 = just the right amount of information)"]
    p.strategy1 = row["What was your strategy to navigate to location B?"]
    # p.arrival1 = hs.haversine(geojson_object['features'][-1]['geometry']['coordinates'],arrival1)
    p.arrival1 = geojson_object['features'][-1]['geometry']['coordinates'] in arrival1
    
    p.inside1 = 0
    p.outside1 = 0
    for i in range(len(geojson_object['features'])):
        if(geojson_object['features'][i]['geometry']['coordinates'] in path1):
            p.inside1 += 1
        else:
            p.outside1 += 1
    p.moves1 = p.inside1+p.outside1
    p.ratio1 = p.inside1/p.moves1

    p.time1 = 0
    p.explore1 = 0
    for i in range(len(geojson_object['features'])):
        try:
          p.explore1 += geojson_object['features'][i]['properties']['heading_pitch']
        except:
          p.explore1 += geojson_object['features'][i]['properties']['hp'] # weird but necessary
        try:
          p.time1 += geojson_object['features'][i]['properties']['time']
        except:
          p.time1 = p.time1

    if(p.explore1 == 0):
        p.explore1 = None
    else:
        p.explore1 = p.explore1/p.moves1
    if(p.time1 == 0):
        p.time1 = None
      
    

    participants += [p]
            




csv2 = open('NT2.csv', newline='\n')
reader2 = csv.DictReader(csv2)

for row in reader2:

    # Decompress GeoJSON track
    compressed_base64 = row['Do not change this text !'].replace(' ', '+')
    compressed_bytes = base64.b64decode(compressed_base64)
    decompressed_bytes = zlib.decompress(compressed_bytes)
    decompressed_string = decompressed_bytes.decode('utf-8')
    geojson_object = json.loads(beg_geojson + decompressed_string + end_geojson)

    # Save GeoJSON track into a file
    prop = geojson_object['features'][0]['properties']
    uid = prop['uid']
    task = prop['task']
    map = prop['map']
    f = open('tracks/' + uid + '_' + task + '_' + map + '.geojson', 'w')
    f.write(json.dumps(geojson_object, indent=2))
    f.close()

    # Merge or add participant
    exists = False
    for p in participants:
        if p.uid == uid:
            exists = True
            break

    if(not exists):
        p = Participant(uid)

    p.task2 = task
    p.map2 = map
    p.confidence2 = row["How confident did you feel when navigating from C to D?"]
    p.information2 = row["How would you grade the amount of information on the map? (3 = just the right amount of information)"]
    p.strategy2 = row["What was your strategy to navigate to location D?"]
    # p.arrival2 = hs.haversine(geojson_object['features'][-1]['geometry']['coordinates'],arrival2)
    p.arrival2 = geojson_object['features'][-1]['geometry']['coordinates'] in arrival2

    p.inside2 = 0
    p.outside2 = 0
    for i in range(len(geojson_object['features'])):
        if(geojson_object['features'][i]['geometry']['coordinates'] in path2):
            p.inside2 += 1
        else:
            p.outside2 += 1
    p.moves2 = p.inside2+p.outside2
    p.ratio2 = p.inside2/p.moves2

    p.time2 = 0
    p.explore2 = 0
    for i in range(len(geojson_object['features'])):
        try:
          p.explore2 += geojson_object['features'][i]['properties']['heading_pitch']
        except:
          p.explore2 += geojson_object['features'][i]['properties']['hp'] # weird but necessary
        try:
          p.time2 += geojson_object['features'][i]['properties']['time']
        except:
          p.time2 = p.time2

    if(p.explore2 == 0):
        p.explore2 = None
    else:
        p.explore2 = p.explore2/p.moves2
    if(p.time2 == 0):
        p.time2 = None
    

    p.understanding = row["To your intuitive understanding, what do the colors on buildings represent on the map on the right?"]
    p.familiarity = row["Were you familiar with Google Street View before the survey?"]
    p.studyarea = row["Did you know the study area before the survey?"]
    p.pointing = row["Which pointing device did you use?"]
    p.browser = row["Which web browser did you use?"]
    p.cvd = row["Do you have some type of color vision deficiencies? "]
    p.cvdYes = row["If Yes, which one(s)?"]
    p.gender = row["What is your gender?"]
    p.age = row["How old are you?"]
    p.remarks = row["Do you have comments or remarks about this survey?"]

    if(not exists):
        participants += [p]
        
csv1.close()
csv2.close()

# Write the data in new csv file
csv0 = open('NT12.csv', mode='w')
writer0 = csv.DictWriter(csv0, fieldnames=participants[0].__dict__.keys())
writer0.writeheader()
writer0.writerows([p.__dict__ for p in participants])
csv0.close()


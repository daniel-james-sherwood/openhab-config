#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Change these if rebuilding system
# id = "4b5e171fc9:bbd9c65639"
# token = "oh.token.ANTNlHCUfbMlVSM0Lwv8Ga6Fi4KTrB7W646wKNvTGVJtqzVfzd8USJKNu2VN5NZl8I8S2BAg9oGNFezmQ"

# Off "Mon;4.5;Tue;4.5;Wen;4.5;Thu;4.5;Fri;4.5;Sat;4.5;Sun;4.5"
dayProfiles = {
    "Default": "17,06-00,21,09-00,17,17-00,21,22-00,17",
    "DefaultWE": "17,06-00,21,22-00,17",
    "Bedroom": "13,06-00,19,08-00,13,17-00,17,20-00,19,22-00,13",
    "BedroomWE": "13,07-00,19,09-00,15,17-00,17,20-00,19,22-00,13",
    "CoolBedroom": "11,06-00,15,08-00,11,17-00,15,20-00,15,22-00,11",
    "CoolBedroomWE": "11,07-00,15,09-00,11,17-00,15,20-00,15,22-00,11",
    "Bathroom": "11,06-00,19,08-00,13,20-00,19,22-00,11",
    "BathroomWE": "11,07-00,19,09-00,15,20-00,19,22-00,11",
    "Living": "11,08-00,17,18-00,19,22-00,11",
    "LivingWE": "11,08-00,19,22-00,11",
    "Kitchen": "11,06-00,19,08-00,13,12-00,17,13-00,13,17-00,17,18-00,19,21-00,11",
    "KitchenWE": "11,07-00,19,10-00,17,17-00,19,22-00,11",
    "Office": "11,08-00,19,22-00,11",
    "Off": "4.5",
    "Test1": "4.5,00-30,5.0,01-00,5.5,01-30,6.0,02-00,6.5,02-30,7.0,03-00,7.5,03-30,8.0,04-00,8.5,04-30,9.0,05-00,9.5,05-30,10.0,06-00,10.5",
    "Test2": "4.5,12-30,5.0,12-35,5.5,12-40,6.0,12-45,6.5,12-50,7.0,12-55,7.5,13-00,8.0,13-05,8.5,13-10,9.0,13-15,9.5,13-20,10.0,13-25,10.5",
}

def dailyProfile(mon, tue, wen, thu, fri, sat, sun):
    return "Mon;"+dayProfiles[mon]+";Tue;"+dayProfiles[tue]+";Wen;"+dayProfiles[wen]+";Thu;"+dayProfiles[thu]+";Fri;"+dayProfiles[fri]+";Sat;"+dayProfiles[sat]+";Sun;"+dayProfiles[sun]

def weeklyProfile(weekday, weekend = None):
    if weekend == None: weekend = weekday 
    return dailyProfile(weekday, weekday, weekday, weekday, weekday, weekend, weekend)

weekProfiles = {
    "Default": weeklyProfile("Default", "DefaultWE"),
    "Bedroom": weeklyProfile("Bedroom", "BedroomWE"),
    "Cool Bedroom": weeklyProfile("CoolBedroom", "CoolBedroomWE"),
    "Bathroom": weeklyProfile("Bathroom", "BathroomWE"),
    "Living": weeklyProfile("Living", "LivingWE"),
    "Kitchen": weeklyProfile("Kitchen", "KitchenWE"),
    "Office": weeklyProfile("Office", "LivingWE"),
    "Office Weekday": weeklyProfile("Office", "Off"),
    "Off": weeklyProfile("Off"),
    "Test1": weeklyProfile("Test1"),
    "Test2": weeklyProfile("Test2"),
}

#for p in weekProfiles:
#    print(p+" => "+weekProfiles[p])

profileSelect = ", ".join(map(lambda x: '"'+weekProfiles[x]+'"="'+x+'"', sorted(weekProfiles.keys()) ))

#print(profileSelect)

floors = [
    { "ftag": "GF", "fname": "Downstairs", "switch": 1, "rooms": [
        { "rtag": "H",  "rname": "Hall",           "icon": "corridor",       "address": "MEQ1458003" },
        { "rtag": "L",  "rname": "Lounge",         "icon": "sofa",           "address": ["OEQ1952222", "OEQ1952299"], "posn": ["F", "R"] },
        { "rtag": "W",  "rname": "Toilet",         "icon": "toilet",         "address": "MEQ1450552" },
        { "rtag": "K",  "rname": "Kitchen",        "icon": "kitchen",        "address": "OEQ1952225" },
        { "rtag": "U",  "rname": "Utility",        "icon": "washingmachine", "address": "MEQ1447569" },
        { "rtag": "O",  "rname": "Office",         "icon": "office",         "address": "MEQ1443223" },
        { "rtag": "P",  "rname": "Playroom",       "icon": "girl_3",         "address": "MEQ1449018" },
    ] },
    { "ftag": "FF", "fname": "Upstairs", "switch": 2, "rooms": [
        { "rtag": "UL", "rname": "Landing",           "icon": "corridor",       "address": "MEQ1455791" },
        { "rtag": "B1", "rname": "Master Bedroom",    "icon": "parents_3_3",    "address": "MEQ1452222" },
        { "rtag": "E1", "rname": "Master Ensuite",    "icon": "bath",           "address": "MEQ1449013" },
        { "rtag": "B2", "rname": "Bedroom 2",         "icon": "bedroom_blue",   "address": "JEQ0337555" },
        { "rtag": "E2", "rname": "Bedroom 2 Ensuite", "icon": "bath",           "address": "JEQ0253669" },
        { "rtag": "FB", "rname": "Family Bathroom",   "icon": "bath",           "address": "JEQ0687143" },
        { "rtag": "B5", "rname": "Bedroom 5",         "icon": "bedroom_red",    "address": "JEQ0252925" },
        { "rtag": "B3", "rname": "Alex's Bedroom",    "icon": "boy_3",          "address": "OEQ1955544" },
        { "rtag": "B4", "rname": "Kate's Bedroom",    "icon": "girl_3",         "address": "OEQ1419829" },
    ] },
]

string1 = '\n'.join(['Number\t{_rtag}_AT\t"Temperature{_posn}"\t<temperature>\t({rtag_AT}g{rtag}, g{rtag}_T, AT_{_rtag})\t["CurrentTemperature"]\t{{channel="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}:actual_temp"}}',
                     'Number\t{_rtag}_ST\t"Set{_posn}"\t<heating>\t({rtag_ST}, ST_{_rtag})\t["TargetTemperature"]\t{{channel="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}:set_temp"}}',
                     'Number\t{_rtag}_OT\t"Offset{_posn}"\t<heating>\t({rtag_OT}gOT, gOTE, OT_{_rtag})',
                     'String\t_{_rtag}_OT\t"Offset{_posn}"\t<heating>\t{{channel="http:url:maxculconfig:{address}_offsetTemp"}}',
                     'Number\t{_rtag}_VP\t"Valve{_posn}"\t<pressure>\t(g{rtag}, g{rtag}_T, VP_{_rtag})\t{{channel="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}:valve"}}',
                     'Switch\t{_rtag}_LB\t"Battery{_posn} [MAP(lb.map):%s]"\t<lowbattery>\t(_g{rtag}, _g{rtag}_T, LB_{_rtag})\t{{channel="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}:battery_low"}}',
                     'String\t{_rtag}_MD\t"Mode{_posn}"\t<switch>\t({rtag_MD}MD_{_rtag})\t{{channel="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}:mode"}}',
#                     'String\t{_rtag}_EMD\t"Mode{_posn}"\t<switch>\t({rtag_MD}_g{rtag}, EMD_{_rtag})\t{{channel="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}:extended_mode"}}',
#                     'String\t{_rtag}_AMD\t"Alexa Mode{_posn}"\t<switch>\t({rtag_AMD}_g{rtag})\t["homekit:HeatingCoolingMode"]',
                     'String\t{_rtag}_WP\t"Program{_posn}"\t<switch>\t({rtag_WP}WP_{_rtag})\t{{channel="http:url:maxculconfig:{address}_weekProfile"}}',
                     '',
                     'Group:Number\tAT_{_rtag}\t"{rname}{_posn}"\t<temperature>\t({AT_rtag}gAT_{ftag}, gT_{ftag}, gAT, gT)',
                     'Group:Number\tST_{_rtag}\t"{rname}{_posn}"\t<heating>\t({ST_rtag})',
                     'Group:Number\tOT_{_rtag}\t"{rname}{_posn} [%.1f °C]"\t<heating>',
                     'Group:Number\tVP_{_rtag}\t"{rname}{_posn}"\t<pressure>\t({VP_rtag}gVP_{ftag}, gVP, gVM_{ftag}, gVM)',
                     'Group:Switch\tLB_{_rtag}\t"{rname}{_posn} [MAP(lb.map):%s]"\t<lowbattery>\t(gLB, gLBE, gLBC)',
                     'Group:String\tMD_{_rtag}\t"{rname}{_posn}"\t<switch>\t(gMD, gMD_{ftag})',
                     'Group:String\tEMD_{_rtag}\t"{rname}{_posn}"\t<switch>\t(gEMD, gEMD_{ftag})',
                     'Group:String\tWP_{_rtag}\t"{rname}{_posn}"\t<switch>',
                     '',
                     ''])

def write_item_rule(fh, fromitem, toitem):
  fh.write('\n'.join(['rule "{fromitem}->{toitem}"',
                      'when',
                      '\tItem {fromitem} changed',
                      'then',
                      '\tvar newState = {fromitem}.state',
                      '\tif({toitem}.state != newState) {{',
                      '\t\tlogWarn("thermostat.rules", "{fromitem}["+previousState+"->"+{fromitem}.state+"]->{toitem}["+{toitem}.state+"->"+newState+"]")',
                      '\t\t{toitem}.postUpdate(newState)',
                      '\t}}',
                      'end',
                      '',
                      '']).format(fromitem=fromitem, toitem=toitem))

def write_rule(fh, item, tag):
    write_item_rule(fh, item+'_'+tag, tag+'_'+item)
    write_item_rule(fh, tag+'_'+item, item+'_'+tag)

def write_switch_rule(fh, tag):
    fh.write('\n'.join(['rule "gVP_{tag}->P_{tag}"',
                        'when',
                        '\tItem gVP changed or',
                        '\tItem gVM changed or',
                        '\tItem gVP_{tag} changed or',
                        '\tTime cron "0 0/1 * * * ?"',
                        'then',
                        '\tvar newState = if((gVM.state >= 99 || gVP.state >= 150) && gVP_{tag}.state >= 10) ON else OFF',
                        '\tif(P_{tag}.state != newState) {{',
                        '\t\tlogWarn("thermostat.rules", "gVP_{tag}["+(if(previousState!=null) previousState else gVP_{tag}.state)+"->"+gVP_{tag}.state+"]->P_{tag}["+P_{tag}.state+"->"+newState+"]")',
                        '\t\tP_{tag}.sendCommand(newState)',
                        '\t}}',
                        '\t',
                        'end',
                        '',
                        '']).format(tag=tag))

def write_alexa_rulef(fh, tag):
    fh.write('\n'.join(['rule "gEMD/gST_MAX_{tag}->AEMD_{tag}"',
                        'when',
                        '\tItem gEMD_{tag} changed or',
                        '\tItem gST_MAX_{tag} changed',
                        'then',
                        '\tvar newState = if(gEMD_{tag}.state == "MANUAL" && gST_MAX_{tag}.state == 4.5) OFF else transform("MAP", "alexamode.map", ""+gEMD_{tag}.state)',
                        '\tlogWarn("thermostat.rules", "gEMD/gST_MAX_{tag}["+(if(triggeringItem == gEMD_{tag}) previousState else gEMD_{tag}.state)+"->"+gEMD_{tag}.state+"/"+(if(triggeringItem == gST_MAX_{tag}) previousState else gST_MAX_{tag}.state)+"->"+gST_MAX_{tag}.state+"]->AEMD_{tag}["+AEMD_{tag}.state+"->"+newState+"]")',
                        '\tif(AEMD_{tag}.state != newState) {{',
                        '\t\tAEMD_{tag}.postUpdate(newState)',
                        '\t}}',
                        'end',
                        '',
                        '']).format(tag=tag))

def write_alexa_rule(fh, tag):
    pass
#    fh.write('\n'.join(['rule "{tag}_EMD->{tag}_AMD"',
#                        'when',
#                        '\tItem {tag}_EMD changed or',
#                        '\tItem {tag}_ST changed',
#                        'then',
#                        '\tlogWarn("thermostat.rules", "{tag}_EMD/ST["+{tag}_EMD.state+"/"+{tag}_ST.state+"]->{tag}_AMD["+{tag}_AMD.state+"]")',
#                        '\tif ( {tag}_EMD.state == "MANUAL" && {tag}_ST.state == 4.5 ) {{',
#                        '\t\t{tag}_AMD.postUpdate("OFF")',
#                        '\t}} else {{',
#                        '\t\t{tag}_AMD.postUpdate(transform("MAP", "alexamode.map", ""+{tag}_EMD.state))',
#                        '\t}}',
#                        'end',
#                        '',
#                        '']).format(tag=tag))

def write_config_things(fh, address):
    fh.write('\n'.join([
        '\t\t\t\tType string : {address}_offsetTemp "{address}_offsetTemp" [ stateTransformation="JSONPATH:$.configuration.offsetTemp", stateExtension="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}", commandExtension="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}/config", commandTransformation="JS:thermostatOffset.js" ]',
        '\t\t\t\tType string : {address}_weekProfile "{address}_weekProfile" [ stateTransformation="JSONPATH:$.configuration.weekProfile", stateExtension="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}", commandExtension="maxcul:thermostat:4b5e171fc9:bbd9c65639:{address}/config", commandTransformation="JS:weekProfile.js" ]',
        ''
        ]).format(address=address))

def write_offsettemp_rule(fh, tag):
    fh.write('\n'.join(['rule "{tag}_OT->_{tag}_OT"',
                        'when',
                        '\tItem {tag}_OT received command',
                        'then',
                        '\t\tlogWarn("thermostat.rules", "{tag}_OT received command " + receivedCommand)',
                        '\t\t_{tag}_OT.sendCommand(""+receivedCommand)',
                        'end',
                        #'',
                        #'rule "_{tag}_OT"',
                        #'when',
                        #'\tItem _{tag}_OT received command',
                        #'then',
                        #'\t\tlogWarn("thermostat.rules", "_{tag}_OT received command " + receivedCommand)',
                        #'end',
                        '',
                        'rule "_{tag}_OT->{tag}_OT"',
                        'when',
                        '\tItem _{tag}_OT received update',
                        'then',
                        #'\t\tlogWarn("thermostat.rules", "_{tag}_OT received update " + _{tag}_OT.state)',
                        '\t\t{tag}_OT.postUpdate(Double::parseDouble(_{tag}_OT.state.toString()))',
                        'end',
                        '',
                        #'rule "{tag}_OT"',
                        #'when',
                        #'\tItem {tag}_OT received update',
                        #'then',
                        #'\t\tlogWarn("thermostat.rules", "{tag}_OT received update " + {tag}_OT.state)',
                        #'end',
                        #'',
                        '']).format(tag=tag))

fh = open("/etc/openhab/items/thermostat.items", "w")

ru = open("/etc/openhab/rules/thermostat.rules", "w")
ru.write("import java.lang.Double.ParseDouble\n\n")

th = open("/etc/openhab/things/thermostat.things", "w")
th.write('\n'.join(['Thing http:url:maxculconfig "MAX! Bridge Config" [',
	                '\tbaseURL="http://openhabian:8080/rest/things",',
                    '\tauthMode="BASIC_PREEMPTIVE",',
                    '\tusername="oh.token.ANTNlHCUfbMlVSM0Lwv8Ga6Fi4KTrB7W646wKNvTGVJtqzVfzd8USJKNu2VN5NZl8I8S2BAg9oGNFezmQ",',
                    '\tpassword="",',
                    '\tcommandMethod="PUT",',
                    '\tcontentType="application/json",',
	                '\trefresh=15]',
                    '\t{',
	                '\t\tChannels:',
                    '']))

fh.write('\n'.join(['Group:Number:AVG\tgAT\t"Temperature [%.1f °C]"\t<temperature>',
                    'Group:Number:MAX\tgST\t"Set [%.1f °C]"\t<heating>',
                    'Group:Number:AVG\tgOT\t"Offset [%.1f °C]"\t<heating>',
                    'Group:Number:EQUALITY\tgOTE\t"Offset [%.1f °C]"\t<heating>',
                    'Group:Number:SUM\tgVP\t"Valve [%.1f %%]"\t<pressure>',
                    'Group:Number:MAX\tgVM\t"Valve Max [%.1f %%]"\t<pressure>',
                    'Group:Switch:OR(ON,OFF)\tgLB\t"Battery [MAP(lb.map):%s]"\t<lowbattery>',
                    'Group:Switch:EQUALITY\tgLBE\t"Battery [MAP(lb.map):%s]"\t<lowbattery>',
                    'Group:Number:COUNT("ON")\tgLBC\t"Battery [%d Low]"\t<lowbattery>',
                    'Group:String\tgMD\t"Mode"',
                    'Group:String\tgEMD\t"Mode"',
                    'Group\tgMAX',
                    #'Group\tET\t"External [%.1f °C]"\t<temperature>\t(gAT, gH_T, gL_T, gW_T, gK_T, gU_T, gO_T, gP_T, gUL_T, gB1_T, gE1_T, gB2_T, gE2_T, gFB_T, gB3_T, gB4_T, gB5_T)',
                    'Number\tChartPeriod',
                    '',
                    '']).format())
for floor in floors:
    fh.write('\n'.join(['Group\tg_{ftag}\t"{fname}"\t["Thermostat"]',
                        'Group:String\tgMD_{ftag}\t"{fname} - Mode"',
                        'Group:String\tgEMD_{ftag}\t"{fname} - Mode"',
                        'Group:Number:AVG\tgT_{ftag}\t"{fname} - Temperature [%.1f °C]"\t<temperature>',
                        'Group:Number:AVG\tgAT_{ftag}\t"{fname} - Temperature [%.1f °C]"\t<temperature>\t(g_{ftag})\t["CurrentTemperature"]',
                        'Group:Number:AVG\tgST_{ftag}\t"{fname} - Set [%.1f °C]"\t<heating>',
                        'Group:Number:MAX\tgST_MAX_{ftag}\t"{fname} - Set Max [%.1f °C]"\t<heating>\t(g_{ftag})',
                        'Number\tAST_{ftag}\t"{fname} - Alexa Set [%.1f °C]"\t<heating>\t(g_{ftag})\t["TargetTemperature"]',
                        'String\tAEMD_{ftag}\t"{fname} - Alexa Mode"\t<switch>\t(g_{ftag})\t["homekit:HeatingCoolingMode"]',
                        'Group:Number:SUM\tgVP_{ftag}\t"{fname} - Valve [%.0f %%]"\t<pressure>',
                        'Group:Number:MAX\tgVM_{ftag}\t"{fname} - Valve Max [%.0f %%]"\t<pressure>',
                        #'Switch\tPPP_{ftag}\t"{fname} - Pump [%s]"\t{{http=">[ON:GET:http://192.168.0.157/cm?cmnd=Power{switch}%%20on] >[OFF:GET:http://192.168.0.157/cm?cmnd=Power{switch}%%20off] <[http://192.168.0.157/cm?cmnd=Power{switch}:30000:JSONPATH($.*)]"}}',
                        '',
                        '']).format(**floor))
    write_switch_rule(ru, floor["ftag"])
    write_alexa_rulef(ru, floor["ftag"])
    for room in floor["rooms"]:
        if isinstance(room["address"], list):
            d = {**room, **floor}
            fh.write('\n'.join(['Group:Number:AVG\tg{rtag}\t"{rname}"\t["Thermostat"]',
                                'Group:Number:AVG\tg{rtag}_T\t"{rname}"',
                                'Group:Number:AVG\t{rtag}_AT\t"Temperature [%.1f °C]"\t<temperature>',
                                'Group:Number:AVG\t{rtag}_ST\t"Set [%.1f °C]"\t<heating>\t(g{rtag}, g{rtag}_T)', 
                                'Group:Number:AVG\t{rtag}_OT\t"Offset [%.1f °C]"\t<heating>', 
                                'Group:String\t{rtag}_MD\t"Mode [%s]"\t<switch>',
#                                'Group:String\t{rtag}_AMD\t"Alexa Mode [%s]"\t<switch>',
                                'Group:String\t{rtag}_WP\t"Program [%s]"\t<switch>',
                                'Group:Number:AVG\tST_{rtag}\t"{rname} [%.1f °C]"\t<heating>\t(gST_{ftag}, gST_MAX_{ftag}, gT_{ftag}, gST, gT)',
                                'Group:Number:AVG\tAT_{rtag}\t"{rname} [%.1f °C]"\t<temperature>',
                                'Group:Number:SUM\tVP_{rtag}\t"{rname} [%.0f %%]"\t<pressure>',
                                '',
                                '']).format(**d))
            for index in range(len(room["address"])):
                d = {**room, **floor}
                d["_rtag"] = '{rtag}{posn}'.format(rtag=room["rtag"], posn=room["posn"][index])
                d["_posn"] = ' ({posn})'.format(rname=room["rname"], posn=room["posn"][index])
                d["address"] = room["address"][index]
                d["rtag_AT"] = '{rtag}_AT, '.format(**room)
                d["rtag_ST"] = '{rtag}_ST'.format(**room)
                d["rtag_OT"] = '{rtag}_OT, '.format(**room)
                d["rtag_MD"] = '{rtag}_MD, '.format(**room)
#                d["rtag_AMD"] = '{rtag}_AMD, '.format(**room)
                d["rtag_WP"] = '{rtag}_WP, '.format(**room)
                d["AT_rtag"] = 'AT_{rtag}, '.format(**room)
                d["ST_rtag"] = 'ST_{rtag}'.format(**room)
                d["VP_rtag"] = 'VP_{rtag}, '.format(**room)
                fh.write(string1.format(**d))
                #write_rule(ru, 'ST', d["_rtag"])
                #write_rule(ru, 'MD', d["_rtag"])
                write_config_things(th, d["address"])
                write_offsettemp_rule(ru, d["_rtag"])
        else:
                d = {**room, **floor}
                d["_rtag"] = d["rtag"]
                d["_posn"] = ''
                d["rtag_AT"] = ''
                d["rtag_ST"] = 'g{rtag}, g{rtag}_T'.format(**room)
                d["rtag_OT"] = ''
                d["rtag_MD"] = ''
#                d["rtag_AMD"] = 'g{rtag}, '.format(**room)
                d["rtag_WP"] = ''
                d["AT_rtag"] = ''
                d["ST_rtag"] = 'gST_{ftag}, gST_MAX_{ftag}, gT_{ftag}, gST, gT'.format(**d)
                d["VP_rtag"] = ''
                fh.write('\n'.join(['Group:Number:AVG\tg{rtag}\t"{rname}"\t["Thermostat"]',
                                    'Group:Number:AVG\tg{rtag}_T\t"{rname}"',
                                    '',
                                    '']).format(**room))
                fh.write(string1.format(**d))
                #write_rule(ru, 'ST', d["rtag"])
                #write_rule(ru, 'MD', d["rtag"])
                write_alexa_rule(ru, d["rtag"])
                write_config_things(th, d["address"])
                write_offsettemp_rule(ru, d["rtag"])
fh.close()
ru.close()
th.write('\t}\n')
th.close()

fh = open("/etc/openhab/sitemaps/thermostat.sitemap", "w")
fh.write('\n'.join(['sitemap thermostat label="Thermostats" {',
                    '\tFrame label="Overview" {',
                    '\t\tText item=gLB visibility=[gLBE!=UNDEF]',
                    '\t\tText item=gLBC visibility=[gLBE==UNDEF] {',
                    '']))
for floor in floors:
    for room in floor["rooms"]:
        if isinstance(room["address"], list):
            for index in range(len(room["address"])):
                d = {**room}
                d["posn"] = room["posn"][index]
                fh.write('\n'.join(['\t\t\tText item=LB_{rtag}{posn} icon="{icon}"',
                                    '']).format(**d))
        else:
            fh.write('\n'.join(['\t\t\tText item=LB_{rtag} icon="{icon}"',
                                '']).format(**room))
fh.write('\n'.join(['\t\t}',
                    '\t\tSelection item=gMD icon="switch" visibility=[gMD!=UNDEF] mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation"]',
                    '\t\tText item=gMD label="Mode [Various]" icon="switch" visibility=[gMD==UNDEF] {',
                    '\t\t\tSelection item=gMD label="Home" icon="group" mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation"]',
                    #'\t\tSelection item=gEMD icon="switch" visibility=[gEMD!=UNDEF] mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation", "OFF"="OFF", "ECO"="ECO", "COMFORT"="COMFORT", "ON"="ON"]',
                    #'\t\tText item=gEMD label="Mode [Various]" icon="switch" visibility=[gEMD==UNDEF] {',
                    #'\t\t\tSelection item=gEMD label="Home" icon="group" mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation", "OFF"="OFF", "ECO"="ECO", "COMFORT"="COMFORT", "ON"="ON"]',
                    '']))
for floor in floors:
    for room in floor["rooms"]:
        if isinstance(room["address"], list):
            for index in range(len(room["address"])):
                d = {**room}
                d["posn"] = room["posn"][index]
                fh.write('\n'.join(['\t\t\tSelection item=MD_{rtag}{posn} icon="{icon}" mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation"]',
                                    '']).format(**d))
#                fh.write('\n'.join(['\t\t\tSelection item=MD_{rtag}{posn} icon="{icon}" mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation", "OFF"="OFF", "ECO"="ECO", "COMFORT"="COMFORT", "ON"="ON"]',
#                                    '']).format(**d))
        else:
            fh.write('\n'.join(['\t\t\tSelection item=MD_{rtag} icon="{icon}" mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation"]',
                                '']).format(**room))
#            fh.write('\n'.join(['\t\t\tSelection item=MD_{rtag} icon="{icon}" mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation", "OFF"="OFF", "ECO"="ECO", "COMFORT"="COMFORT", "ON"="ON"]',
#                                '']).format(**room))
fh.write('\n'.join(['\t\t}',
                    '\t}',
                    '']))
for floor in floors:
    fh.write('\n'.join(['\tFrame label="{fname}" item=gAT_{ftag} {{',
                        #'\t\tSelection item=gEMD_{ftag} mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation", "OFF"="OFF", "ECO"="ECO", "COMFORT"="COMFORT", "ON"="ON"]',
                        #'\t\tText item=gEMD_{ftag}',
                        #'\t\tSelection item=AEMD_{ftag} mappings=["AUTO"="AUTO", "COOL"="COOL", "HEAT"="HEAT", "ECO"="ECO", "OFF"="OFF"]',
                        '\t\tSetpoint label="Set [%.1f °C]" item=gST_MAX_{ftag} minValue=4.5 maxValue=30 step=0.5',
                        '']).format(**floor))
    for room in floor["rooms"]:
        fh.write('\n'.join(['\t\tText item=AT_{rtag} label="{rname} [%.1f °C]" icon="{icon}" valuecolor=[VP_{rtag}>0="red"] {{',
                            #'\t\t\tDefault item=g{rtag}',
                            '\t\t\tSelection item={rtag}_MD mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation"]',
#                            '\t\t\tSelection item={rtag}_MD mappings=["AUTOMATIC"="Automatic", "MANUAL"="Manual", "BOOST"="Boost", "VACATION"="Vacation", "OFF"="OFF", "ECO"="ECO", "COMFORT"="COMFORT", "ON"="ON"]',
#                            '\t\t\tSelection item={rtag}_AMD mappings=["AUTO"="AUTO", "COOL"="COOL", "HEAT"="HEAT", "ECO"="ECO", "OFF"="OFF"]',
                            '\t\t\tSelection item={rtag}_WP mappings=['+profileSelect+']',
                            '\t\t\tSetpoint item={rtag}_ST label="Set [%.1f °C]" minValue=4.5 maxValue=30 step=0.5',
                            '\t\t\tSetpoint item={rtag}_OT label="Offset [%.1f °C]" minValue=-3.5 maxValue=3.5 step=0.5',
                            '']).format(**room))
        if isinstance(room["address"], list):
            for index in range(len(room["address"])):
                d = {**room}
                d["posn"] = room["posn"][index]
                fh.write('\n'.join(['\t\t\tDefault item={rtag}{posn}_AT label="Temperature ({posn}) [%.1f °C]"',
                                    '']).format(**d))
            for index in range(len(room["address"])):
                d = {**room}
                d["posn"] = room["posn"][index]
                fh.write('\n'.join(['\t\t\tDefault item={rtag}{posn}_VP label="Valve ({posn}) [%.0f %%]"',
                                    '']).format(**d))
            for index in range(len(room["address"])):
                d = {**room}
                d["posn"] = room["posn"][index]
                fh.write('\n'.join(['\t\t\tText item={rtag}{posn}_LB',
                                    '']).format(**d))
        else:
            fh.write('\n'.join(['\t\t\tDefault item={rtag}_AT label="Temperature [%.1f °C]"',
                                '\t\t\tDefault item={rtag}_VP label="Valve [%.0f %%]"',
                                '\t\t\tText item={rtag}_LB',
                                '']).format(**room))
        fh.write('\n'.join(['\t\t\tChart item=g{rtag}_T period=h refresh=6000 visibility=[ChartPeriod==0, ChartPeriod=="Uninitialized"]',
                            '\t\t\tChart item=g{rtag}_T period=D refresh=30000 visibility=[ChartPeriod==1]',
                            '\t\t\tChart item=g{rtag}_T period=W refresh=30000 visibility=[ChartPeriod==2]',
                            '\t\t\tSwitch item=ChartPeriod label="Chart Period" mappings=[0="Hour", 1="Day", 2="Week"]',
                            '\t\t}}',
                            '']).format(**room))

    fh.write('\n'.join(['\t\tText item=gVP_{ftag} label="Valve [%.0f %%]"',
                        '\t\tText item=gVM_{ftag} label="Valve Max [%.0f %%]"',
                        '\t\tText item=P_{ftag} label="Pump [%s]" icon="switch"',
                        #'\t\tDefault item=P_{ftag} label="Pump [%s]" icon="switch"',
                        '\t\tChart item=gVP_{ftag} period=h refresh=6000 visibility=[ChartPeriod==0, ChartPeriod=="Uninitialized"]',
                        '\t\tChart item=gVP_{ftag} period=D refresh=30000 visibility=[ChartPeriod==1]',
                        '\t\tChart item=gVP_{ftag} period=W refresh=30000 visibility=[ChartPeriod==2]',
                        '\t\tSwitch item=ChartPeriod label="Chart Period" mappings=[0="Hour", 1="Day", 2="Week"]',
                        '\t}}',
                        '']).format(**floor))

fh.write('\n'.join(['\tFrame label="Details" {',
                    '\t\tText label="Temperature" item=gAT',
                    '\t\tText label="External [%.1f °C]" item=ET',
                    '\t\tChart item=gAT period=h refresh=6000 visibility=[ChartPeriod==0, ChartPeriod=="Uninitialized"]',
                    '\t\tChart item=gAT period=D refresh=30000 visibility=[ChartPeriod==1]',
                    '\t\tChart item=gAT period=W refresh=30000 visibility=[ChartPeriod==2]',
                    '',
                    '\t\tText label="Set" item=gST',
                    '\t\tSetpoint item=gOTE visibility=[gOTE!=UNDEF] minValue=-3.5 maxValue=3.5 step=0.5',
                    '\t\tText item=gOT visibility=[gOTE==UNDEF] {',
                    '\t\t\tSetpoint item=gOT minValue=-3.5 maxValue=3.5 step=0.5',
                    '']))

for floor in floors:
    for room in floor["rooms"]:
        if isinstance(room["address"], list):
            for index in range(len(room["address"])):
                d = {**room}
                d["posn"] = room["posn"][index]
                fh.write('\n'.join(['\t\t\tSetpoint item=OT_{rtag}{posn} icon="{icon}" minValue=-3.5 maxValue=3.5 step=0.5',
                                    '']).format(**d))
        else:
            fh.write('\n'.join(['\t\t\tSetpoint item=OT_{rtag} icon="{icon}" minValue=-3.5 maxValue=3.5 step=0.5',
                                '']).format(**room))

fh.write('\n'.join(['\t\t}',
                    '\t\tChart item=gST period=h refresh=6000 visibility=[ChartPeriod==0, ChartPeriod=="Uninitialized"]',
                    '\t\tChart item=gST period=D refresh=30000 visibility=[ChartPeriod==1]',
                    '\t\tChart item=gST period=W refresh=30000 visibility=[ChartPeriod==2]',
                    '',
                    '\t\tText label="Valve" item=gVP',
                    '\t\tText label="Valve Max" item=gVM',
                    '\t\tChart item=gVP period=h refresh=6000 visibility=[ChartPeriod==0, ChartPeriod=="Uninitialized"]',
                    '\t\tChart item=gVP period=D refresh=30000 visibility=[ChartPeriod==1]',
                    '\t\tChart item=gVP period=W refresh=30000 visibility=[ChartPeriod==2]',
                    '',
                    '\t\tSwitch item=ChartPeriod label="Chart Period" mappings=[0="Hour", 1="Day", 2="Week"]',
                    '\t}',
                    '',
                    '\tFrame label="Server" {',
                    '\t\tText label="Memory" item=Systeminfo_UsedMemory',
                    '\t\tText label="Storage" item=Systeminfo_UsedStorage',
                    '\t\tText label="Load" item=Systeminfo_Load',
                    '\t\tChart item=Systeminfo_Used period=h refresh=6000 visibility=[ChartPeriod==0, ChartPeriod=="Uninitialized"]',
                    '\t\tChart item=Systeminfo_Used period=D refresh=30000 visibility=[ChartPeriod==1]',
                    '\t\tChart item=Systeminfo_Used period=W refresh=30000 visibility=[ChartPeriod==2]',
                    '',
                    '\t\tSwitch item=ChartPeriod label="Chart Period" mappings=[0="Hour", 1="Day", 2="Week"]',
                    '\t}',
                    '}',
                    '']))
fh.close()


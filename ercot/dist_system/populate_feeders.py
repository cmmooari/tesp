import json;
import tesp_support.feederGenerator as fg;

backbone_config = {'backbone_feeders': {
  'sim_R5-12.47-1':{'vll':13800.0, 'vln':7970.0, 'avg_house':6500.0, 'avg_comm':20000.0},
  'sim_R5-12.47-2':{'vll':12470.0, 'vln':7200.0, 'avg_house':4500.0, 'avg_comm':15000.0},
  'sim_R5-12.47-4':{'vll':12470.0, 'vln':7200.0, 'avg_house':6000.0, 'avg_comm':30000.0},
  'sim_R5-12.47-5':{'vll':12470.0, 'vln':7200.0, 'avg_house':4500.0, 'avg_comm':25000.0}},
                   'outpath':'../case8/',
                   'glmpath':'./',
                   'supportpath':'../../support/schedules/',  # wrt outpath
                   'weatherpath':'../../support/weather/'}    # wrt outpath

#inverterModesBattery = ['GROUP_LOAD_FOLLOWING','LOAD_FOLLOWING','VOLT_VAR_FREQ_PWR','VOLT_WATT','VOLT_VAR','CONSTANT_PF','CONSTANT_PQ','NONE'];
#inverterModesPV = ['VOLT_VAR_FREQ_PWR','VOLT_WATT','VOLT_VAR','CONSTANT_PF','CONSTANT_PQ','NONE'];
#billingModes = ['TIERED_TOU','TIERED_RTP','HOURLY','TIERED','UNIFORM','NONE'];
#eplusVoltageChoices = ['208', '480'];

case_config = {'SimulationConfig':{
	'CaseName':'Bus1',
  'StartTime':'2013-07-01 00:00:00',
  'EndTime':'2013-07-02 00:00:00',
	'SourceDirectory':'~/src/tesp/support'},
               'FeederGenerator':{
               'MetricsInterval':300,
               'MinimumStep':15,
               'ElectricCoolingPercentage':90,
               'ElectricCoolingParticipation':50,
               'SolarPercentage':0,
               'StoragePercentage':20,
               'SolarInverterMode':'CONSTANT_PF',
               'StorageInverterMode':'LOAD_FOLLOWING',
               'BillingMode':'TIERED',
               'MonthlyFee':13,
               'Price':0.102013,
               'Tier1Energy':500,
               'Tier2Energy':1000,
               'Tier3Energy':0,
               'Tier1Price':0.117013,
               'Tier2Price':0.122513,
               'Tier3Price':0,
               'EnergyPlusBus':'',
               'EnergyPlusServiceV': 480, # 208 or 480
               'EnergyPlusXfmrKva':250},
               'BackboneFiles':{'TaxonomyChoice':'sim_R5-12.47-1'},
               'WeatherPrep':{'DataSource':'TX-Houston_Bush_Intercontinental.tmy3'},
               'PYPOWERConfiguration':{
               'TransformerBase':12,
							 'TransmissionVoltage':345}
							 }

bus_config = [
	{'bus':1, 'feeder':'sim_R5-12.47-1', 'weather':'TX-Houston_Bush_Intercontinental.tmy3'},
	{'bus':2, 'feeder':'sim_R5-12.47-2', 'weather':'TX-Houston_Bush_Intercontinental.tmy3'},
	{'bus':3, 'feeder':'sim_R5-12.47-4', 'weather':'TX-Wichita_Falls_Municipal_Arpt.tmy3'},
	{'bus':4, 'feeder':'sim_R5-12.47-2', 'weather':'TX-Houston_Bush_Intercontinental.tmy3'},
	{'bus':5, 'feeder':'sim_R5-12.47-2', 'weather':'TX-Houston_Bush_Intercontinental.tmy3'},
	{'bus':6, 'feeder':'sim_R5-12.47-4', 'weather':'TX-Houston_Bush_Intercontinental.tmy3'},
	{'bus':7, 'feeder':'sim_R5-12.47-4', 'weather':'TX-Houston_Bush_Intercontinental.tmy3'},
	{'bus':8, 'feeder':'sim_R5-12.47-5', 'weather':'TX-El_Paso_International_Ap_Ut.tmy3'},
	]

for i in range(len(bus_config)):
	print ('** populating', bus_config[i]['feeder'], 'for bus', bus_config[i]['bus'], 'in', bus_config[i]['weather'])
	case_config['BackboneFiles']['TaxonomyChoice'] = bus_config[i]['feeder']
	case_config['WeatherPrep']['DataSource'] = bus_config[i]['weather']
	case_config['SimulationConfig']['CaseName'] = 'Bus' + str(bus_config[i]['bus'])
	fg.populate_feeder (config=case_config, taxconfig=backbone_config)




char1 = {'name':'Bella','age':15,'health':100, 'bag':['phone','food'],'str': 20,'attack':{'type':'slap','dmg':5}}
char2 = {'name':'levi','age':17,'health':95, 'bag':['money','knife','water'],'str': 40,'attack':{'type':'stab','dmg':18}}
char3 = {'name':'armin','age':16,'health':92, 'bag':['first aid kit'],'str': 5,'attack':{'type':'hit','dmg':10}}
char4 = {'name':'zoe','age':14,'health':95, 'bag':['lighter','stick'],'str':12,'attack':{'type':'fire','dmg':13}}
#def
def fight(opp1,opp2):
    
    print(opp1)
    print(opp2)
    print('fighting...')
    opp1['health'] -= opp2.get('attack').get('dmg')
    opp2['health'] -= opp1.get('attack').get('dmg')
    #char2['health'] -= 10
    #char3['health'] -= 18
    print(opp1)
    print(opp2)

fight(char1,char4)
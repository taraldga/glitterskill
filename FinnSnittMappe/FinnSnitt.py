# -*- coding: utf-8 -*-
import os
from sets import Set
import os
import re
import collections


def fileread(fname): 
    script_dir = os.path.dirname(__file__)
    with open (os.path.join(script_dir,"ads", "ad-contents", fname)) as myfile:
        data=myfile.read()
    return data

def fileread2(fname): 
    script_dir = os.path.dirname(__file__)
    with open (os.path.join(script_dir,"ikkeData","ads", "ad-contents", fname)) as myfile:
        data=myfile.read()
    return data   
         

def dirListing(fileplacement):
    dirList = os.listdir(fileplacement)
    alldata = ''
    for fname in dirList:
        #print fname
        data = fileread(fname)
        #print data
        alldata = alldata + data
    return alldata

def dirListing2(fileplacement):
    dirList = os.listdir(fileplacement)
    alldata = ''
    for fname in dirList:
        #print fname
        data = fileread2(fname)
        #print data
        alldata = alldata + data
    return alldata
    
def Kjellspython(data,tresholdvalue,stopwords):
    Rawdata = data
    Stopwords = stopwords
    ReRawdata=' '.join(filter(lambda x: x.lower() not in Stopwords,  Rawdata.split(' ')))
    words = re.findall('\w+', ReRawdata.lower())
    print collections.Counter(words).most_common(tresholdvalue)
    return collections.Counter(words).most_common(tresholdvalue)
    
def SagaomString():
    script_dir = os.path.dirname(__file__)
    with open (os.path.join(script_dir, 'sagaenomisfolket.txt')) as myfile:
	words = re.findall('\w+', myfile.read().lower())
	cool = collections.Counter(words).most_common(5000)
	string = ''
	n=4999
	for i in range(n):
		string = string + ' ' +cool[i][0]
    return string

def main():
    
    fileplacement = r"C:\Users\BeateHaram\Documents\Eit\glitterskill\ads\ad-contents" #It-annonser
    filedeplacement = r"C:\Users\BeateHaram\Documents\Eit\glitterskill\ikkeData\ads\ad-contents" #Alle andre annonser
    alldata = dirListing(fileplacement)
    ikkedata = dirListing2(filedeplacement)
    
    tresholdvalue = 60;
    test1 = Kjellspython(alldata, tresholdvalue, ikkedata)
    

    print('-----------------------------------------')
    bok = SagaomString()
    test2 = Kjellspython(alldata, tresholdvalue, bok)
    print('-----------------------------------------')
    Stopwords = ['og','i','det','på','som', 'er' ,'en','til','å','han','av','for','med','at','var','de','ikke','den','har','jeg','om','et','men','så','seg','hun','hadde','fra','vi','du','kan','da','ble','ut','skal','vil','ham','etter','over','ved','også','bare','eller','sa','nå','dette','noe','være','meg','mot','opp','der','når','inn','dem','kunne','andre','blir','alle','noen','sin','ha','år','henne','må','selv','sier','få','kom','denne','enn','to','hans','bli','ville','før','vært','skulle','går','her','slik','gikk','mer','hva','igjen','fikk','man','alt','mange','dash','ingen','får','oss','hvor','under','siden','hele','dag','gang','sammen','ned','kommer','sine','deg','se','første','godt','mellom','måtte','gå','helt','litt','nok','store','aldri','ta','sig','uten','ho','kanskje','blitt','ser','hvis','bergen','sitt','jo','vel','si','vet','hennes','min','tre','ja','samme','mye','nye','tok','gjøre','disse','siste','tid','rundt','tilbake','mens','satt','flere','folk','1','fordi','både','la','gjennom','fått','like','nei','annet','komme','kroner','gjorde','hvordan','2','norge','norske','gjør','oslo','står','stor','gamle','langt','annen','sett','først','mener','hver','barn','rett','ny','tatt','derfor','fram','hos','heller','lenge','alltid','tror','nesten','mann','gi','god','lå','blant','norsk','gjort','visste','bak','tar','liv','mennesker','frem','bort','ein','verden','deres','ikkje','000','tiden','del','vår','mest','eneste','likevel','hatt','dei','tidligere','fire','liten','hvorfor','tenkte','hverandre','holdt','bedre','meget','ting','lite','3','stod','ei','hvert','begynte','gir','ligger','grunn','dere','livet','a','sagt','land','4','kommet','e','neste','far','efter','egen','side','gått','mor','ute','videre','5','millioner','prosent','svarte','sto','begge','allerede','inne','finne','enda','hjem','foran','måte','10','mannen','dagen','hodet','saken','ganger','kjente','stort','blev','mindre','20','landet','byen','plass','kveld','ord','øynene','fem','større','gode','nu','synes','beste','kvinner','ett','satte','hvem','all','9','klart','holde','ofte','stille','spurte','lenger','sted','dager','mulig','utenfor','små','frå','nytt','slike','viser','30','mig','kjenner','samtidig','senere','særlig','våre','akkurat','menn','hørte','mdash','arbeidet','altså','par','din','unge','n','borte','plutselig','fant','fast','kunde','snart','svært','fall','vei','bergens','dessuten','forhold','gjerne','snakket','foto','6','snakke','bør','dersom','imidlertid','lett','tenke','gud','tro','15','jan','gitt','penger','egentlig','mitt','ønsker','ansiktet','kl','dermed','00','slo','12','politiet','faren','eit','bra','je','sitter','sikkert','vite','full','lille','18','glad','fleste','slutt','ene','mine','gjelder','lagt','virkelig','laget','alene','ennå','lang','ganske','johan','omkring','hjemme','vårt','vanskelig','arne','gammel','skulde','tidende','riktig','huset','følte','møte','lørdag','klar','m','kort','viktig','ellers','minst','fortsatt','op','veien','seier','mål','kjent','slags','frode','8','7','stund','arbeid','finnes','ingenting','lange','gangen','stå','lot','rekke','redd','høre','vilde','ga','ti','forteller','overfor','stadig','burde','visst','syntes','fjor','sette','funnet','hjelp','største','løpet','meter','norges','hånden','spørsmål','s','mente','søndag','f','følge','fremdeles','imot','11','hus','kvinne','ventet','reiste','hendene','trodde','usa','legger','viste','regjeringen','eg','årene','eksempel','tenkt','ole','slikt','erik','moren','holder','seks','tenker','19','stedet','tillegg','helst','bruke','skolen','kampen','nettopp','døren','egne','eget','sterkt','betyr','vant','enkelte','nærmere','hvad','50','dårlig','per','trenger','menneske','måten','vise','oppe','finner','legge','and','the','in','of','innen','jobbe','with','arbeidsgiveren','kunder','spennende','as','tilbyr','is','you','faglig','our','kompetanse','are','innenfor','experience','on','kvalifikasjoner','erfaring','utvikle','utvikling','prosjekter','ledende','we','relevant','utvikler','stillingen','work','arbeidsoppgaver','be','egenskaper','jobber','bidra','utdanning','development','kjennskap','teknologi','evne','ansvar','ansatte','will','mulighet','tjenester','medarbeidere','muligheter','an','teknisk','that']
    test3 = Kjellspython(alldata,tresholdvalue, Stopwords)
    
if __name__ == '__main__':main()
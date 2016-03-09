# -*- coding: utf-8 -*-
import os
import re
import collections
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fileread(fname): 
    script_dir = os.path.dirname(__file__)
    with open (os.path.join(script_dir,"ads", "ad-contents", fname)) as myfile:
        data=myfile.read()
    return data
   
#path = 'ads\ad-contents'
#for filename in os.listdir(path):
#x = os.listdir(path)
#print x

def dirListing():
    dirList = os.listdir(r"C:\Users\BeateHaram\Documents\Eit\glitterskill\ads\ad-contents")
    alldata = ''
    for fname in dirList:
        #print fname
        data = fileread(fname)
        #print data
        alldata = alldata + data
    return alldata

def kjellspyton(x,y):
    #Rawdata = 'Unit4 AS0401 OSLO Unit4 er en ledende leverandør av forretningssystemer til tjenesteytende virksomheter og offentlig sektor. Vi leverer ERP, bransjespesifikke forretningsløsninger og applikasjoner. Tusenvis av tjenesteytende virksomheter innen konsulent, utdanning, offentlige tjenester, organisasjonslivet, media, eiendom, engros, bank og finans bruker i dag løsninger fra Unit4. Konsernet har en årlig omsetning på over 500 mill euro og mer enn 4000 ansatte på verdensbasis. Unit4  in business for people.JuniorkonsulenterJuniorkonsulenter NORDISK OPPLÆRINGSPROGRAM Unit4 (Unit4 Business World)Vi styrker konsulentavdelingen i Norden, og her i Norge skal vi ansette 2 kandidater som vil inngå i et nordisk opplæringsprogram. Du vil bli en del av teamet i den norske konsulentavdelingen som utfører rådgivning og implementering relatert til produktene i Unit4 sin portefølje.Konsulentavdelingen tilbyr et bredt spekter av konsulenttjenester relatert til Unit4 Business World (AGRESSO) og andre løsninger i Unit4 sin portefølje. Kundene er store og mellomstore bedrifter og prosjektene er utfordrende, med stor variasjon i kompleksitet og størrelse. Våre oppdrag utføres i henhold til vår standard metodikk for prosjektgjennomføring. Noen av prosjektene gjennomføres helt eller delvis i utlandet.ArbeidsområderHovedområdet ditt vil bli å implementere UBW (AGRESSO) hos våre kunder, sammen med våre seniorkonsulenter. Du vil jobbe tett med en mentor innenfor ditt fagområde som vi tenker du skal utvikle deg i. Noen av arbeidsoppgavene vil være:Bygge opp/ sette opp UBW etter en designet løsningTeste løsningen/ prosessenAvholde kundeopplæring/ kursDelta i workshopperDokumentere løsningJobbe med problemstillinger hos kundenØnsket erfaring/ utdanningDu er nyutdannet, eller har jobbet 12 år som itkonsulent, regnskapsmedarbeider, revisor, lønnskonsulent eller tilsvarende. Utdanning på universitet/ høyskolenivå er et krav.Personlige egenskaperDu er ivrig etter å lære enda mer og bli godt kjent med et ERP system. Du syns tabeller og SQL kan være spennende, og du er ikke redd for å prøve noe nytt. Du evner til å lytte og kommunisere tydelig på norsk, så vel som på engelsk. I perioder må du regne med en del reising.Vi tilbyrVarierte og utfordrende arbeidsoppgaverArbeid med et internasjonalt ledende ERP systemMeget godt og utviklende arbeidsmiljøInternasjonale muligheter Sted: Oslo  Tiltredelse: Snarest Kontakter: Annette Waage Braate, , mob: 47 48012597, epost: annette.braate@unit4.com For elektronisk søknadsskjema: [Klikk her] Søknadsfrist: 03.03.2016Stillingsnummer: 031920160210 (Oppgis ved kontakt med NAV)Kilde: NAV ServicesenterArbeidsstedOsloAntall stillinger2Søknadsfrist03.03.2016Siste publiseringsdato03.03.2016Registrert04.02.2016'
    Rawdata = x
    #Rawdata = Rawdata.encode('utf-8')
    Stopwords = ['og','i','det','på','som', 'er' ,'en','til','å','han','av','for','med','at','var','de','ikke','den','har','jeg','om','et','men','så','seg','hun','hadde','fra','vi','du','kan','da','ble','ut','skal','vil','ham','etter','over','ved','også','bare','eller','sa','nå','dette','noe','være','meg','mot','opp','der','når','inn','dem','kunne','andre','blir','alle','noen','sin','ha','år','henne','må','selv','sier','få','kom','denne','enn','to','hans','bli','ville','før','vært','skulle','går','her','slik','gikk','mer','hva','igjen','fikk','man','alt','mange','dash','ingen','får','oss','hvor','under','siden','hele','dag','gang','sammen','ned','kommer','sine','deg','se','første','godt','mellom','måtte','gå','helt','litt','nok','store','aldri','ta','sig','uten','ho','kanskje','blitt','ser','hvis','bergen','sitt','jo','vel','si','vet','hennes','min','tre','ja','samme','mye','nye','tok','gjøre','disse','siste','tid','rundt','tilbake','mens','satt','flere','folk','1','fordi','både','la','gjennom','fått','like','nei','annet','komme','kroner','gjorde','hvordan','2','norge','norske','gjør','oslo','står','stor','gamle','langt','annen','sett','først','mener','hver','barn','rett','ny','tatt','derfor','fram','hos','heller','lenge','alltid','tror','nesten','mann','gi','god','lå','blant','norsk','gjort','visste','bak','tar','liv','mennesker','frem','bort','ein','verden','deres','ikkje','000','tiden','del','vår','mest','eneste','likevel','hatt','dei','tidligere','fire','liten','hvorfor','tenkte','hverandre','holdt','bedre','meget','ting','lite','3','stod','ei','hvert','begynte','gir','ligger','grunn','dere','livet','a','sagt','land','4','kommet','e','neste','far','efter','egen','side','gått','mor','ute','videre','5','millioner','prosent','svarte','sto','begge','allerede','inne','finne','enda','hjem','foran','måte','10','mannen','dagen','hodet','saken','ganger','kjente','stort','blev','mindre','20','landet','byen','plass','kveld','ord','øynene','fem','større','gode','nu','synes','beste','kvinner','ett','satte','hvem','all','9','klart','holde','ofte','stille','spurte','lenger','sted','dager','mulig','utenfor','små','frå','nytt','slike','viser','30','mig','kjenner','samtidig','senere','særlig','våre','akkurat','menn','hørte','mdash','arbeidet','altså','par','din','unge','n','borte','plutselig','fant','fast','kunde','snart','svært','fall','vei','bergens','dessuten','forhold','gjerne','snakket','foto','6','snakke','bør','dersom','imidlertid','lett','tenke','gud','tro','15','jan','gitt','penger','egentlig','mitt','ønsker','ansiktet','kl','dermed','00','slo','12','politiet','faren','eit','bra','je','sitter','sikkert','vite','full','lille','18','glad','fleste','slutt','ene','mine','gjelder','lagt','virkelig','laget','alene','ennå','lang','ganske','johan','omkring','hjemme','vårt','vanskelig','arne','gammel','skulde','tidende','riktig','huset','følte','møte','lørdag','klar','m','kort','viktig','ellers','minst','fortsatt','op','veien','seier','mål','kjent','slags','frode','8','7','stund','arbeid','finnes','ingenting','lange','gangen','stå','lot','rekke','redd','høre','vilde','ga','ti','forteller','overfor','stadig','burde','visst','syntes','fjor','sette','funnet','hjelp','største','løpet','meter','norges','hånden','spørsmål','s','mente','søndag','f','følge','fremdeles','imot','11','hus','kvinne','ventet','reiste','hendene','trodde','usa','legger','viste','regjeringen','eg','årene','eksempel','tenkt','ole','slikt','erik','moren','holder','seks','tenker','19','stedet','tillegg','helst','bruke','skolen','kampen','nettopp','døren','egne','eget','sterkt','betyr','vant','enkelte','nærmere','hvad','50','dårlig','per','trenger','menneske','måten','vise','oppe','finner','legge','and','the','in','of','innen','jobbe','with','arbeidsgiveren','kunder','spennende','as','tilbyr','is','you','faglig','our','kompetanse','are','innenfor','experience','on','kvalifikasjoner','erfaring','utvikle','utvikling','prosjekter','ledende','we','relevant','utvikler','stillingen','work','arbeidsoppgaver','be','egenskaper','jobber','bidra','utdanning','development','kjennskap','teknologi','evne','ansvar','ansatte','will','mulighet','tjenester','medarbeidere','muligheter','an','teknisk','that']
    ReRawdata=' '.join(filter(lambda x: x.lower() not in Stopwords,  Rawdata.split(' ')))
    words = re.findall('\w+', ReRawdata.lower())
    print collections.Counter(words).most_common(y)
    return collections.Counter(words).most_common(y)
    #f=open("test.txt","w")
    #f.write(str(collections.Counter(words).most_common(40)))
    #print str(collections.Counter(words).most_common(40))
    #f.close()
    #return 
    


def main():
    tresholdValue = 60;
    alldata = dirListing()
    #print(len(alldata))
    commonwords = kjellspyton(alldata,tresholdValue)
    counts = np.zeros(tresholdValue)
    for i in range(0,tresholdValue-1):
        #print(commonwords[i][1])
        counts[i] = commonwords[i][1]
        #words[i] = commonwords[i][0]
    print(counts)
#print(commonwords[i][1])
#fileread()
if __name__ == '__main__':main()
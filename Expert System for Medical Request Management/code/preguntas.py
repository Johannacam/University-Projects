from utils import *
from logic import *

# Variables --------------------------- 
Dolor1 = 0
Dolor2 = 0
Desorientacion = 0
TosConFlema = 0
TemperaturaBaja = 0
TosConSangre = 0
PerdidaDeApetito = 0
Ronquera = 0
DolorDeHuesos = 0
ProblemasDeMemoria = 0
EstadosDepresivos = 0
SomnolenciaDiurna = 0
SudoresNocturnos = 0
AumentoDePeso = 0
DisfuncionSexual = 0
DolorAlRespirar = 0
DolorAlToser = 0
Fatiga = 0
DolorCorporal = 0
PerdidaRecienteDelOlfatoOGusto = 0
Nauseas = 0
Vomito = 0
Diarrea = 0
SibilanciaAlExhalar = 0
ProblemasParaDormir = 0
Escalofrios = 0
RespiracionRapida  = 0
PerdidaDePeso = 0
DolorArticulaciones = 0
Acropaquia = 0
DolorDePecho = 0
TosPersistente = 0
TosSeca = 0
DificultadRespirar = 0
Cansancio = 0
Debilidad = 0
Congestion = 0
GoteoNasal = 0
DolorGarganta = 0
DolorOjos = 0
Fiebre = 0
DolorCabeza = 0
DolorMuscular = 0
Sudoracion = 0
Gripe = 0
Covid19 = 0
Asma = 0
Influenza = 0
FibrosisPulmonar = 0
Neumonia = 0
CancerPulmon = 0
Apnea = 0
Tuberculosis = 0
Bronquitis = 0

# Funciones------------------------------
def P_Tos(clauses):
    print("¿Usted tiene tos? [s/n]")
    res = input()
    if res == 's':
        P_TosPersistente(clauses)
    else:
        P_Apnea(clauses)
        P_Asma(clauses)

def P_Dolor1(clauses):
    global Dolor1
    if Dolor1:
        return 
    Dolor1 = 1
    print("¿Usted experimenta algun tipo de dolor1? [s/n]")
    res = input()
    if res == 's':
        P_DolorGarganta(clauses)
    else:
        print("No se ha podido encontrar un diagnostico para usted.")

def P_Dolor2(clauses):
    global Dolor2
    if Dolor2:
        return 
    Dolor2 = 1
    print("¿Usted experimenta algun tipo de dolor2? [s/n]")
    res = input()
    if res == 's':
        P_DolorCabeza(clauses)
    else:
        print("No se ha podido encontrar un diagnostico para usted.")

def P_Gripe(clauses):
    global Gripe
    if Gripe:
        return
    Gripe = 1
    P_TosPersistente(clauses,0)
    P_TosSeca(clauses)
    P_DificultadRespirar(clauses)
    P_Cansancio(clauses)
    P_Debilidad(clauses)
    P_Congestion(clauses)
    P_GoteoNasal(clauses)
    P_DolorGarganta(clauses,0)
    P_DolorOjos(clauses)
    P_Fiebre(clauses,0)
    P_DolorCabeza(clauses,0)
    P_DolorMuscular(clauses)
    P_Escalofrios(clauses)
    P_Sudoracion(clauses)

# Covid
def P_Covid19(clauses):
    global Covid19
    if Covid19:
        return
    Covid19 = 1
    P_Fiebre(clauses,0)
    P_Escalofrios(clauses)
    P_TosPersistente(clauses,0)
    P_DificultadRespirar(clauses)
    P_Fatiga(clauses)
    P_DolorMuscular(clauses)
    P_DolorCorporal(clauses)
    P_DolorCabeza(clauses,0)
    P_PerdidaRecienteDelOlfatoOGusto(clauses)
    P_DolorGarganta(clauses,0)
    P_Congestion(clauses)
    P_GoteoNasal(clauses)
    P_Nauseas(clauses)
    P_Vomito(clauses)
    P_Diarrea(clauses)

# Influenza
def P_Influenza(clauses):
    global Influenza
    if Influenza:
        return
    Influenza = 1
    P_Fiebre(clauses,0)
    P_Escalofrios(clauses)
    P_TosPersistente(clauses,0)
    P_DolorGarganta(clauses,0)
    P_Congestion(clauses)
    P_DolorMuscular(clauses)
    P_DolorCorporal(clauses)
    P_DolorCabeza(clauses,0)
    P_Fatiga(clauses)
    P_Vomito(clauses)
    P_Diarrea(clauses)

# Fibrosis Pulmonar 
def P_FibrosisPulmonar(clauses):
    global FibrosisPulmonar
    if FibrosisPulmonar:
        return
    FibrosisPulmonar = 1
    P_DificultadRespirar(clauses)
    P_TosSeca(clauses)
    P_TosPersistente(clauses,0)
    P_RespiracionRapida(clauses)
    P_PerdidaDePeso(clauses)
    P_Cansancio(clauses)
    P_DolorArticulaciones(clauses)
    P_DolorMuscular(clauses)
    P_Acropaquia(clauses)

# Cáncer de Pulmón
def P_CancerPulmon(clauses):
    global CancerPulmon
    if CancerPulmon:
        return
    CancerPulmon = 1
    P_DificultadRespirar(clauses)
    P_TosConSangre(clause)
    P_TosPersistente(clauses,0)
    P_Cansancio(clauses)
    P_PerdidaDePeso(clauses)
    P_PerdidaDeApetito(clauses)
    P_DolorDePecho(clauses)
    P_Ronquera(clauses)
    P_DolorDeHuesos(clauses)
    P_DolorCabeza(clauses,0)

# Bronquitis
def P_Bronquitis(clauses):
    global Bronquitis
    if Bronquitis:
        return
    Bronquitis = 1
    P_TosConFlema(clauses)
    P_TosSeca(clauses)
    P_DolorDePecho(clauses)
    P_Cansancio(clauses)
    P_DolorCabeza(clauses,0)
    P_DolorCorporal(clauses)
    P_DolorGarganta(clauses,0)

# Asma
def P_Asma(clauses):
    global Asma
    if Asma:
        return
    Asma = 1
    P_DificultadRespirar(clauses) 
    P_SibilanciaAlExhalar(clauses)
    P_ProblemasParaDormir(clauses)

# Neumonía
def P_Neumonia(clauses):
    global Neumonia
    if Neumonia:
        return
    Neumonia = 1
    P_Desorientacion(clauses)
    P_TosConFlema(clauses)
    P_TemperaturaBaja(clauses)
    P_DificultadRespirar(clauses)
    P_Fiebre(clauses,0)
    P_Sudoracion(clauses)
    P_Fatiga(clauses)
    P_Nauseas(clauses)
    P_Vomito(clauses)
    P_Diarrea(clauses)
    P_Escalofrios(clauses)
    P_DolorDePecho(clauses)

# Apnea del sueño 
def P_Apnea(clauses):
    global Apnea
    if Apnea:
        return
    Apnea = 1
    P_ProblemasDeMemoria(clauses)
    P_EstadosDepresivos(clauses)
    P_SomnolenciaDiurna(clauses)
    P_SudoresNocturnos(clauses) 
    P_AumentoDePeso(clauses)
    P_DisfuncionSexual(clauses)
    P_DolorCabeza(clauses,0)
    P_Fatiga(clauses)

# Tuberculosis
def P_Tuberculosis(clauses):
    global Tuberculosis
    if Tuberculosis:
        return
    Tuberculosis = 1
    P_TosConFlema(clauses)
    P_TosConSangre(clauses,0)
    P_DolorAlRespirar(clauses)
    P_DolorAlToser(clauses)
    P_TosPersistente(clauses,0)
    P_Fiebre(clauses,0)
    P_Sudoracion(clauses)
    P_Fatiga(clauses)
    P_Escalofrios(clauses)
    P_PerdidaDePeso(clauses)
    P_DolorDePecho(clauses)
    P_PerdidaDeApetito(clauses)

def P_Desorientacion(clauses):
    global Desorientacion
    if Desorientacion:
        return
    Desorientacion = 1
    print("¿Se ha sentido desorientado últimamente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Desorientacion(Paciente)"))

def P_TosConFlema(clauses):
    global TosConFlema
    if TosConFlema == 1:
        return
    TosConFlema = 1
    print("¿Tiene tos con flemas? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosConFlema(Paciente)"))

def P_TosConFlema1(clauses, ban=1):
    global TosConFlema
    if TosConFlema == 1:
        return
    TosConFlema = 1
    print("¿Tiene tos con flemas? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosConFlema(Paciente)"))
        if ban:
            P_FibrosisPulmonar(clauses)
    else:
        if ban:
            P_Gripe(clauses)

def P_TosConFlema2(clauses, ban=1):
    global TosConFlema
    if TosConFlema == 1:
        return
    TosConFlema = 1
    print("¿Tiene tos con flemas? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosConFlema(Paciente)"))
        if ban:
            P_Tuberculosis(clauses)
    else:
        if ban:
            P_CancerPulmon(clauses)

def P_TemperaturaBaja(clauses):
    global TemperaturaBaja
    if TemperaturaBaja:
        return
    TemperaturaBaja = 1
    print("¿Ha tenido temperatura corporal baja? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TemperaturaBaja(Paciente)"))

def P_TosConSangre(clauses, ban=1):
    global TosConSangre
    if TosConSangre:
        return
    TosConSangre = 1
    print("¿Tiene tos con sangre? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosConSangre(Paciente)"))
        if ban:
            P_TosConFlema2(clauses)
    else:
        if ban:
            P_Covid19(clauses)
            P_Influenza(clauses)

def P_PerdidaDeApetito(clauses):
    global PerdidaDeApetito
    if PerdidaDeApetito:
        return
    PerdidaDeApetito = 1
    print("¿Ha tenido pérdidas de apetito recientemente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("PerdidaDeApetito(Paciente)"))

def P_Ronquera(clauses):
    global Ronquera
    if Ronquera:
        return
    Ronquera = 1
    print("¿Actualmente ronca? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Ronquera(Paciente)"))

def P_DolorDeHuesos(clauses):
    global DolorDeHuesos
    if DolorDeHuesos:
        return
    DolorDeHuesos = 1
    print("¿Presenta dolor de huesos? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorDeHuesos(Paciente)"))

def P_ProblemasDeMemoria(clauses):
    global ProblemasDeMemoria
    if ProblemasDeMemoria:
        return
    ProblemasDeMemoria = 1
    print("¿Tiene mala memoria? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("ProblemasDeMemoria(Paciente)"))

def P_EstadosDepresivos(clauses):
    global EstadosDepresivos
    if EstadosDepresivos:
        return
    EstadosDepresivos = 1
    print("¿Ha experimentado estados depresivos últimamente?  [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Desorientacion(Paciente)"))

def P_SomnolenciaDiurna(clauses):
    global SomnolenciaDiurna
    if SomnolenciaDiurna:
        return
    SomnolenciaDiurna = 1
    print("¿Tiene ganas de dormir todo el día? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("SomnolenciaDiurna(Paciente)"))

def P_SudoresNocturnos(clauses):
    global SudoresNocturnos
    if SudoresNocturnos:
        return
    SudoresNocturnos = 1
    print("¿Suda durante la noche? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("SudoresNocturnos(Paciente)"))
    
def P_AumentoDePeso(clauses):
    global AumentoDePeso
    if AumentoDePeso:
        return
    AumentoDePeso = 1
    print("¿Recientemente ha aumentado de peso de manera involuntaria? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("AumentoDePeso(Paciente)"))

def P_DisfuncionSexual(clauses):
    global DisfuncionSexual
    if DisfuncionSexual:
        return
    DisfuncionSexual = 1
    print("¿Presenta disfunción sexual? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DisfuncionSexual(Paciente)"))

def P_DolorAlRespirar(clauses):
    global DolorAlRespirar
    if DolorAlRespirar:
        return
    DolorAlRespirar = 1
    print("¿Tiene dolor al respirar? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorAlRespirar(Paciente)"))

def P_DolorAlToser(clauses):
    global DolorAlToser
    if DolorAlToser:
        return
    DolorAlToser = 1
    print("¿Tiene dolor al toser? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorAlToser(Paciente)"))

def P_Fatiga(clauses):
    global Fatiga
    if Fatiga:
        return
    Fatiga = 1
    print("¿Tiene Fatiga?  [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Fatiga(Paciente)"))

def P_DolorCorporal(clauses):
    global DolorCorporal
    if DolorCorporal:
        return
    DolorCorporal = 1
    print("¿Presenta dolor corporal? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorCorporal(Paciente)"))

def P_PerdidaRecienteDelOlfatoOGusto(clauses):
    global PerdidaRecienteDelOlfatoOGusto
    if PerdidaRecienteDelOlfatoOGusto:
        return
    PerdidaRecienteDelOlfatoOGusto = 1
    print("¿Presenta pérdida reciente del olfato o gusto? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("PerdidaRecienteDelOlfatoOGusto(Paciente)"))

def P_Nauseas(clauses):
    global Nauseas
    if Nauseas:
        return
    Nauseas = 1
    print("¿Ha experimentado náuseas?  [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Nauseas(Paciente)"))

def P_Vomito(clauses):
    global Vomito
    if Vomito:
        return
    Vomito = 1
    print("¿Ha tenido vómito? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Vomito(Paciente)"))

def P_Diarrea(clauses):
    global Diarrea
    if Diarrea:
        return
    Diarrea = 1
    print("¿Tiene diarrea? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Diarrea(Paciente)"))

def P_SibilanciaAlExhalar(clauses):
    global SibilanciaAlExhalar
    if SibilanciaAlExhalar:
        return
    SibilanciaAlExhalar = 1
    print("¿Presenta sibilancia al exhalar?  [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("SibilanciaAlExhalar(Paciente)"))

def P_ProblemasParaDormir(clauses):
    global ProblemasParaDormir
    if ProblemasParaDormir:
        return
    ProblemasParaDormir = 1
    print("¿Tiene problemas para dormir? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("ProblemasParaDormir(Paciente)"))

def P_Escalofrios(clauses):
    global Escalofrios
    if Escalofrios:
        return
    Escalofrios = 1
    print("¿Presenta escalofríos? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Escalofrios(Paciente)"))

def P_RespiracionRapida (clauses):
    global RespiracionRapida
    if RespiracionRapida:
        return
    RespiracionRapida = 1
    print("¿Presenta respiración agitada? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("RespiracionRapida(Paciente)"))

def P_PerdidaDePeso(clauses):
    global PerdidaDePeso
    if PerdidaDePeso:
        return
    PerdidaDePeso = 1
    print("¿Presenta pérdida de peso? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("PerdidaDePeso(Paciente)"))

def P_DolorArticulaciones(clauses):
    global DolorArticulaciones
    if DolorArticulaciones:
        return
    DolorArticulaciones = 1
    print("¿Ha tenido dolor de articulaciones? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorArticulaciones(Paciente)"))

def P_Acropaquia(clauses):
    global Acropaquia
    if Acropaquia:
        return
    Acropaquia = 1
    print("¿Presenta acropaquia? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Acropaquia(Paciente)"))

def P_DolorDePecho(clauses):
    global DolorDePecho
    if DolorDePecho:
        return
    DolorDePecho = 1
    print("¿Presenta dolor de pecho?  [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorDePecho(Paciente)"))

def P_TosPersistente(clauses, ban=1):
    global TosPersistente
    if TosPersistente:
        return
    TosPersistente = 1
    print("¿Usted experimenta tos persistente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosPersistente(Paciente)"))
        if ban:
            P_TosSeca1(clauses)
    else:
        if ban:
            P_TosSeca2(clauses)

def P_TosSeca(clauses):
    global TosSeca
    if TosSeca:
        return
    TosSeca = 1
    print("¿Usted experimenta tos seca? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosSeca(Paciente)"))

def P_TosSeca1(clauses, ban=1):
    global TosSeca
    if TosSeca:
        return
    TosSeca = 1
    print("¿Usted experimenta tos seca? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosSeca(Paciente)"))
        if ban:
            P_TosConFlema1(clauses)
    else:
        if ban:
            P_TosConSangre(clauses)

def P_TosSeca2(clauses, ban=1):
    global TosSeca
    if TosSeca:
        return
    TosSeca = 1
    print("¿Usted experimenta tos seca? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("TosSeca(Paciente)"))
        if ban:
            P_Bronquitis(clauses)
    else:
        if ban:
            P_Neumonia(clauses)

def P_DificultadRespirar(clauses):
    global DificultadRespirar
    if DificultadRespirar:
        return
    DificultadRespirar = 1
    print("¿Suele presentar dificultad para respirar? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DificultadRespirar(Paciente)"))

def P_Cansancio(clauses):
    global Cansancio
    if Cansancio:
        return
    Cansancio = 1
    print("¿Siente cansancio con frecuencia? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Cansancio(Paciente)"))

def P_Debilidad(clauses):
    global Debilidad
    if Debilidad:
        return
    Debilidad = 1
    print("¿Siente debilidad con frecuencia? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Debilidad(Paciente)"))

def P_Congestion(clauses):
    global Congestion
    if Congestion:
        return
    Congestion = 1
    print("¿Experimenta congestión nasal? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Congestion(Paciente)"))

def P_GoteoNasal(clauses):
    global GoteoNasal
    if GoteoNasal:
        return
    GoteoNasal = 1
    print("¿Experimenta goteo nasal? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("GoteoNasal(Paciente)"))

def P_DolorGarganta(clauses, ban=1):
    global DolorGarganta
    if DolorGarganta:
        return
    DolorGarganta = 1
    print("¿Siente dolor de garganta ocasionalmente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorGarganta(Paciente)"))
        if ban:
            P_Gripe(clauses)
            P_FibrosisPulmonar(clauses)
    else:
        if ban:
            P_CancerPulmon(clauses)
            P_Tuberculosis(clauses)
            P_Bronquitis(clauses)

def P_DolorOjos(clauses):
    global DolorOjos
    if DolorOjos:
        return
    DolorOjos = 1
    print("¿Siente dolor en los ojos ocasionalmente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorOjos(Paciente)"))

def P_Fiebre(clauses, ban=1):
    global Fiebre
    if Fiebre:
        return
    Fiebre = 1
    print("¿Ha presentado fiebre recientemente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Fiebre(Paciente)"))
        if ban:
            P_Influenza(clauses)
    else:
        if ban:
            P_Covid19(clauses)
            P_Asma(clauses)
            P_Apnea(clauses)

def P_DolorCabeza(clauses,ban=1):
    global DolorCabeza
    if DolorCabeza:
        return
    DolorCabeza = 1
    print("¿Siente dolor de cabeza ocasionalmente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorCabeza(Paciente)"))
        if ban:
            P_CancerPulmon(clauses)
            P_Bronquitis(clauses)
    else:
        if ban:
            P_Tuberculosis(clauses)

def P_DolorMuscular(clauses):
    global DolorMuscular
    if DolorMuscular:
        return
    DolorMuscular = 1
    print("¿Siente dolor muscular ocasionalmente? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("DolorMuscular(Paciente)"))

def P_Sudoracion(clauses):
    global Sudoracion
    if Sudoracion:
        return
    Sudoracion = 1
    print("¿Experimenta sudoración? [s/n]")
    res = input()
    if res == 's':
        clauses.append(expr("Sudoracion(Paciente)"))
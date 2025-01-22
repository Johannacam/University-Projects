#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from utils import *
from logic import *
from preguntas import *
from clausulas import *

#------------------------------------------------------------------------------------------------------------------
#   KB de enfermedades y tratamiento
#------------------------------------------------------------------------------------------------------------------
clauses = []
haz_clausulas(clauses)
P_Tos(clauses)
enf_kb = FolKB(clauses)

#------------------------------------------------------------------------------------------------------------------
#   Forward chaining
#------------------------------------------------------------------------------------------------------------------


# Enfermedades
tGripe = len(list(fol_bc_ask(enf_kb, expr('Gripe(Paciente)'.format(name)))))
tCovid19 = len(list(fol_bc_ask(enf_kb, expr('Covid19(Paciente)'.format(name)))))
tAsma = len(list(fol_bc_ask(enf_kb, expr('Asma(Paciente)'.format(name)))))
tInfluenza = len(list(fol_bc_ask(enf_kb, expr('Influenza(Paciente)'.format(name)))))
tFibrosis = len(list(fol_bc_ask(enf_kb, expr('FibrosisPulmonar(Paciente)'.format(name)))))
tNeumonia = len(list(fol_bc_ask(enf_kb, expr('Neumonia(Paciente)'.format(name)))))
tCancer = len(list(fol_bc_ask(enf_kb, expr('CancerPulmon(Paciente)'.format(name)))))
tApnea = len(list(fol_bc_ask(enf_kb, expr('Apnea(Paciente)'.format(name)))))
tTuberculosis = len(list(fol_bc_ask(enf_kb, expr('Tuberculosis(Paciente)'.format(name)))))
tBronquitis = len(list(fol_bc_ask(enf_kb, expr('Bronquitis(Paciente)'.format(name)))))

print("Tu diagnóstico es:")

if tGripe:
    print("- Gripe")
if tCovid19:
    print("- Covid19")
if tAsma:
    print("- Asma")
if tInfluenza:
    print("- Influenza")
if tFibrosis:
    print("- Fibrosis")
if tNeumonia:
    print("- Neumonia")
if tCancer:
    print("- Cancer")
if tApnea:
    print("- Apnea")
if tTuberculosis:
    print("- Tuberculosis")
if tBronquitis:
    print("- Bronquitis")

print("Tu tratamiento es:")
if tGripe:
    print("Descanso, Mantenerse hidratado, Paracetamol, Ibuprofeno, Ácido acetilsalicílico, Clorfenamina, Frenadol, Couldina, y/o Dextrometorfano")
if tCovid19:
    print("Antiviral: Remdesivir (Veklury) por 3 días consecutivos")
if tAsma:
    print("Corticoides inhalados, Modificadores de leucotrienos, Agonistas beta de acción prolongada sólo con corticoides inhalados, y/o Antagonistas muscarínicos de acción prolongada se agrega en casos graves de asma.")
if tInfluenza:
    print("Oseltamivir, Zanamivir, Peramivir, y/o Baloxavir")
if tFibrosis:
    print("Terapia de oxígeno para personas con niveles bajos de oxígeno, Rehabilitación pulmonar, Trasplante de pulmón en casos avanzados, y/o Pirfenidona (Esbriet) o Nintedanib (Ofev)")
if tNeumonia:
    print("Antibiótico, Ácido acetilsalicílico, Ibuprofeno, y/o Paracetamol")
if tCancer:
    print("Lobectomía, Neumonectomía, Segmentectomía o resección en cuña, Resección segmentaria Radioterapia, Quimioterapia Radioterapia estereotáctica corporal, Terapia dirigida con medicamentos, y/o Inmunoterapia")
if tApnea:
    print("Realizar ejercicio físico, Tener un peso saludable, Limitar consumo de alcohol, Limitar el consumo de cafeína, Dejar de fumar, y/o Tener hábitos de sueño saludables ")
if tTuberculosis:
    print("Isoniacida, Rifampicina, Etambutol, y/o Pirazinamida")
if tBronquitis:
    print("No se usan antibióticos, Paracetamol o ácido acetilsalicílico Descanso, y/o Mantenerse hidratado")

else:
    print("No hay diagnóstico ni tratamiento")

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------




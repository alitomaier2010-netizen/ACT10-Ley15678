# =============================================================================
# Laboratorio de Programación (LPR 5.° Año) — E.E.S.T. N.º 1 "Eduardo Ader"
# Vicente López — 5.° 3.° A-B
# ACTIVIDAD 10 BIS: Simulador de Normativa de Celulares en el Aula (Ley 15.678)
# DOCENTE: Mansilla Muñoz York Elías
# ESTUDIANTE: Maier, Alexis
# Rama del repositorio: ley15678
# =============================================================================

"""Filtro de decisiones: ¿se puede usar el celular en el aula en este momento?

Regla general (Ley 15.678, Provincia de Buenos Aires): los estudiantes no
pueden usar celulares, tablets ni pantallas durante la jornada escolar.

Excepción pedagógica: sólo con requerimiento y autorización explícita del
docente, y con fines estrictamente pedagógicos.

Emergencia familiar: se canaliza institucionalmente a través de preceptoría
y/o dirección; no habilita el uso libre del dispositivo en clase.
"""


# -----------------------------------------------------------------------------
# Función que concentra la lógica condicional if / elif / else del diagrama
# -----------------------------------------------------------------------------
def evaluar_uso(autorizacion_docente, emergencia_familiar):
    """Devuelve la decisión del filtro según el contexto del aula."""
    if autorizacion_docente == True:
        return (
            "[ACCESO PERMITIDO] El celular solo para estudiar y para aprender "
            "(fines pedagógicos)."
        )
    elif emergencia_familiar == True:
        return (
            "[CANALIZACIÓN INSTITUCIONAL] Gestionar la comunicación urgente "
            "a través de preceptoría y/o dirección."
        )
    else:
        return (
            "[RESTRICCIÓN LEY 15.678] Tu celular debe permanecer guardado "
            "en la mochila."
        )


def mostrar_caso(titulo, autorizacion_docente, emergencia_familiar):
    """Muestra el estado de las variables y la rama que se ejecuta."""
    print(f"--- {titulo} ---")
    print(f"Estado de Autorización Docente : {autorizacion_docente}")
    print(f"Estado de Emergencia Validada  : {emergencia_familiar}\n")
    print(evaluar_uso(autorizacion_docente, emergencia_familiar))
    print("=" * 52 + "\n")


print("=" * 52)
print("=== SISTEMA DE ASESORAMIENTO NORMATIVO ESCOLAR ===")
print("=" * 52 + "\n")

# Casos de prueba: cubren las tres ramas del algoritmo.
casos = [
    ("Caso A — autorización docente (excepción pedagógica)", True, False),
    ("Caso B — emergencia familiar validada", False, True),
    ("Caso C — sin autorización ni emergencia (regla general)", False, False),
]

for titulo, autorizacion, emergencia in casos:
    mostrar_caso(titulo, autorizacion, emergencia)

print("Fin del simulador. Ley 15.678 — Provincia de Buenos Aires.")

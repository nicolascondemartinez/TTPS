"""Datos falsos del prototipo (sin base de datos)."""
ROLES = {"paciente": "Paciente", "medico": "Médico tratante", "administrativo": "Administrativo",
         "bioinformatico": "Bioinformático", "gerente": "Gerente médico", "transportista": "Transportista"}

NAV = {
 "paciente": [("Inicio", "paciente.inicio"), ("Presupuesto", "paciente.presupuesto"), ("Sacar turno", "paciente.turno"), ("Resultados y chat", "paciente.resultados")],
 "medico": [("Inicio", "medico.inicio"), ("Alta de paciente", "medico.alta_paciente"), ("Alta de estudio", "medico.alta_estudio"), ("Historial", "medico.historial"), ("Cupones", "medico.cupones")],
 "administrativo": [("Presupuestos", "administrativo.inicio"), ("Obras sociales", "administrativo.obras"), ("Turnos", "administrativo.turnos"), ("Recepción y resultados", "administrativo.recepcion"), ("Lotes y FedEx", "administrativo.lotes"), ("Transportistas", "administrativo.transportistas")],
 "bioinformatico": [("Cola de estudios", "bioinformatico.inicio"), ("Cargar variantes", "bioinformatico.analizar")],
 "gerente": [("Patologías", "gerente.inicio"), ("Definir patología", "gerente.patologia"), ("Cupones", "gerente.cupones")],
 "transportista": [("Orden del día", "transportista.inicio")],
}

ESTADOS = ["Creado", "Pagado", "Turno sacado", "Listo para retirar", "En camino hacia el laboratorio central",
           "Esperando armado de lote", "En viaje a Corea", "En análisis por bioinformática",
           "En análisis de un bioinformático", "Finalizado"]
PATOLOGIAS = ["Fabry", "Pompe", "Mucopolisacaridosis 1", "Gaucher", "ASMD"]
GENES = {"Fabry": "GLA", "Pompe": "GAA", "Mucopolisacaridosis 1": "IDUA", "Gaucher": "GBA1", "ASMD": "SMPD1"}
PACIENTES = ["Lucía Fernández", "Martín Gómez", "Sofía Ramírez", "Tomás Acosta", "Valentina Ruiz"]

def precio(g): return 500 + 30 * max(0, g - 5)

ESTUDIOS = [dict(id=101 + i, paciente=p, patologia=pa, genes=g, estado=e, urgente=u, precio=precio(g)) for i, (p, pa, g, e, u) in enumerate([
    (PACIENTES[0], "Fabry", 8, "Creado", False), (PACIENTES[1], "Pompe", 5, "En análisis por bioinformática", True),
    (PACIENTES[2], "Gaucher", 6, "Turno sacado", False), (PACIENTES[3], "ASMD", 5, "En análisis por bioinformática", False),
    (PACIENTES[4], "Mucopolisacaridosis 1", 5, "Finalizado", False)])]

OBRAS = [("OSDE", 80), ("Swiss Medical", 70), ("PAMI", 100), ("IOMA", 60)]
CENTROS = [("Centro Norte", "Av. Libertador 1200", 3), ("Centro Sur", "Calle 7 nº 450", 2), ("Centro Oeste", "Rivadavia 3300", 4)]
LOTES = [dict(id="L-01", muestras=10, estado="Esperando retiro", urgente=False), dict(id="L-02", muestras=3, estado="Esperando retiro", urgente=True)]
AVISOS = ["Su presupuesto está disponible.", "Recordatorio: turno el lunes 9:15 en Centro Norte (inasistencias acumuladas: 1 de 5)."]

DATA = dict(roles=ROLES, estados=ESTADOS, patologias=PATOLOGIAS, genes=GENES, pacientes=PACIENTES, estudios=ESTUDIOS,
            obras=OBRAS, centros=CENTROS, lotes=LOTES, avisos=AVISOS, precio=precio)

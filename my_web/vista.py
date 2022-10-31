def vistareporte(reporte, parametros=None):
    from sga.models import ClaseMaestria
    from django.template import Template, Context
    from datetime import datetime
    data = {}
    data['clases'] = clases = ClaseMaestria.objects.filter(materia=int(parametros['materia']),tipoactividad=int(parametros['tipo']),periodo=int(parametros['periodo']),actor=int(parametros['actor']))
    data['tipo']="Síncronas" if int(parametros['tipo'])==1 else "Asíncronas"
    #data['materia']=clases[0]
    data['actor']= True if int(parametros['actor'])==1 else False 
    data['fecha_act'] = datetime.now().date()

    tpl = Template(reporte.html)
    return tpl.render(Context(data))
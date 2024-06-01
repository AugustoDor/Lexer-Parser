# Generated from Gramática.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,340,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,1,0,1,0,3,0,93,
        8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,3,2,102,8,2,1,2,1,2,3,2,106,8,2,
        1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,3,6,122,
        8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,135,8,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,8,3,8,144,8,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,
        1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        3,15,179,8,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,20,1,20,1,20,3,20,198,8,20,1,21,1,21,1,21,
        1,21,1,22,1,22,1,22,1,22,1,22,3,22,209,8,22,1,22,1,22,1,23,1,23,
        1,23,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,3,26,
        227,8,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,238,8,
        28,1,28,3,28,241,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,3,29,253,8,29,1,30,1,30,1,30,3,30,258,8,30,1,31,1,31,1,31,
        1,31,1,32,1,32,1,32,3,32,267,8,32,1,32,3,32,270,8,32,1,32,1,32,1,
        32,1,32,1,32,1,32,1,32,1,32,1,32,3,32,281,8,32,1,33,1,33,1,33,1,
        34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,308,8,38,1,39,1,
        39,1,39,3,39,313,8,39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,
        41,3,41,324,8,41,1,41,1,41,1,41,3,41,329,8,41,1,42,1,42,1,42,1,43,
        1,43,1,43,1,44,1,44,1,44,1,44,0,0,45,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,
        66,68,70,72,74,76,78,80,82,84,86,88,0,2,1,0,35,36,2,0,34,34,40,40,
        321,0,92,1,0,0,0,2,94,1,0,0,0,4,98,1,0,0,0,6,107,1,0,0,0,8,110,1,
        0,0,0,10,113,1,0,0,0,12,118,1,0,0,0,14,123,1,0,0,0,16,127,1,0,0,
        0,18,147,1,0,0,0,20,150,1,0,0,0,22,153,1,0,0,0,24,156,1,0,0,0,26,
        159,1,0,0,0,28,162,1,0,0,0,30,178,1,0,0,0,32,180,1,0,0,0,34,183,
        1,0,0,0,36,186,1,0,0,0,38,189,1,0,0,0,40,194,1,0,0,0,42,199,1,0,
        0,0,44,203,1,0,0,0,46,212,1,0,0,0,48,215,1,0,0,0,50,218,1,0,0,0,
        52,223,1,0,0,0,54,228,1,0,0,0,56,232,1,0,0,0,58,242,1,0,0,0,60,254,
        1,0,0,0,62,259,1,0,0,0,64,263,1,0,0,0,66,282,1,0,0,0,68,285,1,0,
        0,0,70,288,1,0,0,0,72,291,1,0,0,0,74,294,1,0,0,0,76,297,1,0,0,0,
        78,309,1,0,0,0,80,314,1,0,0,0,82,318,1,0,0,0,84,330,1,0,0,0,86,333,
        1,0,0,0,88,336,1,0,0,0,90,93,3,2,1,0,91,93,5,48,0,0,92,90,1,0,0,
        0,92,91,1,0,0,0,93,1,1,0,0,0,94,95,5,29,0,0,95,96,3,4,2,0,96,97,
        5,30,0,0,97,3,1,0,0,0,98,101,3,10,5,0,99,100,5,33,0,0,100,102,3,
        6,3,0,101,99,1,0,0,0,101,102,1,0,0,0,102,105,1,0,0,0,103,104,5,33,
        0,0,104,106,3,8,4,0,105,103,1,0,0,0,105,106,1,0,0,0,106,5,1,0,0,
        0,107,108,5,2,0,0,108,109,5,41,0,0,109,7,1,0,0,0,110,111,5,3,0,0,
        111,112,5,41,0,0,112,9,1,0,0,0,113,114,5,1,0,0,114,115,5,31,0,0,
        115,116,3,12,6,0,116,117,5,32,0,0,117,11,1,0,0,0,118,121,3,14,7,
        0,119,120,5,33,0,0,120,122,3,12,6,0,121,119,1,0,0,0,121,122,1,0,
        0,0,122,13,1,0,0,0,123,124,5,29,0,0,124,125,3,16,8,0,125,126,5,30,
        0,0,126,15,1,0,0,0,127,128,3,20,10,0,128,129,5,33,0,0,129,130,3,
        22,11,0,130,134,5,33,0,0,131,132,3,28,14,0,132,133,5,33,0,0,133,
        135,1,0,0,0,134,131,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,
        137,3,18,9,0,137,138,5,33,0,0,138,139,3,24,12,0,139,143,5,33,0,0,
        140,141,3,26,13,0,141,142,5,33,0,0,142,144,1,0,0,0,143,140,1,0,0,
        0,143,144,1,0,0,0,144,145,1,0,0,0,145,146,3,38,19,0,146,17,1,0,0,
        0,147,148,5,4,0,0,148,149,5,39,0,0,149,19,1,0,0,0,150,151,5,5,0,
        0,151,152,5,41,0,0,152,21,1,0,0,0,153,154,5,6,0,0,154,155,5,38,0,
        0,155,23,1,0,0,0,156,157,5,7,0,0,157,158,7,0,0,0,158,25,1,0,0,0,
        159,160,5,8,0,0,160,161,5,47,0,0,161,27,1,0,0,0,162,163,5,9,0,0,
        163,164,3,30,15,0,164,29,1,0,0,0,165,179,5,34,0,0,166,167,5,29,0,
        0,167,179,5,30,0,0,168,169,5,31,0,0,169,179,5,32,0,0,170,171,5,29,
        0,0,171,172,3,32,16,0,172,173,5,33,0,0,173,174,3,34,17,0,174,175,
        5,33,0,0,175,176,3,36,18,0,176,177,5,30,0,0,177,179,1,0,0,0,178,
        165,1,0,0,0,178,166,1,0,0,0,178,168,1,0,0,0,178,170,1,0,0,0,179,
        31,1,0,0,0,180,181,5,20,0,0,181,182,5,41,0,0,182,33,1,0,0,0,183,
        184,5,21,0,0,184,185,5,41,0,0,185,35,1,0,0,0,186,187,5,22,0,0,187,
        188,5,41,0,0,188,37,1,0,0,0,189,190,5,23,0,0,190,191,5,31,0,0,191,
        192,3,40,20,0,192,193,5,32,0,0,193,39,1,0,0,0,194,197,3,42,21,0,
        195,196,5,33,0,0,196,198,3,40,20,0,197,195,1,0,0,0,197,198,1,0,0,
        0,198,41,1,0,0,0,199,200,5,29,0,0,200,201,3,44,22,0,201,202,5,30,
        0,0,202,43,1,0,0,0,203,204,3,46,23,0,204,208,5,33,0,0,205,206,3,
        48,24,0,206,207,5,33,0,0,207,209,1,0,0,0,208,205,1,0,0,0,208,209,
        1,0,0,0,209,210,1,0,0,0,210,211,3,50,25,0,211,45,1,0,0,0,212,213,
        5,27,0,0,213,214,5,41,0,0,214,47,1,0,0,0,215,216,5,28,0,0,216,217,
        5,41,0,0,217,49,1,0,0,0,218,219,5,25,0,0,219,220,5,31,0,0,220,221,
        3,52,26,0,221,222,5,32,0,0,222,51,1,0,0,0,223,226,3,54,27,0,224,
        225,5,33,0,0,225,227,3,52,26,0,226,224,1,0,0,0,226,227,1,0,0,0,227,
        53,1,0,0,0,228,229,5,29,0,0,229,230,3,56,28,0,230,231,5,30,0,0,231,
        55,1,0,0,0,232,233,3,46,23,0,233,237,5,33,0,0,234,235,3,48,24,0,
        235,236,5,33,0,0,236,238,1,0,0,0,237,234,1,0,0,0,237,238,1,0,0,0,
        238,240,1,0,0,0,239,241,3,58,29,0,240,239,1,0,0,0,240,241,1,0,0,
        0,241,57,1,0,0,0,242,252,5,24,0,0,243,244,5,31,0,0,244,245,3,60,
        30,0,245,246,5,32,0,0,246,253,1,0,0,0,247,248,5,29,0,0,248,253,5,
        30,0,0,249,250,5,31,0,0,250,253,5,32,0,0,251,253,5,34,0,0,252,243,
        1,0,0,0,252,247,1,0,0,0,252,249,1,0,0,0,252,251,1,0,0,0,253,59,1,
        0,0,0,254,257,3,62,31,0,255,256,5,33,0,0,256,258,3,60,30,0,257,255,
        1,0,0,0,257,258,1,0,0,0,258,61,1,0,0,0,259,260,5,29,0,0,260,261,
        3,64,32,0,261,262,5,30,0,0,262,63,1,0,0,0,263,264,3,46,23,0,264,
        269,5,33,0,0,265,267,3,66,33,0,266,265,1,0,0,0,266,267,1,0,0,0,267,
        268,1,0,0,0,268,270,5,33,0,0,269,266,1,0,0,0,269,270,1,0,0,0,270,
        271,1,0,0,0,271,272,3,68,34,0,272,273,5,33,0,0,273,274,3,70,35,0,
        274,275,5,33,0,0,275,276,3,72,36,0,276,277,5,33,0,0,277,280,3,74,
        37,0,278,279,5,33,0,0,279,281,3,76,38,0,280,278,1,0,0,0,280,281,
        1,0,0,0,281,65,1,0,0,0,282,283,5,10,0,0,283,284,5,38,0,0,284,67,
        1,0,0,0,285,286,5,11,0,0,286,287,5,12,0,0,287,69,1,0,0,0,288,289,
        5,13,0,0,289,290,5,39,0,0,290,71,1,0,0,0,291,292,5,14,0,0,292,293,
        7,0,0,0,293,73,1,0,0,0,294,295,5,15,0,0,295,296,5,40,0,0,296,75,
        1,0,0,0,297,307,5,26,0,0,298,299,5,31,0,0,299,300,3,78,39,0,300,
        301,5,32,0,0,301,308,1,0,0,0,302,303,5,29,0,0,303,308,5,30,0,0,304,
        305,5,31,0,0,305,308,5,32,0,0,306,308,5,34,0,0,307,298,1,0,0,0,307,
        302,1,0,0,0,307,304,1,0,0,0,307,306,1,0,0,0,308,77,1,0,0,0,309,312,
        3,80,40,0,310,311,5,33,0,0,311,313,3,78,39,0,312,310,1,0,0,0,312,
        313,1,0,0,0,313,79,1,0,0,0,314,315,5,29,0,0,315,316,3,82,41,0,316,
        317,5,30,0,0,317,81,1,0,0,0,318,319,3,46,23,0,319,323,5,33,0,0,320,
        321,3,86,43,0,321,322,5,33,0,0,322,324,1,0,0,0,323,320,1,0,0,0,323,
        324,1,0,0,0,324,325,1,0,0,0,325,328,3,84,42,0,326,327,5,33,0,0,327,
        329,3,88,44,0,328,326,1,0,0,0,328,329,1,0,0,0,329,83,1,0,0,0,330,
        331,5,16,0,0,331,332,5,40,0,0,332,85,1,0,0,0,333,334,5,17,0,0,334,
        335,5,18,0,0,335,87,1,0,0,0,336,337,5,19,0,0,337,338,7,1,0,0,338,
        89,1,0,0,0,21,92,101,105,121,134,143,178,197,208,226,237,240,252,
        257,266,269,280,307,312,323,328
    ]

class GramáticaParser ( Parser ):

    grammarFileName = "Gramática.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"empresas\":'", "'\"versi\\u00F3n\":'", 
                     "'\"firma_digital\":'", "'\"ingresos_anuales\":'", 
                     "'\"nombre_empresa\":'", "'\"fundaci\\u00F3n\":'", 
                     "'\"pyme\":'", "'\"link\":'", "'\"direcci\\u00F3n\":'", 
                     "'\"edad\":'", "'\"cargo\":'", "<INVALID>", "'\"salario\":'", 
                     "'\"activo\":'", "'\"fecha_contrataci\\u00F3n\":'", 
                     "'\"fecha_inicio\":'", "'\"estado\":'", "<INVALID>", 
                     "'\"fecha_fin\":'", "'\"calle\":'", "'\"ciudad\":'", 
                     "'\"pais\":'", "'\"departamentos\":'", "'\"empleados\":'", 
                     "'\"subdepartamentos\":'", "'\"proyectos\":'", "'\"nombre\":'", 
                     "'\"jefe\":'", "'{'", "'}'", "'['", "']'", "','", "'null'", 
                     "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "EMPRESAS", "VERSION", "FIRMA_DIGITAL", 
                      "INGRESOS_ANUALES", "NOMBRE_EMPRESA", "FUNDACION", 
                      "PYME", "LINK", "DIRECCION", "EDAD", "CARGO", "TIPO_CARGO", 
                      "SALARIO", "ACTIVO", "FECHA_CONTRATACION", "FECHA_INICIO", 
                      "ESTADO", "TIPO_ESTADO", "FECHA_FIN", "CALLE", "CIUDAD", 
                      "PAIS", "DEPARTAMENTOS", "EMPLEADO_LISTA", "SUBDEPARTAMENTOS_LISTA", 
                      "PROYECTOS_LISTA", "NOMBRE", "JEFE", "ABRO_LLAVE", 
                      "CIERRO_LLAVE", "ABRO_CORCHETE", "CIERRO_CORCHETE", 
                      "COMA", "NULL", "TRUE", "FALSE", "DIGIT", "INT", "FLOAT", 
                      "DATE", "STRING", "URL_STRING", "PROTOCOLO", "DOMINIO", 
                      "PUERTO", "RUTA", "URL", "WS" ]

    RULE_json = 0
    RULE_t_json = 1
    RULE_t_contenido = 2
    RULE_t_version = 3
    RULE_t_firma_digital = 4
    RULE_t_empresas = 5
    RULE_t_listaempresas = 6
    RULE_t_empresa = 7
    RULE_t_contenidoempresa = 8
    RULE_t_ingresos_anuales = 9
    RULE_t_nombre_empresa = 10
    RULE_t_fundacion = 11
    RULE_t_pyme = 12
    RULE_t_link = 13
    RULE_t_direccion = 14
    RULE_t_tipo_direccion = 15
    RULE_t_calle = 16
    RULE_t_ciudad = 17
    RULE_t_pais = 18
    RULE_t_departamentos = 19
    RULE_t_listadepartamentos = 20
    RULE_t_departamento = 21
    RULE_t_contenidodepartamento = 22
    RULE_t_nombre = 23
    RULE_t_jefe = 24
    RULE_t_subdepartamentos = 25
    RULE_t_listasubdepartamentos = 26
    RULE_t_subdepartamento = 27
    RULE_t_contenidosubdepartamentos = 28
    RULE_t_empleados = 29
    RULE_t_listaempleados = 30
    RULE_t_empleado = 31
    RULE_t_contenidoempleado = 32
    RULE_t_edad = 33
    RULE_t_cargo = 34
    RULE_t_salario = 35
    RULE_t_activo = 36
    RULE_t_fecha_contratacion = 37
    RULE_t_proyectos = 38
    RULE_t_listaproyectos = 39
    RULE_t_proyecto = 40
    RULE_t_contenidoproyecto = 41
    RULE_t_fecha_inicio = 42
    RULE_t_estado = 43
    RULE_t_fecha_fin = 44

    ruleNames =  [ "json", "t_json", "t_contenido", "t_version", "t_firma_digital", 
                   "t_empresas", "t_listaempresas", "t_empresa", "t_contenidoempresa", 
                   "t_ingresos_anuales", "t_nombre_empresa", "t_fundacion", 
                   "t_pyme", "t_link", "t_direccion", "t_tipo_direccion", 
                   "t_calle", "t_ciudad", "t_pais", "t_departamentos", "t_listadepartamentos", 
                   "t_departamento", "t_contenidodepartamento", "t_nombre", 
                   "t_jefe", "t_subdepartamentos", "t_listasubdepartamentos", 
                   "t_subdepartamento", "t_contenidosubdepartamentos", "t_empleados", 
                   "t_listaempleados", "t_empleado", "t_contenidoempleado", 
                   "t_edad", "t_cargo", "t_salario", "t_activo", "t_fecha_contratacion", 
                   "t_proyectos", "t_listaproyectos", "t_proyecto", "t_contenidoproyecto", 
                   "t_fecha_inicio", "t_estado", "t_fecha_fin" ]

    EOF = Token.EOF
    EMPRESAS=1
    VERSION=2
    FIRMA_DIGITAL=3
    INGRESOS_ANUALES=4
    NOMBRE_EMPRESA=5
    FUNDACION=6
    PYME=7
    LINK=8
    DIRECCION=9
    EDAD=10
    CARGO=11
    TIPO_CARGO=12
    SALARIO=13
    ACTIVO=14
    FECHA_CONTRATACION=15
    FECHA_INICIO=16
    ESTADO=17
    TIPO_ESTADO=18
    FECHA_FIN=19
    CALLE=20
    CIUDAD=21
    PAIS=22
    DEPARTAMENTOS=23
    EMPLEADO_LISTA=24
    SUBDEPARTAMENTOS_LISTA=25
    PROYECTOS_LISTA=26
    NOMBRE=27
    JEFE=28
    ABRO_LLAVE=29
    CIERRO_LLAVE=30
    ABRO_CORCHETE=31
    CIERRO_CORCHETE=32
    COMA=33
    NULL=34
    TRUE=35
    FALSE=36
    DIGIT=37
    INT=38
    FLOAT=39
    DATE=40
    STRING=41
    URL_STRING=42
    PROTOCOLO=43
    DOMINIO=44
    PUERTO=45
    RUTA=46
    URL=47
    WS=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class JsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_json(self):
            return self.getTypedRuleContext(GramáticaParser.T_jsonContext,0)


        def WS(self):
            return self.getToken(GramáticaParser.WS, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)




    def json(self):

        localctx = GramáticaParser.JsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_json)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.t_json()
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.match(GramáticaParser.WS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_jsonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def t_contenido(self):
            return self.getTypedRuleContext(GramáticaParser.T_contenidoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_json" ):
                listener.enterT_json(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_json" ):
                listener.exitT_json(self)




    def t_json(self):

        localctx = GramáticaParser.T_jsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_t_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GramáticaParser.ABRO_LLAVE)
            self.state = 95
            self.t_contenido()
            self.state = 96
            self.match(GramáticaParser.CIERRO_LLAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_contenidoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_empresas(self):
            return self.getTypedRuleContext(GramáticaParser.T_empresasContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramáticaParser.COMA)
            else:
                return self.getToken(GramáticaParser.COMA, i)

        def t_version(self):
            return self.getTypedRuleContext(GramáticaParser.T_versionContext,0)


        def t_firma_digital(self):
            return self.getTypedRuleContext(GramáticaParser.T_firma_digitalContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_contenido

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenido" ):
                listener.enterT_contenido(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenido" ):
                listener.exitT_contenido(self)




    def t_contenido(self):

        localctx = GramáticaParser.T_contenidoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_t_contenido)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.t_empresas()
            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(GramáticaParser.COMA)
                self.state = 100
                self.t_version()


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 103
                self.match(GramáticaParser.COMA)
                self.state = 104
                self.t_firma_digital()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_versionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION(self):
            return self.getToken(GramáticaParser.VERSION, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_version

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_version" ):
                listener.enterT_version(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_version" ):
                listener.exitT_version(self)




    def t_version(self):

        localctx = GramáticaParser.T_versionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_t_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(GramáticaParser.VERSION)
            self.state = 108
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_firma_digitalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FIRMA_DIGITAL(self):
            return self.getToken(GramáticaParser.FIRMA_DIGITAL, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_firma_digital

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_firma_digital" ):
                listener.enterT_firma_digital(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_firma_digital" ):
                listener.exitT_firma_digital(self)




    def t_firma_digital(self):

        localctx = GramáticaParser.T_firma_digitalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_t_firma_digital)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GramáticaParser.FIRMA_DIGITAL)
            self.state = 111
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_empresasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMPRESAS(self):
            return self.getToken(GramáticaParser.EMPRESAS, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramáticaParser.ABRO_CORCHETE, 0)

        def t_listaempresas(self):
            return self.getTypedRuleContext(GramáticaParser.T_listaempresasContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramáticaParser.CIERRO_CORCHETE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_empresas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empresas" ):
                listener.enterT_empresas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empresas" ):
                listener.exitT_empresas(self)




    def t_empresas(self):

        localctx = GramáticaParser.T_empresasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_t_empresas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(GramáticaParser.EMPRESAS)
            self.state = 114
            self.match(GramáticaParser.ABRO_CORCHETE)
            self.state = 115
            self.t_listaempresas()
            self.state = 116
            self.match(GramáticaParser.CIERRO_CORCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_listaempresasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_empresa(self):
            return self.getTypedRuleContext(GramáticaParser.T_empresaContext,0)


        def COMA(self):
            return self.getToken(GramáticaParser.COMA, 0)

        def t_listaempresas(self):
            return self.getTypedRuleContext(GramáticaParser.T_listaempresasContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_listaempresas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listaempresas" ):
                listener.enterT_listaempresas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listaempresas" ):
                listener.exitT_listaempresas(self)




    def t_listaempresas(self):

        localctx = GramáticaParser.T_listaempresasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_t_listaempresas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.t_empresa()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 119
                self.match(GramáticaParser.COMA)
                self.state = 120
                self.t_listaempresas()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_empresaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def t_contenidoempresa(self):
            return self.getTypedRuleContext(GramáticaParser.T_contenidoempresaContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_empresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empresa" ):
                listener.enterT_empresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empresa" ):
                listener.exitT_empresa(self)




    def t_empresa(self):

        localctx = GramáticaParser.T_empresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_t_empresa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(GramáticaParser.ABRO_LLAVE)
            self.state = 124
            self.t_contenidoempresa()
            self.state = 125
            self.match(GramáticaParser.CIERRO_LLAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_contenidoempresaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_nombre_empresa(self):
            return self.getTypedRuleContext(GramáticaParser.T_nombre_empresaContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramáticaParser.COMA)
            else:
                return self.getToken(GramáticaParser.COMA, i)

        def t_fundacion(self):
            return self.getTypedRuleContext(GramáticaParser.T_fundacionContext,0)


        def t_ingresos_anuales(self):
            return self.getTypedRuleContext(GramáticaParser.T_ingresos_anualesContext,0)


        def t_pyme(self):
            return self.getTypedRuleContext(GramáticaParser.T_pymeContext,0)


        def t_departamentos(self):
            return self.getTypedRuleContext(GramáticaParser.T_departamentosContext,0)


        def t_direccion(self):
            return self.getTypedRuleContext(GramáticaParser.T_direccionContext,0)


        def t_link(self):
            return self.getTypedRuleContext(GramáticaParser.T_linkContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_contenidoempresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidoempresa" ):
                listener.enterT_contenidoempresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidoempresa" ):
                listener.exitT_contenidoempresa(self)




    def t_contenidoempresa(self):

        localctx = GramáticaParser.T_contenidoempresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_t_contenidoempresa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.t_nombre_empresa()
            self.state = 128
            self.match(GramáticaParser.COMA)
            self.state = 129
            self.t_fundacion()
            self.state = 130
            self.match(GramáticaParser.COMA)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 131
                self.t_direccion()
                self.state = 132
                self.match(GramáticaParser.COMA)


            self.state = 136
            self.t_ingresos_anuales()
            self.state = 137
            self.match(GramáticaParser.COMA)
            self.state = 138
            self.t_pyme()
            self.state = 139
            self.match(GramáticaParser.COMA)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 140
                self.t_link()
                self.state = 141
                self.match(GramáticaParser.COMA)


            self.state = 145
            self.t_departamentos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_ingresos_anualesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INGRESOS_ANUALES(self):
            return self.getToken(GramáticaParser.INGRESOS_ANUALES, 0)

        def FLOAT(self):
            return self.getToken(GramáticaParser.FLOAT, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_ingresos_anuales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_ingresos_anuales" ):
                listener.enterT_ingresos_anuales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_ingresos_anuales" ):
                listener.exitT_ingresos_anuales(self)




    def t_ingresos_anuales(self):

        localctx = GramáticaParser.T_ingresos_anualesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_t_ingresos_anuales)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(GramáticaParser.INGRESOS_ANUALES)
            self.state = 148
            self.match(GramáticaParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_nombre_empresaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOMBRE_EMPRESA(self):
            return self.getToken(GramáticaParser.NOMBRE_EMPRESA, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_nombre_empresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_nombre_empresa" ):
                listener.enterT_nombre_empresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_nombre_empresa" ):
                listener.exitT_nombre_empresa(self)




    def t_nombre_empresa(self):

        localctx = GramáticaParser.T_nombre_empresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_t_nombre_empresa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(GramáticaParser.NOMBRE_EMPRESA)
            self.state = 151
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_fundacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNDACION(self):
            return self.getToken(GramáticaParser.FUNDACION, 0)

        def INT(self):
            return self.getToken(GramáticaParser.INT, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_fundacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fundacion" ):
                listener.enterT_fundacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fundacion" ):
                listener.exitT_fundacion(self)




    def t_fundacion(self):

        localctx = GramáticaParser.T_fundacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_t_fundacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(GramáticaParser.FUNDACION)
            self.state = 154
            self.match(GramáticaParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_pymeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYME(self):
            return self.getToken(GramáticaParser.PYME, 0)

        def TRUE(self):
            return self.getToken(GramáticaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GramáticaParser.FALSE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_pyme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_pyme" ):
                listener.enterT_pyme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_pyme" ):
                listener.exitT_pyme(self)




    def t_pyme(self):

        localctx = GramáticaParser.T_pymeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_t_pyme)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(GramáticaParser.PYME)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_linkContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINK(self):
            return self.getToken(GramáticaParser.LINK, 0)

        def URL(self):
            return self.getToken(GramáticaParser.URL, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_link" ):
                listener.enterT_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_link" ):
                listener.exitT_link(self)




    def t_link(self):

        localctx = GramáticaParser.T_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_t_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(GramáticaParser.LINK)
            self.state = 160
            self.match(GramáticaParser.URL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_direccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIRECCION(self):
            return self.getToken(GramáticaParser.DIRECCION, 0)

        def t_tipo_direccion(self):
            return self.getTypedRuleContext(GramáticaParser.T_tipo_direccionContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_direccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_direccion" ):
                listener.enterT_direccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_direccion" ):
                listener.exitT_direccion(self)




    def t_direccion(self):

        localctx = GramáticaParser.T_direccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_t_direccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(GramáticaParser.DIRECCION)
            self.state = 163
            self.t_tipo_direccion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_tipo_direccionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NULL(self):
            return self.getToken(GramáticaParser.NULL, 0)

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramáticaParser.ABRO_CORCHETE, 0)

        def CIERRO_CORCHETE(self):
            return self.getToken(GramáticaParser.CIERRO_CORCHETE, 0)

        def t_calle(self):
            return self.getTypedRuleContext(GramáticaParser.T_calleContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramáticaParser.COMA)
            else:
                return self.getToken(GramáticaParser.COMA, i)

        def t_ciudad(self):
            return self.getTypedRuleContext(GramáticaParser.T_ciudadContext,0)


        def t_pais(self):
            return self.getTypedRuleContext(GramáticaParser.T_paisContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_tipo_direccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_tipo_direccion" ):
                listener.enterT_tipo_direccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_tipo_direccion" ):
                listener.exitT_tipo_direccion(self)




    def t_tipo_direccion(self):

        localctx = GramáticaParser.T_tipo_direccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_t_tipo_direccion)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(GramáticaParser.NULL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(GramáticaParser.ABRO_LLAVE)
                self.state = 167
                self.match(GramáticaParser.CIERRO_LLAVE)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 168
                self.match(GramáticaParser.ABRO_CORCHETE)
                self.state = 169
                self.match(GramáticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 170
                self.match(GramáticaParser.ABRO_LLAVE)
                self.state = 171
                self.t_calle()
                self.state = 172
                self.match(GramáticaParser.COMA)
                self.state = 173
                self.t_ciudad()
                self.state = 174
                self.match(GramáticaParser.COMA)
                self.state = 175
                self.t_pais()
                self.state = 176
                self.match(GramáticaParser.CIERRO_LLAVE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_calleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALLE(self):
            return self.getToken(GramáticaParser.CALLE, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_calle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_calle" ):
                listener.enterT_calle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_calle" ):
                listener.exitT_calle(self)




    def t_calle(self):

        localctx = GramáticaParser.T_calleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_t_calle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(GramáticaParser.CALLE)
            self.state = 181
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_ciudadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CIUDAD(self):
            return self.getToken(GramáticaParser.CIUDAD, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_ciudad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_ciudad" ):
                listener.enterT_ciudad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_ciudad" ):
                listener.exitT_ciudad(self)




    def t_ciudad(self):

        localctx = GramáticaParser.T_ciudadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_t_ciudad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(GramáticaParser.CIUDAD)
            self.state = 184
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_paisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAIS(self):
            return self.getToken(GramáticaParser.PAIS, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_pais

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_pais" ):
                listener.enterT_pais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_pais" ):
                listener.exitT_pais(self)




    def t_pais(self):

        localctx = GramáticaParser.T_paisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_t_pais)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(GramáticaParser.PAIS)
            self.state = 187
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_departamentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEPARTAMENTOS(self):
            return self.getToken(GramáticaParser.DEPARTAMENTOS, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramáticaParser.ABRO_CORCHETE, 0)

        def t_listadepartamentos(self):
            return self.getTypedRuleContext(GramáticaParser.T_listadepartamentosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramáticaParser.CIERRO_CORCHETE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_departamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_departamentos" ):
                listener.enterT_departamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_departamentos" ):
                listener.exitT_departamentos(self)




    def t_departamentos(self):

        localctx = GramáticaParser.T_departamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_t_departamentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(GramáticaParser.DEPARTAMENTOS)
            self.state = 190
            self.match(GramáticaParser.ABRO_CORCHETE)
            self.state = 191
            self.t_listadepartamentos()
            self.state = 192
            self.match(GramáticaParser.CIERRO_CORCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_listadepartamentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_departamento(self):
            return self.getTypedRuleContext(GramáticaParser.T_departamentoContext,0)


        def COMA(self):
            return self.getToken(GramáticaParser.COMA, 0)

        def t_listadepartamentos(self):
            return self.getTypedRuleContext(GramáticaParser.T_listadepartamentosContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_listadepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listadepartamentos" ):
                listener.enterT_listadepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listadepartamentos" ):
                listener.exitT_listadepartamentos(self)




    def t_listadepartamentos(self):

        localctx = GramáticaParser.T_listadepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_t_listadepartamentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.t_departamento()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 195
                self.match(GramáticaParser.COMA)
                self.state = 196
                self.t_listadepartamentos()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_departamentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def t_contenidodepartamento(self):
            return self.getTypedRuleContext(GramáticaParser.T_contenidodepartamentoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_departamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_departamento" ):
                listener.enterT_departamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_departamento" ):
                listener.exitT_departamento(self)




    def t_departamento(self):

        localctx = GramáticaParser.T_departamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_t_departamento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(GramáticaParser.ABRO_LLAVE)
            self.state = 200
            self.t_contenidodepartamento()
            self.state = 201
            self.match(GramáticaParser.CIERRO_LLAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_contenidodepartamentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_nombre(self):
            return self.getTypedRuleContext(GramáticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramáticaParser.COMA)
            else:
                return self.getToken(GramáticaParser.COMA, i)

        def t_subdepartamentos(self):
            return self.getTypedRuleContext(GramáticaParser.T_subdepartamentosContext,0)


        def t_jefe(self):
            return self.getTypedRuleContext(GramáticaParser.T_jefeContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_contenidodepartamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidodepartamento" ):
                listener.enterT_contenidodepartamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidodepartamento" ):
                listener.exitT_contenidodepartamento(self)




    def t_contenidodepartamento(self):

        localctx = GramáticaParser.T_contenidodepartamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_t_contenidodepartamento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.t_nombre()
            self.state = 204
            self.match(GramáticaParser.COMA)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 205
                self.t_jefe()
                self.state = 206
                self.match(GramáticaParser.COMA)


            self.state = 210
            self.t_subdepartamentos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_nombreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOMBRE(self):
            return self.getToken(GramáticaParser.NOMBRE, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_nombre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_nombre" ):
                listener.enterT_nombre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_nombre" ):
                listener.exitT_nombre(self)




    def t_nombre(self):

        localctx = GramáticaParser.T_nombreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_t_nombre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(GramáticaParser.NOMBRE)
            self.state = 213
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_jefeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JEFE(self):
            return self.getToken(GramáticaParser.JEFE, 0)

        def STRING(self):
            return self.getToken(GramáticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_jefe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_jefe" ):
                listener.enterT_jefe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_jefe" ):
                listener.exitT_jefe(self)




    def t_jefe(self):

        localctx = GramáticaParser.T_jefeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_t_jefe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(GramáticaParser.JEFE)
            self.state = 216
            self.match(GramáticaParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_subdepartamentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBDEPARTAMENTOS_LISTA(self):
            return self.getToken(GramáticaParser.SUBDEPARTAMENTOS_LISTA, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramáticaParser.ABRO_CORCHETE, 0)

        def t_listasubdepartamentos(self):
            return self.getTypedRuleContext(GramáticaParser.T_listasubdepartamentosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramáticaParser.CIERRO_CORCHETE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_subdepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_subdepartamentos" ):
                listener.enterT_subdepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_subdepartamentos" ):
                listener.exitT_subdepartamentos(self)




    def t_subdepartamentos(self):

        localctx = GramáticaParser.T_subdepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_t_subdepartamentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(GramáticaParser.SUBDEPARTAMENTOS_LISTA)
            self.state = 219
            self.match(GramáticaParser.ABRO_CORCHETE)
            self.state = 220
            self.t_listasubdepartamentos()
            self.state = 221
            self.match(GramáticaParser.CIERRO_CORCHETE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_listasubdepartamentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_subdepartamento(self):
            return self.getTypedRuleContext(GramáticaParser.T_subdepartamentoContext,0)


        def COMA(self):
            return self.getToken(GramáticaParser.COMA, 0)

        def t_listasubdepartamentos(self):
            return self.getTypedRuleContext(GramáticaParser.T_listasubdepartamentosContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_listasubdepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listasubdepartamentos" ):
                listener.enterT_listasubdepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listasubdepartamentos" ):
                listener.exitT_listasubdepartamentos(self)




    def t_listasubdepartamentos(self):

        localctx = GramáticaParser.T_listasubdepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_t_listasubdepartamentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.t_subdepartamento()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 224
                self.match(GramáticaParser.COMA)
                self.state = 225
                self.t_listasubdepartamentos()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_subdepartamentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def t_contenidosubdepartamentos(self):
            return self.getTypedRuleContext(GramáticaParser.T_contenidosubdepartamentosContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_subdepartamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_subdepartamento" ):
                listener.enterT_subdepartamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_subdepartamento" ):
                listener.exitT_subdepartamento(self)




    def t_subdepartamento(self):

        localctx = GramáticaParser.T_subdepartamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_t_subdepartamento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(GramáticaParser.ABRO_LLAVE)
            self.state = 229
            self.t_contenidosubdepartamentos()
            self.state = 230
            self.match(GramáticaParser.CIERRO_LLAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_contenidosubdepartamentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_nombre(self):
            return self.getTypedRuleContext(GramáticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramáticaParser.COMA)
            else:
                return self.getToken(GramáticaParser.COMA, i)

        def t_jefe(self):
            return self.getTypedRuleContext(GramáticaParser.T_jefeContext,0)


        def t_empleados(self):
            return self.getTypedRuleContext(GramáticaParser.T_empleadosContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_contenidosubdepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidosubdepartamentos" ):
                listener.enterT_contenidosubdepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidosubdepartamentos" ):
                listener.exitT_contenidosubdepartamentos(self)




    def t_contenidosubdepartamentos(self):

        localctx = GramáticaParser.T_contenidosubdepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_t_contenidosubdepartamentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.t_nombre()
            self.state = 233
            self.match(GramáticaParser.COMA)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 234
                self.t_jefe()
                self.state = 235
                self.match(GramáticaParser.COMA)


            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 239
                self.t_empleados()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_empleadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMPLEADO_LISTA(self):
            return self.getToken(GramáticaParser.EMPLEADO_LISTA, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramáticaParser.ABRO_CORCHETE, 0)

        def t_listaempleados(self):
            return self.getTypedRuleContext(GramáticaParser.T_listaempleadosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramáticaParser.CIERRO_CORCHETE, 0)

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def NULL(self):
            return self.getToken(GramáticaParser.NULL, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_empleados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empleados" ):
                listener.enterT_empleados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empleados" ):
                listener.exitT_empleados(self)




    def t_empleados(self):

        localctx = GramáticaParser.T_empleadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_t_empleados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(GramáticaParser.EMPLEADO_LISTA)
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 243
                self.match(GramáticaParser.ABRO_CORCHETE)
                self.state = 244
                self.t_listaempleados()
                self.state = 245
                self.match(GramáticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 2:
                self.state = 247
                self.match(GramáticaParser.ABRO_LLAVE)
                self.state = 248
                self.match(GramáticaParser.CIERRO_LLAVE)
                pass

            elif la_ == 3:
                self.state = 249
                self.match(GramáticaParser.ABRO_CORCHETE)
                self.state = 250
                self.match(GramáticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 4:
                self.state = 251
                self.match(GramáticaParser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_listaempleadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_empleado(self):
            return self.getTypedRuleContext(GramáticaParser.T_empleadoContext,0)


        def COMA(self):
            return self.getToken(GramáticaParser.COMA, 0)

        def t_listaempleados(self):
            return self.getTypedRuleContext(GramáticaParser.T_listaempleadosContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_listaempleados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listaempleados" ):
                listener.enterT_listaempleados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listaempleados" ):
                listener.exitT_listaempleados(self)




    def t_listaempleados(self):

        localctx = GramáticaParser.T_listaempleadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_t_listaempleados)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.t_empleado()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 255
                self.match(GramáticaParser.COMA)
                self.state = 256
                self.t_listaempleados()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_empleadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def t_contenidoempleado(self):
            return self.getTypedRuleContext(GramáticaParser.T_contenidoempleadoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_empleado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empleado" ):
                listener.enterT_empleado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empleado" ):
                listener.exitT_empleado(self)




    def t_empleado(self):

        localctx = GramáticaParser.T_empleadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_t_empleado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(GramáticaParser.ABRO_LLAVE)
            self.state = 260
            self.t_contenidoempleado()
            self.state = 261
            self.match(GramáticaParser.CIERRO_LLAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_contenidoempleadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_nombre(self):
            return self.getTypedRuleContext(GramáticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramáticaParser.COMA)
            else:
                return self.getToken(GramáticaParser.COMA, i)

        def t_cargo(self):
            return self.getTypedRuleContext(GramáticaParser.T_cargoContext,0)


        def t_salario(self):
            return self.getTypedRuleContext(GramáticaParser.T_salarioContext,0)


        def t_activo(self):
            return self.getTypedRuleContext(GramáticaParser.T_activoContext,0)


        def t_fecha_contratacion(self):
            return self.getTypedRuleContext(GramáticaParser.T_fecha_contratacionContext,0)


        def t_proyectos(self):
            return self.getTypedRuleContext(GramáticaParser.T_proyectosContext,0)


        def t_edad(self):
            return self.getTypedRuleContext(GramáticaParser.T_edadContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_contenidoempleado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidoempleado" ):
                listener.enterT_contenidoempleado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidoempleado" ):
                listener.exitT_contenidoempleado(self)




    def t_contenidoempleado(self):

        localctx = GramáticaParser.T_contenidoempleadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_t_contenidoempleado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            self.t_nombre()
            self.state = 264
            self.match(GramáticaParser.COMA)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==33:
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 265
                    self.t_edad()


                self.state = 268
                self.match(GramáticaParser.COMA)


            self.state = 271
            self.t_cargo()
            self.state = 272
            self.match(GramáticaParser.COMA)
            self.state = 273
            self.t_salario()
            self.state = 274
            self.match(GramáticaParser.COMA)
            self.state = 275
            self.t_activo()
            self.state = 276
            self.match(GramáticaParser.COMA)
            self.state = 277
            self.t_fecha_contratacion()
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 278
                self.match(GramáticaParser.COMA)
                self.state = 279
                self.t_proyectos()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_edadContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EDAD(self):
            return self.getToken(GramáticaParser.EDAD, 0)

        def INT(self):
            return self.getToken(GramáticaParser.INT, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_edad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_edad" ):
                listener.enterT_edad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_edad" ):
                listener.exitT_edad(self)




    def t_edad(self):

        localctx = GramáticaParser.T_edadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_t_edad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(GramáticaParser.EDAD)
            self.state = 283
            self.match(GramáticaParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_cargoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARGO(self):
            return self.getToken(GramáticaParser.CARGO, 0)

        def TIPO_CARGO(self):
            return self.getToken(GramáticaParser.TIPO_CARGO, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_cargo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_cargo" ):
                listener.enterT_cargo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_cargo" ):
                listener.exitT_cargo(self)




    def t_cargo(self):

        localctx = GramáticaParser.T_cargoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_t_cargo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(GramáticaParser.CARGO)
            self.state = 286
            self.match(GramáticaParser.TIPO_CARGO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_salarioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SALARIO(self):
            return self.getToken(GramáticaParser.SALARIO, 0)

        def FLOAT(self):
            return self.getToken(GramáticaParser.FLOAT, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_salario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_salario" ):
                listener.enterT_salario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_salario" ):
                listener.exitT_salario(self)




    def t_salario(self):

        localctx = GramáticaParser.T_salarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_t_salario)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(GramáticaParser.SALARIO)
            self.state = 289
            self.match(GramáticaParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_activoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIVO(self):
            return self.getToken(GramáticaParser.ACTIVO, 0)

        def TRUE(self):
            return self.getToken(GramáticaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GramáticaParser.FALSE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_activo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_activo" ):
                listener.enterT_activo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_activo" ):
                listener.exitT_activo(self)




    def t_activo(self):

        localctx = GramáticaParser.T_activoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_t_activo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(GramáticaParser.ACTIVO)
            self.state = 292
            _la = self._input.LA(1)
            if not(_la==35 or _la==36):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_fecha_contratacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FECHA_CONTRATACION(self):
            return self.getToken(GramáticaParser.FECHA_CONTRATACION, 0)

        def DATE(self):
            return self.getToken(GramáticaParser.DATE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_fecha_contratacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fecha_contratacion" ):
                listener.enterT_fecha_contratacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fecha_contratacion" ):
                listener.exitT_fecha_contratacion(self)




    def t_fecha_contratacion(self):

        localctx = GramáticaParser.T_fecha_contratacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_t_fecha_contratacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(GramáticaParser.FECHA_CONTRATACION)
            self.state = 295
            self.match(GramáticaParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_proyectosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROYECTOS_LISTA(self):
            return self.getToken(GramáticaParser.PROYECTOS_LISTA, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramáticaParser.ABRO_CORCHETE, 0)

        def t_listaproyectos(self):
            return self.getTypedRuleContext(GramáticaParser.T_listaproyectosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramáticaParser.CIERRO_CORCHETE, 0)

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def NULL(self):
            return self.getToken(GramáticaParser.NULL, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_proyectos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_proyectos" ):
                listener.enterT_proyectos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_proyectos" ):
                listener.exitT_proyectos(self)




    def t_proyectos(self):

        localctx = GramáticaParser.T_proyectosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_t_proyectos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(GramáticaParser.PROYECTOS_LISTA)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 298
                self.match(GramáticaParser.ABRO_CORCHETE)
                self.state = 299
                self.t_listaproyectos()
                self.state = 300
                self.match(GramáticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 2:
                self.state = 302
                self.match(GramáticaParser.ABRO_LLAVE)
                self.state = 303
                self.match(GramáticaParser.CIERRO_LLAVE)
                pass

            elif la_ == 3:
                self.state = 304
                self.match(GramáticaParser.ABRO_CORCHETE)
                self.state = 305
                self.match(GramáticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 4:
                self.state = 306
                self.match(GramáticaParser.NULL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_listaproyectosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_proyecto(self):
            return self.getTypedRuleContext(GramáticaParser.T_proyectoContext,0)


        def COMA(self):
            return self.getToken(GramáticaParser.COMA, 0)

        def t_listaproyectos(self):
            return self.getTypedRuleContext(GramáticaParser.T_listaproyectosContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_listaproyectos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listaproyectos" ):
                listener.enterT_listaproyectos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listaproyectos" ):
                listener.exitT_listaproyectos(self)




    def t_listaproyectos(self):

        localctx = GramáticaParser.T_listaproyectosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_t_listaproyectos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.t_proyecto()
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 310
                self.match(GramáticaParser.COMA)
                self.state = 311
                self.t_listaproyectos()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_proyectoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRO_LLAVE(self):
            return self.getToken(GramáticaParser.ABRO_LLAVE, 0)

        def t_contenidoproyecto(self):
            return self.getTypedRuleContext(GramáticaParser.T_contenidoproyectoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramáticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_proyecto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_proyecto" ):
                listener.enterT_proyecto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_proyecto" ):
                listener.exitT_proyecto(self)




    def t_proyecto(self):

        localctx = GramáticaParser.T_proyectoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_t_proyecto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(GramáticaParser.ABRO_LLAVE)
            self.state = 315
            self.t_contenidoproyecto()
            self.state = 316
            self.match(GramáticaParser.CIERRO_LLAVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_contenidoproyectoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def t_nombre(self):
            return self.getTypedRuleContext(GramáticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramáticaParser.COMA)
            else:
                return self.getToken(GramáticaParser.COMA, i)

        def t_fecha_inicio(self):
            return self.getTypedRuleContext(GramáticaParser.T_fecha_inicioContext,0)


        def t_estado(self):
            return self.getTypedRuleContext(GramáticaParser.T_estadoContext,0)


        def t_fecha_fin(self):
            return self.getTypedRuleContext(GramáticaParser.T_fecha_finContext,0)


        def getRuleIndex(self):
            return GramáticaParser.RULE_t_contenidoproyecto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidoproyecto" ):
                listener.enterT_contenidoproyecto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidoproyecto" ):
                listener.exitT_contenidoproyecto(self)




    def t_contenidoproyecto(self):

        localctx = GramáticaParser.T_contenidoproyectoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_t_contenidoproyecto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.t_nombre()
            self.state = 319
            self.match(GramáticaParser.COMA)
            self.state = 323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 320
                self.t_estado()
                self.state = 321
                self.match(GramáticaParser.COMA)


            self.state = 325
            self.t_fecha_inicio()
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 326
                self.match(GramáticaParser.COMA)
                self.state = 327
                self.t_fecha_fin()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_fecha_inicioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FECHA_INICIO(self):
            return self.getToken(GramáticaParser.FECHA_INICIO, 0)

        def DATE(self):
            return self.getToken(GramáticaParser.DATE, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_fecha_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fecha_inicio" ):
                listener.enterT_fecha_inicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fecha_inicio" ):
                listener.exitT_fecha_inicio(self)




    def t_fecha_inicio(self):

        localctx = GramáticaParser.T_fecha_inicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_t_fecha_inicio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(GramáticaParser.FECHA_INICIO)
            self.state = 331
            self.match(GramáticaParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_estadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESTADO(self):
            return self.getToken(GramáticaParser.ESTADO, 0)

        def TIPO_ESTADO(self):
            return self.getToken(GramáticaParser.TIPO_ESTADO, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_estado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_estado" ):
                listener.enterT_estado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_estado" ):
                listener.exitT_estado(self)




    def t_estado(self):

        localctx = GramáticaParser.T_estadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_t_estado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(GramáticaParser.ESTADO)
            self.state = 334
            self.match(GramáticaParser.TIPO_ESTADO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class T_fecha_finContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FECHA_FIN(self):
            return self.getToken(GramáticaParser.FECHA_FIN, 0)

        def DATE(self):
            return self.getToken(GramáticaParser.DATE, 0)

        def NULL(self):
            return self.getToken(GramáticaParser.NULL, 0)

        def getRuleIndex(self):
            return GramáticaParser.RULE_t_fecha_fin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fecha_fin" ):
                listener.enterT_fecha_fin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fecha_fin" ):
                listener.exitT_fecha_fin(self)




    def t_fecha_fin(self):

        localctx = GramáticaParser.T_fecha_finContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_t_fecha_fin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(GramáticaParser.FECHA_FIN)
            self.state = 337
            _la = self._input.LA(1)
            if not(_la==34 or _la==40):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






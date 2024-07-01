# Generated from C:/Lexer-Parser/src/Gramatica.g4 by ANTLR 4.13.1
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
        4,1,49,336,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,175,8,15,1,16,
        1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,
        1,20,1,20,1,20,3,20,194,8,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,3,22,205,8,22,1,22,1,22,1,23,1,23,1,23,1,24,1,24,1,24,
        1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,3,26,223,8,26,1,27,1,27,
        1,27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,234,8,28,1,28,3,28,237,8,
        28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,3,29,249,8,
        29,1,30,1,30,1,30,3,30,254,8,30,1,31,1,31,1,31,1,31,1,32,1,32,1,
        32,3,32,263,8,32,1,32,3,32,266,8,32,1,32,1,32,1,32,1,32,1,32,1,32,
        1,32,1,32,1,32,3,32,277,8,32,1,33,1,33,1,33,1,34,1,34,1,34,1,35,
        1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,3,38,304,8,38,1,39,1,39,1,39,3,39,309,8,
        39,1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,3,41,320,8,41,1,
        41,1,41,1,41,3,41,325,8,41,1,42,1,42,1,42,1,43,1,43,1,43,1,44,1,
        44,1,44,1,44,0,0,45,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,
        78,80,82,84,86,88,0,3,1,0,35,36,2,0,37,37,39,39,2,0,34,34,40,40,
        315,0,92,1,0,0,0,2,94,1,0,0,0,4,98,1,0,0,0,6,107,1,0,0,0,8,110,1,
        0,0,0,10,113,1,0,0,0,12,118,1,0,0,0,14,123,1,0,0,0,16,127,1,0,0,
        0,18,147,1,0,0,0,20,150,1,0,0,0,22,153,1,0,0,0,24,156,1,0,0,0,26,
        159,1,0,0,0,28,162,1,0,0,0,30,174,1,0,0,0,32,176,1,0,0,0,34,179,
        1,0,0,0,36,182,1,0,0,0,38,185,1,0,0,0,40,190,1,0,0,0,42,195,1,0,
        0,0,44,199,1,0,0,0,46,208,1,0,0,0,48,211,1,0,0,0,50,214,1,0,0,0,
        52,219,1,0,0,0,54,224,1,0,0,0,56,228,1,0,0,0,58,238,1,0,0,0,60,250,
        1,0,0,0,62,255,1,0,0,0,64,259,1,0,0,0,66,278,1,0,0,0,68,281,1,0,
        0,0,70,284,1,0,0,0,72,287,1,0,0,0,74,290,1,0,0,0,76,293,1,0,0,0,
        78,305,1,0,0,0,80,310,1,0,0,0,82,314,1,0,0,0,84,326,1,0,0,0,86,329,
        1,0,0,0,88,332,1,0,0,0,90,93,3,2,1,0,91,93,5,48,0,0,92,90,1,0,0,
        0,92,91,1,0,0,0,93,1,1,0,0,0,94,95,5,29,0,0,95,96,3,4,2,0,96,97,
        5,30,0,0,97,3,1,0,0,0,98,101,3,10,5,0,99,100,5,33,0,0,100,102,3,
        6,3,0,101,99,1,0,0,0,101,102,1,0,0,0,102,105,1,0,0,0,103,104,5,33,
        0,0,104,106,3,8,4,0,105,103,1,0,0,0,105,106,1,0,0,0,106,5,1,0,0,
        0,107,108,5,2,0,0,108,109,5,47,0,0,109,7,1,0,0,0,110,111,5,3,0,0,
        111,112,5,47,0,0,112,9,1,0,0,0,113,114,5,1,0,0,114,115,5,31,0,0,
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
        0,151,152,5,47,0,0,152,21,1,0,0,0,153,154,5,6,0,0,154,155,5,37,0,
        0,155,23,1,0,0,0,156,157,5,7,0,0,157,158,7,0,0,0,158,25,1,0,0,0,
        159,160,5,8,0,0,160,161,5,46,0,0,161,27,1,0,0,0,162,163,5,9,0,0,
        163,164,3,30,15,0,164,29,1,0,0,0,165,175,5,34,0,0,166,167,5,29,0,
        0,167,168,3,32,16,0,168,169,5,33,0,0,169,170,3,34,17,0,170,171,5,
        33,0,0,171,172,3,36,18,0,172,173,5,30,0,0,173,175,1,0,0,0,174,165,
        1,0,0,0,174,166,1,0,0,0,175,31,1,0,0,0,176,177,5,20,0,0,177,178,
        5,47,0,0,178,33,1,0,0,0,179,180,5,21,0,0,180,181,5,47,0,0,181,35,
        1,0,0,0,182,183,5,22,0,0,183,184,5,47,0,0,184,37,1,0,0,0,185,186,
        5,23,0,0,186,187,5,31,0,0,187,188,3,40,20,0,188,189,5,32,0,0,189,
        39,1,0,0,0,190,193,3,42,21,0,191,192,5,33,0,0,192,194,3,40,20,0,
        193,191,1,0,0,0,193,194,1,0,0,0,194,41,1,0,0,0,195,196,5,29,0,0,
        196,197,3,44,22,0,197,198,5,30,0,0,198,43,1,0,0,0,199,200,3,46,23,
        0,200,204,5,33,0,0,201,202,3,48,24,0,202,203,5,33,0,0,203,205,1,
        0,0,0,204,201,1,0,0,0,204,205,1,0,0,0,205,206,1,0,0,0,206,207,3,
        50,25,0,207,45,1,0,0,0,208,209,5,27,0,0,209,210,5,47,0,0,210,47,
        1,0,0,0,211,212,5,28,0,0,212,213,5,47,0,0,213,49,1,0,0,0,214,215,
        5,25,0,0,215,216,5,31,0,0,216,217,3,52,26,0,217,218,5,32,0,0,218,
        51,1,0,0,0,219,222,3,54,27,0,220,221,5,33,0,0,221,223,3,52,26,0,
        222,220,1,0,0,0,222,223,1,0,0,0,223,53,1,0,0,0,224,225,5,29,0,0,
        225,226,3,56,28,0,226,227,5,30,0,0,227,55,1,0,0,0,228,229,3,46,23,
        0,229,233,5,33,0,0,230,231,3,48,24,0,231,232,5,33,0,0,232,234,1,
        0,0,0,233,230,1,0,0,0,233,234,1,0,0,0,234,236,1,0,0,0,235,237,3,
        58,29,0,236,235,1,0,0,0,236,237,1,0,0,0,237,57,1,0,0,0,238,248,5,
        24,0,0,239,240,5,31,0,0,240,241,3,60,30,0,241,242,5,32,0,0,242,249,
        1,0,0,0,243,244,5,29,0,0,244,249,5,30,0,0,245,246,5,31,0,0,246,249,
        5,32,0,0,247,249,5,34,0,0,248,239,1,0,0,0,248,243,1,0,0,0,248,245,
        1,0,0,0,248,247,1,0,0,0,249,59,1,0,0,0,250,253,3,62,31,0,251,252,
        5,33,0,0,252,254,3,60,30,0,253,251,1,0,0,0,253,254,1,0,0,0,254,61,
        1,0,0,0,255,256,5,29,0,0,256,257,3,64,32,0,257,258,5,30,0,0,258,
        63,1,0,0,0,259,260,3,46,23,0,260,265,5,33,0,0,261,263,3,66,33,0,
        262,261,1,0,0,0,262,263,1,0,0,0,263,264,1,0,0,0,264,266,5,33,0,0,
        265,262,1,0,0,0,265,266,1,0,0,0,266,267,1,0,0,0,267,268,3,68,34,
        0,268,269,5,33,0,0,269,270,3,70,35,0,270,271,5,33,0,0,271,272,3,
        72,36,0,272,273,5,33,0,0,273,276,3,74,37,0,274,275,5,33,0,0,275,
        277,3,76,38,0,276,274,1,0,0,0,276,277,1,0,0,0,277,65,1,0,0,0,278,
        279,5,10,0,0,279,280,5,37,0,0,280,67,1,0,0,0,281,282,5,11,0,0,282,
        283,5,12,0,0,283,69,1,0,0,0,284,285,5,13,0,0,285,286,7,1,0,0,286,
        71,1,0,0,0,287,288,5,14,0,0,288,289,7,0,0,0,289,73,1,0,0,0,290,291,
        5,15,0,0,291,292,5,40,0,0,292,75,1,0,0,0,293,303,5,26,0,0,294,295,
        5,31,0,0,295,296,3,78,39,0,296,297,5,32,0,0,297,304,1,0,0,0,298,
        299,5,29,0,0,299,304,5,30,0,0,300,301,5,31,0,0,301,304,5,32,0,0,
        302,304,5,34,0,0,303,294,1,0,0,0,303,298,1,0,0,0,303,300,1,0,0,0,
        303,302,1,0,0,0,304,77,1,0,0,0,305,308,3,80,40,0,306,307,5,33,0,
        0,307,309,3,78,39,0,308,306,1,0,0,0,308,309,1,0,0,0,309,79,1,0,0,
        0,310,311,5,29,0,0,311,312,3,82,41,0,312,313,5,30,0,0,313,81,1,0,
        0,0,314,315,3,46,23,0,315,319,5,33,0,0,316,317,3,86,43,0,317,318,
        5,33,0,0,318,320,1,0,0,0,319,316,1,0,0,0,319,320,1,0,0,0,320,321,
        1,0,0,0,321,324,3,84,42,0,322,323,5,33,0,0,323,325,3,88,44,0,324,
        322,1,0,0,0,324,325,1,0,0,0,325,83,1,0,0,0,326,327,5,16,0,0,327,
        328,5,40,0,0,328,85,1,0,0,0,329,330,5,17,0,0,330,331,5,18,0,0,331,
        87,1,0,0,0,332,333,5,19,0,0,333,334,7,2,0,0,334,89,1,0,0,0,21,92,
        101,105,121,134,143,174,193,204,222,233,236,248,253,262,265,276,
        303,308,319,324
    ]

class GramaticaParser ( Parser ):

    grammarFileName = "Gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"empresas\":'", "<INVALID>", "'\"firma_digital\":'", 
                     "'\"ingresos_anuales\":'", "'\"nombre_empresa\":'", 
                     "<INVALID>", "'\"pyme\":'", "'\"link\":'", "<INVALID>", 
                     "'\"edad\":'", "'\"cargo\":'", "<INVALID>", "'\"salario\":'", 
                     "'\"activo\":'", "<INVALID>", "'\"fecha_inicio\":'", 
                     "'\"estado\":'", "<INVALID>", "'\"fecha_fin\":'", "'\"calle\":'", 
                     "'\"ciudad\":'", "<INVALID>", "'\"departamentos\":'", 
                     "'\"empleados\":'", "'\"subdepartamentos\":'", "'\"proyectos\":'", 
                     "'\"nombre\":'", "'\"jefe\":'", "'{'", "'}'", "'['", 
                     "']'", "','", "'null'", "'true'", "'false'" ]

    symbolicNames = [ "<INVALID>", "EMPRESAS", "VERSION", "FIRMA_DIGITAL", 
                      "INGRESOS_ANUALES", "NOMBRE_EMPRESA", "FUNDACION", 
                      "PYME", "LINK", "DIRECCION", "EDAD", "CARGO", "TIPO_CARGO", 
                      "SALARIO", "ACTIVO", "FECHA_CONTRATACION", "FECHA_INICIO", 
                      "ESTADO", "TIPO_ESTADO", "FECHA_FIN", "CALLE", "CIUDAD", 
                      "PAIS", "DEPARTAMENTOS", "EMPLEADO_LISTA", "SUBDEPARTAMENTOS_LISTA", 
                      "PROYECTOS_LISTA", "NOMBRE", "JEFE", "ABRO_LLAVE", 
                      "CIERRO_LLAVE", "ABRO_CORCHETE", "CIERRO_CORCHETE", 
                      "COMA", "NULL", "TRUE", "FALSE", "INT", "DIGIT", "FLOAT", 
                      "DATE", "URL_STRING", "PROTOCOLO", "DOMINIO", "PUERTO", 
                      "RUTA", "URL", "STRING", "WS", "ERROR" ]

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
    INT=37
    DIGIT=38
    FLOAT=39
    DATE=40
    URL_STRING=41
    PROTOCOLO=42
    DOMINIO=43
    PUERTO=44
    RUTA=45
    URL=46
    STRING=47
    WS=48
    ERROR=49

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
            return self.getTypedRuleContext(GramaticaParser.T_jsonContext,0)


        def WS(self):
            return self.getToken(GramaticaParser.WS, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJson" ):
                listener.enterJson(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJson" ):
                listener.exitJson(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJson" ):
                return visitor.visitJson(self)
            else:
                return visitor.visitChildren(self)




    def json(self):

        localctx = GramaticaParser.JsonContext(self, self._ctx, self.state)
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
                self.match(GramaticaParser.WS)
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
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def t_contenido(self):
            return self.getTypedRuleContext(GramaticaParser.T_contenidoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_json

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_json" ):
                listener.enterT_json(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_json" ):
                listener.exitT_json(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_json" ):
                return visitor.visitT_json(self)
            else:
                return visitor.visitChildren(self)




    def t_json(self):

        localctx = GramaticaParser.T_jsonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_t_json)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(GramaticaParser.ABRO_LLAVE)
            self.state = 95
            self.t_contenido()
            self.state = 96
            self.match(GramaticaParser.CIERRO_LLAVE)
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
            return self.getTypedRuleContext(GramaticaParser.T_empresasContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def t_version(self):
            return self.getTypedRuleContext(GramaticaParser.T_versionContext,0)


        def t_firma_digital(self):
            return self.getTypedRuleContext(GramaticaParser.T_firma_digitalContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_contenido

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenido" ):
                listener.enterT_contenido(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenido" ):
                listener.exitT_contenido(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_contenido" ):
                return visitor.visitT_contenido(self)
            else:
                return visitor.visitChildren(self)




    def t_contenido(self):

        localctx = GramaticaParser.T_contenidoContext(self, self._ctx, self.state)
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
                self.match(GramaticaParser.COMA)
                self.state = 100
                self.t_version()


            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 103
                self.match(GramaticaParser.COMA)
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
            return self.getToken(GramaticaParser.VERSION, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_version

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_version" ):
                listener.enterT_version(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_version" ):
                listener.exitT_version(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_version" ):
                return visitor.visitT_version(self)
            else:
                return visitor.visitChildren(self)




    def t_version(self):

        localctx = GramaticaParser.T_versionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_t_version)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.match(GramaticaParser.VERSION)
            self.state = 108
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.FIRMA_DIGITAL, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_firma_digital

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_firma_digital" ):
                listener.enterT_firma_digital(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_firma_digital" ):
                listener.exitT_firma_digital(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_firma_digital" ):
                return visitor.visitT_firma_digital(self)
            else:
                return visitor.visitChildren(self)




    def t_firma_digital(self):

        localctx = GramaticaParser.T_firma_digitalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_t_firma_digital)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(GramaticaParser.FIRMA_DIGITAL)
            self.state = 111
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.EMPRESAS, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramaticaParser.ABRO_CORCHETE, 0)

        def t_listaempresas(self):
            return self.getTypedRuleContext(GramaticaParser.T_listaempresasContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramaticaParser.CIERRO_CORCHETE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_empresas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empresas" ):
                listener.enterT_empresas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empresas" ):
                listener.exitT_empresas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_empresas" ):
                return visitor.visitT_empresas(self)
            else:
                return visitor.visitChildren(self)




    def t_empresas(self):

        localctx = GramaticaParser.T_empresasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_t_empresas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(GramaticaParser.EMPRESAS)
            self.state = 114
            self.match(GramaticaParser.ABRO_CORCHETE)
            self.state = 115
            self.t_listaempresas()
            self.state = 116
            self.match(GramaticaParser.CIERRO_CORCHETE)
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
            return self.getTypedRuleContext(GramaticaParser.T_empresaContext,0)


        def COMA(self):
            return self.getToken(GramaticaParser.COMA, 0)

        def t_listaempresas(self):
            return self.getTypedRuleContext(GramaticaParser.T_listaempresasContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_listaempresas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listaempresas" ):
                listener.enterT_listaempresas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listaempresas" ):
                listener.exitT_listaempresas(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_listaempresas" ):
                return visitor.visitT_listaempresas(self)
            else:
                return visitor.visitChildren(self)




    def t_listaempresas(self):

        localctx = GramaticaParser.T_listaempresasContext(self, self._ctx, self.state)
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
                self.match(GramaticaParser.COMA)
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
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def t_contenidoempresa(self):
            return self.getTypedRuleContext(GramaticaParser.T_contenidoempresaContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_empresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empresa" ):
                listener.enterT_empresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empresa" ):
                listener.exitT_empresa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_empresa" ):
                return visitor.visitT_empresa(self)
            else:
                return visitor.visitChildren(self)




    def t_empresa(self):

        localctx = GramaticaParser.T_empresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_t_empresa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(GramaticaParser.ABRO_LLAVE)
            self.state = 124
            self.t_contenidoempresa()
            self.state = 125
            self.match(GramaticaParser.CIERRO_LLAVE)
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
            return self.getTypedRuleContext(GramaticaParser.T_nombre_empresaContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def t_fundacion(self):
            return self.getTypedRuleContext(GramaticaParser.T_fundacionContext,0)


        def t_ingresos_anuales(self):
            return self.getTypedRuleContext(GramaticaParser.T_ingresos_anualesContext,0)


        def t_pyme(self):
            return self.getTypedRuleContext(GramaticaParser.T_pymeContext,0)


        def t_departamentos(self):
            return self.getTypedRuleContext(GramaticaParser.T_departamentosContext,0)


        def t_direccion(self):
            return self.getTypedRuleContext(GramaticaParser.T_direccionContext,0)


        def t_link(self):
            return self.getTypedRuleContext(GramaticaParser.T_linkContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_contenidoempresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidoempresa" ):
                listener.enterT_contenidoempresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidoempresa" ):
                listener.exitT_contenidoempresa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_contenidoempresa" ):
                return visitor.visitT_contenidoempresa(self)
            else:
                return visitor.visitChildren(self)




    def t_contenidoempresa(self):

        localctx = GramaticaParser.T_contenidoempresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_t_contenidoempresa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.t_nombre_empresa()
            self.state = 128
            self.match(GramaticaParser.COMA)
            self.state = 129
            self.t_fundacion()
            self.state = 130
            self.match(GramaticaParser.COMA)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 131
                self.t_direccion()
                self.state = 132
                self.match(GramaticaParser.COMA)


            self.state = 136
            self.t_ingresos_anuales()
            self.state = 137
            self.match(GramaticaParser.COMA)
            self.state = 138
            self.t_pyme()
            self.state = 139
            self.match(GramaticaParser.COMA)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 140
                self.t_link()
                self.state = 141
                self.match(GramaticaParser.COMA)


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
            return self.getToken(GramaticaParser.INGRESOS_ANUALES, 0)

        def FLOAT(self):
            return self.getToken(GramaticaParser.FLOAT, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_ingresos_anuales

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_ingresos_anuales" ):
                listener.enterT_ingresos_anuales(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_ingresos_anuales" ):
                listener.exitT_ingresos_anuales(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_ingresos_anuales" ):
                return visitor.visitT_ingresos_anuales(self)
            else:
                return visitor.visitChildren(self)




    def t_ingresos_anuales(self):

        localctx = GramaticaParser.T_ingresos_anualesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_t_ingresos_anuales)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(GramaticaParser.INGRESOS_ANUALES)
            self.state = 148
            self.match(GramaticaParser.FLOAT)
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
            return self.getToken(GramaticaParser.NOMBRE_EMPRESA, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_nombre_empresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_nombre_empresa" ):
                listener.enterT_nombre_empresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_nombre_empresa" ):
                listener.exitT_nombre_empresa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_nombre_empresa" ):
                return visitor.visitT_nombre_empresa(self)
            else:
                return visitor.visitChildren(self)




    def t_nombre_empresa(self):

        localctx = GramaticaParser.T_nombre_empresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_t_nombre_empresa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(GramaticaParser.NOMBRE_EMPRESA)
            self.state = 151
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.FUNDACION, 0)

        def INT(self):
            return self.getToken(GramaticaParser.INT, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_fundacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fundacion" ):
                listener.enterT_fundacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fundacion" ):
                listener.exitT_fundacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_fundacion" ):
                return visitor.visitT_fundacion(self)
            else:
                return visitor.visitChildren(self)




    def t_fundacion(self):

        localctx = GramaticaParser.T_fundacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_t_fundacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(GramaticaParser.FUNDACION)
            self.state = 154
            self.match(GramaticaParser.INT)
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
            return self.getToken(GramaticaParser.PYME, 0)

        def TRUE(self):
            return self.getToken(GramaticaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GramaticaParser.FALSE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_pyme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_pyme" ):
                listener.enterT_pyme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_pyme" ):
                listener.exitT_pyme(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_pyme" ):
                return visitor.visitT_pyme(self)
            else:
                return visitor.visitChildren(self)




    def t_pyme(self):

        localctx = GramaticaParser.T_pymeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_t_pyme)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(GramaticaParser.PYME)
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
            return self.getToken(GramaticaParser.LINK, 0)

        def URL(self):
            return self.getToken(GramaticaParser.URL, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_link

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_link" ):
                listener.enterT_link(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_link" ):
                listener.exitT_link(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_link" ):
                return visitor.visitT_link(self)
            else:
                return visitor.visitChildren(self)




    def t_link(self):

        localctx = GramaticaParser.T_linkContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_t_link)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(GramaticaParser.LINK)
            self.state = 160
            self.match(GramaticaParser.URL)
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
            return self.getToken(GramaticaParser.DIRECCION, 0)

        def t_tipo_direccion(self):
            return self.getTypedRuleContext(GramaticaParser.T_tipo_direccionContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_direccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_direccion" ):
                listener.enterT_direccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_direccion" ):
                listener.exitT_direccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_direccion" ):
                return visitor.visitT_direccion(self)
            else:
                return visitor.visitChildren(self)




    def t_direccion(self):

        localctx = GramaticaParser.T_direccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_t_direccion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(GramaticaParser.DIRECCION)
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
            return self.getToken(GramaticaParser.NULL, 0)

        def ABRO_LLAVE(self):
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def t_calle(self):
            return self.getTypedRuleContext(GramaticaParser.T_calleContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def t_ciudad(self):
            return self.getTypedRuleContext(GramaticaParser.T_ciudadContext,0)


        def t_pais(self):
            return self.getTypedRuleContext(GramaticaParser.T_paisContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_tipo_direccion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_tipo_direccion" ):
                listener.enterT_tipo_direccion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_tipo_direccion" ):
                listener.exitT_tipo_direccion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_tipo_direccion" ):
                return visitor.visitT_tipo_direccion(self)
            else:
                return visitor.visitChildren(self)




    def t_tipo_direccion(self):

        localctx = GramaticaParser.T_tipo_direccionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_t_tipo_direccion)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(GramaticaParser.NULL)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(GramaticaParser.ABRO_LLAVE)
                self.state = 167
                self.t_calle()
                self.state = 168
                self.match(GramaticaParser.COMA)
                self.state = 169
                self.t_ciudad()
                self.state = 170
                self.match(GramaticaParser.COMA)
                self.state = 171
                self.t_pais()
                self.state = 172
                self.match(GramaticaParser.CIERRO_LLAVE)
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


    class T_calleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALLE(self):
            return self.getToken(GramaticaParser.CALLE, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_calle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_calle" ):
                listener.enterT_calle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_calle" ):
                listener.exitT_calle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_calle" ):
                return visitor.visitT_calle(self)
            else:
                return visitor.visitChildren(self)




    def t_calle(self):

        localctx = GramaticaParser.T_calleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_t_calle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(GramaticaParser.CALLE)
            self.state = 177
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.CIUDAD, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_ciudad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_ciudad" ):
                listener.enterT_ciudad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_ciudad" ):
                listener.exitT_ciudad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_ciudad" ):
                return visitor.visitT_ciudad(self)
            else:
                return visitor.visitChildren(self)




    def t_ciudad(self):

        localctx = GramaticaParser.T_ciudadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_t_ciudad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(GramaticaParser.CIUDAD)
            self.state = 180
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.PAIS, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_pais

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_pais" ):
                listener.enterT_pais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_pais" ):
                listener.exitT_pais(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_pais" ):
                return visitor.visitT_pais(self)
            else:
                return visitor.visitChildren(self)




    def t_pais(self):

        localctx = GramaticaParser.T_paisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_t_pais)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(GramaticaParser.PAIS)
            self.state = 183
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.DEPARTAMENTOS, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramaticaParser.ABRO_CORCHETE, 0)

        def t_listadepartamentos(self):
            return self.getTypedRuleContext(GramaticaParser.T_listadepartamentosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramaticaParser.CIERRO_CORCHETE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_departamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_departamentos" ):
                listener.enterT_departamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_departamentos" ):
                listener.exitT_departamentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_departamentos" ):
                return visitor.visitT_departamentos(self)
            else:
                return visitor.visitChildren(self)




    def t_departamentos(self):

        localctx = GramaticaParser.T_departamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_t_departamentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(GramaticaParser.DEPARTAMENTOS)
            self.state = 186
            self.match(GramaticaParser.ABRO_CORCHETE)
            self.state = 187
            self.t_listadepartamentos()
            self.state = 188
            self.match(GramaticaParser.CIERRO_CORCHETE)
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
            return self.getTypedRuleContext(GramaticaParser.T_departamentoContext,0)


        def COMA(self):
            return self.getToken(GramaticaParser.COMA, 0)

        def t_listadepartamentos(self):
            return self.getTypedRuleContext(GramaticaParser.T_listadepartamentosContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_listadepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listadepartamentos" ):
                listener.enterT_listadepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listadepartamentos" ):
                listener.exitT_listadepartamentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_listadepartamentos" ):
                return visitor.visitT_listadepartamentos(self)
            else:
                return visitor.visitChildren(self)




    def t_listadepartamentos(self):

        localctx = GramaticaParser.T_listadepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_t_listadepartamentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.t_departamento()
            self.state = 193
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 191
                self.match(GramaticaParser.COMA)
                self.state = 192
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
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def t_contenidodepartamento(self):
            return self.getTypedRuleContext(GramaticaParser.T_contenidodepartamentoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_departamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_departamento" ):
                listener.enterT_departamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_departamento" ):
                listener.exitT_departamento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_departamento" ):
                return visitor.visitT_departamento(self)
            else:
                return visitor.visitChildren(self)




    def t_departamento(self):

        localctx = GramaticaParser.T_departamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_t_departamento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(GramaticaParser.ABRO_LLAVE)
            self.state = 196
            self.t_contenidodepartamento()
            self.state = 197
            self.match(GramaticaParser.CIERRO_LLAVE)
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
            return self.getTypedRuleContext(GramaticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def t_subdepartamentos(self):
            return self.getTypedRuleContext(GramaticaParser.T_subdepartamentosContext,0)


        def t_jefe(self):
            return self.getTypedRuleContext(GramaticaParser.T_jefeContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_contenidodepartamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidodepartamento" ):
                listener.enterT_contenidodepartamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidodepartamento" ):
                listener.exitT_contenidodepartamento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_contenidodepartamento" ):
                return visitor.visitT_contenidodepartamento(self)
            else:
                return visitor.visitChildren(self)




    def t_contenidodepartamento(self):

        localctx = GramaticaParser.T_contenidodepartamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_t_contenidodepartamento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.t_nombre()
            self.state = 200
            self.match(GramaticaParser.COMA)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 201
                self.t_jefe()
                self.state = 202
                self.match(GramaticaParser.COMA)


            self.state = 206
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
            return self.getToken(GramaticaParser.NOMBRE, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_nombre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_nombre" ):
                listener.enterT_nombre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_nombre" ):
                listener.exitT_nombre(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_nombre" ):
                return visitor.visitT_nombre(self)
            else:
                return visitor.visitChildren(self)




    def t_nombre(self):

        localctx = GramaticaParser.T_nombreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_t_nombre)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(GramaticaParser.NOMBRE)
            self.state = 209
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.JEFE, 0)

        def STRING(self):
            return self.getToken(GramaticaParser.STRING, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_jefe

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_jefe" ):
                listener.enterT_jefe(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_jefe" ):
                listener.exitT_jefe(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_jefe" ):
                return visitor.visitT_jefe(self)
            else:
                return visitor.visitChildren(self)




    def t_jefe(self):

        localctx = GramaticaParser.T_jefeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_t_jefe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(GramaticaParser.JEFE)
            self.state = 212
            self.match(GramaticaParser.STRING)
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
            return self.getToken(GramaticaParser.SUBDEPARTAMENTOS_LISTA, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramaticaParser.ABRO_CORCHETE, 0)

        def t_listasubdepartamentos(self):
            return self.getTypedRuleContext(GramaticaParser.T_listasubdepartamentosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramaticaParser.CIERRO_CORCHETE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_subdepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_subdepartamentos" ):
                listener.enterT_subdepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_subdepartamentos" ):
                listener.exitT_subdepartamentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_subdepartamentos" ):
                return visitor.visitT_subdepartamentos(self)
            else:
                return visitor.visitChildren(self)




    def t_subdepartamentos(self):

        localctx = GramaticaParser.T_subdepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_t_subdepartamentos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(GramaticaParser.SUBDEPARTAMENTOS_LISTA)
            self.state = 215
            self.match(GramaticaParser.ABRO_CORCHETE)
            self.state = 216
            self.t_listasubdepartamentos()
            self.state = 217
            self.match(GramaticaParser.CIERRO_CORCHETE)
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
            return self.getTypedRuleContext(GramaticaParser.T_subdepartamentoContext,0)


        def COMA(self):
            return self.getToken(GramaticaParser.COMA, 0)

        def t_listasubdepartamentos(self):
            return self.getTypedRuleContext(GramaticaParser.T_listasubdepartamentosContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_listasubdepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listasubdepartamentos" ):
                listener.enterT_listasubdepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listasubdepartamentos" ):
                listener.exitT_listasubdepartamentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_listasubdepartamentos" ):
                return visitor.visitT_listasubdepartamentos(self)
            else:
                return visitor.visitChildren(self)




    def t_listasubdepartamentos(self):

        localctx = GramaticaParser.T_listasubdepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_t_listasubdepartamentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.t_subdepartamento()
            self.state = 222
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 220
                self.match(GramaticaParser.COMA)
                self.state = 221
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
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def t_contenidosubdepartamentos(self):
            return self.getTypedRuleContext(GramaticaParser.T_contenidosubdepartamentosContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_subdepartamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_subdepartamento" ):
                listener.enterT_subdepartamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_subdepartamento" ):
                listener.exitT_subdepartamento(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_subdepartamento" ):
                return visitor.visitT_subdepartamento(self)
            else:
                return visitor.visitChildren(self)




    def t_subdepartamento(self):

        localctx = GramaticaParser.T_subdepartamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_t_subdepartamento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(GramaticaParser.ABRO_LLAVE)
            self.state = 225
            self.t_contenidosubdepartamentos()
            self.state = 226
            self.match(GramaticaParser.CIERRO_LLAVE)
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
            return self.getTypedRuleContext(GramaticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def t_jefe(self):
            return self.getTypedRuleContext(GramaticaParser.T_jefeContext,0)


        def t_empleados(self):
            return self.getTypedRuleContext(GramaticaParser.T_empleadosContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_contenidosubdepartamentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidosubdepartamentos" ):
                listener.enterT_contenidosubdepartamentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidosubdepartamentos" ):
                listener.exitT_contenidosubdepartamentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_contenidosubdepartamentos" ):
                return visitor.visitT_contenidosubdepartamentos(self)
            else:
                return visitor.visitChildren(self)




    def t_contenidosubdepartamentos(self):

        localctx = GramaticaParser.T_contenidosubdepartamentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_t_contenidosubdepartamentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.t_nombre()
            self.state = 229
            self.match(GramaticaParser.COMA)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 230
                self.t_jefe()
                self.state = 231
                self.match(GramaticaParser.COMA)


            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 235
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
            return self.getToken(GramaticaParser.EMPLEADO_LISTA, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramaticaParser.ABRO_CORCHETE, 0)

        def t_listaempleados(self):
            return self.getTypedRuleContext(GramaticaParser.T_listaempleadosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramaticaParser.CIERRO_CORCHETE, 0)

        def ABRO_LLAVE(self):
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def NULL(self):
            return self.getToken(GramaticaParser.NULL, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_empleados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empleados" ):
                listener.enterT_empleados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empleados" ):
                listener.exitT_empleados(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_empleados" ):
                return visitor.visitT_empleados(self)
            else:
                return visitor.visitChildren(self)




    def t_empleados(self):

        localctx = GramaticaParser.T_empleadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_t_empleados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(GramaticaParser.EMPLEADO_LISTA)
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 239
                self.match(GramaticaParser.ABRO_CORCHETE)
                self.state = 240
                self.t_listaempleados()
                self.state = 241
                self.match(GramaticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 2:
                self.state = 243
                self.match(GramaticaParser.ABRO_LLAVE)
                self.state = 244
                self.match(GramaticaParser.CIERRO_LLAVE)
                pass

            elif la_ == 3:
                self.state = 245
                self.match(GramaticaParser.ABRO_CORCHETE)
                self.state = 246
                self.match(GramaticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 4:
                self.state = 247
                self.match(GramaticaParser.NULL)
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
            return self.getTypedRuleContext(GramaticaParser.T_empleadoContext,0)


        def COMA(self):
            return self.getToken(GramaticaParser.COMA, 0)

        def t_listaempleados(self):
            return self.getTypedRuleContext(GramaticaParser.T_listaempleadosContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_listaempleados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listaempleados" ):
                listener.enterT_listaempleados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listaempleados" ):
                listener.exitT_listaempleados(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_listaempleados" ):
                return visitor.visitT_listaempleados(self)
            else:
                return visitor.visitChildren(self)




    def t_listaempleados(self):

        localctx = GramaticaParser.T_listaempleadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_t_listaempleados)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.t_empleado()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 251
                self.match(GramaticaParser.COMA)
                self.state = 252
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
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def t_contenidoempleado(self):
            return self.getTypedRuleContext(GramaticaParser.T_contenidoempleadoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_empleado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_empleado" ):
                listener.enterT_empleado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_empleado" ):
                listener.exitT_empleado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_empleado" ):
                return visitor.visitT_empleado(self)
            else:
                return visitor.visitChildren(self)




    def t_empleado(self):

        localctx = GramaticaParser.T_empleadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_t_empleado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(GramaticaParser.ABRO_LLAVE)
            self.state = 256
            self.t_contenidoempleado()
            self.state = 257
            self.match(GramaticaParser.CIERRO_LLAVE)
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
            return self.getTypedRuleContext(GramaticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def t_cargo(self):
            return self.getTypedRuleContext(GramaticaParser.T_cargoContext,0)


        def t_salario(self):
            return self.getTypedRuleContext(GramaticaParser.T_salarioContext,0)


        def t_activo(self):
            return self.getTypedRuleContext(GramaticaParser.T_activoContext,0)


        def t_fecha_contratacion(self):
            return self.getTypedRuleContext(GramaticaParser.T_fecha_contratacionContext,0)


        def t_proyectos(self):
            return self.getTypedRuleContext(GramaticaParser.T_proyectosContext,0)


        def t_edad(self):
            return self.getTypedRuleContext(GramaticaParser.T_edadContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_contenidoempleado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidoempleado" ):
                listener.enterT_contenidoempleado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidoempleado" ):
                listener.exitT_contenidoempleado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_contenidoempleado" ):
                return visitor.visitT_contenidoempleado(self)
            else:
                return visitor.visitChildren(self)




    def t_contenidoempleado(self):

        localctx = GramaticaParser.T_contenidoempleadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_t_contenidoempleado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.t_nombre()
            self.state = 260
            self.match(GramaticaParser.COMA)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10 or _la==33:
                self.state = 262
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 261
                    self.t_edad()


                self.state = 264
                self.match(GramaticaParser.COMA)


            self.state = 267
            self.t_cargo()
            self.state = 268
            self.match(GramaticaParser.COMA)
            self.state = 269
            self.t_salario()
            self.state = 270
            self.match(GramaticaParser.COMA)
            self.state = 271
            self.t_activo()
            self.state = 272
            self.match(GramaticaParser.COMA)
            self.state = 273
            self.t_fecha_contratacion()
            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 274
                self.match(GramaticaParser.COMA)
                self.state = 275
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
            return self.getToken(GramaticaParser.EDAD, 0)

        def INT(self):
            return self.getToken(GramaticaParser.INT, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_edad

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_edad" ):
                listener.enterT_edad(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_edad" ):
                listener.exitT_edad(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_edad" ):
                return visitor.visitT_edad(self)
            else:
                return visitor.visitChildren(self)




    def t_edad(self):

        localctx = GramaticaParser.T_edadContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_t_edad)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(GramaticaParser.EDAD)
            self.state = 279
            self.match(GramaticaParser.INT)
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
            return self.getToken(GramaticaParser.CARGO, 0)

        def TIPO_CARGO(self):
            return self.getToken(GramaticaParser.TIPO_CARGO, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_cargo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_cargo" ):
                listener.enterT_cargo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_cargo" ):
                listener.exitT_cargo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_cargo" ):
                return visitor.visitT_cargo(self)
            else:
                return visitor.visitChildren(self)




    def t_cargo(self):

        localctx = GramaticaParser.T_cargoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_t_cargo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(GramaticaParser.CARGO)
            self.state = 282
            self.match(GramaticaParser.TIPO_CARGO)
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
            return self.getToken(GramaticaParser.SALARIO, 0)

        def FLOAT(self):
            return self.getToken(GramaticaParser.FLOAT, 0)

        def INT(self):
            return self.getToken(GramaticaParser.INT, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_salario

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_salario" ):
                listener.enterT_salario(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_salario" ):
                listener.exitT_salario(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_salario" ):
                return visitor.visitT_salario(self)
            else:
                return visitor.visitChildren(self)




    def t_salario(self):

        localctx = GramaticaParser.T_salarioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_t_salario)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(GramaticaParser.SALARIO)
            self.state = 285
            _la = self._input.LA(1)
            if not(_la==37 or _la==39):
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


    class T_activoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIVO(self):
            return self.getToken(GramaticaParser.ACTIVO, 0)

        def TRUE(self):
            return self.getToken(GramaticaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(GramaticaParser.FALSE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_activo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_activo" ):
                listener.enterT_activo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_activo" ):
                listener.exitT_activo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_activo" ):
                return visitor.visitT_activo(self)
            else:
                return visitor.visitChildren(self)




    def t_activo(self):

        localctx = GramaticaParser.T_activoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_t_activo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(GramaticaParser.ACTIVO)
            self.state = 288
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
            return self.getToken(GramaticaParser.FECHA_CONTRATACION, 0)

        def DATE(self):
            return self.getToken(GramaticaParser.DATE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_fecha_contratacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fecha_contratacion" ):
                listener.enterT_fecha_contratacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fecha_contratacion" ):
                listener.exitT_fecha_contratacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_fecha_contratacion" ):
                return visitor.visitT_fecha_contratacion(self)
            else:
                return visitor.visitChildren(self)




    def t_fecha_contratacion(self):

        localctx = GramaticaParser.T_fecha_contratacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_t_fecha_contratacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(GramaticaParser.FECHA_CONTRATACION)
            self.state = 291
            self.match(GramaticaParser.DATE)
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
            return self.getToken(GramaticaParser.PROYECTOS_LISTA, 0)

        def ABRO_CORCHETE(self):
            return self.getToken(GramaticaParser.ABRO_CORCHETE, 0)

        def t_listaproyectos(self):
            return self.getTypedRuleContext(GramaticaParser.T_listaproyectosContext,0)


        def CIERRO_CORCHETE(self):
            return self.getToken(GramaticaParser.CIERRO_CORCHETE, 0)

        def ABRO_LLAVE(self):
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def NULL(self):
            return self.getToken(GramaticaParser.NULL, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_proyectos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_proyectos" ):
                listener.enterT_proyectos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_proyectos" ):
                listener.exitT_proyectos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_proyectos" ):
                return visitor.visitT_proyectos(self)
            else:
                return visitor.visitChildren(self)




    def t_proyectos(self):

        localctx = GramaticaParser.T_proyectosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_t_proyectos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(GramaticaParser.PROYECTOS_LISTA)
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 294
                self.match(GramaticaParser.ABRO_CORCHETE)
                self.state = 295
                self.t_listaproyectos()
                self.state = 296
                self.match(GramaticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 2:
                self.state = 298
                self.match(GramaticaParser.ABRO_LLAVE)
                self.state = 299
                self.match(GramaticaParser.CIERRO_LLAVE)
                pass

            elif la_ == 3:
                self.state = 300
                self.match(GramaticaParser.ABRO_CORCHETE)
                self.state = 301
                self.match(GramaticaParser.CIERRO_CORCHETE)
                pass

            elif la_ == 4:
                self.state = 302
                self.match(GramaticaParser.NULL)
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
            return self.getTypedRuleContext(GramaticaParser.T_proyectoContext,0)


        def COMA(self):
            return self.getToken(GramaticaParser.COMA, 0)

        def t_listaproyectos(self):
            return self.getTypedRuleContext(GramaticaParser.T_listaproyectosContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_listaproyectos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_listaproyectos" ):
                listener.enterT_listaproyectos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_listaproyectos" ):
                listener.exitT_listaproyectos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_listaproyectos" ):
                return visitor.visitT_listaproyectos(self)
            else:
                return visitor.visitChildren(self)




    def t_listaproyectos(self):

        localctx = GramaticaParser.T_listaproyectosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_t_listaproyectos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.t_proyecto()
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 306
                self.match(GramaticaParser.COMA)
                self.state = 307
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
            return self.getToken(GramaticaParser.ABRO_LLAVE, 0)

        def t_contenidoproyecto(self):
            return self.getTypedRuleContext(GramaticaParser.T_contenidoproyectoContext,0)


        def CIERRO_LLAVE(self):
            return self.getToken(GramaticaParser.CIERRO_LLAVE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_proyecto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_proyecto" ):
                listener.enterT_proyecto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_proyecto" ):
                listener.exitT_proyecto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_proyecto" ):
                return visitor.visitT_proyecto(self)
            else:
                return visitor.visitChildren(self)




    def t_proyecto(self):

        localctx = GramaticaParser.T_proyectoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_t_proyecto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(GramaticaParser.ABRO_LLAVE)
            self.state = 311
            self.t_contenidoproyecto()
            self.state = 312
            self.match(GramaticaParser.CIERRO_LLAVE)
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
            return self.getTypedRuleContext(GramaticaParser.T_nombreContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(GramaticaParser.COMA)
            else:
                return self.getToken(GramaticaParser.COMA, i)

        def t_fecha_inicio(self):
            return self.getTypedRuleContext(GramaticaParser.T_fecha_inicioContext,0)


        def t_estado(self):
            return self.getTypedRuleContext(GramaticaParser.T_estadoContext,0)


        def t_fecha_fin(self):
            return self.getTypedRuleContext(GramaticaParser.T_fecha_finContext,0)


        def getRuleIndex(self):
            return GramaticaParser.RULE_t_contenidoproyecto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_contenidoproyecto" ):
                listener.enterT_contenidoproyecto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_contenidoproyecto" ):
                listener.exitT_contenidoproyecto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_contenidoproyecto" ):
                return visitor.visitT_contenidoproyecto(self)
            else:
                return visitor.visitChildren(self)




    def t_contenidoproyecto(self):

        localctx = GramaticaParser.T_contenidoproyectoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_t_contenidoproyecto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.t_nombre()
            self.state = 315
            self.match(GramaticaParser.COMA)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 316
                self.t_estado()
                self.state = 317
                self.match(GramaticaParser.COMA)


            self.state = 321
            self.t_fecha_inicio()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 322
                self.match(GramaticaParser.COMA)
                self.state = 323
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
            return self.getToken(GramaticaParser.FECHA_INICIO, 0)

        def DATE(self):
            return self.getToken(GramaticaParser.DATE, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_fecha_inicio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fecha_inicio" ):
                listener.enterT_fecha_inicio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fecha_inicio" ):
                listener.exitT_fecha_inicio(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_fecha_inicio" ):
                return visitor.visitT_fecha_inicio(self)
            else:
                return visitor.visitChildren(self)




    def t_fecha_inicio(self):

        localctx = GramaticaParser.T_fecha_inicioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_t_fecha_inicio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(GramaticaParser.FECHA_INICIO)
            self.state = 327
            self.match(GramaticaParser.DATE)
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
            return self.getToken(GramaticaParser.ESTADO, 0)

        def TIPO_ESTADO(self):
            return self.getToken(GramaticaParser.TIPO_ESTADO, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_estado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_estado" ):
                listener.enterT_estado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_estado" ):
                listener.exitT_estado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_estado" ):
                return visitor.visitT_estado(self)
            else:
                return visitor.visitChildren(self)




    def t_estado(self):

        localctx = GramaticaParser.T_estadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_t_estado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(GramaticaParser.ESTADO)
            self.state = 330
            self.match(GramaticaParser.TIPO_ESTADO)
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
            return self.getToken(GramaticaParser.FECHA_FIN, 0)

        def DATE(self):
            return self.getToken(GramaticaParser.DATE, 0)

        def NULL(self):
            return self.getToken(GramaticaParser.NULL, 0)

        def getRuleIndex(self):
            return GramaticaParser.RULE_t_fecha_fin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterT_fecha_fin" ):
                listener.enterT_fecha_fin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitT_fecha_fin" ):
                listener.exitT_fecha_fin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitT_fecha_fin" ):
                return visitor.visitT_fecha_fin(self)
            else:
                return visitor.visitChildren(self)




    def t_fecha_fin(self):

        localctx = GramaticaParser.T_fecha_finContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_t_fecha_fin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(GramaticaParser.FECHA_FIN)
            self.state = 333
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






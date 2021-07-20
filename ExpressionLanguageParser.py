# -------------------------
# ExpressionLanguageParser.py
#----------------------
import ply.yacc as yacc
from ExpressionLanguageLex import tokens

def p_exp_soma(p):
    '''exp : exp SOMA exp1'''
    p[0] = PlusExp(p[1], p[3])


def p_exp_subtracao(p):
    '''exp : exp SUBTRACAO exp1'''
    p[0] = MinusExp(p[1], p[3])

def p_exp_exp1(p):
    '''exp : exp1'''
    p[0] = p[1]

def p_exp_mul(p):
  '''exp1 : exp1 VEZES exp2'''
  p[0] = TimesExp(p[1], p[3])

def p_exp_div(p):
  '''exp1 : exp1 DIVISAO exp2'''
  p[0] = p[1] / p[3]

def p_exp1_exp2(p):
  '''exp1 : exp2'''
  p[0] = p[1]

def p_exp_pot(p):
  '''exp2 : exp3 POT exp2'''
  p[0] = p[1] ** p[3]

def p_exp2_exp3(p):
  '''exp2 : exp3'''
  p[0] = p[1]

def p_exp3_call(p):
  '''exp3 : call'''  


def p_exp3_num(p):
  '''exp3 : NUMBER'''  
  p[0] = p[1]

def p_exp3_assign(p):
  '''exp3 : assign'''  

def p_exp3_id(p):
  '''exp3 : ID'''  

def p_call_params(p):
  ''' call : ID LPAREN params RPAREN '''

def p_call_empty(p):
  ''' call : ID LPAREN RPAREN '''

def p_params_lst(p):
  ''' params : exp COMMA params '''

def p_params_exp(p):
  ''' params : exp'''

def p_assign(p):
  ''' assign : ID IGUAL exp'''

def p_error(p):
  print('Error')

parser = yacc.yacc()

while True:
 try:
     s = input('calc > ')
 except EOFError:
     break
 if not s: continue
 result = parser.parse(s)
 print(result)

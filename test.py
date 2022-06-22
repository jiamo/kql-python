p = "./kql-lib"

import sys
import clr
columns = []
sys.path.append(p)
clr.AddReference("Kusto.Language")
from Kusto.Language import *
from Kusto.Language.Syntax import *
from Kusto.Language.Symbols import *
import System


k_globals = GlobalState.Default.WithDatabase(
     DatabaseSymbol("db",
     TableSymbol("Shapes", "(id: string, width: real, height: real)"),
     FunctionSymbol("TallShapes", "{ Shapes | where width < height; }")
    ))

query = "TallShapes | where width > 5 | project id, width";
code = KustoCode.ParseAndAnalyze(query, k_globals);
columns = []
def f(n):
    print(n.ReferencedSymbol) 
    if (code.Globals.GetTable(c) != None): 
        columns.append(c)

SyntaxElement.WalkNodes(code.Syntax, f)
print(columns)

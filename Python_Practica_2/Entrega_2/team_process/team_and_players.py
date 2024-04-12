GAMES = 25
GOALS_VALUE = 1.5
GOALS_AVOIED_VALUE = 1.25
ASSISTS_VALUE = 1


def create_Structure(names,goals,goals_avoied,assists):
    """Esta función devuelve una lista de diccionarios a partir de 
       las tres estructuras epasadas como parámetro.
       
       Args:
            names (list): lista de nombres 
            goals (list): lista de goles
            goals_avoied (list): lista de goles evitados 
            assists (list): lista de asistencias
            
       Returns:
            list: lista de diccionarios con las estadisticas"""
       
    stats = []
    
    #uno las tres estructuras en una con zip
    structure=list(zip(names,goals,goals_avoied,assists))
    
    #creo la lista de diccionarios a partir de structure 
    for n,g,ga,a in structure:
        stats.append({"name":n,"goals":g,"goals_avoied":ga,"assists":a})
    
    return stats

def max_scorer(list):
    """Esta función devuelve el nombre y la cantidad de goles
       del jugador/jugadora con más goles
       
       Args:
            list (list): lista de diccionarios
            
       Returns:
            (dict): diccionario con name y goals"""
       
    scorer = max(list, key = lambda x: x["goals"])
    return {"name":scorer["name"],"goals":scorer["goals"]}

def most_influential(list):
    """Esta función devuelve el jugador/jugadra más influyente
    
       Args:
            list (list): lista de diccionarios
            
       Returns:
            (str): nombre de el 'jugador más influyente'"""
    
    return max(list, key= lambda x: x["goals"]*GOALS_VALUE+x["goals_avoied"]*GOALS_AVOIED_VALUE+x["assists"]*ASSISTS_VALUE)["name"]

def total_goals_average(list):
    """Esta función devuelve el promedio de los goles totales en el torneo 
    
       Args:
            list (list): lista de diccionarios
            
       Returns:
            (double): promedio de goles por partido del equipo"""
    
    return sum(players ["goals"] for players in list)/GAMES

def scorer_goals_average(scorer_goals):
    """Esta función devuelve el promedio de los goles
       del jugador/jugadora con más goles del equipo en el torneo 
       
       Args: 
            scorer_goals (int): goles del jugador 
            
       Returns:
            (double): promedio de goles por partido"""
       
    return scorer_goals/GAMES
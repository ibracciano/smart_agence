from datetime import datetime

def extraire_heure(date_et_heure):
  """Extrait l'heure d'un objet datetime ou d'une chaîne de caractères représentant une date et une heure.

  Args:
    date_et_heure: Un objet datetime ou une chaîne de caractères au format ISO 8601 (par exemple, '2023-10-26T10:30:00').

  Returns:
    Une chaîne de caractères représentant l'heure au format HH:MM:SS, ou None si l'entrée n'est pas valide.
  """
  if isinstance(date_et_heure, datetime):
    return date_et_heure.strftime("%H:%M:%S")
  elif isinstance(date_et_heure, str):
    try:
      dt_object = datetime.fromisoformat(date_et_heure.replace('Z', '+00:00'))
      return dt_object.strftime("%H:%M:%S")
    except ValueError:
      print("Format de date et heure non reconnu.")
      return None
  else:
    print("Type d'entrée non valide.")
    return None
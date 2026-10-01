# Wenn du BarcaCH das jemals siehst
# Bitte zu den verschiedenen Jobs Mini-Games hinzufügen
# Hier ist die Grundlage dafür 
# thx Goomby3201 :D

JOBS = {
    "museum": ("Museum putzen", 3),
    "kisten": ("Kisten tragen", 5),
    "nacht": ("Nachtschicht", 8)
}

def do_job(player, job_name):
    if job_name not in JOBS:
        return False

    player.money += JOBS[job_name][1]
    return True


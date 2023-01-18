from core.data.models import DataReplication

# función que nos regresa el estado de autoreplicación del sistema
def is_actual_state_autoreplication():
    actual_state = DataReplication.objects.get(id = 1)
    return actual_state.autoreplication
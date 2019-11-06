

class Trial:
    
    def __init__(self, trial_id, hp, status):
        self.trial_id = trial_id
        self.hp = hp
        self.status = status
        self.metrics = {}

    def load_state(self, state):
        self.trial_id = state['trial_id']
        self.hp = state['hp']  # dict at first
        self.metrics = state['metrics']
        self.status = state['status']

    def get_state(self):
        state_dict = {
            'trial_id': self.trial_id,
            'hp': self.hp,
            'metrics': self.metrics,
            'status': self.status
        }
        return state_dict


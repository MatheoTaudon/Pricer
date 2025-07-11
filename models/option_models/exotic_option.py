# models/exotic_option.py


from models.option_models.option import Option

class ExoticOption(Option):
    def __init__(self, exotic_type: str, num_observations=None, **kwargs):
        super().__init__(**kwargs)
        
        if exotic_type not in ['asian', 'barrier', 'lookback']:
            raise ValueError("Le type exotique doit être 'asian', 'barrier' ou 'lookback'.")
        
        self.exotic_type = exotic_type
        self.num_observations = num_observations

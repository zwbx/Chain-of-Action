"""Append language info and set randomized variation number."""
import gymnasium as gym
import numpy as np
import clip
import logging
from gymnasium.spaces import Box


class LangWrapper(gym.Wrapper, gym.utils.RecordConstructorArgs):
    """Randomize the variation number and language."""

    def __init__(self, env: gym.Env):
        """Init.

        Args:
            env: The environment to apply the wrapper
        """
        gym.utils.RecordConstructorArgs.__init__(self)
        gym.Wrapper.__init__(self, env)
        self.is_vector_env = getattr(env, "is_vector_env", False)
        self.tokenizer = clip.tokenize
        self.desc = None
    
    def reset(self, *args, **kwargs):
        """See base."""
        _env = self.env.unwrapped
        if hasattr(_env, "_task"):
            _env._task.sample_variation()
        obs, info = self.env.reset(*args, **kwargs)
        desc = info.pop("desc")
        desc = desc[np.random.randint(len(desc))]
        self.desc = self.tokenizer(desc).numpy()[0]
        
        return obs, {**info, "desc": self.desc}

    def step(self, action):
        """See base."""
        obs, *rest, info = self.env.step(action)
        return obs, *rest, {**info, "desc": self.desc}

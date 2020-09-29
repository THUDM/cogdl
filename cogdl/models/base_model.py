from typing import Optional, Type, Any

import torch.nn as nn

from cogdl.trainers.base_trainer import BaseTrainer


class BaseModel(nn.Module):
    @staticmethod
    def add_args(parser):
        """Add model-specific arguments to the parser."""
        pass

    @classmethod
    def build_model_from_args(cls, args):
        """Build a new model instance."""
        raise NotImplementedError(
            "Models must implement the build_model_from_args method"
        )

    @staticmethod
    def get_trainer(taskType: Any) -> Optional[Type[BaseTrainer]]:
        return None

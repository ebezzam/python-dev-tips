import hydra
from hydra.utils import instantiate
import numpy as np


class PowerTransform:
    def __init__(self, pow):
        self.pow = pow

    def __call__(self, x):
        return np.power(x, self.pow)


class ExampleZeros:
    def __init__(self, n) -> None:
        self.data = np.zeros(n)

    def __str__(self):
        return str(self.data)


class ExampleArange:
    def __init__(self, n, transform=None) -> None:
        self.data = np.arange(n)
        if transform is not None:
            self.data = transform(self.data)

    def __str__(self):
        return str(self.data)


@hydra.main(version_base=None, config_path="configs", config_name="instantiate")
def run(config):
    example_array = instantiate(config.array)
    print(f"Class: {type(example_array)}, Data: {example_array}")


if __name__ == "__main__":
    run()

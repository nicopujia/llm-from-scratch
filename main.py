import torch


def main():
    print("Apple Silicon chip acceleration:", check_apple_silicon_chip_acceleration())
    print("Tensors of increasing dimensions:", get_tensors())
    print("Tensors type:", [t.dtype for t in get_tensors()])
    print(
        "Tensors type after convertion to float32:",
        [t.dtype for t in convert_tensors_to_float32(get_tensors())],
    )
    print(
        "float32 is particularly useful because they're in the sweet spot "
        "between being usable for most deep learning use cases and computers "
        "being optimized for 32-bit computations."
    )
    print("Tensors shape:", [t.shape for t in get_tensors()])


def check_apple_silicon_chip_acceleration() -> bool:
    return torch.backends.mps.is_available()


def get_tensors() -> list[torch.Tensor]:
    tensor_0d = torch.tensor(1)
    tensor_1d = torch.tensor([1, 2, 3])
    tensor_2d = torch.tensor(
        [
            [1, 2],
            [3, 4],
        ]
    )
    tensor_3d = torch.tensor(
        [
            [[1, 2], [3, 4]],
            [[5, 6], [7, 8]],
        ]
    )

    return [
        tensor_0d,
        tensor_1d,
        tensor_2d,
        tensor_3d,
    ]


def convert_tensors_to_float32(tensors: list[torch.Tensor]) -> list[torch.Tensor]:
    return [t.to(torch.float32) for t in tensors]


if __name__ == "__main__":
    main()

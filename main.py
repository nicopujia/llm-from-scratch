import torch


def main():
    has_apple_silicon_chip_acceleration = check_apple_silicon_chip_acceleration()
    has_nvidia_gpu_acceleration = check_nvidia_gpu_acceleration()
    print("NVIDIA GPUs acceleration:", has_nvidia_gpu_acceleration)
    print("Apple Silicon chip acceleration:", has_apple_silicon_chip_acceleration)

    tensors = get_tensors()
    print("Tensors of increasing dimensions:", tensors)
    print("Tensors type:", [t.dtype for t in tensors])
    print(
        "Tensors type after convertion to float32:",
        [t.dtype for t in convert_tensors_to_float32(tensors)],
    )
    print(
        "float32 is particularly useful because they're in the sweet spot "
        "between being usable for most deep learning use cases and computers "
        "being optimized for 32-bit computations."
    )
    print("Tensors shape:", [t.shape for t in tensors])


def check_nvidia_gpu_acceleration() -> bool:
    # CUDA stands for Compute Unified Device Architecture.
    # It's basically NVIDIA's way to program their GPUs.
    return torch.cuda.is_available()


def check_apple_silicon_chip_acceleration() -> bool:
    # MPS stands for Metal Performance Shaders.
    # It refers to shaders running on Apple hardware.
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
